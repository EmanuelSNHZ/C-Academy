document.addEventListener( 'DOMContentLoaded', function() {
    
    viewPassword();
    handleLoginForm();
} );

function viewPassword() {
    
    const togglePassword = document.querySelector("#togglePassword");
    const passwordInput = document.querySelector("#password");

    togglePassword.addEventListener("click", () => { 
        const isPassword = passwordInput.type === "password";
        passwordInput.type = isPassword ? "text" : "password";

        // Cambiar de icono con el click
        togglePassword.src = isPassword
            ? "build/resources/img/eye.svg"
            : "build/resources/img/eye-closed.svg"
    })
}

function handleLoginForm() {
    const loginForm = document.querySelector("#login-form");
    const errorMessageElement = document.querySelector("#error-message");
    const submitButton = loginForm.querySelector('button[type="submit"]');

    if (loginForm) {
        loginForm.addEventListener("submit", async function (event) {
            
            event.preventDefault();

            // Limpiar errores previos y mostrar estado de carga
            errorMessageElement.textContent = "";
            submitButton.textContent = "Ingresando...";
            submitButton.disabled = true;

            // Recolectar los datos
            const username = document.querySelector("#username").value;
            const password = document.querySelector("#password").value;

            // Validación simple de frontend
            if (!username || !password) {
                mostrarError("Por favor, completa ambos campos.");
                return;
            }

            try {
                // Enviar los datos al Backend
                const response = await fetch('http://127.0.0.1:5000/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                });

                if (response.ok) {
                    // Éxito (código 200-299)
                    const data = await response.json();

                    localStorage.setItem('authToken', data.token);

                    // Redirigir según el rol
                    if (data.role === 'admin') {
                        window.location.href = '/admin/dashboard.html';
                    } else if (data.role === 'student') {
                        window.location.href = '/alumno/dashboard.html';
                    } else {
                        window.location.href = '/dashboard.html';
                    }

                } else {
                    const errorData = await response.json();
                    mostrarError(errorData.error || "Ocurrió un error. Intenta de nuevo.");
                }

            } catch (error) {
                console.error("Error en el fetch:", error);
                mostrarError("No se pudo conectar con el servidor. Revisa tu conexión.");
            }
        });
    }

    /**
     * Muestra un mensaje de error y reactiva el botón.
     * @param {string} message - El mensaje de error a mostrar.
     */
    function mostrarError(message) {
        errorMessageElement.textContent = message;
        submitButton.textContent = "Ingresar";
        submitButton.disabled = false;
    }
}