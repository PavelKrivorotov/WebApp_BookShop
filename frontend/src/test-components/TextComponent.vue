<script setup>
import { useField } from 'vee-validate'

const props = defineProps({
    name: String,
    label: {
        type: String,
        default: 'Custom TextComponent'
    },
});

const { value, errorMessage } = useField(() => props.name);
</script>

<template>
    <v-text-field
    :label="props.label"
    v-model="value"
    :error-messages="errorMessage"
    ></v-text-field>
</template>

<style>
</style>
