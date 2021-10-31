import {validateNotEmpty, validateEmail, validateValEqual} from "../InputValidation.js"
import {addError, addInfo} from "../html/AlertBuilder.js";
import {RegUser} from "../requests/UserApi.js"

document.addEventListener('DOMContentLoaded', () => {
    let regBtn = document.getElementById("reg-btn")
    let newEmail = document.getElementById("new-email")
    let newUsername = document.getElementById("new-username")
    let newPassword = document.getElementById("new-password")
    let newPasswordReply = document.getElementById("new-password-reply")
    let regWindow = document.getElementById("register")

    newUsername.addEventListener('change', () => {
        validateNotEmpty(newUsername)
    })
    newPassword.addEventListener('change', () => {
        validateNotEmpty(newPassword)
    })
    newEmail.addEventListener('change', () => {
        validateEmail(newEmail)
    })
    newPasswordReply.addEventListener('change', () => {
        validateValEqual(newPasswordReply, newPassword)
    })
    regBtn.onclick = async function (e) {
        let changeEvent = new Event("change");
        newUsername.dispatchEvent(changeEvent)
        newEmail.dispatchEvent(changeEvent)
        newPassword.dispatchEvent(changeEvent)
        newPasswordReply.dispatchEvent(changeEvent)
        if (validateNotEmpty(newUsername)
            && validateNotEmpty(newPassword)
            && validateEmail(newEmail)
            && validateValEqual(newPasswordReply, newPassword)) {
            e.preventDefault()
            let regData = await RegUser(newEmail.value, newUsername.value, newPassword.value)
            if (regData.ok) {
                addInfo(regWindow, "Registration successful!")
            } else {
                let errorText = "Error while creating user!";
                for (const error in regData.errors) {
                    errorText += `\n${regData.errors[error]}`
                }
                addError(regWindow, errorText)
            }
        }
    }
})