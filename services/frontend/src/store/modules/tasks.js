import axios from "axios";

const state = {
  tasks: [],
  task: null,
};

const getters = {
  stateTasks: (state) => state.tasks,
  stateTask: (state) => state.task,
};

const actions = {
  async createTask({ dispatch }, task) {
    await axios.post("tasks", task);
    await dispatch("getTasks");
  },
  async getTasks({ commit }) {
    let { data } = await axios.get("tasks");
    commit("setTasks", data);
  },
  async viewTask({ commit }, id) {
    let { data } = await axios.get(`task/${id}`);
    commit("setTask", data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateTask({}, task) {
    await axios.patch(`task/${task.id}`, task.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteTask({}, id) {
    await axios.delete(`task/${id}`);
  },
};

const mutations = {
  setTasks(state, tasks) {
    state.tasks = tasks;
  },
  setTask(state, task) {
    state.task = task;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
