<template>
  <div class="navbar">
    <el-row type="flex" justify="space-between">

        <el-col :span="6">
          <router-link :to="{ name: 'home'}">
          <!-- <img class="img-valign unselectable" src="../assets/skull.png"> -->
          <h1 class="navtitle" >💀 IS THIS MEME DEAD ?</h1>
          </router-link>
        </el-col>

      <el-col :span="2">
        <add-meme class="buttoncenter"></add-meme>
      </el-col>
    </el-row>
    <el-divider/>
  </div>
</template>

<script>
import addMeme from '@/components/AddMeme.vue';

export default {
  name: 'Navbar.vue',
  components: {
    'add-meme': addMeme,
  },
};
</script>

<style scoped>
  .img-valign {
    max-width: 15%;
  }
  .navtitle {
    font-size:2vw;
  }
  .navbar {
    background-color: #f9fafc;
  }
  .buttoncenter {
    padding-top: 1vw;
  }
</style>
