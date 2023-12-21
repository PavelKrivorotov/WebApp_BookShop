<!-- <script setup>
import { ref, reactive } from "vue";

import LoadingComponent from '../components/LoadingComponent.vue'
import TestForm from '../test-components/TestForm.vue';

const initialConfig = reactive({
    name1: 'New `name1` from initialConfig',

    text1: 'Initial from `text1`',
    // select1: 1,
    select1: 'PUBLISH',
    select2: [2, 3],

    file1: 'http://127.0.0.1:8000/images/download/night_house_hcdj1Ev.jpg',
    // file1: [new File(
    //     [],
    //     'night_house_hcdj1Ev.jpg',
    //     {
    //         type: 'image/*',
    //         lastModyfied: new Date().getTime(),
    //     },
    //     'utf-8'
    // )],
});


const activeLoading = ref(false)
</script> -->



<script setup>
import { ref, reactive, computed } from "vue";
import FileComponent from '../test-components/FileComponent.vue';

const file1 = ref(null);
const file1Url = ref(null);

function fileToUrl(file) {
    console.log(file[0]);

    const reader = new FileReader();
    reader.onload = e => {
      file1Url.value = e.target.result;
    };
    
    reader.readAsDataURL(file[0]);
}
</script>

<template>

</template>

<style scoped>
.add-relative-position {
    background-color:red;
    position:relative;
}
</style>
