<script setup>
import Navbar from "./components/Navbar/Navbar.vue";
</script>
<template>
  <div>
    <Navbar />
    <div class="page-content">
      <router-view />
    </div>
  </div>
</template>
