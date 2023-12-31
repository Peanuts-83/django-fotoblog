/**
 * Delete selected photo
 * @param {*} id - photoId : number
 */
function deletePhoto(id) {
    const cookie = getCookie('csrftoken')
    if (confirm('Are you sure to delete this photo?')) {
        fetch(`/photos/${id}/delete/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': cookie
            }
        }).then(response => {
            if (response.ok) {
                console.log('Photo deleted successfully!')
                // reload page
                window.location.href = '/home';
            } else {
                console.error('Something went wrong!')
            }
        }).catch(error => {
            console.error(error)
        })
    }
}

/**
 * Function to retrieve CSRF token from cookies
 * @param {*} name - string
 * @returns string
 */
function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}

/**
 * Display photo
 * Show if url provided
 * Hide if no url provided
 */
function showModal(imageUrl = undefined) {
    const modalWrapper = document.querySelector('.modal-wrapper')
    const modalPhoto = modalWrapper.querySelector('.photo')
    switch (imageUrl) {
        case undefined:
            // doHideModal
            modalPhoto.src = ''
            modalWrapper.style.opacity = 0
            modalWrapper.style.width = 0
            modalWrapper.style.height = 0
            break;
        default:
            // doShowModal
            modalPhoto.src = imageUrl
            modalWrapper.style.opacity = 1
            modalWrapper.style.width = "100%"
            modalWrapper.style.height = "100%"
            break
    }
}