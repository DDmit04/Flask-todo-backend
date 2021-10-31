async function doRequest(url, method, body = {}, headers = {}) {
    let request = {
        method: method,
    }
    if (method != "GET" && method != "HEAD") {
        Object.assign(request, {
            body: body,
            headers: headers
        })
    }
    return await fetch(url, request)
        .then(response => {
            return response;
        })
        .catch(err => {
            return err
        })
    return null
}

export {
    doRequest
}