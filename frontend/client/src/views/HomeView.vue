<style>
</style>

<template>
  <div class="mx-4 my-4">
    <TableComponent></TableComponent>
  </div>
</template>

<script>
import TableComponent from '../components/MachineTable.vue';

export default {
  name: 'HomeView',
  created() {
    document.body.style.backgroundColor = '#F4D35E';
  },
  components: {
    TableComponent,
  },
};
</script>
