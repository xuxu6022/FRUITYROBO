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
