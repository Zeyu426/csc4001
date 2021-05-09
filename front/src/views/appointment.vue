<template>
  <div class="app-container">
    <h1> Apointment </h1>
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <!-- <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.row.id }}
        </template>
      </el-table-column> -->

      <el-table-column label="Name" width="150" align="center">
        <template slot-scope="scope">
          {{ scope.row.name }}
        </template>
      </el-table-column>

      <!-- <el-table-column label="Gender" width="80" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.gender }}</span>
        </template>
      </el-table-column> -->

      <el-table-column label="Department" width="240" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.department }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Title" width="180" align="center">
        <template slot-scope="scope">
          {{ scope.row.title }}
        </template>
      </el-table-column>

      <el-table-column label="Specialty" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.specialty }}
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Registration" width="200">
        <template slot-scope="scope">
          <!-- <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span> -->
          <el-button type="primary" @click="handleClick(scope.row.id)">
            Register
          </el-button>
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'
import request from '@/utils/request'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        available: 'success',
        full: 'info'
        //deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true,
      doc_id: null,
      table_data: []
      /* table_data: [{'id': 1234, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'waiting'},
                    {'id': 2222, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'finished'}], */
    }
  },
  created() {
    // this.doc_id = this.$store.getters.id
    // console.log(this.doc_id)
    // let data = new FormData
    //data.append("radio_id", this.doc_id)
    // data.append("radio_id", 1)

    request({
      url: "/get_appointment_list",
      method: 'post',
      // headers: {
      //   'Content-Type': 'multipart/form-data'
      // },
      // data
    })
    .then(res => {
      let data_list = res.data
      //let dic = {}
      for (var key in res.data) {
        let dic = {
          'id': key,
          'name': data_list[key]['name'], 
          'gender': data_list[key]['gender'], 
          'department': data_list[key]['department'], 
          'office': data_list[key]['office'], 
          'title': data_list[key]['title'],
          'specialty': data_list[key]['specialty'],
          'status': data_list[key]['status']
          }
        this.table_data.push(dic)
      }
      /* console.log(this.table_data)
      console.log(res.data)
      for (var key in res.data) {
        console.log("key: " + key + " ,value: " + res.data[key]);
      } */
    })
    
    this.fetchData()
  },
  methods: {
    handleClick(id) {
        // this.$router.push({name: 'Workbench', query: {conlltion: id}})
      this.patient_id = this.$store.getters.id
      // console.log(this.doc_id)
      let data = new FormData
      //data.append("radio_id", this.doc_id)
      data.append("patient_id", this.patient_id)
      data.append("outdoc_id", id)

      request({
        url: "/arrange_appointment",
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data
      })
      .then(res => {
        if (res.code == 20000){
          var app_id = res.data.app_id
          var waiting = res.data.waiting
          this.$alert("Success! Your appointment id is: " + app_id)
        }
        else{
          this.$alert("Fail")
        }
        // let data_list = res.data
        // //let dic = {}
        // for (var key in res.data) {
        //   let dic = {
        //     'id': key,
        //     'name': data_list[key]['name'], 
        //     'gender': data_list[key]['gender'], 
        //     'department': data_list[key]['department'], 
        //     'office': data_list[key]['office'], 
        //     'title': data_list[key]['title'],
        //     'specialty': data_list[key]['specialty'],
        //     'status': data_list[key]['status']
        //     }
        //   this.table_data.push(dic)
        // }
      })
    },
    fetchData() {
        this.listLoading = true
        this.list = this.table_data
        this.listLoading = false
        /* getList().then(response => {
          this.list = response.data.items
          this.list = this.table_data
          console.log(this.list)
          this.listLoading = false
        }) */

        //
    }
  }
}
</script>
