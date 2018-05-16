# apkserver

用django搭建的后台服务器。主要用于获取带拆包apk及对拆完的包上传。

**运行时环境**

- python 3.6.4
- Django 2.0.5

**主要接口：**

- 文件列表
- 文件下载
- 多文件上传
- 接口测试

**要关注的文件：**

- cfg.py  配置文件输入输出路径
- urls.py  配置接口访问地址及对应的脚本
- view.py 接口具体实现
- manage.py 启动django服务器的管理器
- settings.py 服务器设置
- pmap.jar 主要是对pmap.ser的解析与生成。调用方法见view.py->uploadhole 只有一行命令

**django的安装及用法推荐一个教程在**[这里](http://www.runoob.com/django/django-tutorial.html)


 **manage.py如何启动服务器？**

安装好python后配置环境变量，然后运行以下命令即可：
```
python manage.py runserver 0.0.0.0:8020
```

**其他：**

之前metacore下载测试已经拆过包的洞文件，这个逻辑我没有动，还是按照原来的逻辑走
