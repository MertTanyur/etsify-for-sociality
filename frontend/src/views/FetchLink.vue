<template>
  <div>
    <b-row align-h="center">
      <b-col cols="6">
        <!-- <p>welcome</p>
        <b-form-input
          v-model=""
          placeholder="Please paste an etsify product"
        ></b-form-input> -->
        <b-jumbotron>
          <template #header>Welcome</template>

          <template #lead>
            Please paste a Etsy product link to fetch information
          </template>

          <hr class="my-4" />

          <p>
            Our api uses selenium to look like a natural user to etsy servers so
            please wait!
          </p>
          <b-form-input
            v-model="link"
            placeholder="Enter a link"
            class="my-3"
          ></b-form-input>

          <b-button @click="fetchLink()" variant="primary" href="#"
            >Fetch product</b-button
          >
          <template v-if="showCard">
            <template v-if="apiFetching">
              <b-container class="my-4">
                <b-card no-body>
                  <b-row align-content="strech">
                    <b-col> <b-skeleton-img></b-skeleton-img></b-col>
                    <b-col align-self="center">
                      <b-skeleton animation="fade" width="85%"></b-skeleton>
                      <b-skeleton animation="fade" width="55%"></b-skeleton>
                      <b-skeleton animation="fade" width="70%"></b-skeleton>
                      <b-skeleton animation="fade" width="85%"></b-skeleton>
                      <b-skeleton animation="fade" width="55%"></b-skeleton>
                      <b-skeleton animation="fade" width="70%"></b-skeleton>
                    </b-col>
                  </b-row>
                </b-card>
              </b-container>
            </template>
            <template v-else>
              <b-row align-h="center" class="my-4">
                <b-card
                  no-body
                  class="overflow-hidden"
                  style="max-width: 540px"
                >
                  <b-row no-gutters>
                    <b-col md="6">
                      <b-card-img
                        :src="requestedProduct['image']"
                        alt="Image"
                        class="rounded-0"
                      ></b-card-img>
                    </b-col>
                    <b-col md="6">
                      <b-card-body :title="requestedProduct['name']">
                        <b-card-text class="mt-5">
                          Price: {{ requestedProduct["price"] }}
                        </b-card-text>
                      </b-card-body>
                    </b-col>
                  </b-row>
                </b-card>
              </b-row>
            </template>
          </template>
        </b-jumbotron>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { BASE } from "@/config.js";
export default {
  data() {
    return {
      link: "",
      showCard: false,
      apiFetching: false,
      requestedProduct: {},
    };
  },
  methods: {
    fetchLink: function () {
      console.log("function trigerred");
      this.showCard = true;
      this.apiFetching = true;
      this.$http.get(BASE + "/adding_product?product_link=" + this.link).then(
        (response) => {
          console.log(response);
          response.data["price"] = response.data["price"].replace("+", "");
          this.requestedProduct = response.data;
          this.apiFetching = false;
        },
        (response) => {
          console.log("some error occured response is -> ", response);
        }
      );
    },
  },
};
</script>

<style>
</style>