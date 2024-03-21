import { createRouter, createWebHistory  } from 'vue-router';
import { helpers } from '@/utils/helpers'
import store from '@/store/store'
import auth from '@/views/auth.vue';
import home from '@/views/home.vue';
import item from "@/views/item.vue";

const routes = [
    {
        path: '/auth',
        name: 'auth',
        component: auth,
        meta: { title: 'Вход' },
        props: true
    }, {
        path: '/registration',
        name: 'registration',
        component: auth,
        meta: { title: 'Регистрация' },
        props: {
            default: true,
            template: 'registration'
        }
    },
     {
        path: '/',
        name: 'home',
        component: home,
        meta: { title: 'Каталог' },
        props: true
    },
    {
        path: '/item/:id',
        name: 'item',
        component: item,
        meta: { title: 'Продукт' },
        props: true
    },
    // {
    //     path: '/campaigns',
    //     name: 'campaigns',
    //     component: campaigns,
    //     meta: { title: 'Мои кампании', requiresAuth: true },
    //     props: true,
    // },
];

const router = createRouter({
    history: createWebHistory(),
    linkActiveClass: 'is-subactive',
    linkExactActiveClass: 'is-active',
    routes
});

router.beforeEach((to, from, next) => {
    document.title = to.meta.title + ' - L Radio Direct' || 'L Radio Direct';
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (store.state.user && store.state.user.id) {
            let jwt = helpers.parseJwt(store.state.access);
            let expDate = new Date(jwt.exp * 1000);
            if (expDate < new Date()) {
                next({ name: 'auth' });
            } else {
                next();
            }
        } else {
            next({ name: 'auth' });
        }
    } else {
        next();
    }
});

export default router;
