<template>
  <div class="all">
    <div class="page">

      <div style="margin: 20px">
        <h1 class="one"> Hello, {{name}}!</h1>
      </div>
      
      <!-- <el-row>

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
        
      </el-row> -->
      <el-card style="width:60%; margin-left: 20% ">
        <div slot="header" class="clearfix">
          <h3> Waiting for Doctor </h3>
        </div>
        <div class="panel-group hello">
          <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
            <div class="card-panel-icon-wrapper icon-people">
              <i class="el-icon-user-solid card-panel-icon"></i>
              <!-- svg-icon icon-class="people" /> -->
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Waiting for Doctor
              </div>
              <count-to :start-val="0" :end-val="d_people" :duration="1000" class="card-panel-num" />
            </div>
          </div>
        </div>

        <div class="panel-group hello">
          <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
            <div class="card-panel-icon-wrapper icon-people">
              <i class="el-icon-time card-panel-icon"></i>
              <!-- svg-icon icon-class="people" /> -->
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Waiting Time (min)
              </div>
              <count-to :start-val="0" :end-val="d_time" :duration="1000" class="card-panel-num" />
            </div>
          </div>
        </div>
      </el-card>
      
      <el-card style="width:60%; margin-left: 20% ">
        <div slot="header" class="clearfix">
          <h3> Waiting for CT </h3>
        </div>
        <div class="panel-group hello">
          <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
            <div class="card-panel-icon-wrapper icon-people">
              <i class="el-icon-user-solid card-panel-icon"></i>
              <!-- svg-icon icon-class="people" /> -->
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Waiting for CT
              </div>
              <count-to :start-val="0" :end-val="people" :duration="1000" class="card-panel-num" />
            </div>
          </div>
        </div>

        <div class="panel-group hello">
          <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
            <div class="card-panel-icon-wrapper icon-people">
              <i class="el-icon-time card-panel-icon"></i>
              <!-- svg-icon icon-class="people" /> -->
            </div>
            <div class="card-panel-description">
              <div class="card-panel-text">
                Waiting time (min)
              </div>
              <count-to :start-val="0" :end-val="time" :duration="1000" class="card-panel-num" />
            </div>
          </div>
        </div>
      </el-card>
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
import request from '@/utils/request'

export default {
  name: 'Dashboard',
  components: {
    CountTo,
    PanelGroup
  },
  data() {
    return {
      name: "Jerry",
      d_people: null,
      d_time: null,
      people: null,
      time: null,
      date: new Date().toUTCString(),
      end_people_value: 10,
      end_time_value: 50,
    }
  },
  created() {
    let data = new FormData
    data.append("patient_id", 3)
    request({
      url: "/get_patient_dashboard",
      method: 'post',
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      data
    })
    .then(res => {
      let data_list = res.data
      this.name = data_list['name']
      this.people = data_list['people']
      this.time = data_list['time']
      //console.log(res.data)
    })
    request({
      url: "/get_patient_dashboard2",
      method: 'post',
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      data
    })
    .then(res => {
      let data_list = res.data
      // this.name = data_list['name']
      this.d_people = data_list['people']
      this.d_time = data_list['time']
      //console.log(res.data)
    })
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
  height: 1000px;
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
  top: 80px;
  width: 90%;
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
