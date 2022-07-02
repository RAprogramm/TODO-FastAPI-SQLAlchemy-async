<template>
  <div class="task_app">
    <TaskList />
  </div>
</template>

<script>
import TaskList from "./components/TaskList.vue";

export default {
  name: "App",
  components: {
    TaskList,
  },
};
</script>

<style>
@keyframes back {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.task_app {
  animation-name: back;
  animation-duration: 0.8s;
  width: auto;
  background: gainsboro;
  color: black;
  border-radius: 1.5rem;
  padding: 10px;
  box-shadow: 5px 5px 15px black;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
