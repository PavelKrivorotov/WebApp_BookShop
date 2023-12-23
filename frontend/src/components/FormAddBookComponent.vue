<script setup>
import { ref, reactive, toRefs, watch, onMounted } from 'vue';
import { useForm, useField } from 'vee-validate';

import {
    IsbnValidation,
    TitleValidation,
    PageValidation,
    StateValidation,
    ImageValidation,
    AuthorOrCategoryValidation  } from '../plugins/vee-validate-yup'

import { addBook, setBook } from '../http/request';

import TextComponent from '../test-components/TextComponent.vue';
import SelectComponent from '../test-components/SelectComponent.vue';
import FileComponent from '../test-components/FileComponent.vue'

const props = defineProps({
    schema: {
        type: Array,
        default: [
            {
                type: 'text',
                name: 'isbn',
                label: 'Isbn',
                validationRules: IsbnValidation,
            },
            {
                type: 'text',
                name: 'title',
                label: 'Title',
                validationRules: TitleValidation,
            },
            {
                type: 'text',
                name: 'page',
                label: 'Page',
                validationRules: PageValidation,
            },
            {
                type: 'select',
                name: 'state',
                label: 'State',
                funcRequest: 'state',
                validationRules: StateValidation,
            },
            {
                type: 'select',
                name: 'author',
                label: 'Author',
                funcRequest: 'author',
                validationRules: AuthorOrCategoryValidation,
                multiple: true,
            },
            {
                type: 'select',
                name: 'category',
                label: 'Category',
                funcRequest: 'category',
                validationRules: AuthorOrCategoryValidation,
                multiple: true,
            },
            {
                type: 'file',
                name: 'image',
                label: 'Image',
                validationRules: ImageValidation,
            },
        ],
    },
    initialValues: {
        type: Object,
        default: {
            isbn: undefined,
            title: undefined,
            page: undefined,
            state: undefined,
            author: [],
            category: [],
            image: undefined,
        }
    },
    form: {
        type: Object,
        default: {
            type: 'add',
            readonly: false,
        }
    },
    exclude: {
        type: Array,
        default: [],
    },
});

const emits = defineEmits([
    'beforeRequest',
    'afterResponse',

    'resetForm',
]);

// Not worked! Why??? ---- WORKED!!!! REACTIVE ALL `props`!!!
// 
const propsRef = toRefs(props);
// 
// 

const { handleSubmit, handleReset, setFieldError, setValues } = useForm({
    validationSchema: makeValidShema(),
});

const submit = handleSubmit(async (values) => {
    const formData = makeFormData(values);
    emits('beforeRequest', formData);

    try {
        switch (propsRef.form.value.type) {
            case 'add':
                await addBook(formData);
                break;

            case 'update':
                await setBook(propsRef.initialValues.value.isbn, formData);
                break;

            default:
                break;
        }

        const isbn = values.isbn || propsRef.initialValues.value.isbn;
        emits('afterResponse', true, isbn);
    }
    catch (error) {
        alert('Error at [create/update] new book!');

        emits('afterResponse', false, undefined);
    }
});

function reset() {
    handleReset();
    setValues(propsRef.initialValues.value);
    emits('resetForm');
}

function makeValidShema() {
    const schema = {};
    propsRef.schema.value.forEach(element => {
        if (propsRef.exclude.value.indexOf(element.name) == -1) {
            schema[element.name] = element.validationRules;
        }
    });

    return schema;
}

function makeFormData(values) {
    const formData = new FormData();

    switch (propsRef.form.value.type) {
        case 'add':
            formData.append('isbn', values.isbn);
            formData.append('title', values.title);
            formData.append('page', values.page);
            formData.append('state', values.state);

            values.author.forEach(element => {
                formData.append('author', element);
            });
            values.category.forEach(element => {
                formData.append('category', element)
            });

            formData.append('image', values.image[0]);
            break;

        case 'update':
            values.title != propsRef.initialValues.value.title ?
                formData.append('title', values.title)
                :
                null;

            values.page != propsRef.initialValues.value.page ?
                formData.append('page', values.page)
                :
                null;

            values.state != propsRef.initialValues.value.state ?
                formData.append('state', values.state)
                :
                null;

            JSON.stringify(values.author.sort()) != JSON.stringify(propsRef.initialValues.value.author.sort()) ?
                values.author.forEach(element => {
                    formData.append('author', element);
                })
                :
                null;

            JSON.stringify(values.category.sort()) != JSON.stringify(propsRef.initialValues.value.category.sort()) ?
                values.category.forEach(element => {
                    formData.append('category', element);
                })
                :
                null;

            values.image[0].size !=  0 ?
                formData.append('image', values.image[0])
                :
                null;
            break;
    
        default:
            break;
    }

    return formData;
}

function checkState(name, type, state) {
    if (propsRef.exclude.value.indexOf(name) == -1 && type == state) {
        return true
    }
    return false;
}

watch(
    () => propsRef.initialValues.value,
    () => {
        console.log('\n\nwatcher in FromAddBookComponent worked!\n');
        setValues(propsRef.initialValues.value);
    },
    {immediate: true, deep: true}
);

onMounted(() => {
    console.log('onMounted `FormAddBookComponent!`')
    console.log('\n\npropsRef (in Mounted): ', propsRef.initialValues.value);
});
</script>

<template>
    <v-card
    elevation="4"
    rounded
    >
        <v-form
        @submit="submit"
        @reset="reset"
        class="mx-9 my-7"
        >
            <template v-for="field in props.schema">
                <TextComponent
                v-if="checkState(field.name, field.type, 'text')"
                :name="field.name"
                :label=field.label

                :readonly="propsRef.form.value.readonly"
                ></TextComponent>

                <SelectComponent
                v-else-if="checkState(field.name, field.type, 'select')"
                :name="field.name"
                :label="field.label"
                :func-request="field.funcRequest"
                :multiple="field.multiple"

                :readonly="propsRef.form.value.readonly"
                ></SelectComponent>

                <FileComponent
                v-else-if="checkState(field.name, field.type, 'file')"
                :name="field.name"
                :label="field.label"

                :readonly="propsRef.form.value.readonly"
                :clearable="!propsRef.form.value.readonly"
                ></FileComponent>
            </template>

            <div
            class="d-flex justify-end pt-2"
            >
                <v-btn
                type="reset"
                color="error"
                :disabled="propsRef.form.value.readonly"
                >
                    Cancel
                </v-btn>

                <v-btn
                type="submit"
                color="success"
                :disabled="propsRef.form.value.readonly"
                >
                    Ok
                </v-btn>
        </div>
        </v-form>
    </v-card>
</template>

<style scoped>
</style>
