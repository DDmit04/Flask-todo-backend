import {HOST} from "../Config.js"
import {doRequest} from "../requests/Request.js"

async function AddTask(newTask) {
    return await doRequest(
        HOST + "task/",
        "POST",
        JSON.stringify(newTask),
        {"Content-Type": "application/json; charset=utf-8"}
    )
}

async function DeleteTask(taskId) {
    return await doRequest(
        HOST + "task/" + taskId,
        "DELETE"
    )
}

async function TurnTask(taskId) {
    return await doRequest(
        HOST + "task/" + taskId,
        "PATCH"
    )
}

export {
    AddTask,
    DeleteTask,
    TurnTask
}