<script setup>
import { ref } from 'vue';
import { useField } from 'vee-validate';

const props = defineProps({
    name: String,
    modelValue: String,
});

const emits = defineEmits([
    'update:modelValue',
]);

const { value, errorMessage } = useField(() => props.name);
</script>

<template>
    <v-text-field
    label="Custom input"
    v-model="value"
    :error-messages="errorMessage"
    @update:modelValue="emits('update:modelValue', value)"
    ></v-text-field>
</template>

<style scoped>
</style>
