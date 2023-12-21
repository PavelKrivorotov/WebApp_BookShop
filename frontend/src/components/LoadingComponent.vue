<script setup>
const props = defineProps({
   'isActive': Boolean,
})
</script>

<template>
    <div>
        <v-overlay
        :model-value="props.isActive"
        contained
        class="align-center justify-center"
        scrim="#F5F5F5"
        >
            <v-progress-circular
            color="primary"
            size="64"
            indeterminate
            ></v-progress-circular>
        </v-overlay>
    </div>
</template>

<style scoped>
</style>
