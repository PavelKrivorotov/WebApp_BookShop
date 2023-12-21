import axios from 'axios';

import {
    HTTP_MODE,
    BACKEND_HOST,
    BACKEND_PORT,
    AXIOS_TIMEOUT } from '../settings';

import {
    URL_POST_BOOK_ADD,
    URL_GET_BOOK_RETRIEVE,
    URL_GET_BOOK_LIST,
    URL_GET_BOOK_CHECK_ISBN,

    URL_GET_AUTHOR_LIST,

    URL_GET_CATEGORY_LIST, 
    URL_PATCH_BOOK_UPDATE,
    URL_DELETE_BOOK_REMOVE } from './url';


const axiosObj = axios.create({
    baseURL: `${HTTP_MODE}://${BACKEND_HOST}:${BACKEND_PORT}`,
    timeout: AXIOS_TIMEOUT,
});

export async function getBooks(params=null) {
    try {
        const response = await axiosObj.get(
            URL_GET_BOOK_LIST,
            {
                params: params,
            }
        )
        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function addBook(formData) {
    try {
        const response = await axiosObj.post(
            URL_POST_BOOK_ADD,
            formData,
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function setBook(isbn, formData) {
    try {
        const response = await axiosObj.patch(
            `${URL_PATCH_BOOK_UPDATE}${isbn}`,
            formData,
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function deleteBook(isbn) {
    try {
        const response = await axiosObj.delete(
            `${URL_DELETE_BOOK_REMOVE}${isbn}`
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function getBookRetrieve(isbn) {
    try {
        const response = await axiosObj.get(
            `${URL_GET_BOOK_RETRIEVE}${isbn}`
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function checkBookIsbn(isbn) {
    try {
        const response = await axiosObj.get(
            `${URL_GET_BOOK_CHECK_ISBN}${isbn}`,
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function getAuthors() {
    try {
        const response = await axiosObj.get(
            URL_GET_AUTHOR_LIST,
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}

export async function getCategoryes() {
    try {
        const response = await axiosObj(
            URL_GET_CATEGORY_LIST,
        );

        return response.data;
    }
    catch (error) {
        throw error;
    }
}
