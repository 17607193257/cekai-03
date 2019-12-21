from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import json

# 导入模型类：以下两种导入方式均可，.代表当前路径
# from projects.models import Projects
from .models import Projects
from interfaces.models import Interfaces


def index(request):
    """
    index视图函数
    视图函数，默认支持所有的请求方法，如GET、POST、PUT、DELETE等
    可以使用repuest.method来区分不同的请求返回不同的内容
    :param request：HttpRequest对象
    :return：HttpResponse对象

    """
    if request.method == "GET":
        return HttpResponse("<h1>GET请求：Hello，测开大佬们!<h1>")
    elif request.method == "POST":
        return HttpResponse("<h1>POST请求：Hello，测开大佬们!<h1>")
    elif request.method == "PUT":
        return HttpResponse("<h1>PUT请求：Hello，测开大佬们!<h1>")
    else:
        return HttpResponse("<h1>其他请求：Hello，测开大佬们!<h1>")


# class IndexView(View):
#     '''
#     index 主页类视图
#     1.一个类视图，需要继承View类或者View的子类
#     2.实例方法get、post、put、delete（全部小写）与相应的请求方法一一对应
#     3.get实例方法第一个参数为当前类视图的对象，第二个参数为HttpRequest请求对象
#     4.每一个实例方法必须返回HttpResponse对象或者HttpResponse子类对象
#     '''
#
#     # def get(self, request):
#     #     '''
#     #     第二个参数的名称可以随便定义，但是习惯性用request；
#     #     所有的业务逻辑，都会在后端视图中来定义
#     #     java中的MVC，Django中的MVT
#     #     当前data类似于M，全称Model，负责和数据库交互，进行数据处理
#     #     V全拼View，接收请求，进行业务处理，返回相应
#     #     当前T类似于模板，全称Template，负责构造要返回的html页面
#     #
#     #     :param request:
#     #     :return:
#     #     '''
#     #     # return HttpResponse("<h1>GET请求：Hello，测开大佬们!<h1>")
#
#     #     #假设从数据库中读取了相关数据
#     #     data = [
#     #         {
#     #             "project_name":"前程贷项目",
#     #             "leader":"云淡风轻",
#     #             "app_name":"P2P平台应用"
#     #         },
#     #         {
#     #             "project_name": "探索火星项目",
#     #             "leader": "淡水",
#     #             "app_name": "探索火星应用"
#     #         },
#     #         {
#     #             "project_name": "XXX项目",
#     #             "leader": "开发",
#     #             "app_name": "XXX应用"
#     #         }
#     #     ]
#
#     #     #render函数的第一个参数为HttpRequest对象，第二个参数为静态文件模板，locals()为当前实例方法的本地变量
#     #     # return render(request, "index.html",locals())   #返回的是模板，前后端不分离
#     #     return JsonResponse(data, safe=False)    #返回的数据，前后端分离
#
#     # def get(self, request):
#     #     #一、查询字符串传参：
#     #     #1.request为HttpRequest对象，相当于请求报文
#     #     #2.可以使用request.GET获取查询字符串参数
#     #     #3.获取的是QueryDict对象，可以类比于字典，可以使用[]或者.get()方法获取具体的值
#     #     #4.如果有多个相同的key，可以使用getlist(key)方法获取
#     #     data = [
#     #         {
#     #             "project_name": "前程贷项目",
#     #             "leader": "云淡风轻",
#     #             "app_name": "P2P平台应用"
#     #         },
#     #         {
#     #             "project_name": "探索火星项目",
#     #             "leader": "淡水",
#     #             "app_name": "探索火星应用"
#     #         },
#     #         {
#     #             "project_name": "XXX项目",
#     #             "leader": "开发",
#     #             "app_name": "XXX应用"
#     #         }
#     #     ]
#     #
#     #     #JsonResponse与HttpResponse的区别：
#     #     #JsonResponse第一个参数data，默认情况下只能传递字典类型的数据；
#     #     #如果第一个参数为非字典类型，那么需要指定safe=False；
#     #     #默认的content_type为application/json；
#
#     #     return JsonResponse(data, safe=False)
#
#     # def get(self, request):
#     #     # 创建操作
#     #     # 方法一：
#     #     # 一个模型类相当于一个表（table）
#     #     # 一个模型类对象相当于一条数据（record）
#     #     # one_projects = Projects(name="国产大飞机项目",leader="xxx院士",tester="所见",programmer="龙的传人",
#     #     #          publish_app="国产大飞机APP")
#     #     #
#     #     # #调用模型类对象save()才能执行sql语句
#     #     # one_projects.save()
#     #
#     #     # 方法二：creat方法
#     #     # one_project = Projects.objects.create(name="国产大飞机项目5",leader="xxx院士",tester="所见",programmer="龙的传人",
#     #     #          publish_app="国产大飞机APP")
#     #     #
#     #     # #从表数据的创建，外键可以使用project传入模型对象或者project_id传入项目id
#     #     # Interfaces.objects.create(name="国产大飞机接口",tester="所见",
#     #     #          project=one_project)
#     #     # Interfaces.objects.create(name="国产大飞机接口", leader="xxx院士", tester="所见",
#     #     #                           project_id=one_project.id)
#     #     # Interfaces.objects.create(name="国产大飞机接口", leader="xxx院士", tester="所见",
#     #     #                           project_id=19)
#     #
#     #     # 修改操作
#     #     # 方法一：先获取需要更新的类对象，然后修改相关属性
#     #     # GMT（世界时间）+8=北京时间
#     #     # one_project = Projects.objects.get(id=20)
#     #     # one_project.leader = "啦啦啦啦"
#     #     # one_project.save()
#     #
#     #     # 方法二：
#     #     # Projects.objects.update()
#     #
#     #     # 删除操作
#     #     # 先获取到待删除的数据，然后删除
#     #     # one_project = Projects.objects.get(id=20)
#     #     # one_project = Projects.objects.get(pk=20)#用pk也可以
#     #     # 通过模型
#     #     # one_project.delete()
#     #
#     #     # 查询操作
#     #     # 一、获取一张表中的所有记录
#     #     # 1.调用all()方法返回QuerySet对象，
#     #     # 2.QuerySet对象相当于一个高性能的列表（惰性加载），QuerySet对象中存放的是模型类对象
#     #     # 3.支持列表的数字索引(返回的是模型类对象)、切片（返回的依然是QuerySet对象）
#     #     # 查询集不支持负值索引
#     #     # 4.QuerySet对象.first()可以获取第一个元素、QuerySet对象.last()可以获取最后一个元素
#     #     # qs = Projects.objects.all()
#     #
#     #     # 二、获取某个指定的记录，使用get()
#     #     # 1.如果没有查询到记录，会报错；如果查询到了多个记录，也会报错；只有返回一条记录，才不会报错
#     #     # 2.返回的是模型类对象
#     #     # 3.get方法，最好使用主键或者唯一键去查询
#     #     one_project = Projects.objects.get(id=18)
#     #     # one_project = Projects.objects.get(name='项目1')
#     #     # one_project = Projects.objects.get(leader='某人')  #查询到多个，报错
#     #
#     #     # 三、获取多条记录，使用filter()
#     #     # 1.即使只查出一条数据，仍然返回的是QuerySet对象
#     #     # 2.如果没有匹配的信息，会返回一个空的QuerySet对象，不会报错
#     #     #3.使用字段去查询时，为完整匹配
#     #     Projects.objects.filter(leader="某人")
#     #
#     #     #4.字段名__contains，将包含字符串的数据全部取出
#     #     Projects.objects.filter(name__contains='项目')  # 包含运算，需要传字符串,会将name中包含项目的查询出来
#     #
#     #     #5.字段名__icontains=字符串,将包含指定字符串(忽略大小写)的数据全部取出
#     #     Projects.objects.filter(name__icontains="c")
#     #
#     #     #6.字段名__in=列表，将指定列表中的数据取出
#     #     Projects.objects.filter(leader__in=['可优', '某人'])  # 成员运算，会将leader为可优或者某人的数据查询出来
#     #
#     #     #7.name__endswith=""  ,将以某某结尾的数据取出
#     #     Projects.objects.filter(name__endswith="项目")
#     #     #8.name__startswith="" ，将以某某开头的数据取出
#     #     Projects.objects.filter(name__startswith="国产")
#     #     #9.name__regex="",将与正则表达式匹配的数据取出
#     #     Projects.objects.filter(name__regex=".*9.*")#将名称中存在9的数据取出
#     #     #10.字段名__gt:大于；字段名__gte:大于等于；字段名__lt:小于；字段名__lte:小于等于
#     #
#     #
#     #     #四、关联查询
#     #     #1.将多个条件在同一个filter中指定，那么为"与"的关系
#     #     Projects.objects.filter(name__contains="项目",id__gt=18)  #查询名称中包含项目且id大于18的数据
#     #
#     #     #2.一个QuerySet对象支持链式操作，可以同时调用多个filter
#     #     Projects.objects.filter(name__contains="项目").filter(id__gt=18)
#     #
#     #     #3.“或”的关系，需要使用Q变量,要先导入Q
#     #     #可以使用Q变量来实现
#     #     Projects.objects.filter(Q(name__contains="国产") | Q(id=4))
#     #
#     #     #五、多表关联查询
#     #     #使用从表条件来查询父表数据
#     #     #使用从表模型类名小写__从表字段名__条件运算符
#     #     Projects.objects.filter(interfaces__name__contains="注册") #查询出interfaces表中名称包含注册的接口对应的项目信息
#     #
#     #     #六、获取查询集对象的数量
#     #     #使用查询集对象调用count()方法获取查询集中数据条数
#     #     Projects.objects.filter(name__contains="国产").count()
#     #     #也可以使用len()方法获取查询集中数据条数
#     #     len(Projects.objects.filter(name__contains="国产"))
#     #
#     #     #七、排序操作
#     #     #可以使用查询集对象调用order_by方法来对查询集排序
#     #     #默认是升序，如需要降序，可以在字段名前加-
#     #     Projects.objects.filter(name__contains="项目").order_by("id")  #默认正序
#     #     Projects.objects.filter(name__contains="项目").order_by("-id")  #在排序字段前面加-，为倒序
#     #
#     #
#     #
#     #
#     #     return HttpResponse("项目创建成功")
#
#     # def post(self, request):
#     #     # 如果要以请求体传递参数，绝大多数情况下，get请求没有请求体
#     #     # 二、请求体传参：
#     #     # form表单传参：
#     #     # 1.可以使用request.POST来获取www-form表单类型的参数
#     #     # 2.获取的是QueryDict对象，可以类比于字典，可以使用[]或者.get()方法获取具体的值
#     #     # 3.如果有多个相同的key，可以使用getlist(key)方法获取
#     #
#     #     # django中的响应：
#     #     # HttpResponse第一个参数content为响应体（字符串）
#     #     # 第二个参数为Content-Type，指定响应数据格式,默认为：text/html
#     #     # 第三个参数为响应状态码，默认为200
#     #     return HttpResponse("<h1>POST请求：Hello，测开大佬们!<h1>", status=400)
#     #
#     # def put(self, request, pk):
#     #     # json格式传参：
#     #     # json中字符串只能用双引号，不能用单引号；json中不可能有相同的key；
#     #     # 如果要获取json格式的请求参数，需要从请求体中获取
#     #     # 1.request.body返回的是bytes类型，需要用decode("utf-8")转换为字符串
#     #     # 2.再使用json模块，将json格式的数据转化为字典
#     #     print(json.loads(request.body.decode("utf-8")))
#     #
#     #     # 如果要传文件给后端：
#     #     # request.FILES获取
#     #
#     #     # 四、如果使用请求头来传递参数
#     #     # 1.可以使用request.META来获取参数
#     #     # 2.key值为HTTP_为前缀+传递的参数的key值大写：request.META("HTTP_AUTHORIZATION")
#     #     return HttpResponse("<h1>PUT请求：Hello，测开大佬们!<h1>")

class ProjectsList(View):
    def get(self,request):
        Projects.objects.all()
        pass

    def post(self,request):
        '''
        将前段传递的json格式数据转换为python中的数据类型（模型类）--反序列化
        将模型类对象转换为json格式的数据--序列化
        :param request:
        :return:
        '''
        #1.接收参数&校验参数

        #2.向数据库中新增项目

        #3.返回结果
        pass



class ProjectEdit(View):

    def get(self,request,pk):
        '''
        获取指定项目的信息
        :param request:
        :param pk:
        :return:
        '''
        #1.校验前端传递的pk（项目id）值

        #2.获取指定pk值得项目
        Projects.

        #3.将模型类对象转化为字典
        one_dict={

        }
        pass

    def put(self,request,pk):
        '''
        更新指定的项目
        :param request:
        :param pk:
        :return:
        '''
        # 1.校验前端传递的pk（项目id）值

        # 2.获取指定pk值得项目

        #3.
        pass


    def delete(self,request,pk):
        '''
        删除指定的数据
        :param request:
        :param pk:
        :return:
        '''
        # 1.校验前端传递的pk（项目id）值

        # 2.获取指定pk值得项目

        #3.删除项目

        #4.返回
        pass
