import { createApp } from 'vue'
import { createMemoryHistory, createRouter } from 'vue-router'

import App from './App.vue'
import HomeApp from './apps/HomeApp.vue'
import RhythmApp from './apps/RhythmApp.vue'

const routes = [
    { path: '/', component: HomeApp },
    { path: '/rhythm', component: RhythmApp }
]

const router = createRouter({
    history: createMemoryHistory(),
    routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')
