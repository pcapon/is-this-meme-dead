<template>
  <div>
    <navbar/>
    <div v-loading="loading">
      <meme-item v-for="value in memesList" :memeObject="value"></meme-item>
    </div>
  </div>
</template>

<script>
import memeItem from '@/components/MemeItem.vue';
import navbar from '@/components/Navbar.vue';
import axios from 'axios';

export default {
  name: 'Search.vue',
  components: {
    'meme-item': memeItem,
    'navbar': navbar,
  },
  data() {
    return {
      memesList: '',
    };
  },
  methods: {

  },
  mounted() {
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
  computed: {
    loading: function () {
      if (this.memesList === '') {
        return true;
      }
      return false;
    },
  },

};
</script>

<style scoped>

</style>
