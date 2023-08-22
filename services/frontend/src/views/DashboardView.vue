<template>
  <div>
    <section>
      <h1>Add new task</h1>
      <hr />
      <br />

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input
            type="text"
            name="title"
            v-model="form.title"
            class="form-control"
          />
        </div>
        <div class="mb-3">
          <label for="description" class="form-label">Description:</label>
          <textarea
            name="description"
            v-model="form.description"
            class="form-control"
          ></textarea>
        </div>
        <div class="mb-3">
          <label for="due_date" class="form-label">Due date:</label>
          <VueDatePicker
            v-model="form.due_date"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br /><br />

    <section>
      <h1>Tasks</h1>
      <hr />
      <br />

      <div v-if="tasks.length">
        <div v-for="task in tasks" :key="task.id" class="tasks">
          <div class="card" style="width: 18rem">
            <div class="card-body">
              <ul>
                <li><strong>Task Title:</strong> {{ task.title }}</li>
                <li><strong>User:</strong> {{ task.user.full_name }}</li>
                <li>
                  <router-link :to="{ name: 'Task', params: { id: task.id } }"
                    >View</router-link
                  >
                </li>
              </ul>
            </div>
          </div>
          <br />
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>
  </div>
</template>

<script>
import VueDatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";

export default defineComponent({
  name: "Dashboard",
  components: { VueDatePicker },
  data() {
    return {
      form: {
        title: "",
        description: "",
        due_date: "",
      },
    };
  },
  created: function () {
    this.$store.dispatch("getTasks");
    this.$store.dispatch("viewMe");
    // return this.$store.dispatch("getTasks");
  },
  computed: {
    ...mapGetters({ tasks: "stateTasks", user: "stateUser" }),
  },
  methods: {
    ...mapActions(["createTask"]),
    async submit() {
      await this.createTask(this.form);
    },
  },
});
</script>
