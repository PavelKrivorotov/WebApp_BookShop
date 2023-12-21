<script setup>
</script>

<template>
    <RouterView v-slot="{ Component }">
        <KeepAlive :include="['BookAddViewComponent']">
            <component :is="Component" />
        </KeepAlive>
    </RouterView>
</template>

<style scoped>
</style>
