from django.urls import path

# from projects.views import index
from .views import index    #建议使用这种方式导入，.表示当前目录
from .views import IndexView

#子路由（子应用下创建的路由表）
urlpatterns = [
    path('index_page/',index),
    #如果调用类视图，那么path函数的第二个参数为类视图名.as_view()
    path('index/',IndexView.as_view()),

    #三、路径参数：
    #如果要接收路径参数，需要定义路由时来定义
    #使用路径参数类型转化器（int、slug、uuid）
    #pk是给路径参数命名
    #还需要在类视图或者函数视图中传入路径参数名
    path("index/<int:pk>/",IndexView.as_view())

    path('projects/',.as_view)
    path('projects/<int:pk>/',views.Projects)

]