<template>
  <div>
    <header class="header-login">
      <a href="http://localhost:5500/website/" >C-Academy</a>
    </header>

    <main class="background-login">
      <section class="contenedor login">
        <h1>Iniciar Sesión</h1>
        <form @submit.prevent="handleLogin">
          <div class="input-group">
            <img :src="icons.user" alt="Usuario" class="icon" />
            <input
              v-model="username"
              type="text"
              placeholder="Usuario*"
              autocomplete="username"
              required
            />
          </div>

          <div class="input-group">
            <img :src="icons.lock" alt="Contraseña" class="icon" />
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              placeholder="Contraseña*"
              autocomplete="current-password"
              required
            />
            <img
              :src="showPassword ? icons.eye : icons.eyeClosed"
              alt="Ver Contraseña"
              class="toggle-password"
              @click="togglePassword"
            />
          </div>

          <button type="submit" class="btn-login" :disabled="loading">
            {{ loading ? "Ingresando..." : "Ingresar" }}
          </button>
        </form>
        <p v-if="errorMessage" id="error-message" role="alert" aria-live="assertive">
          {{ errorMessage }}
        </p>
      </section>
    </main>
  </div>
</template>

<script>
import userIcon from '@/assets/icons/user.svg'
import lockIcon from '@/assets/icons/lock.svg'
import eyeIcon from '@/assets/icons/eye.svg'
import eyeClosedIcon from '@/assets/icons/eye-closed.svg'

export default {
  data() {
    return {
      username: "",
      password: "",
      showPassword: false,
      errorMessage: "",
      loading: false,
      icons: {
        user: userIcon,
        lock: lockIcon,
        eye: eyeIcon,
        eyeClosed: eyeClosedIcon
      }
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    async handleLogin() {
      this.errorMessage = "";
      this.loading = true;

      if (!this.username || !this.password) {
        this.showError("Por favor, completa ambos campos.");
        return;
      }

      try {
        const response = await fetch("http://127.0.0.1:5000/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          localStorage.setItem("authToken", data.token);

          // Redirigir según el rol
          if (data.role === "admin") {
            this.$router.push("/admin");
          } else if (data.role === "student") {
            this.$router.push("/student");
          } else {
            this.$router.push("/dashboard");
          }
        } else {
          const errorData = await response.json();
          this.showError(errorData.error || "Ocurrió un error. Intenta de nuevo.");
        }
      } catch (error) {
        console.error("Error en el fetch:", error);
        this.showError("No se pudo conectar con el servidor. Revisa tu conexión.");
      }
    },
    showError(message) {
      this.errorMessage = message;
      this.loading = false;
    },
  },
};
</script>

<style lang="scss">
.webp .background-login {
  background-image: url("../assets/img/hero.webp");
}

.no-webp .background-login {
  background-image: url("../assets/img/hero.png");
}

.header-login {
  background-color: rgba($grisOscuro, 0.1);
  padding: 0.3rem 0;
  text-align: center;

  a {
    text-decoration: none;
    color: $blanco;
    font-family: $fuente_titulo;
    font-size: 3rem;
  }
}

.background-login {
  position: relative;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  width: 100%;
  min-height: 90dvh;
  overflow: hidden;
  display: flex;
  align-items: center;

  .login {
    background: rgba(1, 1, 1, 0.1);
    backdrop-filter: blur(5rem);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 1.5rem;
    padding: 2rem;
    color: $blanco;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.4);
    width: 40rem;
    height: 47rem;

    h1 {
      margin-bottom: 5rem;
    }

    .input-group {
      position: relative;
      margin-bottom: 2rem;

      .icon {
        position: absolute;
        left: 1.2rem;
        top: 50%;
        transform: translateY(-50%);
        width: 1.8rem;
        height: 1.8rem;
        opacity: 0.7;
      }

      input {
        width: 100%;
        height: 5rem;
        padding: 1.2rem 1.2rem 1.2rem 4rem;
        border: 1px solid $violeta;
        border-radius: 6px;
        background: transparent;
        color: $blanco;
        outline: none;
        transition: border-color 0.3s ease;

        &::placeholder {
          color: rgba(255, 255, 255, 0.6);
          font-style: italic;
        }

        &:focus {
          border-color: $violeta;
        }
      }

      .toggle-password {
        position: absolute;
        right: 1.2rem;
        top: 50%;
        transform: translateY(-50%);
        width: 2rem;
        height: 2rem;
        opacity: 0.7;
        cursor: pointer;
      }
    }

    .btn-login {
      @include boton($violeta);
      margin: 2rem auto;
      width: 100%;
      height: 5rem;
      font-size: 2.1rem;
    }

    p {
      color: #d32f2f;
      text-align: center;
      margin: 0 auto;
      font-size: 1.5rem;
    }
  }

  &::before {
    content: "";
    position: absolute;
    inset: 0;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 0;
  }

  * {
    position: relative;
    z-index: 1;
  }
}
</style>
