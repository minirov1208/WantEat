<template>
  <nav class="navbar">
    <router-link to="/">🏠 首頁</router-link>
    |
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  padding: 10px;
  color: white;
  text-align: center;
  z-index: 1000; /* 確保在最上層 */
}

.navbar a {
  color: white;
  text-decoration: none;
  margin: 0 10px;
}

.navbar a:hover {
  text-decoration: underline;
}

/* 讓頁面內容不會被 Navbar 擋住 */
.page-content {
  margin-top: 50px; /* 視 Navbar 高度調整 */
}
</style>
