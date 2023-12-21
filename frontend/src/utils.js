import {
    BACKEND_HOST,
    BACKEND_PORT,
    REGEXP_POINTER_DOMAIN,
    REGEXP_CONTAINER_DOMAIN } from "./settings";

export function replaceUrl(url) {
    if (REGEXP_POINTER_DOMAIN.test(url)) {
        return url.replace(
            REGEXP_POINTER_DOMAIN,
            `/${BACKEND_HOST}:${BACKEND_PORT}/`
        );
    }
    else if (REGEXP_CONTAINER_DOMAIN.test(url)) {
        return url.replace(
            REGEXP_CONTAINER_DOMAIN,
            `/${BACKEND_HOST}:${BACKEND_PORT}/`
        );

    }
    else return null;
}
