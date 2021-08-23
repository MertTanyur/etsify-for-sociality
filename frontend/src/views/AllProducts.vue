<template>
  <div>
    <template>
      <b-row class="m-5" align-content="center">
        <b-col
          md="4"
          sm="6"
          cols="8"
          v-for="info in product_infos"
          :key="info.id"
        >
          <custom-card :info="info" class="m-4"></custom-card>
        </b-col>
      </b-row>
    </template>
  </div>
</template>

<script>
import CustomCard from "@/components/CustomCard.vue";
import { BASE } from "@/config.js";
export default {
  created() {
    this.$http.get(BASE + "/list_products").then(
      (response) => {
        this.product_infos = response.data;
        this.dataFetched = true;
      },
      (response) => {
        console.log("an error occured due to ", response);
      }
    );
  },
  data() {
    return {
      product_infos: {},
      dataFetched: false,
    };
  },
  components: {
    CustomCard,
  },
};
</script>

<style>
</style>