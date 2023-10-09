document.addEventListener("DOMContentLoaded", function (){
    document.getElementById('login-form').addEventListener('submit', function(e){
        e.preventDefault();

        const formData = new FormData(this);

        fetch("api/v1/token/",{
            method: 'POST',
            body: formData
        })
        .then(response => {

            if (response.status == 200){
                // success full
                console.log('successfull')
                let token = response.json()
                token.then(data => {
                    console.log(data)
                    localStorage.setItem('token', JSON.stringify(data));
                    window.location.href = "/";
                })
            }else if (response.status == 401){
                document.getElementById("error-message").innerHTML = `<div class="error-message">Please Check the credential 401</div>`
            }else if (response.status == 404){
                document.getElementById(
                    "error-message"
                ).innerHTML = `<div class="error-message">Please Check the credential 404</div>`;

            }else if (response.status == 400){
                document.getElementById(
                    "error-message"
                ).innerHTML = `<div class="error-message">Please Check the credential 400</div>`;

            }
        })
        .catch(error => {
            console.error('An Error Accoured', error);
        });
    })
})