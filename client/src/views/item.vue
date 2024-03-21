<template>
    <div class="product">
        <div class="loader" v-if="productLoader">
            <b-spinner v-show="productLoader"></b-spinner>
        </div>
        <div v-else>
            <div class="product__name">{{product.name}}</div>
            <div class="product__image">
                <img :src="product.image" :alt="product.name">
            </div>
            <div class="product__price">{{product.price}} ₽</div>
            <div class="product__btn">
                <div class="product__message" v-if="!user.id">Для начала авторизуйтесь</div>
                <div class="product__message" v-if="product.available">Товар добавлен</div>
                <b-button variant="warning" v-else-if="user.id">Добавить в корзину</b-button>
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
            user: this.$store.state.user,
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
    }
}
</script>
