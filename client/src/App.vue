<template>
    <div class="app">
        <app-header/>
        <router-view />
    </div>
</template>

<script>

    import AppHeader from "@/components/app-header.vue";

    export default {
        components: {AppHeader},
        computed: {
            user() {
                return this.$store.state.user;
            }
        },
        created() {
            window.onerror = (message, source, lineno, colno, err) => {
                console.error('Window error', err.message);
            };
        },
        errorCaptured(err, vm, info) {
            console.error('Local error', err.message, vm, info);
        }
    };
</script>
<style lang="sass">
    @import './assets/css/main.scss'
</style>
