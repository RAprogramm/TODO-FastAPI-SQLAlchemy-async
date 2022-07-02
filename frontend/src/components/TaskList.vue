<template>
  <div class="head">
    <h1>Task Manager</h1>
    <button class="btn plus" @click="showForm">+</button>
  </div>
  <div class="addTask" v-if="formIsVisible">
    <input
      type="text"
      placeholder="Title"
      v-model.trim="newTask.title"
      required
    />
    <textarea
      type="text"
      placeholder="Description"
      v-model.trim="newTask.description"
      required
    />
    <div v-if="newTask.title && newTask.description">
      <button
        class="btn add"
        @click.prevent="add_task(newTask.title, newTask.description)"
      >
        Create task
      </button>
    </div>
  </div>
  <ul class="task-list">
    <li v-for="task in all_tasks" :key="task.id" id="taskid">
      <div class="item">
        <h3 class="title">{{ task.title }}</h3>
        <div class="buttons">
          <button class="btn detail" @click="get_task_by_id(task.id)">
            Details
          </button>
        </div>
      </div>
    </li>
  </ul>
  <div v-if="modalIsOpen">
    <TaskModal
      @closeModal="closeModal"
      @get_all="get_all_tasks"
      :task_from_db="task_from_db"
    />
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import TaskModal from "./TaskModal.vue";

const modalIsOpen = ref(false);
const formIsVisible = ref(false);
const all_tasks = ref([]);
const newTask = ref({ title: "", description: "" });
const task_from_db = ref({});

const showForm = () => {
  formIsVisible.value = !formIsVisible.value;
};

const get_all_tasks = async () => {
  try {
    await axios.get("http://127.0.0.1:8000/").then((response) => {
      all_tasks.value = response.data;
    });
  } catch (error) {
    console.log(error);
  }
};
const closeModal = () => {
  modalIsOpen.value = false;
};

const get_task_by_id = async (id) => {
  try {
    await axios.get(`http://127.0.0.1:8000/${id}`).then((response) => {
      task_from_db.value = response.data;
    });
    modalIsOpen.value = !modalIsOpen.value;
  } catch (error) {
    console.log(error);
  }
};
const add_task = async (title, description) => {
  try {
    await axios.post(
      `http://127.0.0.1:8000/?title=${title}&description=${description}`
    );
    get_all_tasks();
  } catch (error) {
    console.log(error);
  }
  newTask.value.title = "";
  newTask.value.description = "";
};

onMounted(async () => {
  await get_all_tasks();
});
</script>

<style scoped>
@keyframes animatetop {
  from {
    top: -300px;
    opacity: 0;
  }
  to {
    top: 30%;
    opacity: 1;
  }
}
.addTask {
  animation-name: animatetop;
  animation-duration: 0.4s;
  display: grid;
}
.detail {
  background: lightblue;
  font-size: 18px;
  text-shadow: 0px 0px black;
  font-weight: bold;
}
.add {
  font-size: 16px;
  width: 130px;
  font-weight: bold;
  color: lightcoral;
  text-shadow: 2px 2px black;
}
.btn {
  border-radius: 2rem;
  cursor: pointer;
  margin: 5px;
}
.btn:focus {
  outline: none;
}
h3 {
  margin: 10px 10px 10px;
  text-align: left;
}
ul {
  animation-name: animatetop;
  animation-duration: 0.4s;
  list-style-type: none;
  padding: 0;
}
.item {
  background: #b9b9b9;
  border-radius: 1.5rem;
  border: solid black 2px;
  margin: 10px;
  padding: 5px;
  justify-content: space-between;
  display: flex;
  box-shadow: 1px 1px 2px black;
  max-width: 100vw;
}
.item:hover {
  box-shadow: 3px 3px 13px black;
  background: gainsboro;
}
.title {
  width: 70%;
  overflow: hidden;
  text-overflow: ellipsis;
}
input {
  border-radius: 1.5rem;
  padding: 5px 20px 5px;
  margin: 3px;
  font-size: 18px;
}
textarea {
  border-radius: 1.5rem;
  padding: 5px 20px 5px;
  margin: 3px;
  font-size: 18px;
}
input:focus {
  outline: none;
}
textarea:focus {
  outline: none;
}
.head {
  display: inline-grid;
  grid-auto-flow: column;
  align-items: center;
}
.plus {
  margin-left: 1rem;
  font-weight: bold;
  font-size: 30px;
  border-radius: 100%;
  width: 40px;
  height: 40px;
}
.detail_window {
  background: #b9b9b9;
  border-radius: 1.5rem;
  border: solid black 2px;
  margin: 10px;
  padding: 10px;
  margin-top: -18px;
  width: 80%;
  display: inline-grid;
}
</style>
