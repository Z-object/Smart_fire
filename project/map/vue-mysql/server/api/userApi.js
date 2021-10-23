var models = require('../db/db');
var express = require('express');
var router = express.Router();
var mysql = require('mysql');
var $sql = require('../db/sqlMap');

// 连接数据库
var conn = mysql.createConnection(models.mysql);

conn.connect();

var jsonWrite = function(res, ret) {
  if(typeof ret === 'undefined') {
        res.send('err');
    } else {
        res.send(ret);
    }
};


// 登录用户接口
router.post('/login', (req, res) => {
    var sql = $sql.user.login;
    var params = req.body;
    var list = []
    conn.query(sql, [params.username,params.password], function(err, result) {
        if (err) {
            console.log(err);
        }
        if (result) {
            jsonWrite(res, result);
            for(var i = 0; i < result.length; i++){
                console.log("请求回来！",result[i])
                console.log("请求结果！",typeof result[i],result[i].password);
            }
        }
    })
});


// 查询所有
router.get('/query/all',(req,res)=>{
    var sql = $sql.data.query;
    var params = req.body;
    var dataList = []
    conn.query(sql,function(error,result){
        if(error){
            console.log(error)
        }
        if(result){
          response = {
            code: 1,
            data: result
          }
          jsonWrite(res,response)
        }
    })
})


router.post('/search',(req,res)=>{
    var sql = $sql.data.searchInfo;
    var params = req.body;
    conn.query(sql,["%"+ params.queryInfo +"%"],function(error,result){
        if(error){
            console.log(error)
        }
        if(result){
          var response = {
            code: 1,
            data: result
          }
          jsonWrite(res,response)
        }
    })
})
router.post('/query/table',(req,res)=>{
    var sql = $sql.data.table;
    var params = req.body;
    conn.query(sql,[(params.page-1)*params.limit,params.limit],function(error,result){
        if(error){
            console.log(error)
        }
        if(result){
          var response = {
            code: 1,
            data: result
          }
          jsonWrite(res,response)
        }
    })
})

// 修改数据
router.post("/updateStudent",(req,res)=>{
    var sql = $sql.user.update;
    var params = req.body;
    console.log(params.id);
    // 传的参数一定要与sql语句参数对应
    conn.query(sql,[params.studentName,params.studentPwd,params.Content,params.id],function(error,result){
        if (error) {
            console.log(error)
        }
        if (result) {
            jsonWrite(res,result)
        }
    })
})

module.exports = router;
