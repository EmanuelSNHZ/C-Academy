import { createApp } from 'vue'
import './styles/main.scss'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')

function supportsWebp() {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img.width > 0 && img.height > 0);
    img.onerror = () => resolve(false);
    img.src =
      "data:image/webp;base64,UklGRiIAAABXRUJQVlA4TCEAAAAvAAAAAAfQ//73v/+BiOh/AAA=";
  });
}

supportsWebp().then((supported) => {
  document.documentElement.classList.add(supported ? "webp" : "no-webp");
});