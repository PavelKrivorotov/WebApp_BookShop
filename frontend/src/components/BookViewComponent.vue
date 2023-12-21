<script setup>
import { ref, reactive, computed, watch, onMounted, onUpdated } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { getBooks } from '../http/request';

import FilterBookComponent from './FilterBookComponent.vue';
import ListBookComponent from './ListBookComponent.vue';
import LoadingComponent from './LoadingComponent.vue';

import {
    DEFAULT_PAGE_SIZE_RADIO_GROP,
    DEFAULT_QUERY_PARAMS,
    DEFAULT_REPLACEMENT_QUERY_PARAMS } from '../settings';

const route = useRoute();
const router = useRouter();

const activeFilter = ref(false);
const activeLoading = ref(true);
const activeContent = ref(true);

const bookCount = ref(null);
const bookList = ref([]);

const config = reactive({
    page: null,
    author: [],
    category: [],

    pageSize: DEFAULT_PAGE_SIZE_RADIO_GROP['5'],
});

const pageCount = computed(() => {
    const pageSize = config.pageSize
    return bookCount.value % pageSize ?
        Math.trunc(bookCount.value / pageSize) + 1
        :
        Math.trunc(bookCount.value / pageSize);
});


async function setBookList() {
    console.log("setBookList worked!")
    activeLoading.value = true;
    activeContent.value = true;

    try {
        const queryParams = makeQueryParams(config)
        const data = await getBooks(queryParams);
        bookCount.value = data.count;

        bookList.value.splice(0, bookList.value.length);
        data.results.forEach(element => {
            bookList.value.push({
                id: element.id,
                isbn: element.isbn,
                image: element.image,
                title: element.title,
                page: element.page,
                state: element.state,
            });
        });
    }
    catch (error) {
        console.error(error)

        activeContent.value=false;
    }
    finally {
        activeLoading.value = false;
    }
}

function getPageFromUrl() {
    return route.query['page'] ?
        Number(route.query['page'])
        :
        DEFAULT_QUERY_PARAMS['page'];
}

function getAuthorFromUrl() {
    return route.query['author'] ?
        route.query['author'].split(',').map((value) => Number(value))
        :
        DEFAULT_QUERY_PARAMS['author'];
}

function getCategoryFromUrl() {
    return route.query['category'] ?
        route.query['category'].split(',').map((value) => Number(value))
        :
        DEFAULT_QUERY_PARAMS['category'];
}

function getPageSizeFromUrl() {
    return route.query['page_size'] ?
        Number(route.query['page_size'])
        :
        DEFAULT_QUERY_PARAMS['page_size'];
}

function makeQueryParams(params) {
    const clean = {};
    Object.keys(params).forEach(element => {
            if (Object.keys(DEFAULT_REPLACEMENT_QUERY_PARAMS).indexOf(element) != -1) {
                clean[DEFAULT_REPLACEMENT_QUERY_PARAMS[element]] = params[element];
            }
            else {
                clean[element] = params[element];
            }
    });

    if (clean['author']) {clean['author'] = clean['author'].join(',')}
    // else {delete clean['author']}

    if (clean['category']) {clean['category'] = clean['category'].join(',')}
    // else {delete clean['category']}

    return clean;
}

watch(
    () => route.query, 
    async () => {
        console.log('WATCH on route.query: ', route.query)

        config.page = getPageFromUrl();
        config.author = getAuthorFromUrl();
        config.category = getCategoryFromUrl();
        config.pageSize = getPageSizeFromUrl();

        await setBookList();
}, {immediate: true});

onMounted(() => {
    console.log('onMounted in `BookViewComponent` worked!')
});

onUpdated(() => {
    console.log('onUpdated in `BookViewComponent` worked!')
});
</script>

<template>
    <v-container fluid>
        <v-row>
            <v-col class="d-flex justify-end">
                <v-btn type="button" @click="activeFilter = !activeFilter">Filter</v-btn>
            </v-col>
        </v-row>
    </v-container>

    <FilterBookComponent
    :is-active=activeFilter
    :config="config"
    @click:ok="(author, category, pageSize) => {
        config.page = 1;
        config.author = author;
        config.category = category;
        config.pageSize = pageSize;

        router.push({
            path: '/books/list',
            query: makeQueryParams(config),
        });

        activeFilter = !activeFilter;
    }"
    @click:close="activeFilter = !activeFilter"
    ></FilterBookComponent>

    <div class="add-relative-position">
        <div v-show="activeContent">
            <ListBookComponent
            :book-list="bookList"
            ></ListBookComponent>

            <v-pagination
            v-model="config.page"
            :length="pageCount"
            total-visible="4"
            @update:modelValue="() => {
                router.push({
                    path: '/books/list',
                    query: makeQueryParams(config),
                });
            }"
            ></v-pagination>

            <LoadingComponent :is-active="activeLoading"></LoadingComponent>
        </div>

        <div v-show="!activeContent">
            <v-container fluid>
                <v-row>
                    <v-col>
                        <h2>No content! .... 404</h2>
                    </v-col>
                </v-row>
            </v-container>
        </div>
    </div>
</template>

<style scoped>
.add-relative-position {
    position: relative;
}
</style>
