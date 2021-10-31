import {addInfo, addError} from "../html/AlertBuilder.js"
import {MailTasks} from "../requests/UserApi.js"

document.addEventListener('DOMContentLoaded', () => {
    let mailBtn = document.getElementById("mail-btn")
    let infoBoard = document.getElementById("info-board")
    mailBtn.onclick = async (e) => {
        e.preventDefault()
        let mailResult = await MailTasks()
        if (mailResult.ok) {
            addInfo(infoBoard, "Mail send!")
        } else {
            addError(infoBoard, "Error while send mail!")
        }
    }
})