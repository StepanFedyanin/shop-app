<template>
    <div class="product">
		<b-overlay
			:show="productLoader"
			no-wrap
			spinner-variant="primary"
		/>
        <div>
            <div class="product__name">{{product.name}}</div>
            <div class="product__image">
                <img :src="product.image" :alt="product.name">
            </div>
            <div class="product__price">{{product.price}} ₽</div>
            <div class="product__btn">
				<b-button variant="warning" :disabled="!token" v-if="product.available" @click="removeOrder">Удалить из корзины</b-button>
				<b-button variant="warning" :disabled="!token" v-else @click="addOrder">Добавить в корзину</b-button>
            </div>
            <div class="product__description">{{product.description}}</div>
        </div>
    </div>
</template>

<script>
import app from "@/services/app";

export default {
    name: 'item',
    data(){
        return{
			token: this.$store.state.access,
            productLoader: false,
            product: {}
        }
    },
    created() {
        this.productLoader = true;
        app.getProduct(this.$route.params.id).then((res)=>{
            this.productLoader = false;
            this.product = res;
        }).catch(()=>{
            this.productLoader = false;
        })
    },
	methods:{
		addOrder(){
			this.productLoader = true;
			app.addOrder(this.product.id).then((res)=>{
				this.productLoader = false;
				this.product.available = true;
				this.$store.dispatch('setOrder', res.product.length);
			}).catch(()=>{
				this.productLoader = false;
			})
		},
		removeOrder(){
			this.productLoader = true;
			app.removeOrder({id:this.product.id}).then((res)=>{
				this.productLoader = false;
				this.product.available = false;
				this.$store.dispatch('setOrder', res.product.length);
			}).catch(()=>{
				this.productLoader = false;
			})
		}
	}
}
</script>
