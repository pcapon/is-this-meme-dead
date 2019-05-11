<template>
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
</template>

<script>
export default {
  name: 'searchcomponent.vue',
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

</style>
