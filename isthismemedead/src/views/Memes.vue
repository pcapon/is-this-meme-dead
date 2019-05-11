<template>
<div>
    <navbar/>
  <el-main class="maincontent" v-loading="loading">
  <h1>MEMES PAGE {{ $route.params.id }}</h1>
    <img class="scaled" :src="memeinfo.image_url"/>
    <el-row>
      <el-col :span="6">
      <el-button round>🖤</el-button>
      </el-col>
      <el-col :span="12">
  <VueSlideBar :isDisabled="true"
               :lineHeight="20"
               :showTooltip="false"
               :processStyle="{ backgroundColor: '#409eff', borderColor: 'red' }"
               v-model="valueslider"/>
      </el-col>
      <el-col :span="6">
      <el-button round>💀</el-button>
      </el-col>
    </el-row>
  </el-main>
</div>
</template>

<script>
import navbar from '@/components/Navbar.vue';
import VueSlideBar from 'vue-slide-bar';
import axios from 'axios';

export default {
  name: 'Memes',
  components: {
    navbar,
    VueSlideBar,
  },
  data() {
    return {
      value: 5,
      memeinfo: '',
    };
  },
  methods: {
    fetchmeme() {
      axios.get('http://127.0.0.1:5000/getmeme', {
        params: {
          id: this.$route.params.id,
        },
      })
        .then((response) => {
          this.memeinfo = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.fetchmeme();
  },
  watch: {
    $route(to, from) {
      this.fetchmeme();
    },
  },
  computed: {
    valueslider: {
      get() {
        let score = 0;
        if (this.memeinfo.no === 0 && this.memeinfo.yes === 0) {
          return 50;
        }
        score = (this.memeinfo.yes / (this.memeinfo.yes + this.memeinfo.no)) * 100;
        return score;
      },
      set(newvalue) {
        console.log(newvalue);
      },
    },
    loading() {
      if (this.memeinfo === '') {
        return true;
      }
      return false;
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
