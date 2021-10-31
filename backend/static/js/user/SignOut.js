import {SignOutUser} from "../requests/UserApi.js"
import {addError} from "../html/AlertBuilder.js";

document.addEventListener('DOMContentLoaded', () => {
    let infoBoard = document.getElementById("info-board")
    let signOutBtn = document.getElementById("sign-out")
    signOutBtn.onclick = async () => {
        let signOutResult = await SignOutUser()
        if (signOutResult.ok) {
            window.location.href = window.location.href;
        } else {
            addError(infoBoard, "Error sign out!")
        }
    }
})