import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import RegisterView from "@/views/RegisterView.vue";
import LoginView from "@/views/LoginView.vue";
import DashboardView from "@/views/DashboardView.vue";
import ProfileView from "@/views/ProfileView.vue";
import TaskView from "@/views/TaskView.vue";
import EditTaskView from "@/views/EditTaskView.vue";
import store from "@/store"; // NEW

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
    meta: { requiresAuth: true },
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterView,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: DashboardView,
    meta: { requiresAuth: true },
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: "/task/:id",
    name: "Task",
    component: TaskView,
    meta: { requiresAuth: true },
    props: true,
  },
  {
    path: "/edittask/:id",
    name: "EditTask",
    component: EditTaskView,
    meta: { requiresAuth: true },
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, _, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    } else {
      var user = store.getters.stateUser;
      console.log(user);
      if (user == null) {
        await store.dispatch("viewMe");
        if (store.getters.isAuthenticated) {
          next();
          return;
        }
        next("/login");
        return;
      }
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
