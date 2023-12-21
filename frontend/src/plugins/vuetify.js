import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css'

import { createVuetify } from "vuetify";
import { md1 } from 'vuetify/blueprints'

import { VApp } from 'vuetify/components/VApp'
import { VMain } from 'vuetify/components/VMain'
import { VAppBar, VAppBarNavIcon, VAppBarTitle } from 'vuetify/components/VAppBar'
import { VContainer, VRow, VCol, VSpacer } from 'vuetify/components/VGrid'
import { VBtn } from 'vuetify/components/VBtn'
import { VIcon } from 'vuetify/components/VIcon'
import { VCard, VCardItem, VCardActions, VCardText } from 'vuetify/components/VCard'
import { VImg } from 'vuetify/components/VImg'
import { VForm } from 'vuetify/components/VForm'
import { VTextField } from 'vuetify/components/VTextField';
import { VSelect } from 'vuetify/components/VSelect'
import { VFileInput } from 'vuetify/components/VFileInput';
import { VOverlay } from 'vuetify/components/VOverlay'
import { VProgressCircular } from 'vuetify/components/VProgressCircular'
import { VDialog } from 'vuetify/components/VDialog'
import { VToolbar, VToolbarTitle } from 'vuetify/components/VToolbar'
import { VFooter } from 'vuetify/components/VFooter'
import { VPagination } from 'vuetify/components/VPagination'
import { VMenu } from 'vuetify/components/VMenu';
import { VList, VListItem } from 'vuetify/components/VList';
import { VRadioGroup } from 'vuetify/components/VRadioGroup';
import { VRadio } from 'vuetify/components/VRadio';

const vuetify = createVuetify({
    blueprint: md1,
    components: {
        VApp,

        VAppBar,
        VAppBarNavIcon,
        VAppBarTitle,

        VMain,

        VContainer,
        VRow,
        VCol,
        VSpacer,

        VBtn,

        VIcon,

        VCard,
        VCardItem,
        VCardActions,
        VCardText,

        VImg,

        VForm,
        VTextField,
        VSelect,
        VFileInput,

        VOverlay,
        VProgressCircular,

        VDialog,

        VToolbar,
        VToolbarTitle,

        VFooter,

        VPagination,
        
        VMenu,

        VList,
        VListItem,

        VRadioGroup,
        VRadio,
    },

    icons: {
        defaultSet: 'mdi',
    },

    defaults: {
        VBtn: {
            rounded: true,
        }
    },

    theme: {
        defaultTheme: 'light',
    },
});

export default vuetify;
