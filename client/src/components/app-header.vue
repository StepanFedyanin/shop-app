<template>
    <div class="header">
        <div class="container header__container">
            <div class="header__logo">
                <img src="@/assets/img/logo.png" alt="">
            </div>
            <div class="header__menu">
                <router-link v-for="item in menuList" class="header__menu--item" :class="[item.link==='basket'&&order&&'m--active',item.link==='basket'&&orderServices&&'m--service--active']" :key="item.link" :to="{name:item.link}">
                    {{item.name}}
                </router-link>
				<div v-if="token" class="header__menu--item" @click="exit">Выйти</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:'app-header',
    data(){
        return{
			token: this.$store.state.access,
			order: this.$store.state.order,
            orderServices: this.$store.state.orderServices,
            menuAuth:[
				{name: 'Каталог',link:'home'},
				{name: 'Корзина',link:'basket'},
			],
			menu:[
                {name: 'Каталог',link:'home'},
				{name: 'Войти',link:'auth'},
				{name: 'Зарегестрироваться',link:'registration'}
			]
        }
    },
	watch:{
		'$store.state.access': {
			immediate: true,
			handler() {
				this.token = this.$store.state.access;
			}
		},
		'$store.state.order': {
			immediate: true,
			handler() {
				this.order = this.$store.state.order;
			}
		},
        '$store.state.orderServices': {
            immediate: true,
            handler() {
                this.orderServices = this.$store.state.orderServices;
            }
        },
	},
	computed:{
		menuList(){
			return this.token? this.menuAuth: this.menu
		}
	},
	methods:{
		exit(){
			this.$store.dispatch('setToken', {access:null,refresh:null});
			this.token = this.$store.state.access;
		}
	}
}
</script>
