<script setup>
</script>

<template id="app">
	<v-app>
		<v-app-bar :elevation="1">
			<template v-slot:prepend>
				<v-btn prepend-icon="mdi-home" to="/">Home</v-btn>
				<v-menu
				open-on-hover
				>
					<template v-slot:activator="{ props }">
						<v-btn
						prepend-icon="mdi-book-multiple"
						type="button"
						v-bind="props"
						>Books</v-btn>
					</template>

					<v-list>
						<v-list-item
						to="/books/add"
						append-icon="mdi-book-plus"
						>Add</v-list-item>

						<v-list-item
						to="/books/list"
						append-icon="mdi-magnify"
						>Search</v-list-item>
					</v-list>
				</v-menu>
				<v-btn prepend-icon="mdi-information" to="/about">about</v-btn>
			</template>
		</v-app-bar>

		<v-main>
			<RouterView />
		</v-main>
	</v-app>
</template>

<style scoped>
</style>
