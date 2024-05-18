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
						<b-button variant="primary" v-if="product.already" @click="removeServicesOrder">Удалить из корзины</b-button>
                        <b-button variant="primary" v-else @click="addServicesOrder">Добавить в корзину</b-button>
                    </template>
				</div>
			</div>
		</div>
	</b-modal>
</template>

<script>
import app from "@/services/app";

export default {
	name: 'ServicesItem',
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
					this.getServices()
				}
			},
		}
	},
	methods:{
		getServices(){
			this.productLoader = true;
			app.servicesById(this.id).then((res)=>{
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
		addServicesOrder(){
			app.addServices({id: this.product.id}).then(()=>{
				this.getServices();
				this.$store.dispatch('setOrderServices', true);
				this.productLoader = false;
			}).catch(()=>{
				this.productLoader = false;
			})
		},
        removeServicesOrder(){
            app.removeServices({id: this.product.id}).then((res)=>{
                this.getServices();
                if (res.services.length===0){
                    this.$store.dispatch('setOrderServices', false);
                }
                this.productLoader = false;
            }).catch(()=>{
                this.productLoader = false;
            })
		}
	}
}
</script>
