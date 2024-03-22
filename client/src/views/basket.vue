<template>
	<div class="basket">
		<div class="basket__container container">
			<div class="basket__title mb-4">Корзина</div>
			<b-overlay
				:show="loader"
				no-wrap
				spinner-variant="warning"
			/>
			<div class="catalog__list mb-4">
				<template v-if="orders.product.length > 0">
					<div v-for="item in orders.product" :key="`catalog_${item.id}`" class="basket__item">
						<div class="catalog__image">
							<img :src="item.image" :alt="item.name"/>
						</div>
						<div class="catalog__name">{{ item.name }}</div>
						<div class="d-flex justify-content-between align-items-center px-2">
							<div class="catalog__price">{{ item.price }} ₽</div>
							<b-button variant="warning" @click="removeOrder(item.id)">
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
				<b-button variant="warning" class="mb-3" @click="pay">
					Оформить заказ
				</b-button>
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
			loader: false
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
			app.removeOrder({id: id}).then((res) => {
				this.loader = false;
				this.orders = res;
				this.$store.dispatch('setOrder', res.product.length);
			}).catch(() => {
				this.loader = false;
			})
		},
		pay() {
			this.loader = true;
			app.pay(this.orders.id).then(() => {
				this.orders = {
					product: []
				};
				this.loader = false;
				this.$store.dispatch('setOrder', 0);
			}).catch(() => {
				this.loader = false;
			})
		}
	}
}
</script>
