<style scoped>
.el-menu {
  margin-top: 0;
  margin-bottom: 0;
  padding-left: 24px;
  padding-right: 24px;
  color: #274C5B;
  position: fixed; /* 设置菜单固定定位 */
  top: 0; /* 距离页面顶部的距离为 0 */
  left: 0; /* 距离页面左侧的距离为 0 */
  width: 100%; /* 宽度占满整个页面 */
  z-index: 1000; /* 确保菜单在其他内容之上 */
  background-color: rgba(255, 255, 255, 0.9); /* 背景颜色 */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
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

.addproduct {
  margin-top: 10px;
}
.addproduct > div {
  margin-bottom: 10px;
}
.product-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
.product {
  border: 1px solid #ddd;
  margin: 10px;
  padding: 10px;
  width: 200px;
  text-align: center;
}
.product-image {
  width: 150px;
  height: 150px;
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
    <img src="../assets/productBanner.png" width="100%">
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 50%; text-align: center;">
    <p style="font-size: 56px; color: #274C5B; font-weight: bold; margin: 0; text-align: center;">
      PRODUCT
    </p>
  </div>
  </div>

  <el-button v-if="!showProductInputFields" type="primary" @click="toggleProductInputFields"
        style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
        ADD
      </el-button>

      <div v-else class="addproduct">
        <div>
          <input type="text" v-model="Name" placeholder="Product Name" required>
        </div>
        <div>
          <input type="text" v-model="Description" placeholder="Description" required>
        </div>
        <div>
          <input type="number" v-model="Price" placeholder="Price" required>
        </div>
        <div>
          <input type="file" @change="handleFileUpload" accept="image/*" required>
        </div>
        <el-button type="primary" @click="addProduct"
          style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
          Confirm
        </el-button>
        <el-button type="primary" @click="toggleProductInputFields"
          style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
          Cancel
        </el-button>
      </div>

      <div class="product-list" style="width: 100%;">
        <div v-for="product in products" :key="product.id" class="product"
          style="background-color: #DEDDDD; border-radius: 10px; margin: 10px;">
          <img :src="'data:image/jpeg;base64,' + product.image" alt="Product Image" class="product-image" />
          <div class="product-info">
            <h2 style="font-weight: bold; color: #274C5B;">{{ product.name }}</h2>
            <p style="font-weight: bold; color: #7EB693;">{{ formatCurrency(product.price) }}</p>
          </div>

          <el-button type="primary" @click="deleteProducts(product.id)"
            style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
            Delete
          </el-button>
          <el-button type="primary" v-if="!product.editing" @click="editProduct(product)"
            style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
            Edit
          </el-button>

          <div v-else>
            <input type="text" v-model="product.name" placeholder="Product Name">
            <input type="text" v-model="product.description" placeholder="Description">
            <input type="number" v-model="product.price" placeholder="Price">
            <input type="file" @change="event => handleFileUpload(event, product)">
            <el-button type="primary" @click="saveChanges(product)"
              style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
              Save
            </el-button>
            <!-- <el-button type="primary" @click="cancelChanges(product)"
              style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
              Cancel
            </el-button> -->
          </div>
        </div>
      </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeIndex = ref('product')

const handleSelect = (index) => {
  activeIndex.value = index
  router.push({ name: index })
}
</script>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      products: [],
      showProductInputFields: false,
      Name: '',
      Description: '',
      Price: '',
      Image: ''
    };
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:5000/products/select')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    formatCurrency(value) {
      return `$${value.toFixed(2)}`;
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
    handleFileUpload(event, product = null) {
      const file = event.target.files[0];
      const reader = new FileReader();

      reader.onload = (e) => {
        const base64Image = e.target.result.split(',')[1];
        if (product) {
          product.editingImage = base64Image; // 将图片转换为Base64编码并存储在产品对象中
        } else {
          this.Image = base64Image; // 将图片转换为Base64编码并存储在Image中
        }
      };

      reader.readAsDataURL(file); // 读取文件并触发onload事件
    },
    toggleProductInputFields() {
      this.showProductInputFields = !this.showProductInputFields;
    },
    addProduct() {
      const { Name, Description, Price, Image } = this;
      this.addProducts(Name, Description, Price, Image);
    },
    addProducts(name, description, price, image) {
      axios.post('http://127.0.0.1:5000/products/add', { name, description, price, image })
        .then(() => {
          const newProduct = { name, description, price, image, editing: false };
          this.products.push(newProduct);
          this.fetchProducts();
          console.log('Product added successfully.');
        })
        .catch(error => {
          console.error('Error adding product:', error);
        });

      // 重置表单字段
      this.Name = '';
      this.Description = '';
      this.Price = '';
      this.Image = '';
      this.toggleProductInputFields();
    },
    editProduct(product) {
      product.editing = true; // 设置产品为可编辑状态
    },
    saveChanges(product) {
      const { id, name, description, price, image } = product;
      axios.put('http://127.0.0.1:5000/products/update', {id,  name, description, price, image })
        .then(() => {
          product.editing = false; // 将产品设为不可编辑状态
          console.log('Product updated successfully.');
        })
        .catch(error => {
          console.error('Error updating product:', error);
        });
    },
    cancelChanges(product) {
      console.log(product);
      product.editing = false; // 取消编辑状态
      console.log(product);
      console.log('hello');
    }
  }
};
</script>