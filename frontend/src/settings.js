export const DEV_HOST = import.meta.env.VITE_DEV_HOST;
export const DEV_PORT = import.meta.env.VITE_DEV_PORT;

export const BACKEND_HOST = import.meta.env.VITE_BACKEND_HOST;
export const BACKEND_PORT = import.meta.env.VITE_BACKEND_PORT;

export const HTTP_MODE = 'http';


// I think -> Bad RegExp...
export const REGEXP_POINTER_DOMAIN = /\/[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5}\//;
// I think -> Bad RegExp..
export const REGEXP_CONTAINER_DOMAIN = /\/[_a-z0-9]+:[0-9]{1,5}\//;

// BAD RegExp ... (Lose:
//      `http://127.0.0.1:8000/images/download/hwdds` -> test --> true
//      `http://127.0.0.1:8000/images/download/hwdd`  -> test --> false
// )
export const REGEXP_IMAGE_URL = new RegExp([
    '^(http|https)://',
    '(([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[0-9]{1,5})|([_a-z0-9]+:[0-9]{1,5}))/',
    'images/download/',
    '[_a-zA-Z0-9]+.[a-z]{3}$',
].join(''));

export const AXIOS_TIMEOUT = 1000;


export const DEFAULT_PAGE_SIZE_RADIO_GROP = {
    '5'  : 5,
    '10' : 10,
    '15' : 15,
};


export const DEFAULT_QUERY_PARAMS = {
    'page'      : 1,
    'author'    : [],
    'category'  : [],
    'page_size' : DEFAULT_PAGE_SIZE_RADIO_GROP['5']
};

export const DEFAULT_REPLACEMENT_QUERY_PARAMS = {
    'pageSize': 'page_size',
};
