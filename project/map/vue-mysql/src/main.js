// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import axios from 'axios'
import QS from 'QS'
import VueResource from 'vue-resource'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

// 自定义组件
import Login from './views/login'
import Index from './views/index'
import Table from './views/table'

// 引入vue-amap
import AMap from 'vue-amap';
Vue.use(AMap);
// 初始化vue-amap
AMap.initAMapApiLoader({
  // 高德的key
  key: '1c15a39b5a983015c3a18670e3f82f0f',
  // 插件集合 （插件按需引入）
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'MarkerClusterer',
    'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor', 'Geocoder']
});

Vue.prototype.$axios = axios
Vue.prototype.$qs = QS

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(ElementUI)
Vue.config.productionTip = false

const router = new VueRouter({
	routes:[
		// {path:"/",name:"Login",component:Login,meta:['哈哈哈','呵呵呵']},
		{path:"/",name:"Login",component:Login,meta:['哈哈哈','呵呵呵']},
		{path:"/index",name:"Index",component:Index,meta:['哼哼哼','盒盒盒']},
		{path:"/table",name:"Table",component:Table},
		{path:"/login",name:"Login",component:Login}
	],
	mode:"history"
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
