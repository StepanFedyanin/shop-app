<template>
    <div class="basket">
        <div class="basket__container container">
            <div class="basket__title mb-4">Корзина</div>
            <b-tabs v-model="tabActive" content-class="mt-auto pt-3" class="h-100 d-flex flex-column">
                <b-tab title="Товары" active :title-item-class="['basket__tab', order&&'m--active']">
                    <div class="loader" v-if="loader">
                        <b-spinner v-show="loader"></b-spinner>
                    </div>
                    <template v-else>
                        <div class="catalog__list mb-4">
                            <template v-if="orders.products?.length > 0">
                                <div v-for="item in orders.products" :key="`catalog_${item.id}`" class="basket__item">
                                    <div class="catalog__image">
                                        <img :src="item.product?.image" :alt="item.product?.name"/>
                                    </div>
                                    <div class="catalog__name">{{ item.product?.name }}</div>
                                    <div class="d-flex justify-content-between align-items-center px-2 mt-3">
                                        <div class="catalog__price">{{ item.quantity }} X {{ item.product?.price }} ₽
                                        </div>
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

                            <b-button variant="primary" class="mb-3" @click="pay"
                                      :disabled="!orders.products?.length || phone.length !== 16">
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
                    </template>
                </b-tab>
                <b-tab title="Услуги" :title-item-class="['basket__tab', orderServices&&'m--service--active']">
                    <div class="loader" v-if="loader">
                        <b-spinner v-show="loader"></b-spinner>
                    </div>
                    <template v-else>
                        <div class="catalog__list mb-4">
                            <template v-if="orders.services?.length > 0">
                                <div v-for="item in orders.services" :key="`catalog_services_${item.id}`"
                                     class="basket__item">
                                    <div class="catalog__image">
                                        <img :src="item.image" :alt="item.name"/>
                                    </div>
                                    <div class="catalog__name">{{ item.name }}</div>
                                    <div class="d-flex justify-content-between align-items-center px-2 mt-3">
                                        <div class="catalog__price">{{ item.price }} ₽</div>
                                        <b-button variant="primary" @click="removeOrderServices(item.id)">
                                            Удалить
                                        </b-button>
                                    </div>
                                </div>
                            </template>
                            <div v-else class="basket__err">
                                Корзина пустая
                            </div>
                        </div>
                        <div class="basket__order mb-4"><span class="mb-5">Сумма к оплате: {{ orders.price }} ₽</span>
                            <b-button variant="primary" class="mb-3" @click="showsServicesForm"
                                      :disabled="!orders.services?.length">
                                Оформить заказ
                            </b-button>
                            <b-modal
                                v-model="showModalServices"
                                centered
                                hide-footer
                                title="Заказ услуг!"
                                @hidden="hiddenModelServices">
                                <div>
                                    <b-form @submit.stop="payServices">
                                        <template v-if="!showSuccessServices">
                                            <b-form-group
                                                id="input-group-email-reg"
                                                label="Дата оказания услуг"
                                                label-for="input-email-reg"
                                            >
                                                <DatePicker
                                                    v-model="servicesForm.date"
                                                    :model-config="calendarConfig"
                                                    :masks="masks"
                                                    :min-date="this.$helpers.formatDate(new Date(), 'YYYY-MM-DD')"
                                                    required
                                                    mode="date"
                                                    color="blue"
                                                >
                                                    <template v-slot="{ inputValue, inputEvents }">
                                                        <b-form-input
                                                            name="campaign_start"
                                                            placeholder="дд.мм.гггг"
                                                            readonly
                                                            required
                                                            size="lg"
                                                            :value="inputValue"
                                                            v-on="inputEvents"
                                                            class="mb-4"
                                                        ></b-form-input>
                                                    </template>
                                                </DatePicker>
                                            </b-form-group>
                                            <b-form-group
                                                id="input-group-email-reg"
                                                label="Желаемое время"
                                                label-for="input-email-reg"
                                                class="mb-2"
                                            >
                                                <div class="d-flex gap-3">
                                                    <b-form-input
                                                        id="input-email-reg"
                                                        v-model="servicesForm.time_start"
                                                        type="time"
                                                        required
                                                        size="lg"
                                                    ></b-form-input>
                                                    <b-form-input
                                                        id="input-email-reg"
                                                        v-model="servicesForm.time_end"
                                                        type="time"
                                                        required
                                                        size="lg"
                                                    ></b-form-input>
                                                </div>
                                            </b-form-group>
                                            <b-form-group
                                                id="input-group-email-reg"
                                                label="Контактный телефон"
                                                label-for="input-email-reg"
                                            >
                                                <b-form-input
                                                    id="input-email-reg"
                                                    v-model="servicesForm.phone"
                                                    type="text"
                                                    v-maska
                                                    required
                                                    placeholder="+7 XXX XXX-XX-XX"
                                                    data-maska="+7 ### ###-##-##"
                                                    size="lg"
                                                ></b-form-input>
                                            </b-form-group>
                                            <b-button
                                                :disabled="!servicesForm.date || !servicesForm.phone || !servicesForm.time_end || !servicesForm.time_start"
                                                variant="primary" class="w-100" type="submit">
                                                Оформить заказ
                                            </b-button>
                                        </template>
                                        <template v-else>
                                            С вами свяжутся в ближайщее время.
                                        </template>
                                    </b-form>
                                </div>
                            </b-modal>
                        </div>
                    </template>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
import app from "@/services/app";
import 'v-calendar/dist/style.css';
import {DatePicker} from 'v-calendar';

export default {
    name: 'basket',
    components: {
        DatePicker,
    },
    data() {
        return {
            orders: {
                product: []
            },
            services: {
                services: []
            },
            loader: false,
            phone: '',
            showModal: false,
            tabActive: 0,
            showModalServices: false,
            servicesForm: {
                phone: null,
                date: null,
                time_start: null,
                time_end: null
            },
            masks: {
                input: 'DD.MM.YYYY',
            },
            calendarConfig: {
                type: 'string',
                mask: 'YYYY-MM-DD'
            },
            showSuccessServices: false,
            order: this.$store.state.order,
            orderServices: this.$store.state.orderServices,
        }
    },
    created() {
    },
    watch: {
        'tabActive': {
            immediate: true,
            handler() {
                if (this.tabActive === 0) {
                    this.getOrder();
                } else {
                    this.getOrderServices();
                }
            }
        },
        '$store.state.order': {
            immediate: true,
            handler() {
                this.order = this.$store.state.order;
            }
        },
        '$store.state.orderServices': {
            immediate: true,
            handler() {
                this.orderServices = this.$store.state.orderServices;
            }
        },
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
        getOrderServices() {
            this.loader = true;
            app.orderServices().then(res => {
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
        removeOrderServices(id) {
            this.loader = true;
            app.removeServices({id: id}).then((res) => {
                this.loader = false;
                this.$store.dispatch('setOrderServices', false);
                this.orders = res;
            }).catch(() => {
                this.loader = false;
            })
        },
        hiddenModel() {
            this.showModal = false
        },
        showsServicesForm() {
            this.showModalServices = true;
        },
        payServices() {
            app.payServices(this.servicesForm).then(() => {
                this.orders = {
                    services: []
                };
                this.$store.dispatch('setOrderServices', false);
                this.showSuccessServices = true;
            }).catch(() => {
            })
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
        },
        hiddenModelServices() {
            this.showModalServices = false;
            this.showSuccessServices = false;
        }
    }
}
</script>
