<style scoped>
.el-menu {
  margin-top: 0;
  margin-bottom: 0;
  padding-left: 24px;
  padding-right: 24px;
  color: #274C5B;
  position: fixed;
  /* 设置菜单固定定位 */
  top: 0;
  /* 距离页面顶部的距离为 0 */
  left: 0;
  /* 距离页面左侧的距离为 0 */
  width: 100%;
  /* 宽度占满整个页面 */
  z-index: 1000;
  /* 确保菜单在其他内容之上 */
  background-color: rgba(255, 255, 255, 0.9);
  /* 背景颜色 */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  /* 添加阴影效果 */
}

.logo-title {
  display: flex;
  align-items: center;
}

.logo {
  width: 40px;
  height: 45px;
  margin-right: 10px;
}

.title {
  margin: 0;
  font-size: 20px;
}

.flex-grow {
  flex-grow: 1;
}

.el-menu-item {
  font-weight: bold;
}

.buttons-edit {
  margin-top: 24px;
  font-weight: bold;
  color: #274C5B;
  background-color: #EFD372;
  float: right;
  border: 1px solid #EFD372;
}

.announcement-image {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 10px;
}

.image-container {
  position: relative;
  margin: 0 100px;
  /* 图片之间的间距 */
}

.image {
  max-width: 500px;
  height: auto;
}

.text-overlay {
  position: absolute;
  top: 50%;
  left: 40%;
  transform: translate(-90%, -50%);
  font-size: 24px;
  font-weight: bold;
}

.container {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
  /* 将背景图像放置在底层 */
}

.product-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  /* 水平居中 */
  align-items: center;
  /* 垂直居中 */
  z-index: 1;
  /* 将产品列表放置在上层 */
}

.product {
  border: 1px solid #ddd;
  margin: 10px;
  padding: 10px;
  width: 200px;
  text-align: center;
}

.product-image {
  width: 100%;
  height: auto;
}

.product-info {
  margin-top: 10px;
}
</style>

<template>
  <el-menu :default-active="activeIndex" class="el-menu" mode="horizontal" :ellipsis="false" @select="handleSelect">
    <div class="logo-title">
      <img src="../assets/Logo.png" alt="Logo" class="logo" />
      <h1 class="title">FRUITY ROBO</h1>
    </div>
    <div class="flex-grow" />
    <el-menu-item index="home" :style="{ color: '#274C5B' }">Home</el-menu-item>
    <el-menu-item index="announcement" :style="{ color: '#274C5B' }">Announcement</el-menu-item>
    <el-menu-item index="product" :style="{ color: '#274C5B' }">Product</el-menu-item>
    <el-menu-item index="purchase" :style="{ color: '#274C5B' }">Purchase</el-menu-item>
    <el-menu-item index="sale" :style="{ color: '#274C5B' }">Sale</el-menu-item>
    <el-menu-item index="comment" :style="{ color: '#274C5B' }">Comment</el-menu-item>
  </el-menu>
  <div style="position: relative; width: 100%;margin-top: 64px;">
    <img src="../assets/homeBanner.jpg" width="100%">
    <div
      style="position: absolute; top: 50%; left: 30%; transform: translate(-50%, -50%); width: 50%; text-align: center;">
      <p style="font-size: 56px; color: #274C5B; font-weight: bold; margin: 0; text-align: left;">
        FRUITY ROBO
      </p>
      <p style="font-size: 42px; color: #7EB693; font-weight: bold; margin:20px 0; text-align: left;">
        OPERATIONS MONITORING
      </p>
    </div>
  </div>
  <div class="announcement-image">
    <div v-if="announcements_detail.length > 0" class="image-container">
      <img src="../assets/announcement1.png" alt="Image 1" class="image">
      <div class="text-overlay" @click="goToAnnouncementPage" style="color: whitesmoke;">{{
    announcements_detail[0].title }}</div>
    </div>
    <div v-if="announcements_detail.length > 0" class="image-container">
      <img src="../assets/announcement2.png" alt="Image 1" class="image">
      <div class="text-overlay" @click="goToAnnouncementPage" style="color: #274C5B;">{{ announcements_detail[1].title
        }}</div>
    </div>
  </div>

  <div class="container" style="margin-top: 10px; display: flex; flex-direction: column; align-items: center;">
    <img src="../assets/Background.png" alt="Background" class="background-image" />
    <h1 style="color: whitesmoke; font-weight: bold; margin-top: 10px;padding-bottom: 20px;">Product</h1>
    <div class="product-list" style="width: 100%;">
      <div v-for="product in products" :key="product.id" class="product"
        style="background-color: #DEDDDD; border-radius: 10px; margin: 30px;">
        <img :src="'data:image/jpeg;base64,' + product.image" alt="Product Image" class="product-image" />
        <div class="product-info">
          <h2 style="font-weight: bold; color: #274C5B;">{{ product.name }}</h2>
          <p style="font-weight: bold; color: #7EB693;">{{ formatCurrency(product.price) }}</p>
        </div>
      </div>
    </div>
    <div style="text-align: center; margin-top: 10px; padding-top: 40px;">
      <el-button type="primary" @click="goToProductPage"
        style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">MORE</el-button>
    </div>
  </div>

  <div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color: #274C5B;">Procurement List</h1>
      <div style="position: relative; text-align: right;">
        <el-button type="primary" @click="goToPurchasePage"
          style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372; margin-top: 24px;">MORE</el-button>
      </div>
    </div>
    <div style="position: relative;">
      <el-table :data="purchases" stripe style="width: 100%; color: #274C5B; font-weight: bold;">
        <el-table-column prop="purchase_date" label="Date"></el-table-column>
        <el-table-column prop="name" label="Name"></el-table-column>
        <el-table-column prop="amount" label="Amount"></el-table-column>
      </el-table>
    </div>
  </div>
  <div>
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color: #274C5B;">Sales</h1>
      <el-button type="primary" @click="goToSalePage" class="buttons-edit">MORE</el-button>
    </div>
    <div style="position: relative;">
      <el-table :data="sales" stripe style="width: 100%; color: #274C5B; font-weight: bold;">
        <el-table-column prop="sales_date" label="Date"></el-table-column>
        <el-table-column prop="amount" label="Amount"></el-table-column>
      </el-table>
    </div>
  </div>
  <div style="position: relative; text-align: center;">
    <img src="../assets/commentBackground.png" width="100%" height="600px">
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%;">
      <h1 style="color: #274C5B;">What do customers say about us?</h1>
      <div style="color: #7EB693; font-weight: bold; font-size: 20px; margin: 40px 0;">
        {{ comments.length > 0 ? comments[0].content : 'No comments available' }}
      </div>
      <el-button type="primary" @click="goToCommentPage"
        style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">MORE</el-button>
    </div>
  </div>

</template>


<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue';

const router = useRouter()
const activeIndex = ref('home')

const handleSelect = (index) => {
  activeIndex.value = index
  router.push({ name: index })
}

const goToSalePage = () => {
  router.push({ name: 'sale' });
}

</script>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      sales: [],
      purchases: [],
      comments: [],
      announcements_detail: [],
      products: [],
      Name: '',
      Description: '',
      Price: ''
    };
  },
  created() {
    this.fetchSales();
    this.fetchPurchases();
    this.fetchComments();
    this.detailAnnouncements();
    this.fetchProducts();
  },
  methods: {
    fetchSales() {
      axios.get('http://localhost:5000/sales')
        .then(response => {
          this.sales = response.data.slice(0, 5);
        })
        .catch(error => {
          console.error('Error fetching sales:', error);
        });
    },
    goToSalePage() {
      this.$router.push({ name: 'sale' });
    },
    goToPurchasePage() {
      this.$router.push({ name: 'purchase' });
    },
    goToAnnouncementPage() {
      this.$router.push({ name: 'announcement' });
    },
    goToCommentPage() {
      this.$router.push({ name: 'comment' });
    },
    goToProductPage() {
      this.$router.push({ name: 'product' });
    },
    fetchPurchases() {
      axios.get('http://localhost:5000/purchases')
        .then(response => {
          this.purchases = response.data.slice(0, 5);
        })
        .catch(error => {
          console.error('Error fetching purchases:', error);
        });
    },
    fetchComments() {
      axios.get('http://127.0.0.1:5000/comments')
        .then(response => {
          this.comments = response.data;
        })
        .catch(error => {
          console.error('Error fetching comments:', error);
        });
    },
    deleteComment(commentId) {
      axios.post('http://127.0.0.1:5000/comments/delete', { id: commentId })
        .then(() => {
          // If successful, remove the deleted comment from the UI
          this.comments = this.comments.filter(comment => comment.id !== commentId);
          console.log('Comment deleted successfully.');
        })
        .catch(error => {
          console.error('Error deleting comment:', error);
        });
    },
    detailAnnouncements() {
      axios.get('http://localhost:5000/announcements/detail')
        .then(response => {
          this.announcements_detail = response.data.slice(0,2);
        })
        .catch(error => {
          console.error('Error fetching announcements:', error);
        });
    },
    fetchProducts() {
      axios.get('http://127.0.0.1:5000/products/select')
        .then(response => {
          this.products = response.data.slice(0, 4);
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    formatCurrency(value) {
      return `$${value.toFixed(2)}`;
    }
  }
};</script>
