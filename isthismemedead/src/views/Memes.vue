<template>
<div>
  <navbar/>
  <h1>MEMES PAGE {{ $route.params.id }}</h1>
</div>
</template>

<script>
import navbar from '@/components/Navbar.vue';

export default {
  name: 'Memes',
  components: {
    navbar,
  },
};
</script>

<style scoped>

</style>
