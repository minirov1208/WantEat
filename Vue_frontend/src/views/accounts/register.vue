<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const username = ref("");
const email = ref("");
const password = ref("");
const errorMessage = ref("");

const register = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/api/register/", {
      username: username.value,
      email: email.value,
      password: password.value,
    });

    // 存入 Token
    localStorage.setItem("access", response.data.access);
    localStorage.setItem("refresh", response.data.refresh);
    localStorage.setItem("user", JSON.stringify(response.data));

    // 註冊成功，跳轉到首頁或會員中心
    router.push("/");
  } catch (error) {
    errorMessage.value = error.response?.data?.error || "註冊失敗";
  }
};
</script>

<template>
  <div>
    <h1>會員註冊</h1>
    <input v-model="username" placeholder="帳號" />
    <input v-model="email" type="email" placeholder="電子郵件" />
    <input v-model="password" type="password" placeholder="密碼" />
    <button @click="register">註冊</button>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>
