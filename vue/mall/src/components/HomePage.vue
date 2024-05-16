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

.button {
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
}

.image-container {
  position: relative;
  margin: 0 10px; /* 图片之间的间距 */
}

.image {
  max-width: 500px; 
  height: auto; 
}

.text-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-90%, -50%);
  font-size: 24px;
  font-weight: bold; 
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
    <div class="image-container">
      <img src="../assets/announcement1.png" alt="Image 1" class="image">
      <div class="text-overlay">announcement</div>
    </div>
    <div class="image-container">
      <img src="../assets/announcement2.png" alt="Image 2" class="image">
      <div class="text-overlay">announcement</div>
    </div>
  </div>

  <div>
    <div style="position: relative;">
      <el-table :data="sales" stripe style="width: 100%; color: #274C5B; font-weight: bold;">
        <el-table-column prop="sales_date" label="Date"></el-table-column>
        <el-table-column prop="amount" label="Amount"></el-table-column>
      </el-table>
      <el-button class="button" type="primary" @click="goToSalePage">MORE</el-button>
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
          this.announcements_detail = response.data;
        })
        .catch(error => {
          console.error('Error fetching announcements:', error);
        });
    },
    fetchProducts() {
      axios.get('http://127.0.0.1:5000/products/select')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    deleteProducts(productId) {
      axios.post('http://127.0.0.1:5000/products/delete', { id: productId })
        .then(() => {
          this.products = this.products.filter(product => product.id !== productId);
          console.log('Product deleted successfully.');
        })
        .catch(error => {
          console.error('Error deleting product:', error);
        });
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = (e) => {
        this.Image = e.target.result; // 将图片转为Base64编码并存储在Image中
      };

      reader.readAsDataURL(file); // 读取文件并触发onload事件
    },
    addProduct() {
      const { Name, Description, Price, Image } = this;
      this.addProducts(Name, Description, Price, Image);
    },

    addProducts(name, description, price, image) {
      axios.post('http://127.0.0.1:5000/products/add', { name, description, price, image })
        .then(() => {
          const newProduct = { name, description, price, image };
          this.products.push(newProduct);
          this.fetchProducts();
          console.log('Product added successfully.');
        })
        .catch(error => {
          console.error('Error adding product:', error);
        });
    },
    editProduct(product) {
      product.editing = true; // 设置产品为可编辑状态
    },

    saveChanges(product) {
      const { id, name, description, price, image } = product;
      axios.put(`http://127.0.0.1:5000/products/update/${id}`, { name, description, price, image })
        .then(() => {
          product.editing = false; // 将产品设为不可编辑状态
          console.log('Product updated successfully.');
        })
        .catch(error => {
          console.error('Error updating product:', error);
        });
    },

    cancelChanges(product) {
      product.editing = false; // 取消编辑状态
    }
  }
};</script>
