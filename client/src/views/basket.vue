<template>
	<div class="basket">
		<div class="basket__container container">
			<div class="basket__title mb-4">Корзина</div>
			<b-overlay
				:show="loader"
				no-wrap
				spinner-variant="primary"
			/>
			<div class="catalog__list mb-4">
				<template v-if="orders.products?.length > 0">
					<div v-for="item in orders.products" :key="`catalog_${item.id}`" class="basket__item">
						<div class="catalog__image">
							<img :src="item.product?.image" :alt="item.product?.name"/>
						</div>
						<div class="catalog__name">{{ item.product?.name }}</div>
						<div class="d-flex justify-content-between align-items-center px-2 mt-3">
							<div class="catalog__price">{{ item.quantity }} X {{ item.product?.price }} ₽</div>
							<b-button variant="primary" @click="removeOrder(item.product?.id)">
								Удалить
							</b-button>
						</div>
					</div>
				</template>
				<div v-else class="basket__err">
					Корзина пустая
				</div>
			</div>
			<div class="basket__order mb-4">
				<span class="mb-5">
									Сумма к оплате: {{ orders.price }} ₽
				</span>
				<b-form>
					<b-form-group
						id="input-group-email-reg"
						label="Контактный телефон"
						label-for="input-email-reg"
					>
						<b-form-input
							id="input-email-reg"
							v-model="phone"
							type="text"
							v-maska
							required
							placeholder="+7 XXX XXX-XX-XX"
							data-maska="+7 ### ###-##-##"
							size="lg"
						></b-form-input>
					</b-form-group>
				</b-form>
				
				<b-button variant="primary" class="mb-3" @click="pay" :disabled="!orders.products?.length || phone.length !== 16">
					Оформить заказ
				</b-button>
				<b-modal
					v-model="showModal"
					centered
					hide-footer
					title="Вы успешно оформили заказ!"
					@hidden="hiddenModel">
					С вами свяжутся в ближайщее время.
				</b-modal>
			</div>
		</div>
	</div>
</template>

<script>
import app from "@/services/app";

export default {
	name: 'basket',
	data() {
		return {
			orders: {
				product: []
			},
			loader: false,
			phone: '',
			showModal: false
		}
	},
	created() {
		this.getOrder();
	},
	methods: {
		getOrder() {
			this.loader = true;
			app.order().then(res => {
				this.loader = false;
				this.orders = res;
			}).catch(() => {
				alert('Не удалось получить данные корзины')
			})
		},
		removeOrder(id) {
			this.loader = true;
			app.remove_by_id_product({id: id}).then((res) => {
				console.log(res.products)
				if (res.products.length === 0) {
					this.$store.dispatch('setOrder', false);
				}
				this.loader = false;
				this.orders = res;
			}).catch(() => {
				this.loader = false;
			})
		},
		hiddenModel(){
			this.showModal = false
		},
		pay() {
			this.loader = true;
			app.pay({id: this.orders.id, phone: this.phone}).then(() => {
				this.orders = {
					product: []
				};
				this.loader = false;
				this.showModal = true
				this.$store.dispatch('setOrder', 0);
			}).catch(() => {
				this.loader = false;
			})
		}
	}
}
</script>
