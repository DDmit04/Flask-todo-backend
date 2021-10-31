function validateValEqual(input, secInput) {
    if (input.value != secInput.value && secInput.value != "") {
        makeInputInvalid(input)
        return false
    } else if (secInput.value != secInput.value) {
        makeInputInvalid(input)
        return false
    }
    return true
}

function validateEmail(input) {
    let filter = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/
    if (filter.test(input.value)) {
        makeInputValid(input)
        return true
    } else {
        makeInputInvalid(input)
        return false
    }
}

function validateNotEmpty(input) {
    if (input.value.trim() === "") {
        makeInputInvalid(input)
        return false
    } else {
        makeInputValid(input)
        return true
    }
}

function makeInputInvalid(input) {
    input.classList.remove("is-valid")
    input.classList.add("is-invalid")
}

function makeInputValid(input) {
    input.classList.remove("is-invalid")
    input.classList.add("is-valid")
}

export {
    makeInputInvalid,
    makeInputValid,
    validateEmail,
    validateValEqual,
    validateNotEmpty
}