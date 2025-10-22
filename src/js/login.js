document.addEventListener( 'DOMContentLoaded', function() {
    
    viewPassword();
} );

function viewPassword() {
    
    const togglePassword = document.querySelector("#togglePassword");
    const passwordInput = document.querySelector("#password");

    togglePassword.addEventListener("click", () => { 
        const isPassword = passwordInput.type === "password";
        passwordInput.type = isPassword ? "text" : "password";

        // Cambiar de icono con el click
        togglePassword.src = isPassword
            ? "build/resources/img/eye-closed.svg"
            : "build/resources/img/eye.svg";
    })
}