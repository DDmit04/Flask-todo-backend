import {HOST} from "../Config.js"
import {doRequest} from "../requests/Request.js"


async function AuthUser(usernameOrEmail, password) {
    let data = {
        "usernameOrEmail": usernameOrEmail,
        "password": password,
    }
    return await doRequest(
        HOST + "user/in",
        "POST",
        JSON.stringify(data),
        {"Content-Type": "application/json; charset=utf-8"}
    )
}

async function GetUser() {
    return await doRequest(
        HOST + "user/",
        "GET"
    )
}

async function MailTasks() {
    return await doRequest(
        HOST + "task/mail",
        "GET",
    )
}

async function RegUser(email, username, password) {
    let data = {
        "email": email,
        "username": username,
        "password": password
    }
    return await doRequest(
        HOST + "user/",
        "POST",
        JSON.stringify(data),
        {"Content-Type": "application/json"}
    )
}

async function SignOutUser() {
    return await doRequest(
        HOST + "user/out",
        "GET",
    )
}

export {
    AuthUser,
    GetUser,
    MailTasks,
    RegUser,
    SignOutUser
}