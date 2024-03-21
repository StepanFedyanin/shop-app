const ajax = {
    timeout: 45000,
    responseType: 'json',
    responseEncoding: 'utf8'
};

const serviceUrl = {
    url: '//direct.lradio.ru',
    localPath: '//l-direct.flexidev.ru',
    protocol: 'http',
    port: '80',
    api: '/api',
    onLocal: false
}

let urlPath = `${serviceUrl.url}${serviceUrl.api}`;
if (serviceUrl.onLocal || window.location.hostname === 'localhost') {
    urlPath = `${serviceUrl.localPath}:${serviceUrl.port}${serviceUrl.api}`;
}

let servicePath = `${serviceUrl.protocol}:${window.location.hostname === 'localhost' ? 
                serviceUrl.localPath + ':' + serviceUrl.port : serviceUrl.url }`

const app = {
    url: `${urlPath}`,
    token: 'd53d94913abf172aed172eb875bf546fcfdd5cef'
};

const cache = {
    storage: 'sessionStorage'
};

const logger = {
    url: `${urlPath}/logger`,
    level: 'debug',
    token: 'd53d94913abf172aed172eb875bf546fcfdd5cef'
};

const mainMenu = [
    {
/*
        link: '/home',
        name: 'home',
        role: 'all',
        icon: 'home',
        title: 'Главная'
    }, {
*/
        link: '/campaign',
        name: 'campaign',
        role: 'all',
        icon: 'campaign',
        title: 'Создать кампанию'
    }, {
        link: '/campaigns',
        name: 'campaigns',
        role: 'all',
        icon: 'campaigns',
        title: 'Мои кампании'
    }, {
        link: '/reports',
        name: 'reports',
        role: 'all',
        icon: 'reports',
        title: 'Отчеты'
    }, {
        link: '/pay',
        name: 'pay',
        role: 'all',
        icon: 'pay',
        title: 'Платные ролики'
    }
]

const accountMenu = [
    {
        link: '/profile',
        name: 'profile',
        role: 'all',
        icon: 'profile',
        title: 'Профиль'
    }, {
        link: '/alerts',
        name: 'alerts',
        role: 'all',
        icon: 'alerts',
        title: 'Уведомления'
    }
]

const topMenu = [
    {
        link: '/profile',
        name: 'profile',
        role: 'all',
        icon: 'settings',
        title: 'Профиль'
    }, {
        link: '/alerts',
        name: 'alerts',
        role: 'all',
        icon: 'alerts',
        title: 'Уведомления'
    }
]

export {
    ajax,
    app,
    cache,

    logger,

    mainMenu,
    accountMenu,
    topMenu,
    servicePath
};