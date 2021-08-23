<template>
  <div>
    <b-row align-h="center" class="my-2">
      <b-col cols="8">
        <b-navbar type="dark" variant="dark">
          <b-navbar-brand>Etsify</b-navbar-brand>
          <b-navbar-nav class="ml-auto">
            <!-- Navbar dropdowns -->
            <b-nav-item-dropdown text="Products" right>
              <b-dropdown-item href="#/">Get product from link</b-dropdown-item>
              <b-dropdown-item href="#/specificProduct"
                >See a specific product from id</b-dropdown-item
              >
              <b-dropdown-item href="#/allProducts">
                See all products that previously fetched
              </b-dropdown-item>
            </b-nav-item-dropdown>

            <b-nav-item-dropdown text="About" right>
              <b-dropdown-item href="#/devlog">Devlog</b-dropdown-item>
              <b-dropdown-item href="#/projectDescription"
                >Project description</b-dropdown-item
              >
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-navbar>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>