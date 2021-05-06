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
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Doctor ID </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Gender </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Telephone </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Address </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Office </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Name </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
        <el-col :span="12">
          <form>
            <h1 class="name font1"> Name </h1>
            <div class="name">
              <span> 11111 </span>
            </div>
          </form>
        </el-col>
      </el-row>

      <!-- <el-row>
        <el-col :span="12">
          <h1 class="name font1"> Name </h1>
        </el-col>
        <el-col :span="12">
          <div class="name2">
            <span> 11111 </span>
          </div>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <h1 class="name font1"> Doctor ID </h1>
        </el-col>
        <el-col :span="12">
          <div class="name2">
            <span> 11111 </span>
          </div>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <h1 class="name font1"> Gender </h1>
        </el-col>
        <el-col :span="12">
          <div class="name2">
            <span> 11111 </span>
          </div>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <h1 class="name font1"> Telephone </h1>
        </el-col>
        <el-col :span="12">
          <div class="name2">
            <span> 11111 </span>
          </div>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <h1 class="name font1"> Address </h1>
        </el-col>
        <el-col :span="12">
          <div class="name2">
            <span> 11111 </span>
          </div>
        </el-col>
      </el-row>

      <el-row>
        <el-col :span="12">
          <h1 class="name font1"> Office </h1>
        </el-col>
        <el-col :span="12">
          <div class="name2">
            <span> 11111 </span>
          </div>
        </el-col>
      </el-row> -->



      <!-- <div v-for="o in 4" :key="o" class="text item">
        {{'列表内容 ' + o }}
      </div> -->

    </el-card>
  </div>
</template>

<script>

export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          name: '',
          email: '',
          avatar: '',
          role: ''
        }
      }
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