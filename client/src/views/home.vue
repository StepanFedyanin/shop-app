<template>
    <div class="home">
        <div class="catalog container">
            <div class="loader" v-if="catalogLoader">
                <b-spinner v-show="catalogLoader"></b-spinner>
            </div>
            <div v-else class="catalog__list">
                <div v-for="item in catalog" :key="`catalog_${item.id}`" class="catalog__item">
                    <div class="catalog__image">
                        <img :src="item.image" :alt="item.name"/>
                    </div>
                    <div class="catalog__name">{{item.name}}</div>
                    <div class="catalog__price">{{item.price}} ₽</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import app from "@/services/app";

    export default {
        name: 'home',
        components: {
        },
        props: {
        },
        data() {
            return {
                catalog: [],
                catalogLoader: false,
            };
        },
        computed: {
        },
        created() {
            this.getCatalog();
        },
        methods: {
           getCatalog(){
               this.catalogLoader = true;
               app.getCatalog().then(res=>{
                   this.catalog = res
                   this.catalogLoader = false;
               }).catch(()=>{
                   this.catalogLoader = false;
               })
           }
        }
    };
</script>
