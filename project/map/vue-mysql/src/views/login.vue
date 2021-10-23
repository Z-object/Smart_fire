<template>
  <div id="hello">
    <h1>{{ msg }}</h1>
    <div class="demo-input-suffix">
      <el-form>
        <el-form-item>
          <el-input
            placeholder="请输入用户名"
            prefix-icon="el-icon-user-solid"
            name="username"
            v-model="userName">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-input
            placeholder="请输入密码"
            v-model="passWord"
            prefix-icon="el-icon-lock"
            show-password
            name="password">
          </el-input>
        </el-form-item>
      </el-form>
      <div>
        <el-button type="primary" @click="login">登录</el-button>
<!--        <el-button @click="select">注册</el-button>-->
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'hello',
    data () {
      return {
        msg: '欢迎使用城市消防地理数据显示平台',
        userName: '',
        passWord: ''
      }
    },
    methods: {
      addUser() {
        let name = this.userName;
        let pwd = this.passWord;
        this.$axios.post('/api/addUser', {
          username: name,
          password: pwd
        },{}).then((response) => {
          alert('注册成功,跳转至登录组件')
          console.log('注册请求成功',response);
        })
      },
      select(){
        let name = this.userName;
        let pwd = this.passWord;
        this.$axios.post('/api/select',{
          username:name,
          password:pwd
        },{}).then((response)=>{
          console.log(response.data);
          var len = response.data.length;
          if(len==1){
            alert('用户已存在')
          }else{
            if (name==""||pwd=="") {
              alert('注册失败，输入值不能为空!')
            }else{
              console.log('注册成功!')
              this.addUser();
            }
          }
        })
      },
      login(){
        let name = this.userName;
        let pwd = this.passWord;
        // this.$axios.post('/api/login', {
        //   username: name,
        //   password: pwd
        // },{}).then((response) => {
        //   var content = response.data;
        //   if(content.length != 0){
        //     this.$notify({
        //       title: 'info',
        //       message: '登陆成功!',
        //       type: 'success'
        //     });
        //     console.log('登陆请求成功',content);
        //     this.$router.push({
        //       name:'Index',
        //       params:{
        //         username:name,
        //         password:pwd
        //       }
        //     })
        //   }else{
        //     this.$message({
        //       showClose: true,
        //       message: '账号或密码错误!',
        //       type: 'error'
        //     });
        //   }
        // },
        // function(response){
        //   console.log(response);
        // })
        this.$notify({
          title: 'info',
          message: '登陆成功!',
          type: 'success'
        });
        console.log('登陆请求成功');
        this.$router.push({
          name:'Index',
          params:{
            username:name,
            password:pwd
          }
        })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
form input{
  margin-top: 10px;
}

.el-input{
  width: 300px;
}
</style>
