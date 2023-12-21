<script setup>
import { ref, reactive, computed, watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { getBookRetrieve, deleteBook} from '../http/request';
import { replaceUrl } from '../utils';

import FormAddBookComponent from './FormAddBookComponent.vue';
import LoadingComponent from './LoadingComponent.vue';

import ConfirmDialogComponent from '../test-components/ConfirmDialogComponent.vue';

const route = useRoute();
const router = useRouter();

const isLoading = ref(true);
const isActiveDeleteDialog = ref(false);

const config = reactive({
    isbn: null,
    title: null,
    page: null,
    state: null,

    author: [],
    category: [],
    
    image: null,
});

const form = reactive({
    type: 'update',
    readonly: true,
});

async function setBookData(isbn=null) {
    try {
        const _isbn = isbn || route.params.isbn;
        const data = await getBookRetrieve(_isbn);

        console.log("SET DATA IN SET BOOK DATA")

        config.isbn = data.isbn;
        config.title = data.title;
        config.page = data.page;
        config.state = data.state;
        config.author = data.author;
        config.category = data.category;
        config.image = replaceUrl(data.image);
    }
    catch (error) {
        console.error(error);
    }
    finally {
        isLoading.value = false;
    }
}

async function deleteBookData() {
    isLoading.value = true;

    try {
        const data = await deleteBook(config.isbn);

        router.push({
            path: '/books/list',
        })
    }
    catch (error) {
        console.error(error)
    }
    finally {
        isLoading.value = false;
    }
}

function beforeRequest(formData) {
    console.log('In `BookRetrieveViewComponent`: ', formData);

    isLoading.value = true;
}

function afterResponse(state, isbn) {
    console.log('Updated: ', state);
    console.log('isbn: ', isbn);

    // isLoading.value = false;
    form.readonly = !form.readonly;

    if (isbn) {
        setBookData(isbn);
    }
}

function resetForm() {
    console.log('Reset form in `BookRetrieveViewComponent`');

    form.readonly = !form.readonly;
}

function clickDeleteDialogNo() {
    isActiveDeleteDialog.value = false;
}

function clickDeleteDialogYes() {
    isActiveDeleteDialog.value = false;
    deleteBookData();
}

onMounted(async () => {
    isLoading.value = true;
    await setBookData();
});
</script>

<template>
    <v-card class="mx-4 my-5">
        <template v-slot:title>
            <h3>ISBN: #{{ config.isbn }}</h3>
        </template>

        <template v-slot:append>
            <v-btn
            prepend-icon="mdi-pencil"
            @click="form.readonly = !form.readonly"
            :active="!form.readonly"
            :disabled="!form.readonly"
            >Change</v-btn>

            <v-btn
            prepend-icon="mdi-delete"
            @click="isActiveDeleteDialog=true"
            >Delete</v-btn>
        </template>

        <v-container fluid>
            <v-row>
                <v-col>
                    <v-img
                    :src="config.image"
                    ></v-img>
                </v-col>

                <v-col>
                    <FormAddBookComponent
                    :initial-values="config"
                    :form="form"
                    :exclude="['isbn']"
                    @beforeRequest="beforeRequest"
                    @afterResponse="afterResponse"
                    @resetForm="resetForm"
                    ></FormAddBookComponent>
                </v-col>
            </v-row>
        </v-container>

        <LoadingComponent :is-active="isLoading"></LoadingComponent>
        <ConfirmDialogComponent
        :is-active="isActiveDeleteDialog"
        @click:no="clickDeleteDialogNo"
        @click:yes="clickDeleteDialogYes"
        ></ConfirmDialogComponent>
    </v-card>
</template>

<style scoped>
</style>
