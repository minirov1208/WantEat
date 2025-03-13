import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore("auth", () => {
  const user = ref(null);

  // 設定使用者
  const setUser = (userData) => {
    user.value = userData;
    localStorage.setItem("user", JSON.stringify(userData)); // 存入 localStorage
  };

  // 讀取本地的使用者資訊 (應用啟動時自動載入)
  const loadUser = () => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      user.value = JSON.parse(storedUser);
    }
  };

  // 登出功能
  const logout = () => {
    user.value = null;
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    localStorage.removeItem("user");
  };

  return { user, setUser, loadUser, logout };
});
