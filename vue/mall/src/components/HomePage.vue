<style scoped>
.el-menu {
  margin-top: 0;
  margin-bottom: 0;
  padding-left: 24px;
  padding-right: 24px;
  color: #274C5B;
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
  font-weight: bold; /* 设置字体加粗 */
}

</style>

<template>
    <el-menu
      :default-active="activeIndex"
      class="el-menu"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
      <div class="logo-title">
        <img src="../assets/Logo.png" alt="Logo" class="logo" />
        <h1 class="title">FRUITY ROBO</h1>
      </div>
      <div class="flex-grow" />
      <el-menu-item index="home" style="font-weight: bold;">Home</el-menu-item>
      <el-menu-item index="sale">Sale</el-menu-item>
      <el-menu-item index="product">Product</el-menu-item>
      <el-menu-item index="purchase">Purchase</el-menu-item>
      <el-menu-item index="announcement">Announcement</el-menu-item>
      <el-menu-item index="comment">Comment</el-menu-item>
    </el-menu>  
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeIndex = ref('home')

const handleSelect = (index) => {
  activeIndex.value = index
  router.push({ name: index })
}
</script>
