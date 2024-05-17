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
    <img src="../assets/commentBanner.png" width="100%">
    <div
      style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 50%; text-align: center;">
      <p style="font-size: 72px; color: #EFD372; font-weight: bold; margin: 0; text-align: center;">
        COMMENT
      </p>
    </div>
  </div>
  <div style="display: flex; flex-direction: column;">
  <div v-for="comment in comments" :key="comment.id" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between;">
    <div style="margin: 10px 40px;">
      <div style="font-weight: bold; color: #274C5B; font-size: 24px;">{{ comment.comment_date }}</div>
      <div style="font-weight: bold; color: #7EB693; font-size: 16px;">{{ comment.content }}</div>
    </div>
    <el-button type="primary" @click="deleteComment(comment.id)"
        style="font-weight: bold; background-color: #EFD372; color: #274C5B; border-color: #EFD372;">DELETE</el-button>
  </div>
</div>

</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const activeIndex = ref('comment')

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
      comments: [],
    };
  },
  created() {
    this.fetchComments();
  },
  methods: {
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
    }
  }
};</script>
