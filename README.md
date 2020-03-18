### 1. 获取django版本

> python -m django --version 


### 2. 创建项目(mysite 为项目名字)
> django-admin startproject mysite
+ 将生成如下文件
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
### 3. 用于开发的简易服务器
> python manage.py runserver
> python manage.py runserver 8080
> python manage.py runserver 0:8000

### 4. 创建应用
> python manage.py startapp Auto
+ 这里Auto是app neme
+ 这个命令也会创建一些文件
```
Auto/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### 5. 编写第一个视图函数
开始编写第一个视图。打开 Auto/views.py，把下面这些 Python 代码输入进去：
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

这是 Django 中最简单的视图。如果想看见效果，我们需要将一个 URL 映射到它——这就是我们需要 URLconf 的原因了。

创建 URLconf，请在 Auto 目录里新建一个 urls.py 文件。你的应用目录现在看起来应该是这样：
```
Auto/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```
在 Auto/urls.py 中，输入如下代码：
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
下一步是要在根 URLconf 文件中指定我们创建的 polls.urls 模块。在 AutoiOS/urls.py 文件的 urlpatterns 列表里插入一个 include()， 如下：
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
函数 include() 允许引用其它 URLconfs。每当 Django 遇到 include() 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理。
我们设计 include() 的理念是使其可以即插即用。因为应用有它自己的 URLconf( APPs/urls.py )，他们能够被放在 "/xxx/" ， "/fun_xxx/" ，"/content/xxx/"，或者其他任何路径下，这个应用都能够正常工作。

### 6. 数据库配置
打开 settings.py 这是个包含了 Django 项目设置的 Python 模块。
通常，这个配置文件使用 SQLite 作为默认数据库。如果你不熟悉数据库，或者只是想尝试下 Django，这是最简单的选择。Python 内置 SQLite，所以你无需安装额外东西来使用它。当你开始一个真正的项目时，你可能更倾向使用一个更具扩展性的数据库，例如 PostgreSQL，避免中途切换数据库这个令人头疼的问题。
通常，这个配置文件使用 SQLite 作为默认数据库。如果你不熟悉数据库，或者只是想尝试下 Django，这是最简单的选择。Python 内置 SQLite，所以你无需安装额外东西来使用它。当你开始一个真正的项目时，你可能更倾向使用一个更具扩展性的数据库，例如 PostgreSQL，避免中途切换数据库这个令人头疼的问题。

如果你想使用其他数据库，你需要安装合适的 database bindings ，然后改变设置文件中 DATABASES 'default' 项目中的一些键值：

ENGINE -- 可选值有 'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.db.backends.mysql'，或 'django.db.backends.oracle'。其它 可用后端。
NAME - 数据库的名称。如果使用的是 SQLite，数据库将是你电脑上的一个文件，在这种情况下， NAME 应该是此文件的绝对路径，包括文件名。默认值 os.path.join(BASE_DIR, 'db.sqlite3') 将会把数据库文件储存在项目的根目录。
如果你不使用 SQLite，则必须添加一些额外设置，比如 USER 、 PASSWORD 、 HOST 等等。想了解更多数据库设置方面的内容，请看文档：DATABASES 。

### 7. 设置 settings.py TIME_ZONE 为你自己时区。
### 8. 创建数据表
>  python manage.py migrate
### 9. 创建数据库模型
```
设计哲学

模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为。Django 遵循 DRY Principle 。它的目标是你只需要定义数据模型，然后其它的杂七杂八代码你都不用关心，它们会自动从模型生成。

This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely derived from your models file, and are essentially a history that Django can roll through to update your database schema to match your current models.
```
#### 在 Auto应用中的models.py 中编写数据库模型
```
from django.db import models

#这里设计模型

class AutoiOS(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

```
### 激活模型
上面的一小段用于创建模型的代码给了 Django 很多信息，通过这些信息，Django 可以：

为这个应用创建数据库 schema（生成 CREATE TABLE 语句）。
创建可以与 表 对象进行交互的 Python 数据库 API。
但是首先得把 Auto 应用安装到我们的项目里。
现在你的 Django 项目会包含 Auto 应用。接着运行下面的命令：
> python manage.py makemigrations Auto
会有如下输出

```
Migrations for 'Auto':
  Auto\migrations\0001_initial.py
    - Create model AutoiOS
```
现在，再次运行 migrate 命令，在数据库里创建新定义的模型的数据表
> python manage.py migrate

