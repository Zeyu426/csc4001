<template>
  <div class="all">
    <div class="page">

      <!-- <div>
        <h1 class="one"> Hello, {{doctor_name}}!</h1>
      </div> -->
      
      <el-row>

        <el-col span="12">
          <div class="left">
            <h1 class="one"> Hello, {{doctor_name}}!</h1>
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


      <el-row :gutter="40" class="panel-group">
        <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
          <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
            <div class="card-panel-icon-wrapper icon-people">
              <i class="el-icon-user-solid card-panel-icon"></i>
              <!-- svg-icon icon-class="people" /> -->
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Processing
              </div>
              <count-to :start-val="0" :end-val="102400" :duration="2600" class="card-panel-num" />
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
          <div class="card-panel" @click="handleSetLineChartData('messages')">
            <div class="card-panel-icon-wrapper icon-message">
              <i class="el-icon-user-solid card-panel-icon"></i>
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Waiting CT
              </div>
              <count-to :start-val="0" :end-val="81212" :duration="3000" class="card-panel-num" />
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
          <div class="card-panel" @click="handleSetLineChartData('purchases')">
            <div class="card-panel-icon-wrapper icon-money">
              <i class="el-icon-user-solid card-panel-icon"></i>
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Finished
              </div>
              <count-to :start-val="0" :end-val="9280" :duration="3200" class="card-panel-num" />
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
          <div class="card-panel" @click="handleSetLineChartData('shoppings')">
            <div class="card-panel-icon-wrapper icon-shopping">
              <i class="el-icon-user-solid card-panel-icon"></i>
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Total
              </div>
              <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
            </div>
          </div>
        </el-col>
      </el-row>
      <!-- <div class="panel-group hello">
        <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
          <div class="card-panel-icon-wrapper icon-people">
            <svg-icon icon-class="peoples" class-name="card-panel-icon" />
            <i class="el-icon-user-solid card-panel-icon"></i>
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              Waiting for
            </div>
            <count-to :start-val="0" :end-val="end_people_value" :duration="1000" class="card-panel-num" />
          </div>
        </div>
      </div>

      <div class="panel-group hello">
        <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
          <div class="card-panel-icon-wrapper icon-people">
            <svg-icon icon-class="peoples" class-name="card-panel-icon" />
            <i class="el-icon-time card-panel-icon"></i>
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">
              Waiting for
            </div>
            <count-to :start-val="0" :end-val="end_people_value" :duration="1000" class="card-panel-num" />
          </div>
        </div>
      </div> -->
      <!-- <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
        <div class="card-panel-icon-wrapper icon-people">
          <svg-icon icon-class="peoples" class-name="card-panel-icon" />
        </div>
        <div class="card-panel-description">
          <div class="card-panel-text">
            New Visits
          </div>
          <count-to :start-val="0" :end-val="102400" :duration="2600" class="card-panel-num" />
        </div>
      </div> -->
      <!-- <panel-group @handleSetLineChartData="handleSetLineChartData" /> -->
    </div>
  </div>
</template>

<script>
import CountTo from 'vue-count-to'
import PanelGroup from '../components/PanelGroup'

const lineChartData = {
  newVisitis: {
    expectedData: [100, 120, 161, 134, 105, 160, 165],
    actualData: [120, 82, 91, 154, 162, 140, 145]
  },
  messages: {
    expectedData: [200, 192, 120, 144, 160, 130, 140],
    actualData: [180, 160, 151, 106, 145, 150, 130]
  },
  purchases: {
    expectedData: [80, 100, 121, 104, 105, 90, 100],
    actualData: [120, 90, 100, 138, 142, 130, 130]
  },
  shoppings: {
    expectedData: [130, 140, 141, 142, 145, 150, 160],
    actualData: [120, 82, 91, 154, 162, 140, 130]
  }
}

export default {
  name: 'Dashboard',
  components: {
    CountTo,
    PanelGroup
  },
  data() {
    return {
      doctor_name: "Jerry",
      date: new Date().toUTCString(),
      end_people_value: 10,
      end_time_value: 50,
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
    handleSetLineChartData(type) {
      this.$emit('handleSetLineChartData', type)
    },
    handleSetLineChartData(type) {
      this.lineChartData = lineChartData[type]
    }
  }
}
</script>

<style lang="scss" scoped>
.all {
  background-color: rgb(240, 242, 245);
  height: 800px;
}
.hello {
  width: 300px;
  margin: 0 auto;
}

.one {
  display: inline;
}

.page {
  position: relative;
  /* width: 600px;
  height: 300px; */
  margin: 0 auto;
  top: 30px;
  width: 80%;
  text-align: center;
  background-color: rgb(240, 242, 245);
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

.panel-group {
  margin-top: 18px;
  top: 50px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);
    /* margin: 0 auto; */


    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-people {
        background: #40c9c6;
      }

      .icon-message {
        background: #36a3f7;
      }

      .icon-money {
        background: #f4516c;
      }

      .icon-shopping {
        background: #34bfa3
      }
    }

    .icon-people {
      color: #40c9c6;
    }

    .icon-message {
      color: #36a3f7;
    }

    .icon-money {
      color: #f4516c;
    }

    .icon-shopping {
      color: #34bfa3
    }

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }
  }
}

@media (max-width:550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>
