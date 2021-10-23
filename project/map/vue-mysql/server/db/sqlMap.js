/**
 * Created by xiaoze on 2017/12/5.
 */
// sql语句
var sqlMap = {
  data: {
    query: "SELECT * FROM test.t_fire",
    searchInfo: "SELECT * FROM test.t_fire where concat(type, level, province, city) like ?",
    table: "SELECT * FROM test.t_fire limit ?, ?"
  },
  // 用户
  user: {


    add: 'INSERT INTO `user`(`username`,`password`) VALUES (?,?)',
    login:"SELECT `password` FROM `user` WHERE username = ? AND `password` = ?",
    select:"SELECT * FROM USER WHERE username = ? AND PASSWORD = ?",
    query:"SELECT * FROM grade_analysis.avg_grade",
    delete:"DELETE FROM student WHERE id = ?",
    addStudent:"INSERT INTO student(`studentName`,`studentPwd`,`Content`) VALUES (?,?,?)",
    selectStudent:"SELECT * FROM student WHERE studentName = ?",
    update:"UPDATE student SET studentName = ?,studentPwd = ?,Content = ? WHERE id = ?"
  }
}
module.exports = sqlMap;
