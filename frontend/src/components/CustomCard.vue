<template>
  <b-card
    no-body
    style="max-width: 20rem"
    :img-src="info.image"
    img-alt="Image"
    img-top
    img-height="200px"
    img-width="120px"
  >
    <template #header>
      <h4 class="mb-0">id: {{ info._id }}</h4>
    </template>

    <b-card-body>
      <b-card-sub-title class="mb-2">Product Name:</b-card-sub-title>
      <b-card-text>
        {{ info.name }}
      </b-card-text>
    </b-card-body>

    <b-list-group flush>
      <b-list-group-item
        ><b>Price</b>: {{ info.price.replace("+", "").replace("Price:", "") }}
      </b-list-group-item>
      <b-list-group-item><b>Product id: </b> {{ info._id }}</b-list-group-item>
    </b-list-group>
  </b-card>
</template>

<script>
export default {
  props: {
    info: {},
  },
};
</script>

<style>
</style>