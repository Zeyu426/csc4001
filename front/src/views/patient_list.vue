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

      <el-table-column label="Sickness" align="center">
        <template slot-scope="scope">
          {{ scope.row.sickness }}
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="CT Imaging Diagnosis" width="200">
        <template slot-scope="scope">
          <!-- <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span> -->
          <el-button type="primary" @click="handleClick(scope.row.id)">
            Generate
          </el-button>
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'

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
      table_data: [{'id': 1234, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'waiting'},
                    {'id': 2222, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'finished'}]
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    handleClick(id) {
      this.$router.push({name: 'Workbench', query: {conlltion: id}})
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
