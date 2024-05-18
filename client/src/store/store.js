import {createStore} from 'vuex';
import VuexPersist from 'vuex-persist'

const vuexPersist = new VuexPersist({
    key: 'shop-app',
    storage: window.localStorage
});


const store = createStore({
    state: {
        user: {},
        error: null,
        loader: null,
        access: null,
        refresh: null,
        order: 0,
        orderServices: 0
    },
    plugins: [vuexPersist.plugin],
    mutations: {
        USER(state, user) {
            state.user = user;
        },
        TOKENS(state, tokens) {
            state.access = tokens.access;
            state.refresh = tokens.refresh;
        },
        ORDER(state, data) {
            state.order = data;
        },
        ORDER_SERVICES(state, data) {
            state.orderServices = data;
        },
    },
    actions: {
        setUser(context, user) {
            context.commit('USER', user);
        },
        clearUser(context) {
            context.commit('USER', {});
        },
        setToken(context, tokens) {
            context.commit('TOKENS', tokens);
        },
        clearToken(context) {
            context.commit('TOKENS', {});
        },
        setOrder(context,data) {
            context.commit('ORDER', data);
        },
        setOrderServices(context,data) {
            context.commit('ORDER_SERVICES', data);
        },
    }
});

export default store;


