import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import SalePage from '../components/SalePage.vue';
import ProductPage from '../components/ProductPage.vue';
import PurchasePage from '../components/PurchasePage.vue';
import AnnouncementPage from '../components/AnnouncementPage.vue';
import CommentPage from '../components/CommentPage.vue';

const routes = [
  // {
  //   path: '/',
  //   redirect: '/home' // 添加重定向规则
  // },
  {
    path: '/home',
    name: 'home',
    component: HomePage
  },
  {
    path: '/sale',
    name: 'sale',
    component: SalePage
  },
  {
    path: '/product',
    name: 'product',
    component: ProductPage
  },
  {
    path: '/purchase',
    name: 'purchase',
    component: PurchasePage
  },
  {
    path: '/announcement',
    name: 'announcement',
    component: AnnouncementPage
  },
  {
    path: '/comment',
    name: 'comment',
    component: CommentPage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
