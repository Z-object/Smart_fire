<template>
  <div class="add">
    <el-row :gutter="10">
      <el-col :span="14" >
        <div class="grid-content bg-purple">
          <el-form ref="form" label-width="100px">
            <el-form-item label="姓名">
              <el-input v-model="username"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input type="password" v-model="password"></el-input>
            </el-form-item>
            <el-form-item label="token" v-if="sign">
              <el-input v-model="sign" disabled></el-input>
            </el-form-item>
            <el-button type="primary" @click="login">登陆认证</el-button>
            <el-button type="danger" @click="exit">登出</el-button>
          </el-form>
        </div>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <el-row :gutter="10">
      <el-col :span="14" >
        <div class="grid-content bg-purple">
          <el-form ref="form" label-width="100px">
            <el-form-item label="token">
              <el-input v-model="sendSign"></el-input>
            </el-form-item>
            <el-form-item label="接受用户">
              <el-input v-model="otherUser"></el-input>
            </el-form-item>
            <el-form-item label="消息">
              <el-input v-model="sendMsg"></el-input>
            </el-form-item>
            <el-button type="primary" @click="sendMessage">发送消息</el-button>
          </el-form>
        </div>
      </el-col>
    </el-row>

    <el-divider></el-divider>

    <el-row :gutter="10">
      <el-col :span="14" >
        <div class="grid-content bg-purple">
          <el-form ref="form" label-width="100px">
            <el-form-item label="凭证token">
              <el-input v-model="pullSign"></el-input>
            </el-form-item>
          </el-form>
          <el-button type="primary" @click="pullMessage">接收消息</el-button>
          <el-table-column v-for="item in messageList" v-bind:key="item.id">
            {{item.fromUser}} : {{item.content}}
          </el-table-column>
        </div>
      </el-col>
    </el-row>

    <el-divider></el-divider>

    <el-row :gutter="10">
      <el-col :span="14" >
        <div class="grid-content bg-purple">
          <el-form ref="form" label-width="100px">
<!--            <el-form-item label="token">-->
<!--              <el-input v-model="sign"></el-input>-->
<!--            </el-form-item>-->
            <el-form-item label="被邀请用户">
              <el-input v-model="inviteUser"></el-input>
            </el-form-item>
            <el-form-item label="被邀请人凭证">
              <el-input v-model="inviteSign"></el-input>
            </el-form-item>
            <el-button type="primary" @click="invite">邀请某人</el-button>
          </el-form>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'add',
    data(){
      return{
        username: "",
        password: "",
        sign: "",
        sendSign: "",
        sendMsg: "",
        otherUser: "",
        messageList: [],
        inviteUser: "",
        inviteSign: "",
        pullSign: ""
      }
    },
    methods:{
      login(){
        this.$axios.post('/api/login/create/connection',{
          username: this.username,
          password: this.password
        }).then((response)=>{
          if(response.data.code == 1){
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'success'
            })
            this.sign = response.data.data
            this.username = this.username
          }else{
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'warning'
            })
          }
        })
      },
      sendMessage(){
        this.$axios.post('/api/send/msg',{
          sign: this.sendSign,
          fromUser: this.username,
          toUser: this.otherUser,
          content: this.sendMsg
        }).then((response)=>{
          if(response.data.code == 1){
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'success'
            })
            this.sendMsg = ""
          }else{
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'warning'
            })
            this.sendSign = ""
          }
        })
      },

      pullMessage() {
        this.$axios.post('/api/pull/msg',{
          sign: this.pullSign,
          username: this.username,
        }).then((response)=>{
          if(response.data.code == 1){
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'success'
            })
            this.messageList = response.data.data
          }else{
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'warning'
            })
            this.pullSign = ""
          }
        })
      },

      invite() {
        this.$axios.post('/api/invite/user',{
          sign: this.sign,
          username: this.username,
          inviteUsername: this.inviteUser
        }).then((response)=>{
          if(response.data.code == 1){
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'success'
            })
            this.inviteSign = response.data.data
          }else{
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'warning'
            })
          }
        })
      },
      exit() {
        this.$axios.get('/api/stop/connnect/' + this.username)
          .then((response)=>{
          if(response.data.code == 1){
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'success'
            })
            this.sign = ""
            this.inviteSign = ""
            this.pullSign = ""
          }else{
            this.$message({
              showClose: true,
              message: response.data.msg,
              type: 'warning'
            })
          }
        })
      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
