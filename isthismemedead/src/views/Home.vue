<template>
  <div class="home">
      <navbar/>
    <el-main>
    <el-row  type="flex" class="row-bg" justify="center">
        <!-- <img class="img-valign unselectable" src="../assets/skull.png"> -->
        <span class="mainTitle unselectable">💀 IS THIS MEME DEAD ?</span>
    </el-row>
    <div style="margin-top: 15px;">
      <el-row>
        <el-col :span="8" :offset="8">
      <searchbar></searchbar>
        </el-col>
      </el-row>
    </div>
    </el-main>
  </div>
</template>

<script>
// @ is an alias to /src
import navbar from '@/components/Navbar.vue';
import searchbar from '@/components/searchcomponent.vue';

export default {
  components: {
    navbar,
    searchbar,
  },
  name: 'home',
  data() {
    return {
      select: '',
    };
  },
};
</script>

<style scoped>
  .img-valign {
    width: 90px;
    margin: auto;
    height: auto;
    vertical-align: middle;
    margin-bottom: 4em;
  }
  .mainTitle {
    text-align: center;
    font-size:4vw;
  }
  *.unselectable {
    -moz-user-select: -moz-none;
    -khtml-user-select: none;
    -webkit-user-select: none;

    /*
      Introduced in IE 10.
      See http://ie.microsoft.com/testdrive/HTML5/msUserSelect/
    */
    -ms-user-select: none;
    user-select: none;
  }
</style>
