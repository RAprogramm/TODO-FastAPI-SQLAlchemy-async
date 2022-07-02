<template>
  <div class="backmodal"></div>
  <div class="modal">
    <div v-if="!inputsIsShow">
      <div class="modalHeader">
        <h1>{{ task_from_db.title }}</h1>
        <h1 class="closeIcon" @click="$emit('closeModal')">✗</h1>
      </div>
      <div class="modalBody">
        <h4>Task #{{ task_from_db.id }}</h4>
        <h3>{{ task_from_db.description }}</h3>
      </div>
      <div class="buttons modalFooter">
        <button class="btn update" @click="makeChanges">Update</button>
        <button class="btn delete" @click="remove_task">Delete</button>
      </div>
    </div>
    <div v-else class="updating">
      <div class="modalHeader">
        <h2>Updating task</h2>
        <h1 class="closeIcon" @click="$emit('closeModal')">✗</h1>
      </div>
      <div class="modalBody">
        <label for="title">New title</label>
        <input
          name="title"
          type="text"
          placeholder="New title"
          v-model.trim="task.title"
          required
        />
        <label for="description">New description</label>
        <textarea
          type="text"
          placeholder="New description"
          v-model.trim="task.description"
          required
        />
      </div>
      <div class="buttons modalFooter">
        <button
          class="btn confirm"
          @click="update_task(updatedTask.title, updatedTask.description)"
        >
          Confirm ✓
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

const props = defineProps(["task_from_db"]);
const emit = defineEmits(["get_all", "closeModal"]);

const task = ref(props.task_from_db);
const inputsIsShow = ref(false);
const updatedTask = ref({ title: "", description: "" });

const makeChanges = () => {
  inputsIsShow.value = !inputsIsShow.value;
};

const update_task = async (title, description) => {
  const oldTitle = task.value.title;
  const oldDescription = task.value.description;
  if (title === "") {
    title = oldTitle;
  }
  if (description === "") {
    description = oldDescription;
  }
  try {
    await axios.put(
      `http://127.0.0.1:8000/${task.value.id}?title=${title}&description=${description}`
    );
    emit("get_all");
  } catch (error) {
    console.log(error);
  }
  task.value.title = title;
  task.value.description = description;
  inputsIsShow.value = !inputsIsShow.value;
};

const remove_task = async () => {
  try {
    await axios.delete(`http://127.0.0.1:8000/?id=${task.value.id}`);
    emit("get_all");
    emit("closeModal");
  } catch (error) {
    console.log(error);
  }
};
</script>

<style>
@keyframes animatetop {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.modal {
  border-radius: 1.5rem;
  padding: 1rem;
  background: grey;
  position: absolute;
  z-index: 999;
  width: 90%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation-name: animatetop;
  animation-duration: 0.8s;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.modalHeader {
  margin-left: 1rem;
  display: flex;
  justify-content: space-between;
}
.closeIcon {
  cursor: pointer;
}
.modalBody {
  display: flex;
  flex-direction: column;
  text-align: left;
  margin-left: 3rem;
}
.modalFooter {
  margin: 1rem;
}
.btn {
  cursor: pointer;
  font-size: 20px;
}
.update {
  text-shadow: 1px 1px black;
  width: 180px;
  background: #b28459;
  font-weight: bold;
  color: whitesmoke;
}
.update:hover {
  background: #d19a66;
}
.confirm {
  text-shadow: 1px 1px black;
  width: 180px;
  background: #8dc149;
  color: whitesmoke;
  font-weight: bold;
}
.confirm:hover {
  background: #98c379;
}
.delete {
  text-shadow: 1px 1px black;
  width: 180px;
  background: #c1515a;
  color: whitesmoke;
  font-weight: bold;
}
.delete:hover {
  background: #e86671;
}
.btn {
  border-radius: 2rem;
  cursor: pointer;
  margin: 5px;
}
.buttons {
  display: flex;
}
.btn:focus {
  outline: none;
}
.buttons {
  justify-content: space-between;
  display: flex;
}
@keyframes back {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.backmodal {
  position: absolute;
  background: rgba(0, 0, 0, 0.79);
  height: 100vh;
  width: 100vw;
  left: 0;
  top: 0;
  animation-name: back;
  animation-duration: 0.6s;
}
input {
  width: 60%;
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
</style>
