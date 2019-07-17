# 引入表单类
from django import forms
# 引入User模型
from django.contrib.auth.models import User

# 登录表单，继承了forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 注册用户表单
class UserRegisterForm(forms.ModelForm):
    # 复写User的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        # 嵌套类，主要用于指定数据的一些属性
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码进行检测
    def clean_password2(self):
        data = self.cleaned_data    # 对数据进行清洗，保留有用的数据
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("输入的密码不一致，请重试")
    