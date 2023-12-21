<script setup>
import { ref, watch, onMounted } from 'vue'
import { useField } from 'vee-validate';

import { getAuthors, getCategoryes } from '../http/request'

const props = defineProps({
    name: String,
    label: {
        type: String,
        default: 'CustomSelectComponent'
    },
    multiple: {
        type: Boolean,
        default: false,
    },
    funcRequest: String,
});

const isLoading = ref(true);
const defaultItems = ref([]);
const { value, errorMessage } = useField(() => props.name)

function setDefaultValues() {
    if (props.multiple) {
        const validItems = [];

        if (value.value) {
            if (defaultItems.value.length) {
                defaultItems.value.forEach(element1 => {
                    // If value.value is `undefined` or `null`???
                    value.value.forEach(element2 => {
                        if (element2 == element1.value) {
                            validItems.push(element2);
                        }
                    });
                });

                if (JSON.stringify(value.value.sort()) != JSON.stringify(validItems.sort())) {
                    value.value = validItems;
                }
            }
        }
    }
    else {
        // if (value.value) --> always is True??? 
        if (value.value) {
            let validItem = null;
            defaultItems.value.forEach(element => {
                if (value.value == element.value) {
                    validItem = element.value;
                }
            });
            value.value = validItem;
        }
    }
}

async function setDefaultItems() {
    try {
        var data = null;
        var _value = 'id';
        var _text = 'name';

        switch (props.funcRequest) {
            case 'author':
                _text = 'name';
                data = await getAuthors();
                break;
            
            case 'category':
                _text = 'title';
                data = await getCategoryes();
                break;

            case 'state':
                _text = 'title'
                data = {
                    results: [
                        {id: 'PUBLISH', title: 'PUBLISH'},
                        {id: 'UNPUBLISH', title: 'UNPUBLISH'},
                        {id: 'NEW', title: 'NEW'},
                    ],
                };
        }

        data.results.forEach(element => {
            defaultItems.value.push({
                value: element[_value],
                text: element[_text],
            });
        });
    }
    catch (error) {
        console.error(error);
    }
    finally {
        setDefaultValues();
        isLoading.value = false;
    }
}

watch(
    () => value.value,
    (newValue, oldValue) => {
        setDefaultValues();
    },
);

onMounted(async () => {
    console.log('Mounted in SelectComponent')

    isLoading.value = true;
    await setDefaultItems();
});
</script>

<template>
    <v-select
    :label="props.label"
    v-model="value"
    :error-messages="errorMessage"
    :items="defaultItems"
    item-title="text"
    item-value="value"
    :multiple="props.multiple"
    :loading="isLoading"
    :disabled="isLoading"
    ></v-select>
</template>

<style scoped>
</style>
