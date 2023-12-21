<script setup>
const props = defineProps({
    isActive: Boolean,
    title: {
        type: String,
        default: 'Delete dialog',
    },
    text: {
        type: String,
        default: 'Are you shure want to delete this card?'
    },
});

const emits = defineEmits([
    'click:yes',
    'click:no',
]);
</script>

<template>
    <v-dialog
    v-model="props.isActive"
    width="350"
    persistent
    >
        <v-card>
            <template v-slot:title>
                {{ title }}
            </template>

            <v-card-text>
                {{ text }}
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                @click="emits('click:no')"
                >No</v-btn>

                <v-btn
                @click="emits('click:yes')"
                >Yes</v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<style>
</style>
