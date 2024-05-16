<template>
	<div class="home">
		<div class="catalog container">
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
			<ProductItem :id="idSelectedProductItem" :show="showProductItem" @hidden="hidden"/>
		</div>
	</div>
</template>

<script>
import app from "@/services/app";
import ProductItem from "@/components/ProductItem.vue";

export default {
	name: 'home',
	components: {ProductItem},
	props: {},
	data() {
		return {
			catalog: [],
			catalogLoader: false,
			showProductItem: false,
			idSelectedProductItem: true
		};
	},
	computed: {},
	created() {
		this.getCatalog();
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
		hidden(){
			this.showProductItem = false;
		},
		selectedItem(item){
			this.showProductItem = true;
			this.idSelectedProductItem	= item.id;
		},
		next(name, params) {
			this.$router.push({name, params})
		}
	}
};
</script>
