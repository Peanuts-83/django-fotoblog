/**
 * Update photo on input change
 */
function doUpdatePhoto(event) {
    const photoProfile = document.querySelector('#photo-profile')
    if (photoProfile) {
        photoProfile.src = URL.createObjectURL(event.target.files[0])
    }
}