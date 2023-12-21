<script setup>
import { useForm } from 'vee-validate';
import * as yup from 'yup';

import TestInput from './TestInput.vue';

import TextComponent from './TextComponent.vue';
import SelectComponent from './SelectComponent.vue';
import FileComponent from './FileComponent.vue'

const props = defineProps({
    initialValues: {
        type: Object,
        default: {
            name1: 'Default `name1` value'
        }
    }
});

const { handleSubmit, handleReset } = useForm({
    validationSchema: {
        name1: yup.string().required(),

        text1: yup.string().min(2).max(30).required(),
        select1: yup.string().required(),
        select2: yup.array().length(2),
        file1: yup.array().length(1),
    },
    initialValues: props.initialValues,
});

const submit = handleSubmit((values) => {
    console.log(values)
});
</script>

<template>
    <v-container fluid>
        <v-row class="w-50 mx-auto">
            <v-col>
                <v-form @submit="submit" @reset="handleReset">
                    <TestInput
                    name="name1"
                    ></TestInput>


                    <TextComponent
                    name="text1"
                    ></TextComponent>

                    <SelectComponent
                    name="select1"
                    func-request="state"
                    ></SelectComponent>

                    <SelectComponent
                    name="select2"
                    func-request="author"
                    :multiple="true"
                    ></SelectComponent>

                    <FileComponent
                    name="file1"
                    ></FileComponent>

                    <div class="d-flex justyfi-end">
                        <v-btn type="reset">Reset</v-btn>
                        <v-btn type="submit">Submit</v-btn>
                    </div>
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<style scoped>
</style>
