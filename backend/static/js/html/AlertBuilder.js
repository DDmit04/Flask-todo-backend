function addInfo(element, message) {
    addAlert(element, message, "INFO")
}

function addError(element, message) {
    addAlert(element, message, "ERROR")
}

function addAlert(element, message, type) {
    let alert = createAlert(message, type)
    element.prepend(alert)
}

function createAlert(message, type) {
    let closeBtn = document.createElement("button")
    closeBtn.classList.add('btn-close')
    closeBtn.setAttribute('type', 'button')
    closeBtn.setAttribute('data-bs-dismiss', 'alert')
    closeBtn.setAttribute('aria-label', 'close')

    let alertDiv = document.createElement("div")
    alertDiv.classList.add('alert')
    alertDiv.classList.add('my-2')
    alertDiv.classList.add('alert-dismissible')
    alertDiv.setAttribute('role', 'alert')

    if (type == 'ERROR') {
        alertDiv.classList.add("alert-danger")
    } else if (type == "INFO") {
        alertDiv.classList.add("alert-info")
    }

    alertDiv.innerHTML = message
    alertDiv.appendChild(closeBtn)
    return alertDiv
}

export {
    addInfo,
    addError
}