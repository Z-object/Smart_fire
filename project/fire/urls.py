from django.conf.urls import include, url
from django.urls import path

from . import views  # 导入本文件下的views



urlpatterns = [
    url(r'^index$', views.index),
    url(r'^login$', views.login),
    url(r'^login1$', views.login1),
    url(r'^register$', views.register),
    url(r'^register1$', views.register1),
    url(r'^personcenter$', views.personcenter),
    url(r'^test', views.test),
    url(r'^search$', views.search),
    url(r'^alterpsd$', views.alterpsd),
    url(r'^adminpsd$', views.adminpsd),
    url(r'^adminaltpsd$', views.adminaltpsd),
    url(r'^adindex$', views.adindex),
    url(r'^adlogin$', views.adlogin),
    url(r'^index2', views.index2),
    url(r'^delete$', views.delete),
    url(r'^firesi$', views.firesi),
    url(r'^fight$', views.fight),
    url(r'^exper$', views.exper),
    url(r'^exper_search$', views.exper_search),
    url(r'^users(?P<pindex>\d*)$', views.users),
    url(r'^user_save$', views.user_save),
    url(r'^adminfight', views.adminfight),
    url(r'^adminexper', views.adminexper),
    url(r'^save_user$', views.save_user),
    url(r'^updateFiresi$', views.updateFiresi),
    url(r'^updatef$', views.updatef),
    url(r'^updatefight$', views.updatefight),
    url(r'^updatee$', views.updatee),
    url(r'^updatefire$', views.updatefire),
    url(r'^alterfiresi$', views.alterfiresi),
    url(r'^alterfiresi1$', views.alterfiresi1),
    url(r'^alterfight$', views.alterfight),
    url(r'^alterfight1$', views.alterfight1),
    url(r'^alterexper$', views.alterexper),
    url(r'^alterexper1$', views.alterexper1),
    url(r'^firesidetail$', views.firesidetail),
    url(r'^firesidetail1$', views.firesidetail1),
    url(r'^fireside$', views.fireside),
    url(r'^fightdetail$', views.fightdetail),
    url(r'^fightdetail1$', views.fightdetail1),
    url(r'^fightde$', views.fightde),
    url(r'^experdetail$', views.experdetail),
    url(r'^experdetail1$', views.experdetail1),
    url(r'^experde$', views.experde),
    url(r'^updateexper$', views.updateexper),
    url(r'^deleteexper$', views.deleteexper),
    url(r'^deletefight$', views.deletefight),
    url(r'^deletefiresi$', views.deletefiresi),
    url(r'^alterpsdhtml$', views.alterpsdhtml),
    url(r'^alterpsm$', views.alterpsm),
    url(r'^fightsearch'
        r'$', views.fightsearch),
    url(r'^adfisearch$', views.adfisearch),
    url(r'^adfgsearch$', views.adfgsearch),
    url(r'^adexsearch$', views.adexsearch),
    url(r'^show_upload$', views.show_upload),  # 显示上传图片页面
    url(r'^upload_handle$', views.upload_handle),
    url(r'^rep_index$', views.rep_index),  # 爬虫首页模块
    url(r'^rep_firesi$', views.rep_firesi),  # 火灾基本情况爬取
    url(r'^rep_fight$', views.rep_fight),  # 作战指挥情况爬取
    url(r'^rep_exper$', views.rep_exper),  # 经验总结分析爬取
    url(r'^ruleindex$', views.ruleindex),  # 救援方案查询界面
    url(r'^adminruleindex$', views.adminruleindex),  # 救援方案查询界面
    url(r'^lev', views.lev),
    url(r'^cat', views.cat),
    url(r'^admincat', views.admincat),
    url(r'^adminlev', views.adminlev),
    url(r'^admindec', views.admindec),
    url(r'^dec', views.dec),  # 方案管理界面
    url(r'^decdelete$', views.decdelete),  # 方案管理删除
    url(r'^decadd$', views.decadd),  # 方案管理增加
    url(r'^decupdata$', views.decupdata),  # 方案管理修改
    url(r'^levdelete$', views.levdelete),
    url(r'^levadd$', views.levadd),
    url(r'^levupdate$', views.levupdate),
    url(r'^catdelete$', views.catdelete),
    url(r'^catadd$', views.catadd),
    url(r'^catupdate$', views.catupdate),
    url(r'^ajax_sb$', views.ajax_sb),  # 救援方案查询数据处理
    url(r'^typevis$', views.typevis),
    url(r'^datevis$', views.datevis),
    url(r'^pronvis$', views.pronvis),
]