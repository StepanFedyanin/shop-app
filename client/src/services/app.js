import {app as settings} from '@/settings';
import {REST, RESTError} from './rest';

export default class extends REST {
    static get settings() {
        return settings;
    }

    static obtainToken(params) {
        return this._post(`token/create`, {}, params).then((data) => {
            let tokens = data;
            return tokens;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось авторизоваться');
        });
    }

    static refreshToken(token) {
        return this._post(`token/refresh`, {}, {refresh: token}).then((data) => {
            let tokens = data;
            return tokens;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось обновит токен');
        });
    }

    static createUser(params) {
        return this._post(`user/create_user`, {}, params).then((data) => {
            let tokens = data;
            return tokens;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось создать пользователя');
        });
    }

    static getUser() {
        return this._get(`user`, {}).then((data) => {
            let user = data;
            return user;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось получить пользователя');
        });
    }

    static getCatalog(){
        return this._get(`produce`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось получить каталог');
        });
    }

    static getProduct(id){
        return this._get(`produce/${id}`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось получить продукт');
        });
    }
    
    static auth(data){
        return this._post(`token/create`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось авторизоваться');
        });
    }
    
    static registration(data){
        return this._post(`user/create_user`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    
    static order(){
        return this._get(`produce/order/get_list`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    
    static addOrder(id){
        return this._get(`produce/order/${id}`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    static removeOrder(data){
        return this._post(`produce/order/remove`, {},data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    
    static pay(data){
        return this._post(`produce/order/pay`, {},data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    
}
