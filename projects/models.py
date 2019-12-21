from django.db import models

# Create your models here.

class Person(models.Model):
    '''
    创建Person表，相当于数据库中的一个表

    '''
    #类属性：相当于数据库表中的字段
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


#1.每个应用下的数据库模型类，需要在当前应用下的projects/models.py文件中定义
#2.一个数据库模型类相当于一个数据表（table）
#3.数据库模型类必须继承Model或者Model子类
class Projects(models.Model):
    '''
    创建Project模型类
    '''

    #4.模型类中定义的类属性，一个类属性相当于数据表中的一个字段
    #5.默认会创建一个自动递增的id主键
    #如果手动创建了一个primary_key=True的类属性，则Django不会自动创建id
    # id = models.IntegerField()  #IntegerField不会自增
    #6.verbose_name可以设置更人性化的字段名
    #7.help_text来设置字段的描述信息（在api接口文档）
    id = models.AutoField(verbose_name="id主键",primary_key=True,help_text="id主键")   #AutoFile会自增，默认就是这样创建的

    #8.unipue设置当前字段是否唯一，默认unique=False
    #9.用max_length来限制字段的最大长度
    name = models.CharField(verbose_name="项目名称",help_text="项目名称",unique=True,max_length=200)
    leader = models.CharField(verbose_name="项目负责人",help_text="项目负责人",max_length=30)
    tester = models.CharField(verbose_name="测试负责人",help_text="测试负责人",max_length=30)
    programmer = models.CharField(verbose_name="开发负责人",help_text="开发负责人",max_length=30)
    publish_app = models.CharField(verbose_name="发布应用",help_text="发布应用",max_length=100)

    #10.default来指定默认值，
    #11.blank用于设置在创建项目时前端可以不用传此字段
    #12.null用于设置数据库此字段允许为空
    desc = models.CharField(verbose_name="简要描述",help_text="简要描述",
                             max_length=200,default="",blank=True,null=True)


    #13.auto_now_add在新增数据时，会自动添加当前创建的时间（只会添加一次）
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间",help_text="创建时间")
    #14.auto_now在每次更新时，会自动修改更新时间（每次更新都会修改）
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间",help_text="更新时间")

    #如果数据表中有历史数据，然后添加了新的字段，则需要给该字段设置默认值，或者设置为可以为空
    # age = models.IntegerField(default=0)
    # age2 = models.IntegerField(null=True)

    #生成迁移脚本：python manage.py makemigrations 子应用名（可添加也可以不添加，不添加则会将所有的子应用进行迁移）
    #执行迁移脚本：python manage.py migrate 子应用名（可添加也可以不添加，不添加则会将所有的子应用进行迁移）

    #默认情况下，创建的数据库表名为：子应用名_模型类名小写

    #创建内部类（在类的里面创建类）
    #定义Meta内部类，用于设置当前数据模型元数据信息
    class Meta:
        #可以在Meta中使用db_table自定义表名
        db_table = "tb_projects"
        verbose_name = "项目"

    def __str__(self):
        return self.name
