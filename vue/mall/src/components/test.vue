<template>
  <div>
    <div>
      <h1>Sales List</h1>
      <ul>
        <li v-for="sale in sales" :key="sale.id">
          {{ sale.id }} (Amount: {{ sale.amount }})
        </li>
      </ul>
    </div>
    <div>
      <h1>Comments List</h1>
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          {{ comment.id }} (Date: {{ comment.comment_date }} - Content: {{ comment.content }})
          <button @click="deleteComment(comment.id)">Delete</button>
        </li>
      </ul>
    </div>
    <div>
      <h1>Announcements_detail List</h1>
      <ul>
        <li v-for="announcement_detail in announcements_detail" :key="announcement_detail.id">
          {{ announcement_detail.id }} (Title: {{ announcement_detail.title }})
        </li>
      </ul>
    </div>
    <div>
  <h1>Products List</h1>
  <ul>
    <li v-for="product in products" :key="product.id">
      <div v-if="product.editing">
        <input type="text" v-model="product.name" placeholder="Name">
        <input type="text" v-model="product.description" placeholder="Description">
        <input type="number" v-model="product.price" placeholder="Price">
        <input type="text" v-model="product.image" placeholder="Image">
        <button @click="saveChanges(product)">Save</button>
        <button @click="cancelChanges(product)">Cancel</button>
      </div>
      <div v-else>
        {{ product.id }} (Name: 
        <span @click="editProduct(product)" style="cursor: pointer; pointer-events: auto;">{{ product.name }}</span>
        - Price: {{ product.price }})
        <img :src="product.image" alt="Product Image" style="max-width: 100px; max-height: 100px;"
          @click="editProduct(product)">
          <button @click="deleteProducts(product.id)">Delete</button>
      </div>
    </li>
  </ul>
</div>

    <div class="add-product-form">
      <h2>Add Product</h2>
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
        <input type="text" v-model="Image" placeholder="Image" required>
        <input type="file" @change="handleFileUpload" accept="image/*" required>
      </div>
      <div>
        <button @click="addProduct" class="add-button">Add Product</button>
      </div>
    </div>

    <el-row class="mb-4">
      <el-button round>Round</el-button>
      <el-button type="primary" round>Primary</el-button>
      <el-button type="success" round>Success</el-button>
      <el-button type="info" round>Info</el-button>
      <el-button type="warning" round>Warning</el-button>
      <el-button type="danger" round>Danger</el-button>
    </el-row>
  </div>
</template>

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
          this.sales = response.data;
        })
        .catch(error => {
          console.error('Error fetching sales:', error);
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
};
</script>
