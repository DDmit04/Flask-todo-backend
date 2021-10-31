import {TurnTask, DeleteTask} from "../requests/TaskApi.js"
import {addError} from "../html/AlertBuilder.js"

document.addEventListener('DOMContentLoaded', () => {
    let infoBoard = document.getElementById("info-board")
    loadTurnButtons()
    loadDeleteButtons()

    function loadDeleteButtons() {
        let deleteButtons = document.getElementsByClassName('delete-task-btn')
        for (const deleteButton of deleteButtons) {
            let taskId = deleteButton.id
            deleteButton.onclick = async (e) => {
                e.preventDefault()
                let turnTaskResult = await DeleteTask(taskId)
                if (turnTaskResult.ok) {
                    window.location.href = window.location.href;
                } else {
                    addError(infoBoard, "Error while deleting task!")
                }
            }
        }
    }

    function loadTurnButtons() {
        let turnButtons = document.getElementsByClassName('turn-task-btn')
        for (const turnButton of turnButtons) {
            let taskId = turnButton.id
            turnButton.onclick = async (e) => {
                e.preventDefault()
                let turnTaskResult = await TurnTask(taskId)
                if (turnTaskResult.ok) {
                    window.location.href = window.location.href;
                } else {
                    addError(infoBoard, "Error while turning task!")
                }
            }
        }
    }
})