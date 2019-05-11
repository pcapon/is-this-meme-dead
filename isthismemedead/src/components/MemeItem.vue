<template>
  <router-link :to="{ name: 'memes', params: { id: memeObject.id }}">
  <el-card class="padcard" shadow="hover">
    <el-row :gutter="20">
      <el-col :span="8"><img class="scaled" :src="memeObject.image_url"/></el-col>
      <el-col :span="16">
        <h1>{{ memeObject.title }}</h1><p/>
        <span>{{ memeObject.Year }}</span><p/>
        <span>{{ memeObject.Origin }}</span><p/>
      </el-col>
    </el-row>
  </el-card>
  </router-link>
</template>

<script>
export default {
  name: 'MemeItem',
  props: {
    memeObject: Object,
  },
  methods: {
    goToMeme() {
      console.log('work');
    },
  },
};
</script>

<style scoped>
  .scaled
  {
    max-width: 50%;
  }
  .padcard
  {
    margin-bottom: 20px;
  }

</style>
