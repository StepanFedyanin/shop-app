import { createApp } from 'vue'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';
import '@splidejs/vue-splide/css';

import BootstrapVue3 from 'bootstrap-vue-3';
import VueUploadComponent from 'vue-upload-component';
import { vMaska } from 'maska';

import router from './router/router';
import store from './store/store';
import helpers from './utils/helpers';

import App from './App.vue'

const app = createApp(App);
app.use(BootstrapVue3);
app.directive('maska', vMaska);
app.use(store);
app.use(router);
app.component('file-upload', VueUploadComponent);
app.use(helpers);

app.mount('#app');
