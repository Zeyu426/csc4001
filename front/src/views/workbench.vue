<template>
  
  <div class="page bg-box">
    <div class="title">
      <h2> Patient ID: {{patient_id}}</h2>
    </div>
    <div class="components-container bg-box">
      <el-row>
        <el-col :span="12">
        <div>
          <el-upload
            class="upload-demo bg-box"
            drag
            action="https://jsonplaceholder.typicode.com/posts/"
            :headers="headers"
            :on-preview="handlePreview"
            :on-success="handleSuccess"
            :on-change="handleChange"
            :limit="1"
            multiple>
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">Drag picture here. Or <em>click</em></div>
          </el-upload>
        </div>
        </el-col>

        <!-- <el-image
          :src="localUrl"
          :preview-src-list="[localUrl]"
          fit="scale-down"
        ></el-image> -->
        <el-col :span="12">
        <div class="picture bg-box2">
          <!-- <el-image :src="localUrl" fit="cover" style="width=360px, height=180px">
          </el-image> -->
          <img :src="localUrl" width="auto" height="180">

        </div>
        </el-col>
      </el-row>

    </div>

    <div class="button">
      <el-row>
        <el-button type="primary">Generate</el-button>
        <el-button type="primary">Upload<i class="el-icon-upload el-icon--right"></i></el-button>
      </el-row>
    </div>

    <div class="input">
      <el-input
        class="input2"
        type="textarea"
        :autosize="{ minRows: 10, maxRows: 20}"
        placeholder="Please Enter:"
        v-model="textarea2">
      </el-input>
    </div>

    <!-- <div>
      <img src:previewImage class="uploading-image" />
      <input type="file" accept="image/jpeg" @change=uploadImage>
   </div> -->
  </div>
</template>

<script>
import request from '@/utils/request'

export default {
  name: 'Workbench',
  data() {
    return {
      //url: "https://jsonplaceholder.typicode.com/posts/",
      //url: "https://127.0.0.1:8010/upload_image",
      url: "182.61.17.45",
      previewImage: null,
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      textarea2: "",
      patient_id: null,
      localUrl: null,
    }
  },
  mounted() {
    this.patient_id = this.$route.query.conlltion
    console.log(this.patient_id)
  },
  methods: {
    uploadImage(e){
      console.log(e);
      const image = e.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(image);
      reader.onload = e =>{
          this.previewImage = e.target.result;
          console.log(this.previewImage);
      };
    },
    handlePreview(file) {
      //console.log(file)
    },
    handleSuccess(response,file,fileList) {
      console.log(response)
      console.log(file)
      console.log(URL.createObjectURL(file.raw))
      this.localUrl = URL.createObjectURL(file.raw)
      let data = new FormData
      data.append("file", file.raw)
      data.append("name", "111")
      data.append("description", "222")

      request({
        url: "/upload_image",
        method: 'post',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data
      })
      .then(res => {
        console.log(res)
      })
    },
    handleChange(file,fileList) {
      /* var arr = [];
      fileList.forEach((item) => {
        arr.push(item.raw);
      });
      //this.dataList = arr;
      console.log(arr); */
      //console.log(file.raw)
      this.getBase64(file.raw).then(res => {
        //console.log(res)
      })
    },
    getBase64(file) {
      return new Promise(function(resolve, reject) {
        let reader = new FileReader();
        let imgResult = "";
        reader.readAsDataURL(file);
        reader.onload = function() {
          imgResult = reader.result;
        };
        reader.onerror = function(error) {
          reject(error);
        };
        reader.onloadend = function() {
          resolve(imgResult);
        };
      });
    },
  }
}
</script>

<style scoped>
.picture{
  width: 360px;
  height: 180px;
  margin: 0 0 0 20px;
  /* position: absolute;
  top: -20px;
  left: 700px;
  width: 360px;
  height: 200px; */
}
.title {
  position: absolute;
  text-align: left;
  top: -100px;
  left: 20px;
}
.input2{
  height: 400px;
}
.input {
  width: 80%;
  margin: 0 auto;
}
.page {
    position: relative;
    /* width: 600px;
    height: 300px; */
    margin: 0 auto;
    top: 100px;
    text-align: center;
    /* top: 200px; */
}
.button {
  margin: 3%;
  /* position: absolute;
  top: 21%;
  left: 35%; */
}
.uploading-image{
  /* display:flex; */
}
.components-container {
  
  /* width: 800px;
  height: 800px; */
}
.upload-demo {
  text-align: right;
  margin: 0 30px 0 0;
  /* position: absolute;
  left: 300px; */
  /* width: 30%; */
  /* text-align: center; */
  /* position: absolute;
  left: 5%;
  top: 5%; */
}
.bg-box2 {
  border-radius: 1%;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  text-align: center;
}
</style>
