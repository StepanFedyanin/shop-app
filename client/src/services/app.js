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

    static addOrder(data){
        return this._post(`produce/order/add_item`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    static removeItemOrder(data){
        return this._post(`produce/order/remove`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    static remove_by_id_product(data){
        return this._post(`produce/order/remove_by_id_product`, {}, data).then((data) => {
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
    static changeProduct(data){
        return this._post(`produce/order/change_item`, {},data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    static services(){
        return this._get(`produce/services`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    static servicesById(id){
        return this._get(`produce/services/${id}`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }


    static addServices(data){
        return this._post(`produce/services_order/add`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }

    static removeServices(data){
        return this._post(`produce/services_order/remove`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
    static orderServices(){
        return this._get(`produce/services_order`, {}).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }

    static payServices(data){
        return this._post(`produce/services_order/pay`, {}, data).then((data) => {
            return data;
        }).catch((error) => {
            throw new RESTError(error, 'Не удалось зарегистрироваться');
        });
    }
}
