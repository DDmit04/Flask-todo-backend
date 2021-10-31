import {validateNotEmpty} from "../InputValidation.js"
import {addError} from "../html/AlertBuilder.js";
import {AuthUser} from "../requests/UserApi.js"


document.addEventListener('DOMContentLoaded', () => {
    let loginBtn = document.getElementById("login-btn")
    let usernameOrEmail = document.getElementById("username-or-email")
    let password = document.getElementById("password")
    let loginWindow = document.getElementById("auth")

    usernameOrEmail.addEventListener('change', () => {
        validateNotEmpty(usernameOrEmail)
    })
    password.addEventListener('change', () => {
        validateNotEmpty(password)
    })
    loginBtn.onclick = async function (e) {
        let changeEvent = new Event("change");
        usernameOrEmail.dispatchEvent(changeEvent)
        password.dispatchEvent(changeEvent)
        e.preventDefault()
        if (validateNotEmpty(usernameOrEmail)
            && validateNotEmpty(password)) {
            let authorizeData = await AuthUser(usernameOrEmail.value, password.value)
            if (authorizeData.ok) {
                window.location.href = window.location.href;
            } else {
                let errorText = "Wrong username/email or password!";
                for (const error in authorizeData.errors) {
                    errorText += `\n${authorizeData.errors[error]}`
                }
                addError(loginWindow, errorText)
            }
        }
    }
})