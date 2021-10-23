from django import forms
from .models import *

# django将form表单放在forms.py文件中,中间件
# 定义表单类
# 双向通信，将python转为html可识别，将html转为python可识别的
class PersonForm(forms.ModelForm):
    username = forms.CharField(label='账号', required=True)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(), required=True)
    #与models中的数据表进行关联
    class Meta:
        model = Person
        fields = ('username', 'password')


class Ad_PerForm(forms.ModelForm):
    username = forms.CharField(label='账号', required=True)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(), required=True)
    #与models中的数据表进行关联
    class Meta:
        model = Ad_Per
        fields = ('username', 'password')

# 救援方案界面
class IndexForm(forms.Form):
    place = forms.ModelChoiceField(queryset=PlaceInfo.objects.all(), required=True, empty_label=None, label='火灾地点:', widget=forms.Select(attrs={'class': 'form-control', 'id': 'place'}))
    area = forms.CharField(label='火灾面积:',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾面积(单位：㎡)', 'id': 'area'}))
    volume = forms.CharField(label='火灾容积:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾容积（单位：m³）', 'id': 'volume'}))
    call = forms.CharField(label='报警次数:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '报警次数', 'id': 'call'}))
    stage = forms.ModelChoiceField(queryset=StageInfo.objects.all(), required=True, empty_label=None, label='火灾阶段:', widget=forms.Select(attrs={'class': 'form-control', 'id': 'stage'}))
    fire = forms.ModelChoiceField(queryset=FireInfo.objects.all(), required=True, empty_label=None, label='火势大小:', widget=forms.Select(attrs={'class': 'form-control', 'id': 'fire'}))
    speed = forms.ModelChoiceField(queryset=SpeedInfo.objects.all(), required=True, empty_label=None, label='火灾蔓延速度:', widget=forms.Select(attrs={'class': 'form-control', 'id': 'speed'}))
    trapped = forms.CharField(label='被困人数:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '被困人数', 'id': 'trapped'}))
    injured = forms.CharField(label='受伤人数:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '受伤人数', 'id': 'injured'}))
    death = forms.CharField(label='死亡人数:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '死亡人数', 'id': 'death'}))


class DecForm(forms.Form):
    lev = forms.ModelChoiceField(queryset=LevelInfo.objects.all(), required=True, empty_label=None, label='火灾等级',
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    cat = forms.ModelChoiceField(queryset=CategoryInfo.objects.all(), required=True, empty_label=None, label='火灾等级',
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    programme = forms.CharField(label='火灾方案', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '方案'}))


# 火灾方案修改
class UpdataDecForm(forms.Form):
    lev = forms.ModelChoiceField(queryset=LevelInfo.objects.all(), required=True, empty_label=None, label='火灾等级',
                                 widget=forms.Select(attrs={'class': 'form-control', 'id': 'lev'}))
    cat = forms.ModelChoiceField(queryset=CategoryInfo.objects.all(), required=True, empty_label=None, label='火灾等级',
                                 widget=forms.Select(attrs={'class': 'form-control', 'id': 'cat'}))
    programme = forms.CharField(label='火灾方案',
                                widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '方案', 'id': 'programme'}))


# 火灾等级
class AttFrom(forms.Form):
    area = forms.CharField(label='火灾面积',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾面积'}))
    volume = forms.CharField(label='火灾容积', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾容积'}))
    call = forms.CharField(label='报警次数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '报警次数'}))
    stage = forms.CharField(label='火灾阶段', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾阶段'}))
    fire = forms.CharField(label='火势大小', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火势大小'}))
    speed = forms.CharField(label='火灾蔓延速度', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾蔓延速度'}))
    trapped = forms.CharField(label='被困人数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '被困人数'}))
    injured = forms.CharField(label='受伤人数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '受伤人数'}))
    death = forms.CharField(label='死亡人数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '死亡人数'}))
    lev = forms.ModelChoiceField(queryset=LevelInfo.objects.all(), required=True, empty_label=None, label='火灾等级', widget=forms.Select(attrs={'class': 'form-control'}))


class UpdateAttFrom(forms.Form):
    area = forms.CharField(label='火灾面积',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾面积', 'id': 'area'}))
    volume = forms.CharField(label='火灾容积', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾容积', 'id': 'volume'}))
    call = forms.CharField(label='报警次数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '报警次数', 'id': 'call'}))
    stage = forms.CharField(label='火灾阶段', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾阶段', 'id': 'stage'}))
    fire = forms.CharField(label='火势大小', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火势大小', 'id': 'fire'}))
    speed = forms.CharField(label='火灾蔓延速度', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾蔓延速度', 'id': 'speed'}))
    trapped = forms.CharField(label='被困人数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '被困人数', 'id': 'trapped'}))
    injured = forms.CharField(label='受伤人数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '受伤人数', 'id': 'injured'}))
    death = forms.CharField(label='死亡人数', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '死亡人数', 'id': 'death'}))
    lev = forms.ModelChoiceField(queryset=LevelInfo.objects.all(), required=True, empty_label=None, label='火灾等级', widget=forms.Select(attrs={'class': 'form-control', 'id': 'lev'}))


# 火灾类别
class CateFrom(forms.Form):
    address = forms.CharField(label='火灾发生地',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾发生地'}))
    cat = forms.ModelChoiceField(queryset=CategoryInfo.objects.all(), required=True, empty_label=None, label='火灾类别',
                                 widget=forms.Select(attrs={'class': 'form-control'}))

# 火灾类别
class UpdateCateFrom(forms.Form):
    address = forms.CharField(label='火灾发生地',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '火灾发生地', 'id': 'address'}))
    cat = forms.ModelChoiceField(queryset=CategoryInfo.objects.all(), required=True, empty_label=None, label='火灾类别',
                                 widget=forms.Select(attrs={'class': 'form-control', 'id': 'cat'}))
