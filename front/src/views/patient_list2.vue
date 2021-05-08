<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.row.id }}
        </template>
      </el-table-column>

      <el-table-column label="Name" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.name }}
        </template>
      </el-table-column>

      <el-table-column label="Birth Date" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.birthdate }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Gender" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.gender }}
        </template>
      </el-table-column>

      <el-table-column min-width="300px" label="Sickness" align="center">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.sickness" class="edit-input" size="small" />
            <el-button
              class="cancel-btn"
              size="small"
              icon="el-icon-refresh"
              type="warning"
              @click="cancelEdit(row)"
            >
              cancel
            </el-button>
          </template>
          <span v-else>{{ row.sickness }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Edit" width="120">
        <template slot-scope="{row}">
          <el-button
            v-if="row.edit"
            type="success"
            size="small"
            icon="el-icon-circle-check-outline"
            @click="confirmEdit(row)"
          >
            Ok
          </el-button>
          <el-button
            v-else
            type="primary"
            size="small"
            icon="el-icon-edit"
            @click="row.edit=!row.edit"
          >
            Edit
          </el-button>
        </template>
      </el-table-column>

      <el-table-column align="center" label="CT Imaging" width="120">
        <template slot-scope="scope">
          <el-button type="primary" size="small" @click="handleClick3(scope.row.id)">
            Arrange
          </el-button>
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="CT Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="CT Report" width="110" align="center">
        <template slot-scope="scope">
          <!-- <el-button type="text" v-if="scope.row.hasReport" @click="open(scope.row.id)">Report</el-button> -->
          <el-button type="text" @click="handleClick2(scope.row)" v-if="scope.row.report">Report</el-button>

        </template>
      </el-table-column>

      <el-table-column align="center" label="Status" width="200">
        <template slot-scope="scope">
          <el-button type="primary" size="small" @click="handleClick(scope.row.id)">
            Finish
          </el-button>
        </template>
      </el-table-column>

      <!-- <el-table-column align="center" label="CT Imaging Diagnosis" width="200">
        <template slot-scope="scope">
          <el-button type="primary" @click="handleClick(scope.row.id)">
            Generate
          </el-button>
        </template>
      </el-table-column> -->

    </el-table>

    <el-dialog title="CT Report" :visible.sync="dialogTableVisible">
      <div class="input">
        <el-input
          class="input2"
          type="textarea"
          :autosize="{ minRows: 10, maxRows: 20}"
          placeholder="Please Enter:"
          v-model="textarea2">
        </el-input>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getList } from '@/api/table'
import request from '@/utils/request'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        finished: 'success',
        waiting: 'gray'
        //deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true,
      dialogTableVisible: false,
      textarea2: "w2w2wqd",
      table_data: [],
      /* table_data: [{'id': 1234, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'waiting', 'sickness': null, 'originalSickness': null, 'edit': false, 'hasReport': false},
                    {'id': 2222, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'finished', 'sickness': null, 'originalSickness': null, 'edit': false, 'hasReport': true}] */
    }
  },
  created() {
    let out_doc_id = 2
    let data = new FormData
    //data.append("radio_id", this.doc_id)
    data.append("out_doc_id", out_doc_id)

    request({
      url: "/get_main_list",
      method: 'post',
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      data
    })
    .then(res => {
      console.log(res.data)
      let data_list = res.data
      //let dic = {}
      for (var key in res.data) {
        let dic = {'id': key, 'name': data_list[key]['name'], 'birthdate': data_list[key]['birthDate'], 'gender': data_list[key]['gender'], 'status': data_list[key]['ct_status'], 'sickness': data_list[key]['sickness'], 'originalSickness': null, 'edit': false, 'report':data_list[key]['report']}
        if (dic['status'] == 'waiting')
          dic['hasReport'] = false
        if (dic['status'] == 'finished')
          dic['hasReport'] = true

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
    open(id) {

    },
    cancelEdit(row) {
      row.sickness = row.originalSickness
      row.edit = false
      this.$message({
        message: 'The sickness has been restored to the original value',
        type: 'warning'
      })
    },
    confirmEdit(row) {
      row.edit = false
      row.originalSickness = row.sickness
      let data = new FormData
      data.append('patient_id',row.id)
      data.append('sickness',row.sickness)
      request({
        url: "/upload_sickness",
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data
      })
      .then(res => {
      })

      this.$message({
        message: 'The sickness has been edited',
        type: 'success'
      })
    },
    handleClick(id) {
      let data = new FormData
      data.append('patient_id',id)
      request({
        url: "/finish_appointment",
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data
      })
      .then(res => {
      })
      location.reload()
    },
    handleClick2(row) {
      this.dialogTableVisible = true
      this.textarea2 = row.report
    },
    handleClick3(id) {
      let data = new FormData
      data.append('patient_id',id)
      request({
        url: "/arrange_CT",
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data
      })
      .then(res => {
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
