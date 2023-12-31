/**
 * UPLOAD IMAGE: Preview loaded image
 */
const inputImage = document.querySelector("input[type='file']")
const imageElt = document.querySelector("#preview")
inputImage.addEventListener('change', (event) => {
    imageElt.src = URL.createObjectURL(event.target.files[0])
})
