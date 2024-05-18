<template>
	<div class="home">
		<div class="catalog container">
            <b-tabs v-model="tabActive" content-class="mt-3">
                <b-tab title="Товары" active>
                    <div class="loader" v-if="catalogLoader">
                        <b-spinner v-show="catalogLoader"></b-spinner>
                    </div>
                    <div v-else class="catalog__list">
                        <b-card v-for="item in catalog" :key="`catalog_${item.id}`" class="catalog__item" @click="selectedItem(item)">
                            <b-card-text>
                                {{ item.name }}
                            </b-card-text>
                            <div class="catalog__image">
                                <img :src="item.image" :alt="item.name"/>
                            </div>
                            <div class="catalog__price">{{ item.price }} ₽</div>
                        </b-card>
                    </div>
                </b-tab>
                <b-tab title="Услуги">
                    <div class="loader" v-if="catalogLoader">
                        <b-spinner v-show="catalogLoader"></b-spinner>
                    </div>
                    <div v-else class="catalog__list">
                        <b-card v-for="item in services" :key="`services_${item.id}`" class="catalog__item" @click="selectedServices(item)">
                            <b-card-text>
                                {{ item.name }}
                            </b-card-text>
                            <div class="catalog__image">
                                <img :src="item.image" :alt="item.name"/>
                            </div>
                            <div class="catalog__price">{{ item.price }} ₽</div>
                        </b-card>
                    </div>
                </b-tab>
            </b-tabs>
            <ProductItem :id="idSelectedProductItem" :show="showProductItem" @hidden="hidden"/>
            <ServicesItem :id="idSelectedServicesItem" :show="showServicesItem" @hidden="hidden"/>
		</div>
	</div>
</template>

<script>
import app from "@/services/app";
import ProductItem from "@/components/ProductItem.vue";
import ServicesItem from "@/components/ServicesItem.vue";

export default {
	name: 'home',
	components: {ServicesItem, ProductItem},
	props: {},
	data() {
		return {
			catalog: [],
			catalogLoader: false,
			showProductItem: false,
			idSelectedProductItem: true,
            tabActive: 0,
            showServicesItem: false,
            idSelectedServicesItem: true,
            services: []
		};
	},
	computed: {},
	created() {
	},
    watch:{
        'tabActive': {
            immediate: true,
            handler() {
                if (this.tabActive === 0){
                    this.getCatalog();
                }else {
                    this.getServices();
                }
            }
        },
    },
	methods: {
		getCatalog() {
			this.catalogLoader = true;
			app.getCatalog().then(res => {
				this.catalog = res
				this.catalogLoader = false;
			}).catch(() => {
				this.catalogLoader = false;
			})
		},
        getServices() {
            this.catalogLoader = true;
            app.services().then(res => {
                this.services = res
                this.catalogLoader = false;
            }).catch(() => {
                this.catalogLoader = false;
            })
        },
		hidden(){
			this.showProductItem = false;
            this.showServicesItem = false;
		},
		selectedItem(item){
			this.showProductItem = true;
			this.idSelectedProductItem	= item.id;
		},
        selectedServices(item){
            this.showServicesItem = true;
            this.idSelectedServicesItem	= item.id;
        },
		next(name, params) {
			this.$router.push({name, params})
		}
	}
};
</script>
