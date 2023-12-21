<script setup>
import { onMounted, onUpdated } from 'vue';

import { replaceUrl } from '../utils';

const props = defineProps({
    bookList : Array,
})

onMounted(() => {
    console.log('onMounted in `ListBookComponent`')
});

onUpdated(() => {
    console.log('onUpdated in `ListBookComponent`')
});
</script>

<template>
    <v-container fluid>
        <v-row>
            <v-col v-for="book in props.bookList" :key="book.id" cols="12" sm="6" md="4" lg="3">
                <v-card class="h-100">
                    <template v-slot:title>
                        <h3>Isbn: #{{ book.isbn }}</h3>
                    </template>

                    <v-container fluid>
                        <v-row>
                            <v-col>
                                <v-img
                                cover
                                :src="replaceUrl(book.image)"
                                >
                                </v-img>
                            </v-col>

                            <v-col>
                                <span>{{ book.title }}</span><br>
                                <span>{{ book.page  }}</span><br>
                                <span>{{ book.state  }}</span><br>
                            </v-col>
                        </v-row>
                    </v-container>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn :to="`/books/book/${book.isbn}`">Show</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>

            <!-- <Loading :isActive=isLoading></Loading> -->
        </v-row>
    </v-container>
</template>

<style scoped>
</style>
