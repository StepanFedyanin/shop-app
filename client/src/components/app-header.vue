<template>
    <div class="header">
        <div class="container header__container">
            <div class="header__logo">
                <img src="@/assets/img/logo.png" alt="">
            </div>
            <div class="header__menu">
                <router-link v-for="item in menu" class="header__menu--item" :key="item.link" :to="{name:item.link}">
                    {{item.name}}
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name:'app-header',
    data(){
        return{
            menu:[
                {name: 'Каталог',link:'home'},
                {name: 'Корзина',link:'home'}
            ]
        }
    }
}
</script>
