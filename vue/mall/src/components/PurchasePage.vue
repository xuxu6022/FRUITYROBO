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

.addpurchase {
  font-size: 24px;
  font-weight: bold;
  color: #274C5B;
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
    <img src="../assets/purchaseBanner.jpg" width="100%">
    <div
      style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 50%; text-align: center;">
      <p style="font-size: 56px; color: #274C5B; font-weight: bold; margin: 0; text-align: center;">
        PURCHASE
      </p>
    </div>
  </div>

  <div>
      <el-button v-if="!showInputFields" type="primary" @click="toggleInputFields"
        style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
        ADD
      </el-button>
      <div v-else class="addpurchase">
        <div>
          <input type="text" v-model="Name" placeholder="Name" required>
        </div>
        <div>
          <input type="text" v-model="Description" placeholder="Description" required>
        </div>
        <div>
          <input type="number" v-model="Amount" placeholder="Amount" required>
        </div>
        <div>
          <input type="date" v-model="Purchase_date" placeholder="Purchase_Date" required>
        </div>
        <el-button type="primary" @click="handleAddPurchase"
          style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
          Confirm
        </el-button>
        <el-button type="primary" @click="toggleInputFields"
          style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
          Cancel
        </el-button>
      </div>

    <div style="position: relative;">
      <el-table :data="purchases" stripe style="width: 100%; color: #274C5B; font-weight: bold;">
        <el-table-column prop="purchase_date" label="Date"></el-table-column>
        <el-table-column prop="name" label="Name"></el-table-column>
        <el-table-column prop="amount" label="Amount"></el-table-column>
        <el-table-column label="Operation">
          <template #default="scope">
            <el-button type="primary" @click="deletePurchase(scope.row.id)"
              style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">
              DELETE
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeIndex = ref('purchase')

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
      purchases: [],
      Name: '',
      Description: '',
      Amount: null,
      Purchase_date: '',
      showInputFields: false
    };
  },
  created() {
    this.fetchPurchases();
  },
  methods: {
    fetchPurchases() {
      axios.get('http://localhost:5000/purchases')
        .then(response => {
          this.purchases = response.data;
        })
        .catch(error => {
          console.error('Error fetching purchases:', error);
        });
    },
    toggleInputFields() {
      this.showInputFields = !this.showInputFields;
    },
    deletePurchase(purchaseId) {
      axios.post('http://127.0.0.1:5000/purchases/delete', { id: purchaseId })
        .then(() => {
          this.purchases = this.purchases.filter(purchase => purchase.id !== purchaseId);
          console.log('Purchase deleted successfully.');
        })
        .catch(error => {
          console.error('Error deleting Purchase:', error);
        });
    },
    addPurchase() {
      const { Name, Amount, Purchase_date } = this;
      this.addPurchases(Name, Amount, Purchase_date);
    },

    addPurchases(name, amount, purchase_date) {
      axios.post('http://127.0.0.1:5000/purchases/add', { name, amount, purchase_date })
        .then(() => {
          const newPurchase = { name, amount, purchase_date };
          this.purchases.push(newPurchase);
          this.fetchPurchases();
          console.log('Purchase added successfully.');
        })
        .catch(error => {
          console.error('Error adding Purchase:', error);
        });
    },
    handleAddPurchase() {
      this.addPurchase();
      this.toggleInputFields();
    },
    resetForm() {
      this.Name = '';
      this.Description = '';
      this.Amount = null;
      this.Purchase_date = '';
    }
  }
};
</script>