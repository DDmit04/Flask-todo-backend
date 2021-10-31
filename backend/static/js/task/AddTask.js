import {AddTask} from "../requests/TaskApi.js"
import {addError} from "../html/AlertBuilder.js"

document.addEventListener('DOMContentLoaded', () => {
    let infoBoard = document.getElementById("info-board")
    let addTaskBtn = document.getElementById("add-task-btn")
    let taskDescInput = document.getElementById("task-desc")
    let taskStartDateInput = document.getElementById("task-start-date")
    let taskEndDateInput = document.getElementById("task-end-date")

    addTaskBtn.onclick = async (e) => {
        e.preventDefault()
        let desc = taskDescInput.value
        let start = taskStartDateInput.value
        let end = taskEndDateInput.value
        let newTask = {
            "description": desc
        }
        if (start != '') {
            newTask['start'] = start
        }
        if (end != '') {
            newTask['end'] = end
        }
        taskDescInput.value = ""
        taskStartDateInput.value = ""
        taskEndDateInput.value = ""
        let addedTask = await AddTask(newTask)
        if (addedTask.ok) {
            window.location.href = window.location.href;
        } else {
            addError(infoBoard, "Error while adding new task!")
        }
    }
})