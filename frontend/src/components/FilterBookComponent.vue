<script setup>
import { ref, computed, onBeforeUpdate } from 'vue';
import { useForm } from 'vee-validate';

import SelectComponent from '../test-components/SelectComponent.vue';
import GroupComponent from '../test-components/GroupComponent.vue';

const props = defineProps({
    isActive: Boolean,
    config: {
        type: Object,
        default: {
            page: null,
            author: [],
            category: [],

            pageSize: null, // null
        }
    }
});

const emits = defineEmits([
    'click:ok',
    'click:close',
]);

const _author = computed(() => props.config.author);
const _category = computed(() => props.config.category);
// 
const _pageSize = computed(() => props.config.pageSize);


// Alternative!!!
// const _initialValues = computed(() => {
//     const values = {};
//     values['author'] = props.config.author;
//     values['category'] = props.config.category;

//     return values;
// });

const { handleSubmit, handleReset, setValues, values } = useForm({
    validationSchema: null,
    initialValues: {
        author: [],
        category: [],

        pageSize: _pageSize.value, // none
    }

    // initialValues: _initialValues,
});

const submit = handleSubmit((values) => {
    console.log(JSON.stringify(values, null, 2));

    emits('click:ok', values.author, values.category, values.pageSize)
});

function setDefaultValues() {
    setValues({
        author: _author.value,
        category: _category.value,

        pageSize: _pageSize.value, // none
    });
}

function cancel() {
    setDefaultValues();
}

onBeforeUpdate(() => {
    console.log('beforeUpdate worked!')

    setDefaultValues();
});



const radio = ref('1');
</script>

<template>
    <v-dialog v-model="props.isActive" width="425" persistent>
        <v-card rounded>
            <v-toolbar border density="comfortable" class="bg-grey-lighten-5">
                <v-toolbar-title>Filters</v-toolbar-title>
                <v-btn icon="mdi-close" @click="emits('click:close')"></v-btn>
            </v-toolbar>

            <v-card-text>
                <v-form>
                    <SelectComponent
                    label="Author"
                    name="author"
                    func-request="author"
                    :multiple="true"
                    ></SelectComponent>
                    
                    <SelectComponent
                    label="Category"
                    name="category"
                    func-request="category"
                    :multiple="true"
                    ></SelectComponent>

                    <GroupComponent
                    label="Book per page"
                    name="pageSize"
                    class="ml-n4 mt-4 mb-n4"
                    ></GroupComponent>
                </v-form>
            </v-card-text>

            <v-footer border class="pr-2 bg-grey-lighten-5">
                <v-btn type="button" @click="handleReset">Reset</v-btn>

                <v-spacer></v-spacer>

                <v-btn type="button" @click="cancel" >Cancel</v-btn>
                <v-btn type="button" @click="submit">Ok</v-btn>
            </v-footer>
        </v-card>
    </v-dialog>
</template>

<style scoped>
</style>
