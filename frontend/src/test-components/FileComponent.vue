<script setup>
import { watch } from 'vue';
import { useField } from 'vee-validate';

import { REGEXP_IMAGE_URL } from "../settings";

const props = defineProps({
    name: String,
    label: {
        type: String,
        default: 'CustomFileInput',
    },
});

const { value, errorMessage } = useField(() => props.name)

watch(
    () => value.value,
    () => {
        if (REGEXP_IMAGE_URL.test(value.value)) {
            const fileObject = makeFileObject(value.value);
            value.value = [fileObject];
        }
    },
    {immediate: true},
);

function makeFileObject(stringUrl) {
    // Firstly RegExp (/^http[s]{0,1}:\/\/127.0.0.1:8000\/images\/download\/[A-za-z0-9_]{1,}\.[a-z]{1,}$/)
    const splitPath = stringUrl.split('/');
    const fileObject = new File(
        [],
        splitPath[splitPath.length - 1],
        {
            type: 'image/*',
            lastModyfied: new Date().getTime(),
        },
        'utf-8'
    );

    return fileObject;
}
</script>

<template>
    <v-file-input
    :label="props.label"
    v-model="value"
    :error-messages="errorMessage"
    variant="underlined"
    prepend-icon=""
    >
        <template v-slot:message>
            <div class="ml-n4">
                {{ errorMessage }}
            </div>
        </template>
    </v-file-input>
</template>

<style>
</style>
