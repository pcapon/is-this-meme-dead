<template>
  <div class="home">
    <navbar/>
    <el-row  type="flex" class="row-bg" justify="center">
      <el-col :span="12">
        <!-- <img class="img-valign unselectable" src="../assets/skull.png"> -->
        <span class="mainTitle unselectable">💀 IS THIS MEME DEAD ?</span>
      </el-col>
    </el-row>
    <div style="margin-top: 15px;">
      <el-row>
        <el-col :span="8" :offset="8">
      <el-input placeholder="Search for memes"
                @keyup.enter.native="goToSearch" v-model="query" class="input-with-select">
        <el-button
          slot="append"
          type="primary"
          icon="el-icon-search"
          @click="goToSearch" >
            Search
        </el-button>
      </el-input>
        </el-col>
      </el-row>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import navbar from '@/components/Navbar.vue';

export default {
  components: {
    navbar,
  },
  name: 'home',
  methods: {
    goToSearch() {
      this.$router.push({ name: 'search', params: { string: this.query } });
    },
  },
  data() {
    return {
      query: '',
      select: '',
    };
  },
};
</script>

<style scoped>
  .img-valign {
    width: 90px;
    height: auto;
    vertical-align: middle;
    margin-bottom: 4em;
  }
  .mainTitle {
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
