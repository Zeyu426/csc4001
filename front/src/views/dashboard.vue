<template>
  <div class="page bg-box2">
    <el-row>

      <el-col span="12">
        <div class="left">
          <h1 class="one"> Hello, Doctor {{doctor_name}}!</h1>
        </div>
      </el-col>

      <el-col span="12">
        <div class="right">
          <h1 class="clock one">
            {{date}}
          </h1>
        </div>
      </el-col>
      
    </el-row>

    <div class="card-panel-description">
      <div class="card-panel-text">
        New Visits
      </div>
      <count-to :start-val="0" :end-val="102400" :duration="2600" class="card-panel-num" />
    </div>
  </div>
</template>

<script>
import CountTo from 'vue-count-to'

export default {
  name: 'Dashboard',
  components: {
    CountTo
  },
  data() {
    return {
      doctor_name: "Jerry",
      date: new Date().toUTCString(),
    }
  },
  created() {
    let _this = this; // 声明一个变量指向Vue实例this，保证作用域一致
    this.timer = setInterval(() => {
      _this.date = new Date().toUTCString(); // 修改数据date
    }, 1000)
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer); // 在Vue实例销毁前，清除我们的定时器
    }
  },
  methods: {

  }
}
</script>

<style >
.one {
  display: inline;
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

.left {
  text-align: left;
}

.right {
  text-align: right;
}

.bg-box2 {
  border-radius: 1%;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  text-align: center;
}
</style>
