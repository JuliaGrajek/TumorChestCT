const form = document.querySelector("form");
const input = document.querySelector("#file-input");
const button = document.querySelector("#submit-button");
const prediction_el = document.querySelector("#prediction")

form.addEventListener("submit", async event => {
    event.preventDefault();
    button.disabled = true;
    const file = input.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/predict/", {
        method: "POST",
        body: formData
    });

    const json_response = await response.json();
    prediction_el.innerHTML = json_response.prediction;

    button.disabled = false;
});