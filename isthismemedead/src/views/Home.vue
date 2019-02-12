<template>
  <div class="home">
    <el-row type="flex" justify="end" class="row-bg">
      <add-meme></add-meme>
    </el-row>
    <el-row type="flex" align="middle">
      <img class="img-valign unselectable" src="../assets/skull.png">
      <span class="mainTitle unselectable"> IS THIS MEME DEAD ?</span>
    </el-row>
    <div style="margin-top: 15px;">
      <el-input placeholder="Search for memes" v-model="input5" class="input-with-select">
        <el-button slot="append" type="primary" icon="el-icon-search">Search</el-button>
      </el-input>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import addMeme from '@/components/AddMeme.vue';

export default {
  components: {
    'add-meme': addMeme,
  },
  name: 'home',
  methods: {
  },
  data() {
    return {
      input5: '',
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
    font-size: 90px;
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
