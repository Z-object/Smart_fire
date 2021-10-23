<template>
  <div class="update">
    <h2>修改</h2>
    <el-row :gutter="20">
      <el-col :span="12" :offset="6">
        <div class="grid-content bg-purple">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="编号">
              <el-input v-model="form.id":disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="姓名">
              <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="密码">
              <el-input v-model="form.pwd"></el-input>
            </el-form-item>
            <el-form-item label="内容">
              <el-input v-model="form.content"></el-input>
            </el-form-item>
          </el-form>
          <el-button @click="update">确定</el-button>
          <el-button @click="goBack">返回</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'update',
    data(){
      return{
        form:{
          // 将 index 页数据通过 params 传递过来，定义一个对象接收，并绑定到input框上
          id:this.$route.params.id,
          name:this.$route.params.studentName,
          pwd:this.$route.params.studentPwd,
          content:this.$route.params.Content
        }
      }
    },
    methods:{
      goBack(){
        this.$router.back(-1);
      },
      // 修改方法
      update(){
        var id = this.form.id;
        var name = this.form.name;
        var pwd = this.form.pwd;
        var content = this.form.content;
        this.$axios.post('/api/updateStudent', {
          //需要传入所有信息
          id:id,
          studentName: name,
          studentPwd: pwd,
          Content:content
        }).then((response) => {
          // 添加成功更改为 element-ui 的 massage
          this.$message({
            message: '恭喜你，更新成功!',
            type: 'success'
          });
          console.log(response.config.data)
          // 调用返回方法，返回到主页
          this.goBack();
        })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
