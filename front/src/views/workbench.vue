<template>
  <div class="page bg-box">
    <div class="components-container bg-box">
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

    <div>
      <img src:previewImage class="uploading-image" />
      <input type="file" accept="image/jpeg" @change=uploadImage>
   </div>
  </div>
</template>

<script>
import {test} from '../api/user'

export default {
  name: 'Workbench',
  data() {
    return {
      //url: "https://jsonplaceholder.typicode.com/posts/",
      url: "182.61.17.45",
      previewImage: null,
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
  },
  mounted() {
    this.$axios.post('/dev_api/test',
    {
        //stu_id: this.studentID,
    })
    .then(res => {
        console.log(res.data)
    })
    .catch(err => {
        console.log(err);
    });
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
.uploading-image{
  display:flex;
}
.components-container {
  
  /* width: 800px;
  height: 800px; */
}
.upload-demo {
  position: absolute;
  left: 5%;
  top: 10%;
}
.bg-box {
  /* border-radius: 4%;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  text-align: center; */
}
</style>
