import "bootstrap/dist/css/bootstrap.css";
import { createApp } from "vue";
import axios from "axios";

import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/"; // the FastAPI backend

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    const originalRequest = error.config;
    console.log(error);
    console.log(error.response);
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      store.dispatch("logOut");
      return router.push("/login");
    }
  }
});

app.use(router);
app.use(store);
app.component("VueDatePicker", VueDatePicker);
app.mount("#app");
