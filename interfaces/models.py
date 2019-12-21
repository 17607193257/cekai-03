from django.db import models

from projects.models import Projects


# Create your models here.
class Interfaces(models.Model):
    '''
    接口模型类
    一个项目中有多个接口
    一个接口往往属于一个项目
    项目表与接口表的关系：一对多
    需要在“多”的那一侧，去创建外键
    '''
    id = models.AutoField(verbose_name="id主键", help_text="id主键", primary_key=True)
    name = models.CharField(verbose_name="接口名称", help_text="接口名称", unique=True, max_length=200)
    tester = models.CharField(verbose_name="测试负责人", help_text="测试负责人", max_length=200)
    desc = models.CharField(verbose_name="项目描述", help_text="项目描述", default="", blank=True, null=True,
                            max_length=200)

    # ForeignKey第一个参数为“应用名.模型类”或者模型类(需要先导入模型类)
    # project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    # on_delete设置的是：当父表（项目表）中的字段被删除之后，从表该字段的处理方式
    # models.CASCADE：子表也会自动删除
    # models.SET_NULL：子表会自动设置为null
    # related_name:指定父表对子表的引用名，如果不指定，默认为子表模型类名小写_set(interfaces_set)
    #接口表数据迁移后，表中的字段为project_id,存放的是项目id
    project = models.ForeignKey("projects.Projects", on_delete=models.CASCADE, related_name="interfaces",
                                help_text="所属项目")



    create_time = models.DateTimeField(verbose_name="创建时间", help_text="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", help_text="更新时间", auto_now=True)

    class Meta:
        db_table = "tb_interfaces"
        verbose_name="接口"

    def __str__(self):
        return self.name
