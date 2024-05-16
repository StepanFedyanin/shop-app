<template>
	<b-modal
		v-model="showModal"
		centered
		hide-footer
		:title="product.name"
		@hidden="$emit('hidden')">
		<div class="product">
			<b-overlay
				:show="productLoader"
				no-wrap
				spinner-variant="primary"
			/>
			<div>
				<div class="product__image">
					<img :src="product.image" :alt="product.name">
				</div>
				<div class="product__price">{{product.price}} ₽</div>
				<div class="product__description" v-html="product.description?.split('\n').join('<br>')"></div>
				<div class="product__btn">
					<template v-if="!token">
						<b-button variant="primary" @click="next('auth')">Войти</b-button>
					</template>
					<template v-else>
						<b-button variant="primary" v-if="product.quantity===0" @click="addProductOrder">Добавить в корзину</b-button>
						<template v-else>
							<div class="product__btn--number">
								<b-button variant="primary" @click="changeItem(product.quantity-1)">-</b-button>
								<span>{{product.quantity}}</span>
								<b-button variant="primary" @click="changeItem(product.quantity+1)">+</b-button>
							</div>
						</template>
					</template>
				</div>
			</div>
		</div>
	</b-modal>
</template>

<script>
import app from "@/services/app";

export default {
	name: 'ProductItem',
	props:{
		show:{
			type: Boolean,
			default(){
				return false
			}
		},
		id:{
			type: Number,
			default(){
				return null
			}
		}
	},
	data(){
		return{
			token: this.$store.state.access,
			productLoader: false,
			product: {},
			showModal: this.show
		}
	},
	watch:{
		'show':{
			handler() {
				this.showModal = this.show;
				if (this.show && this.id){
					this.getProduct()
				}
			},
		}
	},
	methods:{
		getProduct(){
			this.productLoader = true;
			app.getProduct(this.id).then((res)=>{
				this.productLoader = false;
				this.product = res;
			}).catch(()=>{
				this.productLoader = false;
			})
		},
		next(name, params) {
			this.$emit('hidden')
			this.$router.push({name, params})
		},
		addProductOrder(){
			app.addOrder({id: this.product.id, quantity:1}).then(()=>{
				this.getProduct();
				this.$store.dispatch('setOrder', true);
				this.productLoader = false;
			}).catch(()=>{
				this.productLoader = false;
			})
		},
		changeItem(quantity){
			if (quantity===0){
				app.removeItemOrder({id: this.product.product_order}).then((res)=>{
					if (res.products.length===0){
						this.$store.dispatch('setOrder', true);
					}
					this.productLoader = false;
					this.product.quantity = 0;
				}).catch(()=>{
					this.productLoader = false;
				})
			}else {
				app.changeProduct({id: this.product.product_order,quantity}).then(()=>{
					this.productLoader = false;
					this.product.quantity = quantity;
				}).catch(()=>{
					this.productLoader = false;
				})
			}
		}
	}
}
</script>
