<script setup>
import { useAuthStore } from "@/stores/auth.js";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const { user } = storeToRefs(authStore);
const router = useRouter();

// 🔥 重新整理後自動載入使用者資訊
authStore.loadUser();

const logout = () => {
  authStore.logout();
  router.push("/login");
};
</script>

<template>
  <nav class="navbar">
    <div class="nav-left">
      <router-link to="/">🏠 首頁</router-link>
      |
      <router-link to="/products">🛍️ 商品列表</router-link>
    </div>

    <div class="nav-right">
      <span v-if="user">
        👤 {{ user.username }} |
        <a @click="logout" class="logout">登出</a>
      </span>
      <router-link v-else to="/login">🔑 登入</router-link>
    </div>
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
}

.nav-left a,
.nav-right a {
  color: white;
  text-decoration: none;
  margin: 0 10px;
}

.nav-left a:hover,
.nav-right a:hover {
  text-decoration: underline;
}

.logout {
  cursor: pointer;
  color: red;
}
</style>
