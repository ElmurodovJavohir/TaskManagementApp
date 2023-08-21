<template>
  <section>
    <h1>Edit task</h1>
    <hr/><br/>

    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="title" class="form-label">Title:</label>
        <input type="text" name="title" v-model="form.title" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">Content:</label>
        <textarea
          name="content"
          v-model="form.content"
          class="form-control"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'EditTask',
  props: ['id'],
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    this.GetTask();
  },
  computed: {
    ...mapGetters({ task: 'stateTask' }),
  },
  methods: {
    ...mapActions(['updateTask', 'viewTask']),
    async submit() {
    try {
      let task = {
        id: this.id,
        form: this.form,
      };
      await this.updateTask(task);
      this.$router.push({name: 'Task', params:{id: this.task.id}});
    } catch (error) {
      console.log(error);
    }
    },
    async GetTask() {
      try {
        await this.viewTask(this.id);
        this.form.title = this.task.title;
        this.form.content = this.task.content;
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    }
  },
});
</script>
