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