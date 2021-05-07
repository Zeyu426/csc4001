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

      <el-table-column label="Roles" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.roles }}</span>
        </template>
      </el-table-column>

      <!-- <el-table-column label="Gender" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.gender }}
        </template>
      </el-table-column> -->

      <!-- <el-table-column label="Sickness" align="center">
        <template slot-scope="scope">
          {{ scope.row.sickness }}
        </template>
      </el-table-column> -->

      <el-table-column label="Privilege" aling="center">
        <template slot-scope="scope">
          <el-checkbox-group 
            v-model="scope.row.privilege"
            @change="scope.row.unchange=false">
            <el-checkbox
              v-for="privilege in privilegeOptions" 
              :label="privilege" 
              :key="privilege">
              {{privilege}}
            </el-checkbox>
          </el-checkbox-group>
        </template>
        <!-- <template>
          <el-checkbox-group 
            v-model="checkList"
            :change="checkbox_change">
            <el-checkbox v-for="authority in autorities" :label="authority" :key="authority">{{authority}}</el-checkbox>
            <el-checkbox label="复选框 A"></el-checkbox>
            <el-checkbox label="复选框 B"></el-checkbox>
            <el-checkbox label="复选框 C"></el-checkbox>
            <el-checkbox label="禁用" disabled></el-checkbox>
            <el-checkbox label="选中且禁用" disabled></el-checkbox>
          </el-checkbox-group>
        </template> -->
      </el-table-column>

      <!-- <el-table-column class-name="status-col" label="Status" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column> -->

      <el-table-column align="center" label="Change" width="200">
        <template slot-scope="scope">
          <el-button type="primary" 
            @click="handleClick(scope.row.id)"
            :disabled="scope.row.unchange">
            Submit
          </el-button>
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
// import { getList } from '@/api/table'

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
      table_data: [
        {
          'id': 1234,
          'name': 'fugui',
          'roles': 'super-admin',
          'privilege': ['CT', 'Doctor'],
          'unchange': true
        },
        {
          'id': 2222, 
          'name': 'fugui', 
          'roles': 'CT doctor',
          'privilege': ['Doctor'],
          'unchange': true
        }
      ],
      // checkList: ['选中且禁用','复选框 A'],
      privilegeOptions: ['CT', 'Doctor']
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    handleClick(id) {
      console.log(id)
      // this.$router.push({name: 'Workbench', query: {conlltion: id}})
      for (var i = 0; i < this.table_data.length; i++){
        if (this.table_data[i]['id'] == id){
          this.table_data[i]['unchange'] = true
          break
        }
      }
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
    },
  }
}
</script>
