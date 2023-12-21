<script setup>
import { useField } from 'vee-validate';
import { DEFAULT_PAGE_SIZE_RADIO_GROP } from '../settings';

const props = defineProps({
    name: String,
    label: {
        type: String,
        default: 'Custom radio group',
    },
    inline: {
        type: Boolean,
        default: true,
    },
    class: {
        type: String,
        default: 'ml-n4',
    },
    schema: {
        type: Array,
        default: [
            {
                name: 'radio-1',
                label: '5',
                value: DEFAULT_PAGE_SIZE_RADIO_GROP['5'],
            },
            {
                name: 'radio-2',
                label: '10',
                value: DEFAULT_PAGE_SIZE_RADIO_GROP['10'],
            },
            {
                name: 'radio-3',
                label: '15',
                value: DEFAULT_PAGE_SIZE_RADIO_GROP['15'],
            },
        ]
    }
});

const { value, errorMessage } = useField(() => props.name);
</script>

<template>
    <v-radio-group
    :label="props.label"
    v-model="value"
    :error-messages="errorMessage"
    :inline="props.inline"
    :class="props.class"
    >
        <v-radio
        v-for="field in props.schema"
        :name="field.name"
        :label="field.label"
        :value="field.value"
        ></v-radio>
    </v-radio-group>
</template>

<style scoped>
</style>
