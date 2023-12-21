<script setup>
import { useField } from 'vee-validate';

const props = defineProps({
    name: String
});

const { value, errorMessage } = useField(() => props.name);
</script>

<template>
    <v-text-field
    label="Test field"
    v-model="value"
    :error-messages="errorMessage"
    ></v-text-field>
</template>

<style scoped>
</style>
