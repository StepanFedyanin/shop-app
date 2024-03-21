//import _keys from 'lodash/keys';
import {parse, format} from 'fecha';
import {servicePath} from "@/settings";

const helpers = {
    parseDate: (value, template) => {
        return parse(value, template);
    },

    formatDate: (value, template, isArray=false) => {
        if (isArray) return value.map(obj=>{
            const campaign_start =format(new Date(obj.campaign_start),template);
            const campaign_end = format(new Date(obj.campaign_end),template);
            return {
                campaign_start,
                campaign_end
            }
        })
        else return format(value, template);
    },
    removeKeys(obj, keys) {
        if (Array.isArray(obj)) {
            return obj.map((item) => this.removeKeys(item, keys));
        }
        const newObj = {};
        for (const key in obj) {
            if (!keys.includes(key)) {
                newObj[key] = obj[key];
            }
        }
        return newObj;
    },

    stringForNumber: (value, strings) => {
        let idx = 2;
        let num = value;
        if (num > 100) {
            num = num % 100;
        }
        if ((num < 10) || (num > 19)) {
            let z = num % 10;
            if (z === 1) {
                idx = 0;
            } else if ((z > 1) && (z < 5)) {
                idx = 1;
            }
        }
        return value + ' ' + strings[idx];
    },

    toPrice: (value, params) => {
        if (!params) {
            params = {};
        }
        value = value + '';
        let text = '';
        let l = value.length;
        let i = 0;
        let k;
        while (i < l) {
            k = ((i === 0) && (l % 3 > 0)) ? l % 3 : 3;
            if (i + k < l) {
                text = text + value.substr(i, k) + ' ';
            } else {
                text = text + value.substr(i, k);
            }
            i = i + k;
        }
        if (params.sign) {
            text = text + ' ' + params.sign;
        }
        return text;
    },

    getFileInfo: (file, type) => {
        if (type === 'audio') {
            return new Promise((resolve) => {
                let objectURL;

                if (file instanceof File) {
                    objectURL = URL.createObjectURL(file);
                } else {
                    objectURL = new URL(file, servicePath);
                }
                let mySound = new Audio([objectURL]);
                mySound.addEventListener(
                    "canplaythrough",
                    () => {
                        URL.revokeObjectURL(objectURL);
                        resolve({
                            file,
                            duration: mySound.duration,
                            song: mySound
                        });
                    },
                    false,
                );
            });
        }
    },

    parseJwt: (token) => {
        let base64Url = token.split('.')[1];
        let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        let jsonPayload = decodeURIComponent(atob(base64).split('').map(
            function (c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }
        ).join(''));
        return JSON.parse(jsonPayload);
    }
}

export default {
    install(app) {
        app.helpers = helpers
        app.config.globalProperties.$helpers = helpers
    }
}

export {
    helpers
}