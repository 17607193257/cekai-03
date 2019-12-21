
from django.db import models
from django.http import JsonResponse

'''
一、必做题
1.简单描述两种开发模式的区别

前后端不分离：
返回的是HTML页面，后端控制前端数据的显示；
只能适配浏览器，其他终端不适配；
存在前端等后端，后端等前端的情况，延长了开发周期；


前后端分离：
后端只提供数据，前后端安全独立；
同一套接口可以适配多种终端，如浏览器、app、小程序；
前后端可以同时开发，缩短了开发周期；
'''

'''
2.Django中前端向后端传参的方式有哪些? 后端如何接收?

1.传递查询字符串
接收方式：request.GET

2.请求体传参

传递www-form表单，接收方式：request.POST
传递json数据,接收方式：json.loads(request.body.decode())
传递文件，接收方式：request.FILES

3.传递请求路径
在路由中设置路径解释器并给路径参数命名（如：<int:pk>/），然后在对应的视图函数或者视图类的实例方法中传入路径参数名，

4.传递请求头
接收方式：request.META
'''

'''
3.定义Projects模型类
'''
#
#
# class projects(models.Model):
#     id = models.AutoField(verbose_name="项目id", help_text="项目id", primary_key=True)
#     name = models.CharField(verbose_name="项目名称", help_text="项目名称", unique=True, max_length=200)
#     leader = models.CharField(verbose_name="项目负责人", help_text="项目负责人", max_length=200)
#     tester = models.CharField(verbose_name="测试负责人", help_text="测试负责人", max_length=200)
#     programmer = models.CharField(verbose_name="开发负责人", help_text="开发负责人", max_length=200)
#     publish_app = models.CharField(verbose_name="发布应用", help_text="发布应用", max_length=200)
#     pdesc = models.CharField(verbose_name="项目描述", help_text="项目描述", default="", blank=True, null=True,
#                              max_length=200)  # 允许为空
#
#     create_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", auto_now_add=True)
#     update_time = models.DateTimeField(verbose_name="更新时间", help_text="更新时间", auto_now=True)
#
#     class Meta:
#         db_table = "tb_projects"


'''
二、选做题
1.创建一个返回json格式数据的接口
'''

#在view.py文件中编辑以下内容
def my_request(request):
    data = [{"name": "danshui", "age": 18}, {"hobby": "reading"}]
    if type(data)==dict:
        return JsonResponse(data)
    else:
        return JsonResponse(data, safe=False)





