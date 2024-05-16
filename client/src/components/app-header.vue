<template>
    <div class="header">
        <div class="container header__container">
            <div class="header__logo">
                <img src="@/assets/img/logo.png" alt="">
            </div>
            <div class="header__menu">
                <router-link v-for="item in menuList" class="header__menu--item" :key="item.link" :to="{name:item.link}">
                    {{item.name}}
					<span v-if="item.link==='basket'" class="count" :class="order&&'m--active'"></span>
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
