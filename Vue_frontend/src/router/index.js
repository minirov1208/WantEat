import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import register from "@/views/accounts/register.vue";
import login from "@/views/accounts/login.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/register", component: register },
  { path: "/login", component: login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
