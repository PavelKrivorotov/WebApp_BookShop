<script setup>
import { ref, reactive } from 'vue'

import { useForm, useField } from 'vee-validate'
import * as yup from 'yup'


const { handleSubmit, handleReset, errors } = useForm({
	validationSchema: yup.object({
		firstName: yup.string().required('This is required field!'),
		lastName: yup.string().required('This is required field!'),
		email: yup.string().email('TRhis is invalid E-mail address!').required('This is required field!'),
		password: yup.string().required('This is required field!'),
	})
});

const firstName = useField('firstName')
const lastName = useField('lastName')
const email = useField('email')
const password = useField('password')

const submit = handleSubmit(values => {
	console.log(JSON.stringify(values, null, 2))
});

const reset = handleReset()
</script>

<template>
	<v-container class="fill-height w-50" fluid>
		<v-row >
			<v-col>
				<v-card
				elevation="4"
				rounded
				>
					<v-form @submit=submit @reset=reset class="mx-9 my-7">
						<v-text-field
						label="Name"
						v-model="firstName.value.value"
						:error-messages="firstName.errorMessage.value"
						></v-text-field>

						<v-text-field
						label="Surname"
						v-model="lastName.value.value"
						:error-messages="lastName.errorMessage.value"
						></v-text-field>

						<v-text-field
						label="Email"
						v-model="email.value.value"
						:error-messages="email.errorMessage.value"
						></v-text-field>

						<v-text-field
						label="Password"
						type="password"
						v-model="password.value.value"
						:error-messages="password.errorMessage.value"
						></v-text-field>

						<div class="d-flex justify-end">
							<v-btn type="reset" color="error">Reset</v-btn>
							<v-btn type="submit" color="success">Submit</v-btn>
						</div>
					</v-form>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>

<style scoped>
</style>
