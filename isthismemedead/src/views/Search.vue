<template>
  <div>
      <navbar/>

    <el-main class="maincontent">
      <el-row style="margin-bottom: 40px;">
        <el-col :span="8" :offset="8">
          <searchbar></searchbar>
        </el-col>
      </el-row>
    <div v-loading="loading">
      <meme-item v-for="value in memesList" :memeObject="value"></meme-item>
    </div>
    </el-main>
  </div>
</template>

<script>
import memeItem from '@/components/MemeItem.vue';
import navbar from '@/components/Navbar.vue';
import searchbar from '@/components/searchcomponent.vue';
import axios from 'axios';

export default {
  name: 'Search.vue',
  components: {
    'meme-item': memeItem,
    navbar,
    searchbar,
  },
  data() {
    return {
      memesList: '',
    };
  },
  methods: {
    fetchmemes() {
      axios.get('http://127.0.0.1:5000/search', {
        params: {
          q: this.$route.params.string,
        },
      })
        .then((response) => {
          this.memesList = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.fetchmemes();
  },
  computed: {
    loading() {
      if (this.memesList === '') {
        return true;
      }
      return false;
    },
  },
  watch: {
    $route(to, from) {
      this.fetchmemes();
    },
  },
};
</script>

<style scoped>
.maincontent {
  padding-left: 15%;
  padding-right: 15%;
}
</style>
