from django.db import models





# 用户账号密码模型类
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField


class Person(models.Model):
    SEX = (
        ('man', '男'),
        ('woman', '女'),
    )
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15, null=True)
    goods_pic = models.ImageField(upload_to='fire', default='')
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=15, choices=SEX, null=True)
    phonenumber = models.CharField(max_length=15, null=True)



# 管理员类
class Ad_Per(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)



# 火灾基本情况类

class Firesi(models.Model):
    FISI_CHOICES = (
        ('True', '有'),
        ('False', '没有'),
        ('Null', '未知'),
    )
    FIRE_TYPE = (
        ('A', 'A类'),
        ('B', 'B类'),
        ('C', 'C类'),
        ('D', 'D类'),
        ('E', 'E类'),
        ('F', 'F类'),
        ('Null', '未知'),
    )
    FIRE_LEVEL = (
        ('A', '一般火灾'),
        ('B', '较大火灾'),
        ('C', '重大火灾'),
        ('D', '特别重大火灾'),
        ('Null', '未知'),
    )
    title = models.CharField(max_length=20, null=True, blank=True)  # 火灾标题
    place = models.CharField(max_length=50, null=True, blank=True) # 火灾发生地点
    detal_place = models.CharField(max_length=50, null=True, blank=True)  # 火灾发生详细地址
    date = models.DateField(null=True, blank=True)   # 火灾发生日期
    time = models.CharField(max_length=20, null=True, blank=True)   # 火灾发生时间
    fire_type = models.CharField(max_length=10, null=True, blank=True, choices=FIRE_TYPE)   # 火灾类别
    fire_level = models.CharField(max_length=10, null=True, blank=True, choices=FIRE_LEVEL)  # 火灾级别
    last_time = models.CharField(max_length=10, null=True, blank=True)  # 火灾持续时间
    major_th = models.CharField(max_length=20, null=True, blank=True)    # 主要可燃物
    fire_build = models.CharField(default=True, max_length=20,  choices=FISI_CHOICES)
    water = models.CharField(default=True, max_length=20, choices=FISI_CHOICES)
    air = models.OneToOneField('Air', on_delete=models.CASCADE)  # 火灾基本情况与气象情况一对一







# 气象情况类

class Air(models.Model):
    wind = models.IntegerField(null=True, blank=True)  # 风力
    wind_dir = models.CharField(max_length=20, null=True, blank=True)  # 风向
    weather_con = models.CharField(max_length=20, null=True, blank=True)  # 天气条件
    temper = models.CharField(max_length=20, null=True, blank=True)  # 温度
    hum = models.CharField(max_length=20, null=True, blank=True)  # 湿度




# 建筑结构特点类

class Build_char(models.Model):
    '''True表示是，False表示否'''
    COM_CHOICES = (
        ('True', '是'),
        ('False', '否'),
        ('Null', '未知'),
    )
    com_bulid = models.CharField(default=False, max_length=20,  choices=COM_CHOICES, null=True)  # 普通建筑
    old_build = models.CharField(default=False, max_length=20,  choices=COM_CHOICES, null=True)  # 古建筑
    wuzi_ck = models.CharField(default=False, max_length=20, choices=COM_CHOICES, null=True)  # 物资仓库
    product_cq = models.CharField(default=False, max_length=20, choices=COM_CHOICES, null=True)  # 生产厂区
    chugq = models.CharField(default=False, max_length=20, choices=COM_CHOICES, null=True)  # 储罐区
    hall_build = models.CharField(default=False, max_length=20, choices=COM_CHOICES, null=True)  # 高层建筑
    bfire = models.ForeignKey('Firesi', on_delete=models.CASCADE)  # 火灾基本情况与建筑结构类一对多



# 作战指挥情况类

class Fight_com(models.Model):
    time = models.CharField(max_length=20, null=True, blank=True)  # 接警时间
    person = models.CharField(max_length=20, null=True, blank=True)  # 被困人数
    see_com = models.CharField(max_length=100, null=True, blank=True)  # 侦察情况
    area = models.CharField(max_length=50, null=True, blank=True)  # 火灾区域
    fire_zs = models.CharField(max_length=100, null=True, blank=True)  # 火灾扑救战术
    fire_change = models.CharField(max_length=100, null=True, blank=True)  # 火灾异变
    team = models.OneToOneField('First_team', on_delete=models.CASCADE)  # 作战指挥情况类与第一支消防队到场情况类一对一





# 第一支消防队到场情况类

class First_team(models.Model):
    FITA_CHOICES = (
        ('True', '有'),
        ('False', '没有'),
        ('Null', '未知'),
    )
    area = models.CharField(max_length=20, null=True, blank=True)  # 火灾区域
    develop = models.CharField(max_length=20, null=True, blank=True)  # 火灾发展阶段
    person = models.IntegerField(null=True, blank=True)  # 被困人员数
    fire_recon = models.CharField(max_length=20, null=True, blank=True)  # 火灾侦察情况
    danger = models.CharField(default=False,max_length=20,  choices=FITA_CHOICES, null=True, blank=True)  # 有无重大危险情况，True表示有，False表示无
    fight_task = models.CharField(max_length=20, null=True, blank=True)  # 作战任务
    build_map = models.CharField(default=False,max_length=20,  choices=FITA_CHOICES, null=True, blank=True)  # 有无建筑结构图,True表示有，False表示无



# 火灾救援人员情况类
class Fire_save(models.Model):
    '''True表示到场，False表示未到场'''
    SAVE_CHOICES = (
        ('True', '到场'),
        ('False', '未到场'),
        ('Null', '未知'),
    )
    消防人员 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 消防人员
    群众 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 群众
    部队 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 部队
    专家 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 专家
    政府 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 政府
    交警 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 交警
    公安 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 公安
    医疗 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 医疗
    安监 = models.CharField(default=False, max_length=20, choices=SAVE_CHOICES, null=True, blank=True)  # 安监
    save_team = models.ForeignKey('Fight_com', on_delete=models.CASCADE)  # 作战指挥情况类与火灾救援人员情况类一对多




#  救援装备使用情况类
class Save_eq(models.Model):
    '''True表示使用，False表示未使用'''
    SAEQ_CHOICES = (
        ('True', '使用'),
        ('False', '未使用'),
        ('Null', '未知'),
    )
    水罐车 = models.CharField(default=False, max_length=20, choices=SAEQ_CHOICES, null=True, blank=True)  # 水罐车
    泡沫水罐车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 泡沫水罐车
    高倍水罐车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 高倍水罐车
    二氧化碳消防车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 二氧化碳消防车
    干粉消防车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 干粉消防车
    泡沫干粉联用消防车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 泡沫干粉联用消防车
    登高平台消防车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 登高平台消防车
    云梯消防车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 云梯消防车
    通讯消防车 = models.CharField(default=False, max_length=20,  choices=SAEQ_CHOICES, null=True, blank=True)  # 通讯消防车
    save_eq = models.ForeignKey('Fight_com', on_delete=models.CASCADE)  # 作战指挥情况类与救援装备使用情况类一对多


# 个人防护装备使用情况类
class Person_eq(models.Model):
    头盔 = models.CharField(max_length=20, null=True, blank=True)  # 头盔种类
    防护服 = models.CharField(max_length=20, null=True, blank=True)  # 防护服种类
    呼吸器 = models.CharField(max_length=20, null=True, blank=True)  # 呼吸器种类
    手防护 = models.CharField(max_length=20, null=True, blank=True)  # 手防护种类
    足防护 = models.CharField(max_length=20, null=True, blank=True)  # 足防护种类
    per_eq = models.ForeignKey('Fight_com', on_delete=models.CASCADE)   # 作战指挥情况类与个人防护装备使用情况类一对多



#  经验总结分析类
class Experience(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)  # 火灾标题
    place = models.CharField(max_length=50, null=True, blank=True)  # 火灾发生地点
    area = models.CharField(max_length=50, null=True, blank=True)  # 起火面积
    fire_economic = models.CharField(max_length=100, null=True, blank=True)  # 火灾经济损失
    fire_cause = models.CharField(max_length=100, null=True, blank=True)  # 起火原因
    fire_res = models.CharField(max_length=100, null=True, blank=True)  # 火灾责任相关处理
    fire_exper = models.CharField(max_length=100, null=True, blank=True)  # 火灾扑救主要经验教训
    fire_com = models.CharField(max_length=100, null=True, blank=True)  # 火灾善后补偿情况
    dis_mea = models.CharField(max_length=100, null=True, blank=True)  # 灾后改进措施
    dead = models.OneToOneField('Person_hurt', on_delete=models.CASCADE)  # 经验总结分析类与人员伤亡情况类一对一


#  人员伤亡情况类
class Person_hurt(models.Model):
    死亡人数 = models.IntegerField(null=True, blank=True)  # 死亡人数
    重伤人数 = models.IntegerField(null=True, blank=True)  # 重伤人数
    轻伤人数 = models.IntegerField(null=True, blank=True)  # 轻伤人数
    男性死亡人数 = models.IntegerField(null=True, blank=True)  # 男性死亡人数
    女性死亡人数 = models.IntegerField(null=True, blank=True)  # 女性死亡人数
    本地死亡人数 = models.IntegerField(null=True, blank=True)  # 本地死亡人数
    外地死亡人数 = models.IntegerField(null=True, blank=True)  # 外地死亡人数
    dead_people1 = models.IntegerField(null=True, blank=True)  # 0-14死亡人数
    dead_people2 = models.IntegerField(null=True, blank=True)  # 14-60死亡人数
    dead_people3 = models.IntegerField(null=True, blank=True)  # 60岁以上死亡人数



class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to='fire')

# 火灾等级表
class LevelInfo(models.Model):
    lev = models.CharField(max_length=30, db_column='火灾等级')

    def __str__(self):
        return self.lev
    # 指定模型类对应的表名
    class Meta:
        verbose_name = '火灾等级表'
        verbose_name_plural = '火灾等级表'


# 火灾类别表
class CategoryInfo(models.Model):
    Cgy = models.CharField(max_length=30)

    def __str__(self):
        return self.Cgy
    # 指定模型类对应的表名
    class Meta:
        verbose_name = '火灾类别表'
        verbose_name_plural = '火灾类别表'

# 火灾面积表
class AreaInfo(models.Model):
    area = models.CharField(max_length=20)
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)



# 火灾容积表
class VolumeInfo(models.Model):
    volume = models.CharField(max_length=20)
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)


# 呼警次数表
class CallInfo(models.Model):
    call = models.CharField(max_length=20)


# 火灾阶段表
class StageInfo(models.Model):
    stage = models.CharField(max_length=20)

    # 显示下拉列表正常数据
    def __str__(self):
        return self.stage


# 火势大小表
class FireInfo(models.Model):
    fire = models.CharField(max_length=20)

    # 显示下拉列表正常数据
    def __str__(self):
        return self.fire


# 火灾蔓延速度表
class SpeedInfo(models.Model):
    speed = models.CharField(max_length=20)

    # 显示下拉列表正常数据
    def __str__(self):
        return self.speed


# 被困人数表
class TrappedInfo(models.Model):
    trapped = models.CharField(max_length=20)
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)


# 受伤人数表
class InjuredInfo(models.Model):
    injured = models.CharField(max_length=20)
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)


# 死亡人数表
class DeathInfo(models.Model):
    death = models.CharField(max_length=20)
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)


# 火灾地点表
class PlaceInfo(models.Model):
    address = models.CharField(max_length=20)
    Pcat = models.ForeignKey(CategoryInfo, on_delete=models.CASCADE)

    # 显示下拉列表正常数据
    def __str__(self):
        return self.address
    # 指定模型类对应的表名
    class Meta:
        verbose_name = '火灾地点表'
        verbose_name_plural = '火灾地点表'


# 火灾决策方案表
class DecisionInfo(models.Model):
    programme = models.TextField()
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)
    Pcat = models.ForeignKey(CategoryInfo, on_delete=models.CASCADE)

    # 指定模型类对应的表名
    class Meta:
        verbose_name = '火灾决策方案表'
        verbose_name_plural = '火灾决策方案表'


# 火灾规则表
class FireRuleInfo(models.Model):
    area = models.CharField(max_length=20)
    volume = models.CharField(max_length=20)
    call = models.CharField(max_length=20)
    stage = models.CharField(max_length=20)
    fire = models.CharField(max_length=20)
    speed = models.CharField(max_length=20)
    trapped = models.CharField(max_length=20)
    injured = models.CharField(max_length=20)
    death = models.CharField(max_length=20)
    Alev = models.ForeignKey(LevelInfo, on_delete=models.CASCADE)

    # 指定模型类对应的表名
    class Meta:
        verbose_name = '火灾属性表'
        verbose_name_plural = '火灾属性表'
