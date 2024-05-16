<template>
	<div class="auth container">
		<div class="auth__container container">
			<b-form v-if="typeAuth" class="auth__form" @submit="onSubmitAuth">
				<div class="h2 auth__title mb-4">Авторизация</div>
				<b-form-group
					id="input-group-email"
					label="Почта"
					label-for="input-email"
				>
					<b-form-input
						id="input-email"
						v-model="form.email"
						type="email"
						placeholder="example@mail.ru"
						required
						size="lg"
					></b-form-input>
				</b-form-group>
				<b-form-group
					id="input-group-password"
					label="Пароль"
					label-for="input-password"
				>
					<b-form-input
						id="input-password"
						v-model="form.password"
						type="password"
						required
						size="lg"
					></b-form-input>
				</b-form-group>
				<b-button variant="primary" type="submit">
					Войти
				</b-button>
				<RouterLink :to="{name:'register'}" class="auth__reg">
					Зарегистрироваться?
				</RouterLink>
			</b-form>
			<b-form v-else class="auth__form" @submit="onSubmitReg">
				<div class="h2 auth__title mb-4">Регистрация</div>
				<b-form-group
					id="input-group-email-reg"
					label="Почта"
					label-for="input-email-reg"
				>
					<b-form-input
						id="input-email-reg"
						v-model="form.email"
						type="email"
						placeholder="example@mail.ru"
						required
						size="lg"
					></b-form-input>
				</b-form-group>
				<b-form-group
					id="input-group-password-reg"
					label="Пароль"
					label-for="input-password-reg"
				>
					<b-form-input
						id="input-password-reg"
						v-model="form.password"
						type="password"
						required
						size="lg"
					></b-form-input>
				</b-form-group>
				<b-button variant="primary" type="submit">
					Зарегистрироваться
				</b-button>
				<RouterLink :to="{name:'auth'}" class="auth__reg">
					Войти?
				</RouterLink>
			</b-form>
			<b-overlay
				:show="loader"
				no-wrap
				spinner-variant="primary"
			/>
		</div>
		
	</div>
</template>

<script>
    import { app } from "@/services";

    export default {
        name: 'index',
        props: {
            template: {
                type: String,
                default() { return 'authorization'; }
            }
        },
        data() {
            return {
                showLoaderSending: false,
                form: {
                    email: null,
                    password: ''
                },
				token: this.$store.state.access,
				loader: false,
			};
        },
        computed: {
			typeAuth(){
				return this.$route.name === 'auth'
			}
        },
        created() {
			if (this.token){
				this.next();
			}
            //this.$store.dispatch('hideError');
        },
        methods: {
			onSubmitReg(){
				this.loader = true;
				app.registration(this.form).then(res=>{
					this.next();
					this.loader = false;
					this.$store.dispatch('setToken', res);
				}).catch(()=>{
					this.loader = false;
					alert('Не удалось авторизоваться')
				})
			},
			onSubmitAuth(){
				this.loader = true;
				app.auth(this.form).then(res=>{
					this.next();
					this.loader = false;
					this.$store.dispatch('setToken', res);
				}).catch(()=>{
					this.loader = false;
					alert('Не удалось авторизоваться')
				})
			},
            next() {
                //this.$router.push({ name: 'home' });
                this.$router.push({ name: 'home' });
            },
        }
    };
</script>
