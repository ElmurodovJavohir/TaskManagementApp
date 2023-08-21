<template>
  <div v-if="task">
    <p><strong>Title:</strong> {{ task.title }}</p>
    <p><strong>Content:</strong> {{ task.content }}</p>
    <p><strong>User:</strong> {{ task.user.username }}</p>

    <div v-if="user.id === task.user.id">
      <p><router-link :to="{name: 'EditTask', params:{id: task.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeTask()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Task',
  props: ['id'],
  async created() {
    try {
      await this.viewTask(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ task: 'stateTask', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewTask', 'deleteTask']),
    async removeTask() {
      try {
        await this.deleteTask(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
