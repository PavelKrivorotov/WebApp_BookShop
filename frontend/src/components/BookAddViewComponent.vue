<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import FormAddBookComponent from './FormAddBookComponent.vue'
import LoadingComponent from './LoadingComponent.vue';

const router = useRouter();
const activeLoading = ref(false);

function beforeRequest(formData) {
    console.log('In `BookAddViewComponent`: ', formData);

    activeLoading.value = true;
}

function afterResponse(state, isbn) {
    console.log('Created: ', state);
    console.log('isbn: ', isbn);


    activeLoading.value = false;

    router.push({
        path: `/books/book/${isbn}`,
    });
}
</script>

<template>
    <v-container class="fill-height w-50 add-relative-position" fluid>
        <v-row>
            <v-col>
                <FormAddBookComponent
                @beforeRequest="beforeRequest"
                @afterResponse="afterResponse"
                ></FormAddBookComponent>
            </v-col>
        </v-row>

        <LoadingComponent :is-active="activeLoading"></LoadingComponent>
    </v-container>
</template>

<style scoped>
.add-relative-position {
    position: relative;
}
</style>
