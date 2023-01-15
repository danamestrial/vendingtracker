<template>
    <table class="table">
        <thead>
        <tr>
            <th scope="col">#</th>
            <th scope="col">Handle</th>
            <th scope="col">Location</th>
            <th scope="col">Status</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="item in list" :key="item.id">
            <th scope="row">{{item.id}}</th>
            <td>{{item.handle}}</td>
            <td>{{item.location}}</td>
            <td>{{item.status == 0 ? "Offline" : "Online"}}</td>
        </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MachineTable',
  data() {
    return {
      list: [],
    };
  },
  methods: {
    getList() {
      const path = 'http://127.0.0.1:5000/listall';
      axios.get(path)
        .then((res) => {
          this.list = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getList();
  },
};
</script>
