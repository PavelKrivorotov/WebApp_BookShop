import { createRouter, createWebHistory } from 'vue-router'

import HomePage from '../views/HomePage.vue'
import BookPage from '../views/BookPage.vue'
import AboutPage from '../views/AboutPage.vue'

import BookViewComponent from '../components/BookViewComponent.vue';
import BookAddViewComponent from '../components/BookAddViewComponent.vue'
import BookRetrieveViewComponent from '../components/BookRetrieveViewComponent.vue';

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: '/',
			name: 'home',
			component: HomePage
		},
		{
			path: '/books',
			name: 'books',
			component: BookPage,
			redirect: {
				name: 'book-view',
				query: {
					page: 1,
				}
			},
			children: [
				{
					path: 'list',
					name: 'book-view',
					component: BookViewComponent,
				},
				{
					path: 'add',
					name: 'book-add',
					component: BookAddViewComponent,
				},
				{
					path: 'book/:isbn',
					name: 'book-retrieve',
					component: BookRetrieveViewComponent,
				}
			]
		},
		{
			path: '/about',
			name: 'about',
			component: AboutPage
		}
	]
})

export default router
