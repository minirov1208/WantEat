<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();
const username = ref("");
const password = ref("");
const errorMessage = ref("");

const login = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:8000/api/login/", {
      username: username.value,
      password: password.value,
    });

    const userData = {
      username: response.data.username,
      email: response.data.email,
    };

    localStorage.setItem("user", JSON.stringify(userData));
    authStore.setUser(userData);

    router.push("/");
  } catch (error) {
    errorMessage.value = "登入失敗";
  }
};
</script>

<template>
  <div>
    <h1>登入</h1>
    <input v-model="username" placeholder="帳號" />
    <input v-model="password" type="password" placeholder="密碼" />
    <button @click="login">登入</button>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </div>
</template>
