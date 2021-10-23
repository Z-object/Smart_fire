<template>
  <div>
    <el-form>
    <el-form-item :inline="true">
      <el-col :span="16">
        <el-input placeholder="请输入查询信息, 例如：类型，级别，所属省，所属市"
                max-length="200px"
                v-model="searchInfo"></el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary" @click="search">搜  索</el-button>
      </el-col>
      <el-col :span="2">
        <el-button type="warning" @click="detail">查看明细</el-button>
      </el-col>

    </el-form-item>
    </el-form>
    <div class="amap-wrapper">
      <el-amap
        class="amap-box"
        map-style="fresh"
        :center="center"
        zoom="6"
        :vid="'amap-vue'"
      >
        <el-amap-marker
          v-for="(marker,index) in markers" :key="index"
          :events="events"
          :extData="marker"
          :position="marker.position" />
        <el-amap-info-window
          v-if="window"
          :position="window.position"
          :visible="window.visible"
          :content="window.content"
          :offset="window.offset"
        ></el-amap-info-window>
      </el-amap>
    </div>
    <div id="map" class="container"></div>
  </div>
</template>

<script>
  export default {
    name: 'hello',
    data () {
      return {
        events: {
          click: a =>{
            console.log( a.target.getExtData())
            var value = a.target.getExtData()
            this.showlabel(value)
          }
        },
        searchInfo: '',
        center: [108.9082,37.9452],
        markers: [
          {
            "title": "12·3辽宁沈阳11·19一住宅区发生火灾",
            "startDate": "2019年12月3日",
            "startTime": "21时30分",
            "mainThing": "家电家具等",
            "type": "E类",
            "level": "一般火灾",
            "province": "辽宁省",
            "city": "沈阳市",
            "address": "SR国际新城住宅区起火的是该住宅区内的两栋高层居民楼",
            "visible": false,
            "position" : ["123.435093","41.836743"]},
          {"position" : [108.939621,34.343147]},
          {"position" : [116.407387,39.904179]},
          {"position" : [113.266887,23.133306]},
          {"position" : [114.530399,38.037707]},
          {"position" : [117.330139,31.734559]}
        ],
        window: null
      }
    },
    methods: {
      init() {
        this.$axios.get('/api/query/all')
          .then((response)=>{
          if(response.data.code == 1){
            this.$message({
              showClose: true,
              message: '查询成功',
              type: 'success'
            })
            var result = response.data.data
            for (var i = 0; i < result.length; i++) {
              if (result[i]) {
                let strPosition = result[i].position
                if (strPosition) {
                  result[i].position = strPosition.toString().split(",")
                  result[i].position.map(Number)
                }
              }
            }
            this.markers = result
          }else{
            this.$message({
              showClose: true,
              message: '查询失败',
              type: 'warning'
            })
            this.markers = null;
          }
        })
      },
      search() {
        console.log('search')
        this.$axios.post('/api/search', {
          queryInfo: this.searchInfo
        }).then((response)=>{
            if(response.data.code == 1){
              this.$message({
                showClose: true,
                message: '查询成功',
                type: 'success'
              })
              var result = response.data.data
              for (var i = 0; i < result.length; i++) {
                if (result[i]) {
                  let strPosition = result[i].position
                  if (strPosition) {
                    result[i].position = strPosition.toString().split(",")
                    result[i].position.map(Number)
                  }
                }
              }
              this.markers = result
            }else{
              this.$message({
                showClose: true,
                message: '查询失败',
                type: 'warning'
              })
              this.markers = null;
            }
          })
      },
      showlabel(marker){
        console.log("click")
        this.window={
          position: marker.position,
          visible: !marker.visible,
          content: "" +
            "<div>"+"火灾标题："+marker.title + "</div>" +
            "<div>"+"时间："+marker.start_time+"</div>" +
            "<div>"+"主要可燃物："+marker.main_thing+"</div>" +
            "<div>"+"火灾类型："+"<span style='color: blue'>"+marker.type+"</span>"+"</div>"+
            "<div>"+"火灾级别："+"<span style='color: blue'>"+marker.level+"</span>"+"</div>"+
            "<div>"+"所属省份："+marker.province+"</span>"+"</div>"+
            "<div>"+"所属市："+marker.city+"</span>"+"</div>"+
            "<div>"+"地点："+marker.address+"</span>"+"</div>"
          ,
          offset: [5,-15]
        }
        marker.visible = !marker.visible
      },
      detail() {
        this.$router.push({
          name:'Table'
        })
      }

    },
    mounted(){
      this.init()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .amap-wrapper {
    width: 100%;
    height: 800px;
  }
  .container {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 600px;
  }
</style>
