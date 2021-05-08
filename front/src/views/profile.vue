<template>
  <div class="page">
    <el-card class="box-card">

      <div slot="header" class="header clearfix">
        <span>Basic Information</span>
      </div>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Name </h1>
            <div class="name">
              <span> {{name}} </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Doctor ID </h1>
            <div class="name">
              <span> {{doc_id}} </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Gender </h1>
            <div class="name">
              <span> {{gender}} </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Telephone </h1>
            <div class="name">
              <span> {{telephone}} </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Department </h1>
            <div class="name">
              <span> {{department}} </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Office </h1>
            <div class="name">
              <span> {{office}} </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Title </h1>
            <div class="name">
              <span> {{title}} </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Specialty </h1>
            <div class="name">
              <span> {{specialty}} </span>
            </div>
          </form>
        </el-col>
      </el-row>

    </el-card>
  </div>
</template>

<script>
import request from '@/utils/request'

export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          
        }
      }
    }
  },
  data() {
    return {
      list: null,
      listLoading: true,
      name: null,
      doc_id: null,
      gender: null,
      telephone: null,
      department: null,
      office: null,
      title: null,
      specialty: null,
      table_data: [{'id': 1234, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'waiting'},
                    {'id': 2222, 'name': 'fugui', 'birthdate': '2020-01-01', 'gender': 'female', 'status': 'finished'}]
    }
  },
  created() {
    let data = new FormData
    data.append('doc_id',1)
   request({
      url: "/get_CT_doctor_profile",
      method: 'post',
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      data
    })
    .then(res => {
      let data_list = res.data
      this.name = data_list['name']
      this.doc_id = data_list['doc_id']
      this.gender = data_list['gender']
      this.department = data_list['department']
      this.telephone = data_list['phone']
      this.office = data_list['office']
      this.title = data_list['title']
      this.specialty = data_list['specialty']
      console.log(res.data)
    })
  },
  methods: {
    
  }
}
</script>

<style>
.name {
  text-align: left;
  margin: 30px 0 30px 0;
}

.name2 {
  text-align: right;
  margin: 30px 0 30px 0;
}

.page {
  position: relative;
  /* width: 600px;
  height: 300px; */
  margin: 0 auto;
  top: 30px;
  width: 90%;
  text-align: center;
  /* top: 200px; */
}

.box-card {
  width: 800px;
  margin: 0 auto;
}

.header {
  text-align: left;
  font-family: "lucida sans unicode", "lucida grande", sans-serif;
  font-size: 24px;
  font-weight: bold;
  letter-spacing: 0pt;
  word-spacing: 0pt;
}

.font1 {
  font-family: helvetica, sans-serif;
  color: #C9C3C3;
  font-size: 18px;
  letter-spacing: 0pt;
  word-spacing: 0pt;

}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}

.bg-box2 {
  border-radius: 1%;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  text-align: center;
}

</style>