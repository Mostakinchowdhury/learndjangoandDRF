# Django + DRF ফুল হ্যান্ড নোড

আমি প্রোগ্রামিং সবচেয়ে বেস্ট উপায়ে শিখতে চাই আর কোনকিছু দীর্ঘদিন ধরে মনে রাখার উপায় এবং কোনকিছু
বেস্ট ওয়েতে শেখার প্রসেস হলো সেই টপিক ভালো করে পড়া হ্যান্ড নোড করা এবং তা বেশি বেশি করে প্র্যাক্টিস
করা। তাই আমি django শিখতেসি এবং তা দীর্ঘদিন ধরে মনে রাখার জন্য হ্যান্ডনোট করসি যাতে ভবিৎষতে আমি
django এবং DRF রিভাইস দিতে পারি। আমি আশা করসি যদি কেউ django + DRF জানেন কিন্তু অনেকদিন ধরে
প্র্যাক্টিসে না করার কারণে আপনি অনেক কিছু ভুলে যান তাহলে এই হ্যান্ডনোট টি পরে আপনি রিভাইস দিতে পারেন
এর ফল আপনার আবার সবকিছু আয়ত্তে আসবে ইনশাআল্লাহ।

## Authors

- [@Mostakin IBN Mohir Ali](https://github.com/Mostakinchowdhury)

## Day 1: Django Introduction & Setup

django হলো পাইথন ল্যাংগুয়েজ এর ফ্রেমওয়ার্ক যা দিয়ে আমরা ওয়েব এপ্লিকেশন এর ব্যাকএন্ড নিয়ে কাজ করতে
পারি। Django MVT প্যাটার্নে কাজ করা। M=Model ,v=view এন্ড T=template. আমাদেরকে django কমপ্লিট সেটআপ
করার জন্য কিছু step ফলো করার লাগবে নিচে তা এক এক করে করে আমি Explain করছি ।

#### Step 1

Django সেটআপ করার জন্য প্রথমে আমাদের একটা পাইথন ভার্চুয়াল এনভায়রনমেন্ট Make করতে হবে। ভার্চুয়াল
এনভায়রনমেন্ট make করার জন্য নিচে কমান্ড তা cmd তে run করতে হবে।

```bash
  python -m venv environment_name

```

- এনভায়রনমেন্ট টিকে একটিভ করার জন্য নিচে কমান্ড তা রান করতে হবে

```bash
   environment_name\scripts\activate
```

#### Step 2

এই step এ আমাদের django নিচের কমান্ড দিয়ে ইনস্টল করে নিতে হবে।

```bash
  pip install django

```

- django relatate সব subcomand দেখার জন্য আমরা নিচের কমান্ড টা রান করতে পারি এই কমান্ড টা রান করলে
  আমাদের django relatate সব sub command এর একটা list দেখতে পাবো এই কম্যান্ড গুলা দিয়েই মূলত django
  এর সব কাজ করতে হয়।

```bash
  django-admin

```

- output হিসাবে টার্মিনাল এ এই লিস্ট টা পাবো

```bash
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
```

#### Step 3

এবার django দিয়ে আমাদের একটা project make করতে হবে যেই প্রজেক্ট এ অনেকগুলা এপ থাকবে। প্রজেক্ট
বানানোর জন্য django এর sub command থেকে startproject কমান্ড টা রান করতে হবে।

```bash
  django-admin startproject project-folder-name

```

- project-folder-name না দিয়ে যদি শুধু একটা . (ডট) দেয় তাহলে প্রজেক্ট এর জন্য কোন ফোল্ডার ক্রিটে না
  হয়ে root ফোল্ডার এর প্রজেক্ট bundle ডাউনলোড হবে।

#### Step 3

লাস্ট স্টেপ টাতে আমরা আমাদের django এর বিল্ড ইন সার্ভার টাকে রান করবে এর জন্য আমাদের নিচের কমান্ড টা
লিখতে হবে কমান্ড promt এ।

- যদি আমরা . না দিয়ে নতুন projects এর জন্য ফোল্ডার Create করি তাহলে আগে সেই ফোল্ডার এ যেতে হবে

```bash
   cd project-folder-name

```

- এরপর আমাদের সার্ভার রান করার জন্য নিচের কমান্ড তা রান করতে হবে আর যদি . দিয়া project create করি
  নতুন ফোল্ডার না বানাই তাহলে আমাদের cd করে কোন ফোল্ডার এ যেতে হইবে না।

```bash
   python manage.py runserver

```

- Now you are create a blank django project successfully

## Startapp Basic view render

- App create করার জন্য আমাদের নিচের কম্যান্ড টা রান করতে হবে।

  ```bash
  python manage.py startapp app-name

  ```

- এরপর project এর মেইন setting.py এর ভিতর installed_apps এ গিয়ে apps টাকে add করে দিতে হবে।

```python

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "Your-app-name",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

- এরপর main এর urls.py তে গিয়ে এপ এর urls.py কে include করতে হবে

```python
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("yourappname.urls"))
]

```

- এখন আমাদের এপ এর urls.py এ গিয়ে app_name সেট করতে হবে এবং সেই সাথে views.py এ গিয়ে ভিউ create করতে
  হবে তা urls.py তে urls mapping করে পাথ সেট করে দিতে হবে

app/urls.py

```python
from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path('',views.viewname)
]
```

app/views.py

```python
from django.shortcuts import render

def viewname(request):
  return render(request,"appname/htmlfilename.html")
```

- এখন আমাদের simple টেম্পলেট রেন্ডার করার জন্য লাস্ট একটা স্টেপ রয়েছে তা হলো টেম্পলেটে create করা।
  টেমপ্লেট create করার জন্য আমাদের app ফোল্ডার এ template নামে একটা ফোল্ডার create করতে হবে এবং সেই
  ফোল্ডার এর ভিতর এপ এর নামের সাথে মিল রেখে আর ও একটা ফোল্ডার crete করতে হবে finally সেই ফোল্ডার এ
  html ফাইল বা template গুলা create করে রাখতে হবে। html ফাইল এর পাথ অবশ্যই
  appname/templates/appname/htmlfilename.html হবে

app/templates/appname/htmlfilename.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple django themplate</title>
  </head>
  <body>
    <h1>Hi i am new to django welcome to django</h1>
  </body>
</html>
```

[ Now You are succesfully compleate "Startapp Basic view render" topic by following 5 step]

## Day 2: Templates, Static Files & URL Routing

- Base Template ও Template Inheritance

- Static Files (CSS, JS, Images)

- url, name, {% url %} tag

#### <১> Base Template ও Template Inheritance :

আগের দিনে আমরা পড়েছি যে টেম্পলেট বা html ফাইল এর path অবশ্যই app/template/app-name/htmlfilename.html
হতেই হবে। সেভাবে আমরা html file বা django template banate পারি। django তে html ফাইল গুলা আমরা
ড্যাঙ্গ টেম্পলেট হিসাবে craete করি তা আমরা জানি।django templat এ অনেক কিছু বিল্ড ইন syntex থাকে যা
বেসিক html এ থাকে না তার moddhe একটা ওয়ান অফ টি বেস্ট সিন্টেক্স হচ্ছে template ইনহেরিট এবং টেম্পলেট
include টেম্পলেট ইনহেরিট হলো ক্লাস ইনহেরিট এর মতো জেক ইনহেরিট করবে তার সবকিছু ওখানে পাবো + আমরা নিচে
থেকে আরো কিছু এলিমেন্ট ট্যাগ use করবো। {% extends %} মূলত parent template থেকে structure/inheritance
নেয়। এটা বলে: "আমি এই template-এর ভিতর বসে নিজের content দেখাবো।"

কখন ব্যবহার করব?

যখন তুমি একটি base layout বানিয়ে বিভিন্ন পেইজে একই header, footer, navbar ইত্যাদি রাখতে চাও।

extendbase.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}My Website{% endblock %}</title>
  </head>
  <body>
    <header>Navbar</header>

    {% block content %} {% endblock %}

    <footer>Copyright ©</footer>
  </body>
</html>
```

home.html

```html
{% extends "base.html" %} {% block title %}Home Page{% endblock %} {% block content %}
<h1>Welcome to Home Page</h1>
{% endblock %}
```

include হলো php এর ইনক্লুড এর মতো বা sass এর import এর মতো {% include %} দিয়ে অন্য একটি ছোট template
ফাইলকে বর্তমান ফাইলে টুকরা অংশ হিসেবে বসানো হয়।যখন তুমি একটুকরো কোড (যেমন: navbar, sidebar,
product_card) একাধিক ফাইলে ব্যবহার করতে চাও। তখন include use করবো।

navbar.html

```html
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
  </ul>
</nav>
```

base.html

```html
<body>
  {% include "navbar.html" %} {% block content %}{% endblock %} {% include "footer.html" %}
</body>
```

include vs extend

| বিষয়                       | `{% extends %}`                     | `{% include %}`                       |
| -------------------------- | ----------------------------------- | ------------------------------------- |
| 📚 উদ্দেশ্য                | Template inherit (layout structure) | Template reuse (ছোট অংশ টুকরা)        |
| 🏗️ কাজ                     | base template থেকে layout নেয়       | নির্দিষ্ট অংশ অন্য template-এ বসায়    |
| 📦 ব্যবহার                 | page structure তৈরি করতে            | reusable section (navbar, card) বসাতে |
| 📄 base tag লাগে           | হ্যাঁ                               | না                                    |
| 🧠 Block system ব্যবহার হয় | হ্যাঁ (`{% block %}` দিয়ে)          | না (just বসায়)                        |

#### <২> Static Files (CSS, JS, Images)

Django-তে Static Folder ব্যবহার করার মূল কারণ🔹

✅ Path ব্যবস্থাপনা সহজ ও নিরাপদ তুমি যদি সরাসরি এমন লিখো:

```html
<link rel="stylesheet" href="css/style.css" />
```

তাহলে Django বুঝবেই না — এই ফাইল কোথায় আছে।

কিন্তু তুমি যদি লিখো:

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

Django নিজেই বুঝে যাবে — ফাইলটা কোথায় আছে, কিভাবে serve করতে হবে, এবং ডিপ্লয়মেন্টে কীভাবে handle
করতে হবে।

✅ ডিপ্লয়মেন্টে কাজ করে

সোজা কথায়, Django production mode (live server) এ তোমার static file serve করবে না যদি তুমি
{% static %} ব্যবহার না করো।

ডিপ্লয়মেন্টে Django নিচের কমান্ড দিয়ে static ফাইল এক জায়গায় নিয়ে নেয়:

```
python manage.py collectstatic
```

এটা তখন সব static ফাইল STATIC_ROOT এ রাখে — যাতে nginx/gunicorn serve করতে পারে।

✅ Multiple app এর মধ্যে ফাইল conflict থেকে রক্ষা করে ধরো তোমার ২টা app:

blog

shop

দুটোতেই style.css আছে। তুমি যদি static folder use না করো, তাহলে কোনটা কোনটার ফাইল — Django জানবে না।

কিন্তু তুমি যদি app-ভিত্তিক static রাখো: blog/static/blog/style.css shop/static/shop/style.css তাহলে
Django পরিষ্কার বুঝতে পারবে কোনটা কার।

blog হলো app আর এর ভিতর static টা হলো app static আর প্রজেক্ট এর ভিতর static টা হলো project স্ট্যাটিক
এটা গ্লোবাল whole app এর জন্য করবে।

✅ Django-তে Static File ব্যবহারের জন্য করণীয় 🔶 Step 1: settings.py এ Static এর config

python settings.py

```
STATIC_URL = '/static/'
```

উন্নত ব্যবহারের জন্য (optional কিন্তু ভালো)

```
STATICFILES_DIRS = [
   BASE_DIR / "static",
]
```

🔶 Step 2: Project ফোল্ডারে static/ নামের ফোল্ডার বানাও

```
your_project/
├── manage.py
├── your_app/
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
```

👉 এই ফোল্ডারের ভিতরে CSS/JS/Image রাখো

🔶 Step 3: Template ফাইলের শুরুতে {% load static %} ব্যবহার করো

```
{% load static %}
```

🔶 Step 4: Static Files লিংক করো {% static %} ট্যাগ দিয়ে ✅ CSS ফাইল:

```html
<link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

✅ JS ফাইল:

```html
<script src="{% static 'js/main.js' %}"></script>
```

✅ Image ফাইল:

```html
<img src="{% static 'images/banner.jpg' %}" alt="Banner" />
```

ফুল html

```html
{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <title>My Website</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
  </head>
  <body>
    <h1>Welcome</h1>
    <img src="{% static 'images/logo.png' %}" alt="Logo" />

    <script src="{% static 'js/app.js' %}"></script>
  </body>
</html>
```

structure

```
project/
├── static/
│   └── css/
│       └── global.css
├── blog/
│   └── static/
│       └── blog/
│           └── blog.css
```

blog/template/blog/htmlname.html

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/global.css' %}" />
<link rel="stylesheet" href="{% static 'blog/blog.css' %}" />
```

❗ যদি static কাজ না করে:

✅ ১. settings.py এ STATICFILES_DIRS আছে কিনা দেখো

✅ ২. template ফাইলে {% load static %} দেয়া হয়েছে কিনা

✅ ৩. ফাইল path ভুল আছে কিনা (সব ছোট হাতের হলে ভালো হয়)

✅ ৪. Django server চালু আছে কিনা python manage.py runserver

#### Some FAQ FOR STATIC FOLDER

| প্রশ্ন                          | উত্তর                                                        |
| ------------------------------- | ------------------------------------------------------------ |
| Static folder কেন ব্যবহার করবো? | Django static file serve করতে পারে ও ডিপ্লয়মেন্টে সংগ্রহ করে |
| সরাসরি path দিলেই হয় না?        | হয় না — Django serve করতে পারবে না                           |
| কখন app-static রাখবো?           | যখন file শুধুমাত্র ওই app এর মধ্যে ব্যবহৃত                   |
| কখন project-static রাখবো?       | যখন file global/base layout এ ব্যবহৃত হয়                     |
| Static file auto serve হয় কখন?  | development mode এ, debug=True হলে                           |

                        |

### <৩> url, name, {% url %} tag

🧠 ১. url কি? url অর্থ হচ্ছে — Django-এর রাউটিং সিস্টেম। এই রাউট দিয়ে Django বোঝে কোন view ফাংশন কোন
path বা address এ চলবে।

🧠 ২. name কি? Django-তে url pattern-এ name দিলে তুমি ঐ URL টা টেমপ্লেট, রিডাইরেক্ট বা রিভার্স করার
সময় নাম দিয়ে access করতে পারো।

👉 সহজভাবে বললে: name হলো url এর nickname যেটা দিয়ে {% url %} ট্যাগ, reverse(), redirect() ইত্যাদিতে
কাজ করা যায়।

🔖 ৩. {% url %} template tag 👉 টেমপ্লেটের ভেতরে href বা লিংকের ভিতরে name দিয়ে URL generate করতে
ব্যবহৃত হয়।

```
{% url 'url_name' %}
```

✅ step ১

```python
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about_page'),
    path('contact/<int:id>/', views.contact, name='contact_page'),
]
```

✅ step ২

```python
# myapp/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Home Page")

def about(request):
    return HttpResponse("About Page")

def contact(request, id):
    return HttpResponse(f"Contact Page of ID: {id}")
```

✅ step ৩ Template file (HTML)

```html
{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <title>Navigation</title>
  </head>
  <body>
    <!-- Static URL (not recommended) -->
    <a href="/about/">About</a>

    <!-- Dynamic URL (recommended) -->
    <a href="{% url 'about_page' %}">About</a>

    <!-- URL with dynamic parameter -->
    <a href="{% url 'contact_page' 5 %}">Contact ID 5</a>
  </body>
</html>
```

📝 Syntax:

| কাজ                | Syntax                                             |
| ------------------ | -------------------------------------------------- |
| সিম্পল URL         | `{% url 'name' %}`                                 |
| ভেরিয়েবল সহ        | `{% url 'name' variable %}`                        |
| একাধিক প্যারামিটার | `{% url 'name' param1 param2 %}`                   |
| with keyword args  | `{% url 'name' id=5 %}` _(if view accepts kwargs)_ |

✅ কেন {% url %} ট্যাগ ব্যবহার করব?

| কারণ               | ব্যাখ্যা                                       |
| ------------------ | ---------------------------------------------- |
| ✅ Maintainability | URL path বদল হলেও template পরিবর্তন করতে হয় না |
| ✅ DRY Principle   | এক জায়গায় নাম দিলে সব জায়গায় কাজ হয়            |
| ✅ Error free      | Hardcoded path লিখলে ভুল হওয়ার সম্ভাবনা বেশি   |
| ✅ Dynamic Routing | ID / slug / username ইত্যাদি সহজে বসানো যায়    |

🧪 উদাহরণ (Dynamic Routing)

```python

# urls.py
path('user/<int:id>/', views.user_profile, name='user_profile')
#views.py:
def user_profile(request, id):
    return HttpResponse(f"User ID: {id}")
```

```html
<!-- template.html: -->
<a href="{% url 'user_profile' 42 %}">User 42</a>
```

🔁 View থেকে URL reverse করার জন্য:

```python
from django.urls import reverse
reverse('user_profile', args=[42])
```

✅ Shortcut: redirect('name', args=[id])

```python
from django.shortcuts import redirect
return redirect('user_profile', id=5)
```

Common mistake

| ভুল                                  | কারণ                                             |
| ------------------------------------ | ------------------------------------------------ |
| `{% url home %}` → ❌                | কোটেশন ছাড়া লেখা যাবে না                         |
| `{% url 'contact_page' %}` → ✅      | Always use quotes                                |
| `{% url 'contact_page' id=5 %}` → ✅ | keyword argument দিলে অবশ্যই নাম ও মান লিখতে হবে |

ফাইনাল রিভিশন

```python
URL Pattern:
path('route/', views.function, name='route_name')

Template Usage:
{% url 'route_name' %} → for simple URL
{% url 'route_name' id %} → for dynamic URL

```

Bonus Tip: include() + name-spacing or app_name

```python
# project/urls.py
from . import views
app_name="home"
urlpatterns = [
    path('blog/', include('blog.urls', namespace='blog')),
    path('blog/',views.navbar,name="nav"),
]

```

```html
{% url 'blog:post_detail' 1 %} {% url 'home:nav'%}
```

## ✅ Day 3: Models & Admin Panel

1.models.Model দিয়ে DB Table তৈরি

2.makemigrations, migrate

3.Django Admin setup

4.Admin থেকে ডাটা Insert/Update/Delete

$ নিচের এই ৫ টি step ফলো করার মাধ্যমে আমরা এই ৪ টি টপিক আয়ত্ত করতে পারবো । এখানে প্রতিটা স্টেপ খুব
সুন্দর করে explain করা হলো।

📌 Step 1: models.py ফাইলে Table (Model) Define করুন 👉 myapp/models.py ফাইলে একটি ক্লাস তৈরি করুন
যেটা models.Model থেকে ইনহেরিট করে:

from django.db import models

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

| লাইন                          | ব্যাখ্যা                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `class Student(models.Model)` | Student নামে টেবিল হবে (ডিফল্টভাবে `myapp_student`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `CharField`                   | স্ট্রিং রাখার জন্য (ম্যাক্স লেন্থ দিতে হয়)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `IntegerField`                | সংখ্যা রাখে                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `EmailField`                  | ইমেইল ফিল্ড, সাথে unique=true মানে একই ইমেইল ২ বার রাখা যাবে না                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `auto_now_add=True`           | একবার object তৈরি হলে অটোমেটিক সময় যোগ হবে                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `__str__()`                   | অ্যাডমিন বা টেমপ্লেটে সুন্দরভাবে নাম।যখন আমরা sql এ group by এটা দিয়া টেবিল কে কোন colum এর ভিত্তিতে group করি তখন একাধিক raw বা table অবজেক্ট একটা অবজেক্ট raw এ কনভার্ট হয়। তখন ওই merge raw te কিন্তু আমরা প্রতিটা mergekrito কলাম কে হাইলাইট করার জন্য count(colum),max (colum ),average (colum) asb use করি Jen একটা ভ্যালু দিয়া পুরা মার্জ হয় কালাম হাইলাইট হয় . তেমনি যখন একটা raw বা অবজেক্ট কে আমরা mean করি django তে tokhon ওই অবজেক্ট এর সব কালাম এর নাম তো বলা সম্ভব হয় না ওই পুরা অবজেক্ট তাকে একটা colum দিয়া মিন করতে হয় সো ওই টেবিল টা কে কোন colum এর ভ্যালু দিয়া হাইলাইট করবো তা এই **str** ডান্ডার মেথড এ রিটার্ন করতে হয়। |

#### 📌 Step 2: Model Change এর পর makemigrations চালান

```bash
python manage.py makemigrations
```

🔹 কারণ: এটা Django কে বলে, “আমার মডেলে পরিবর্তন এসেছে, এগুলোর জন্য মাইগ্রেশন ফাইল বানাও।”

#### 📌 Step 3: ডেটাবেজে টেবিল তৈরির জন্য migrate চালান

```bash
python manage.py migrate
```

🔹 কারণ: এটা মাইগ্রেশন ফাইল দেখে আসল ডেটাবেইসে টেবিল তৈরি করে। database কে migrate মানে আপগ্রেড করে।

#### 📌 Step 4: Admin Panel-এ দেখতে চাইলে, Admin-এ রেজিস্টার করুন

👉 myapp/admin.py:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)

```

🔹 কারণ: এটা করলে Django Admin panel-এ Student মডেলটি দেখতে পাবেন এবং Create/Update মানে CRUD
অপারেশন চালাতে পারবেন django অ্যাডমিন এর মাধ্যমে।

📌 Step 5: সুপার ইউজার তৈরি করুন (admin panel চালানোর জন্য)

```bash
python manage.py createsuperuser
```

👉 তারপর লগইন করুন:

```arduino
http://127.0.0.1:8000/admin
```

🔹 কারণ: Admin Panel চালাতে একজন superuser লাগে।আর এভাবে একজন অ্যাডমিন মানে super ইউসার create করতে
হয় যে কিনা পুরা ওয়েব app টা কন্ট্রোল করবে। এই app এর কতৃপক্ষ।

#### 🧠 Django Admin Registration with modeladmin(custom configaretion)

👉 দুইভাবে Model Admin রেজিস্টার করা যায়:

##### 🔷 ১. admin.site.register() – কিভাবে কাজ করে? (Traditional way)

```python
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
#admin.site.register(model, modeladmin=None)
```

➤ Required ও Optional Part:

| Argument     | প্রয়োজনীয়?  | ব্যাখ্যা                                                                                       |
| ------------ | ----------- | ---------------------------------------------------------------------------------------------- |
| `model`      | ✅ Required | কোন Model টাকে admin প্যানেলে রেজিস্টার করছো                                                   |
| `modeladmin` | ❌ Optional | ওই মডেলের জন্য কাস্টম `ModelAdmin` ক্লাস দিলে এটা দিতে হয়, না দিলে default settings ব্যবহার হয় |

➤ কাজের ধরন: Django এর Admin প্যানেলে নির্দিষ্ট একটা Model যুক্ত করে।

যদি modeladmin না দাও, তাহলে Django ModelAdmin এর default behavior ব্যবহার করে।

🔷 ২. @admin.register(Model) – কিভাবে কাজ করে?

```python
@admin.register(Model)
class MyModelAdmin(admin.ModelAdmin):
    ...
```

➤ কাজের ধরন:

- এটি মূলত admin.site.register() এর শর্টকাট।

- ডেকোরেটর হিসেবে কাজ করে, মডেল এবং ModelAdmin ক্লাসকে একত্র করে। admin.register(model) একটা
  ডেকোরেটর function রিটার্ন করে সেই decorator ফাঙ্কশন আবার modeladmin paramitar হিসাবে নেয় এবং ওই
  মডেল অ্যাডমিন class অনুযায়ী ওই মডেল এর জন্য অ্যাডমিন প্যানেল এ কাস্টম ভিউ configer করে।

cleaner, DRY (Don't Repeat Yourself) style.

➤ Example:

```python
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
```

✅ এটাও admin.site.register(Product, ProductAdmin) এর মতোই কাজ করে, কিন্তু একসাথে লিখে ফেলা যায়।

🔁 admin.site.register() vs @admin.register() – তুলনা: | বিষয় | `admin.site.register()` |
`@admin.register()` | | ----------- | --------------------------------- |
---------------------------- | | পদ্ধতি | Function call | Decorator | | কোডের ধরন | আলাদা আলাদা
ক্লাস ও রেজিস্ট্রেশন | একই জায়গায় সব | | পরিচ্ছন্নতা | একটু লম্বা হয় | Clean & Compact | | প্রয়োজন |
যখন dynamic ভাবে register করতে হয় | যখন statically register করছো |

🟩 Suggestion:

যদি অনেকগুলো মডেল একসাথে রেজিস্টার করতে হয় বা আলাদা আলাদা ModelAdmin ক্লাস লাগবে, তাহলে
admin.site.register() ভালো। যদি একটি মডেল ও একটি ModelAdmin হয়, তাহলে @admin.register() ব্যবহার করো।

🧩 ModelAdmin ক্লাস কী করে? ModelAdmin হল Django Admin panel-এর জন্য কাস্টমাইজেশন ক্লাস। এটা দিয়েই
তুমি Admin interface কনফিগার করো।

🎯 কাজের তালিকা:

| Attribute                                 | কাজ                                   |
| ----------------------------------------- | ------------------------------------- |
| `list_display`                            | লিস্ট পেইজে ফিল্ড দেখায়               |
| `list_display_links`                      | কোন ফিল্ডে ক্লিক করলে edit পেইজে যাবে |
| `readonly_fields`                         | শুধু দেখাবে, edit করা যাবে না         |
| `search_fields`                           | সার্চবারে কোন ফিল্ড দিয়ে খুঁজবে       |
| `list_filter`                             | সাইডবারে ফিল্টার অপশন                 |
| `ordering`                                | কোন ক্রমে দেখাবে (ASC/DESC)           |
| `admin.site.register(model, admin_class)` | ক্লাসিক পদ্ধতি                        |
| `@admin.register(model)`                  | ডেকোরেটর পদ্ধতি (cleaner)             |

উদাহরণ:

```python
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    list_display_links = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
```

💡 মনে রাখার কৌশল (Shortcut Summary)

```pgsql
admin.site.register(Model, AdminClass)
➡️ সাধারণ পদ্ধতি, বড় প্রজেক্টে বেশি দরকার হয়

@admin.register(Model)
➡️ শর্টকাট ডেকোরেটর, ছোট কোডে clean লেখা যায়

ModelAdmin
➡️ admin panel এ কাস্টমাইজেশন করতে ব্যবহার হয়

ModelAdmin এ যেগুলো মনে রাখব:
✅ list_display       → কোন ফিল্ড লিস্টে দেখাবো
✅ list_display_links → কোনটা ক্লিক করলে edit e যাবে
✅ readonly_fields    → কোনটা edit করা যাবে না
✅ search_fields      → কোন ফিল্ড দিয়ে সার্চ হবে
✅ list_filter        → কোন ফিল্ডে ফিল্টার
✅ ordering           → কোন ফিল্ডে সাজাবে
```

✅ অতিরিক্ত কিছু গুরুত্বপূর্ণ মডেল ফিল্ড ও তাদের কাজ:

| Field                              | কাজ                  |
| ---------------------------------- | -------------------- |
| `CharField(max_length=...)`        | টেক্সট রাখে          |
| `TextField()`                      | বড় টেক্সট রাখে       |
| `IntegerField()`                   | সংখ্যা রাখে          |
| `FloatField()`                     | দশমিক সংখ্যা         |
| `BooleanField()`                   | True/False           |
| `EmailField()`                     | ইমেইল রাখে           |
| `DateTimeField(auto_now_add=True)` | তৈরি হওয়ার সময়       |
| `DateTimeField(auto_now=True)`     | প্রতিবার আপডেটের সময় |

📁 ফোল্ডার স্ট্রাকচার (সংক্ষেপে)

```pgsql
myproject/
├── manage.py
├── myproject/
│   └── settings.py
├── myapp/
│   ├── models.py       ← মডেল ফাইল
│   ├── admin.py        ← অ্যাডমিনে রেজিস্টার
│   └── migrations/
```

🧠 মনে রাখবেন:

- models.Model ব্যবহার করে আপনি Python ক্লাস দিয়ে SQL টেবিল তৈরি করতে পারেন।

- প্রতিবার মডেলে পরিবর্তন এলে আবার makemigrations এবং migrate দিতে হয়।

## ✅ Day 4: CRUD with ORM

1.Create/Read/Update/Delete (CRUD) operations

2.Django shell / ORM query practice

3.View থেকে DB data fetch করা

4.Data form দিয়ে insert করা

আমি এই লেসন গুলা কমপ্লিট করার জন্য কিছু স্টেপ নিচে এক্সপ্লেইন করসি যেটা দেখে আমরা এই লেসন তা কমপ্লিট
করতে পারি। উপরের এই ৫ টি লেসন আমরা নিচের এই ১০ টা স্টেপ এর মাধ্যমে আমরা রিভিশন দিতে পারবো
ইনশাআল্লাহ।

🔹 STEP 1: Django ORM (Object Relational Mapper) ORM দিয়ে Python কোড লিখেই ডেটাবেজে কাজ করা যায়, SQL
না লিখেও। Shell চালু করো:

```bash
 python manage.py shell
```

🔹 STEP 2: Create (তৈরি করা)

```python
from app_name.models import Product

# 1. Create with create()
Product.objects.create(name='Mobile', price=5000)

# 2. Create with instance
p = Product(name='Laptop', price=80000)
p.save()

```

🔹 STEP 3: Read (ডেটা পড়া)

```python
# সব ডেটা পড়া
Product.objects.all()

# Filter করা
Product.objects.filter(price__gt=5000)

# একক ডেটা
Product.objects.get(id=1)

```

🔹 STEP 4: Update (আপডেট করা)

```python
# প্রথমে instance আনো
p = Product.objects.get(id=1)
p.price = 6000
p.save()

```

🔹 STEP 5: Delete (মুছে ফেলা)

```python
# প্রথমে instance আনো
p = Product.objects.get(id=1)
p.delete()

```

🔹 STEP 6: View থেকে DB Data Fetch করা

```python
# views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
   products = Product.objects.all()
   return render(request, 'products.html', {'products': products})


```

products.html টেম্পলেট এ সেই ডাটা access করা।

```html
<!-- products.html -->
{% for product in products %}
<p>{{ product.name }} - {{ product.price }}</p>
{% endfor %}
```

🔹 STEP 7: Form দিয়ে Data Insert করা (without ModelForm)

```html
<!-- form.html -->
<form method="POST">
  {% csrf_token %}
  <input type="text" name="name" />
  <input type="number" name="price" />
  <button type="submit">Add Product</button>
</form>
```

```python
# views.py
from .models import Product
from django.shortcuts import render.redirect


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        Product.objects.create(name=name, price=price)
        return redirect("formsucces")
    return render(request, 'form.html')

```

🔹 STEP 8: Form + Modelform দিয়ে Data Insert করা

```python
# forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
```

👉 ModelForm ব্যবহার করলে ম্যানুয়ালি input বানাতে হয় না। Django নিজেই ফর্ম ফিল্ড তৈরি করে নেয়।

```python
# views.py

from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
```

```html
<!-- templates/add_product.html -->

<h2>Add Product</h2>
<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Add</button>
</form>
```

📝 {{ form.as_p }} মানে ফর্ম ফিল্ডগুলো <p> ট্যাগের ভিতরে রেন্ডার হবে।

🔹 STEP 8: Form + Modelform দিয়ে Data Update (Edit Product) করা

```python
# views.py

from .models import Product
from .forms import ProductForm

def edit_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})

```

```html
<!-- templates/edit_product.html -->

<h2>Edit Product</h2>
<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Update</button>
</form>
```

📌 instance=product দিলে form প্রি-ফিলড হবে আগের ডেটা দিয়ে। 📌 (request.POST, instance=product) দিলে
instance এর ডাটা মানে আগের ডাটা request.POST দ্বারা replace করবে।

🔹Django ModelForm এর ৪টি রূপ

| রূপ নম্বর | রূপ (Code)                                         | উদ্দেশ্য               | কখন ব্যবহার হয়                       | ব্যাখ্যা / উদাহরণ                                              |
| --------- | -------------------------------------------------- | ---------------------- | ------------------------------------ | -------------------------------------------------------------- |
| 1         | `ProductForm()`                                    | Empty form             | ফাঁকা ফর্ম দেখাতে                    | নতুন প্রোডাক্ট add করার সময়, প্রথমবার ফর্ম দেখানো হয়           |
| 2         | `ProductForm(data=request.POST)`                   | POST ডেটা নেওয়া        | ফর্ম সাবমিট হওয়ার পর ভ্যালিডেশন করতে | ইনপুট ভ্যালিড হলে `form.save()` করা হয়                         |
| 3         | `ProductForm(instance=product)`                    | প্রি-ফিল্ড ফর্ম        | আগের ডেটা সহ ফর্ম দেখাতে             | Edit করার সময় আগের প্রোডাক্টের ইনফো দিয়ে ফর্ম পূরণ হয়          |
| 4         | `ProductForm(data=request.POST, instance=product)` | Update with validation | ফর্ম সাবমিট করে ডেটা আপডেট করার সময়  | পুরাতন ডেটার উপর নতুন ভ্যালু বসিয়ে `save()` করলে ডেটা আপডেট হয় |

🔸 STEP 10: Advanced Product List View

```python
# views.py

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
```

```html
<!-- templates/product_list.html -->

<h2>Product List</h2>
<table border="1">
  <tr>
    <th>Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Actions</th>
  </tr>
  {% for p in products %}
  <tr>
    <td>{{ p.name }}</td>
    <td>{{ p.price }}</td>
    <td>{{ p.description }}</td>
    <td>
      <a href="{% url 'edit_product' p.id %}">Edit</a> |
      <a href="{% url 'delete_product' p.id %}">Delete</a>
    </td>
  </tr>
  {% endfor %}
</table>
```

✅ রিভিশন কৌশল:

| Form রূপ                                  | Context (কোথায় ব্যবহার হয়?)         |
| ----------------------------------------- | ----------------------------------- |
| `ProductForm()`                           | নতুন ফর্ম দেখানোর সময়               |
| `ProductForm(request.POST)`               | সাবমিটের পর ইনপুট যাচাই             |
| `ProductForm(instance=...)`               | আগের ডেটা প্রি-ফিল্ড করার সময়       |
| `ProductForm(request.POST, instance=...)` | সাবমিট করে আগের ডেটা আপডেট করার সময় |

## ✅ Day 5: Model Relationship

- one-to-one(onetonefield)
- One-to-Many (ForeignKey)
- Many-to-Many(manytomanyfield)
- related_name, related_query_name
- Query set chaining (filter, exclude)

#### 🔗 ১. One-to-One সম্পর্ক (OneToOneField)

- দুইটি মডেল যখন একে অপরের সঙ্গে এক-এক সম্পর্ক তৈরি করে।
- যখন একটা টেবিল এর একটা Raw অন্য একটা টেবিল এর একটা raw এর সাথে সম্পর্কযুক্ত।
- যেমন: প্রতিটি User এর একটাই Profile থাকবে।আবার যেমন একটা ইউসার এর একটাই settings থাকে বা একটাই।
  এখানে users একটা টেবিল আবার settings আর একটা টেবিল প্রোফাইল আর একটা টেবিল বুঝানো হয়েছে।

✅ কোড উদাহরণ:

```python
class User(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

🔍 on_delete=models.CASCADE মানে যদি User মুছে যায়, তার Profile-ও মুছে যাবে।

#### 🔗 ২. One-to-Many সম্পর্ক (ForeignKey)

- একটি মডেল অনেক গুলো instance-কে রিপ্রেজেন্ট করতে পারে অন্য একটি মডেলের মধ্য দিয়ে।
- যখন একটা টেবিল এর একটা raw অন্য একটা টেবিল এর এক বা একাধিক raw এর সাথে সম্পর্কযুক্ত।বলা যায় অনেক
  তা পিতা পুত্রের মধ্যে সম্পর্কের মতো এক পিতার এক বা একাধিক সন্তান থাকতে পারে।এই ক্ষেত্রে পিতা হলো
  যেই টেবিল কে foregnkey হিসাবে সেট করসি অন্যদিকে পুত্র হলে যেই টেবিলে foregnkey সেট করছি।
- যেমন: একটি Category-এর মধ্যে অনেকগুলো Product থাকতে পারে।আবার একটা ইউসার এর একাধিক message থাকতে
  পারে। একটা ইউসার একধিক অর্ডার দিতে পারে।এই ক্ষেত্রে user,category হলো পিতা টেবিল আর
  message,order,product হলো পুত্র টেবিল

✅ কোড উদাহরণ:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```

🔍 এখানে Product মডেলে ForeignKey রয়েছে Category-র সাথে। এক ক্যাটেগরিতে অনেক প্রোডাক্ট থাকতে পারে।

#### 🔗 ৩. Many-to-Many সম্পর্ক (ManyToManyField)

- দুইটি মডেলের মধ্যে অনেক-থেকে-অনেক সম্পর্ক।
- যখন একটি টেবিল এর এক বা একাধিক raw এর সাথে আরেকটি টেবিল এর এক বা একাধিক raw সম্পর্কযুক্ত। অনেক টা
  চাচা ভাতিজার সম্পর্কের মতো এক চাচার এক বা একাধিক ভাতিজা থাকতে পারে আবার এক ভাতিজার এক বা একাধিক
  চাচা থাকতে পারে।

- যেমন: একজন Student অনেক এক বা Course করতে পারে, আবার একটি Course-এ এক বা অনেক Student থাকতে
  পারে।একটি ট্যাগ এক বা একধিক পোস্ট এ এপলাই হতে পারে আবার একটি পোস্ট এ একাধিক ট্যাগ use হতে পারে।

✅ কোড উদাহরণ:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```

#### 🔄 ৪. related_name ও related_query_name

related_name:

- এটি reverse relationship করার সময় ব্যবহার হয়।

- যেখান থেকে relation তৈরি হয়নি, সেখান থেকেও access করতে দেয়।
- মানে পরস্পর সম্পর্কযুক্ত টেবিল গুলার ক্ষেত্রে একটা টেবিল এর raw এর সাথে সম্পর্কযুক্ত অন্য টেবিল
  raw এর এক্সেস।ralated name দ্বারা আমরা reverse এক্সেস এর name সেভ করতে পারি বাই ডেফল্ট এটা
  relatedtablename_sets থাকে তা আমরা চেঞ্জ করে নিজের মতো রাখতে পারি।
- এটা হচ্ছে Child Model থেকে Parent Model কে access করার পর, Parent এর reverse relation-এ Child গুলো
  কিসের মাধ্যমে access করব সেটা define করে।

🔸 সহজভাবে: Parent Model থেকে Child-দের access করার নাম।

✅ উদাহরণ:

```python
class Blog(models.Model):
    title = models.CharField(max_length=100)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
```

এখানে আমরা blog টেবিল হতে কি name দিয়া এর Raw এর মানে প্রতিটা blog এর comment এক্সেস করবো তা রিলেটেড
name দিয়া বলে দিতে পারি আমরা।

🔍 ব্যবহার:

```python
blog = Blog.objects.get(id=1)
comments = blog.comments.all()  # related_name ব্যবহার করে
```

##### related_query_name:

- এটি QuerySet chaining-এর সময় ফিল্টার করার জন্য কাজে আসে। ✅ উদাহরণ:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_query_name='books_written')

```

🔍 ব্যবহার:

```python
Author.objects.filter(books_written__title__icontains='python')
```

- মানে হলো প্যারেন্ট হতে ডাইরেক্ট তার রেলেটেট চাইল্ড raw গুলার ফিল্ড ট্র্যাক করতে পারি
  related_query_name হলো প্যারেন্ট এর রিলেটেড চাইল্ড গুলার অবজেক্ট এর ওপর কি নাম দিয়া query বা
  অপারেশন চালাবো। অর্থাৎ এটা রিলেটেড চাইল্ড গুলার queryset,fieldsets কে বুঝায়। যার ওপর বিভিন্ন
  কোয়েরি চলা হবে। বলা যায় এটা parent.childset এর shortform.
- এটা হচ্ছে যখন তুমি Parent Model কে filter করবে তার Child Model এর কোন attribute ব্যবহার করে, তখন
  কোন নামে query চলবে — সেটা define করে।

🔸 সহজভাবে: Parent Model কে filter করার সময়, related Child field-কে কোন নামে চেনাবে — সেটা। child এর
field অনুযায়ী প্যারেন্ট কে ফিল্টার বা প্যারেন্ট এ কোয়েরি চালানো। Parent Model থেকে Child-fields
অনুযায়ী কোয়েরি চালার নাম।

🔗 ৫. QuerySet Chaining (ফিল্টার করার জন্য)

✅ filter(): নির্দিষ্ট কিছু ডেটা ফিল্টার করতে:

```python
Product.objects.filter(price__gt=100)
```

✅ exclude(): নির্দিষ্ট কিছু বাদ দিতে:Filter এর উল্টো। ফিল্টার শর্ত মানা অবজেক্ট গুলা রিটার্ন করে আর
exclude শর্ত না মানা অবজেক্ট গুলা রিটার্ন করে

```python
Product.objects.exclude(product_type='digital')
```

🧠 Bonus Tip:

- সবসময় সম্পর্কের ধরন বুঝে OneToOneField, ForeignKey বা ManyToManyField ব্যবহার করতে হবে।

- related_name দিয়ে reverse querying আরও readable এবং manageable হয়।

- related_query_name দিয়ে queryset chaining অনেক clean হয়।

---

## ✅ Day 6: Django Forms & ModelForm

#  Django Form Handling Handnote ✍️

এই নোটটি Django Form Handling নিয়ে আজকের আলোচনা অনুযায়ী তৈরি করা হয়েছে — প্রতিটি টপিক, function,
এবং concept সুন্দরভাবে ব্যাখ্যা করে future এ রিভিশনের জন্য সংরক্ষণ করা হলো।

---

### 🎯 1. Form vs ModelForm

| Aspect                           | Form                                                          | ModelForm                                                 |
| -------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------- |
| Data Source                      | Manual Field define                                           | Model থেকে Field auto create                              |
| Use-case                         | Non-model data অথবা manual validation                         | Direct Model CRUD জন্য                                    |
| Advantage                        | বেশি control                                                  | auto fields, less code                                    |
| 🎯 উদ্দেশ্য                      | ম্যানুয়ালি ফিল্ড বানিয়ে ফর্ম তৈরি করা                         | মডেল এর উপর ভিত্তি করে ফর্ম অটো তৈরি করা                  |
| 🧱 Field কিভাবে তৈরি হয়          | প্রত্যেকটি Field নিজে declare করতে হয়                         | Model এর Field গুলো নিজে নিজে ফর্মে যুক্ত হয়              |
| 📝 কোথায় ব্যবহার হয়              | যখন কোনো মডেলের উপর ভিত্তি করে ফর্ম না, বরং কাস্টম ইনপুট লাগে | যখন কোনো মডেলের ইনপুট/ডেটা CRUD এর জন্য ফর্ম তৈরি করতে হয় |
| 🔧 Validation                    | প্রতিটি ফিল্ড এর জন্য নিজে ম্যানুয়ালি validation দিতে হয়      | মডেল এর validation অটো ইমপ্লিমেন্ট হয়ে যায়                |
| 🛠 কাজের নিয়ন্ত্রণ                | সব কিছু নিজের মত করে কাস্টমাইজ করা যায়                        | অনেক কিছু অটো হয়ে যায়, তবে উইজেট ও লেবেল কাস্টম করা যায়   |
| 🧩 কোডের পরিমাণ                  | অনেক বেশি কোড লিখতে হয়                                        | অনেক কম কোডে ফর্ম তৈরি হয়ে যায়                            |
| 🧑‍💻 Performance & Maintainability | কোড বড় হয়, কিন্তু স্পেসিফিক নিয়ন্ত্রণ পাওয়া যায়               | কোড ছোট হয়, কিন্তু সব কিছু অটো ম্যানেজ করে                |

---

### 🎯 2. Custom Validation

### 🔹 Field level validation:

```python
# Tag name field এর validation
class MyForm(forms.Form):
    tag = forms.CharField()

#    def clean_fieldname()  syntex নির্দিষ্ট একটা ফিল্ড এর জন্য কাস্টম বালিটেশন
    def clean_tag(self):
        value = self.cleaned_data['tag']
        if 'badword' in value:
            raise forms.ValidationError("Don't use bad words")
        return value.stripe() # cleaned_data["field"] আপডেট করা হলো
"""
```

🔸clean_field মেথড ব্যানার উদ্দেশ কোন নির্দিষ্ট ফিল্ড ভ্যালিডেট করা `cleaned_data["field"]` আপডেট
করে সেই ভ্যালু রিটার্ন করা django এটাই ধরে নেয় এই ভাবেই কাজ করে আর return না দিলে
`dango ভাবে ডেভেলপার null রিটার্ন করছে` তাই তার সেই ফিল্ড এর ভ্যালু null করে রাখে তখন সেই ভ্যালু বা
ফিল্ড টেম্পলেট ভিউ কোথায় যাবে না। কারণ null ।

🔸 clean\_<fieldname>() Method

| বৈশিষ্ট্য               | ব্যাখ্যা                                                  |
| ----------------------- | --------------------------------------------------------- |
| কখন চলে?                | নির্দিষ্ট ফিল্ডের validation এর সময়                       |
| কিভাবে define করো?      | `def clean_email(self):` এর মতো করে                       |
| কোন ফিল্ডের জন্য চলে?   | শুধুমাত্র ওই নির্দিষ্ট ফিল্ডের জন্য                       |
| return দিতে হয়?        | ✔️ **হ্যাঁ, দিতে হবেই**                                   |
| return দিলে কী হয়?      | ওই ফিল্ডের `cleaned_data[field]` আপডেট হয়                |
| return না দিলে কী হয়?   | Django ধরে নেয় `None` বা ফিল্ড বাদ যায়                  |
| কিসের জন্য ব্যবহার করো? | format ঠিক করা, lowercase/uppercase, custom check ইত্যাদি |

### 🔹 Form level validation (clean method override):

```python
    def clean(self):
        data = super().clean()  # default validation কাজ করে
        if data.get('password') != data.get('confirm_password'):
          #def clean_add_error(fieldname,error_msg)  syntex নির্দিষ্ট ফিলস এর error dict এ error অ্যাড করার জন্য
            self.add_error('confirm_password', "Password doesn't match")
```

🔸 `super().clean()` না দিলে built-in validation (required, type check) execute হতো না।

🔸 `this.clean()` দিলে সে নিজের মানে যেটা চাইল্ড এ বানাইছি সেটা কল recersive behave করতো। করতো আসল
বিল্ড ইন ক্লিন কল করতো না যার ফলে clean_data নামে dict টাও পেতাম না যেটা বা ভ্যালিডেটে ডাটাগুলার
dict বানাইয়া store করে।আর কল না করলে `defauld validation` ও পাইতাম না clean_dict ও পাইতাম না।

🔸 custom clean method এ শুধু return করলে হবে না, আমাদের add_error বা raise ValidationError দিয়ে ভুল
নির্দেশ করতে হবে।

🔸 clean() মেথড ব্যানার উদ্দেশ ফর্ম এর একাধিক ফিল্ড ভ্যালিডেট করা বা ফুল ফর্ম ভ্যালিডেট করা এবং
self.cleaned_data মোডিফাই করা যখন আমরা cleaned_data=super().clean() দিলে django এর বিল্ড ইন
cleared_data মোডিফাই হয় কারণ super().clean() cleaned_data dict রিটার্ন করে। তখন django clean()
এরথেকে expectetion ফুলফিল হয়। আর এর পর আর ও যদি মোডিফাই করি যেমন cleaned_data["name"]=
cleaned_data["name"].upper() এটার পর চাইলে return cleaned_data দিলে দিতে পারি না হলে django নিজেই তা
করে কারণ এটা clean() মেথড এর behave। তাই return দেওয়া জুরুরি না optional

🔸 clean() Method

| বৈশিষ্ট্য                          | ব্যাখ্যা                                                              |
| ---------------------------------- | --------------------------------------------------------------------- |
| কখন চলে?                           | সব ফিল্ডের built-in ও field-level clean শেষ হওয়ার পর                 |
| সব ফিল্ডের cleaned_data available? | ✔️ হ্যাঁ                                                              |
| return বাধ্যতামূলক?                | ❌ না, return না করলেও Django আগের `self.cleaned_data` ইউজ করে        |
| return দিলে কী হয়?                 | পুরো `cleaned_data` override হয়                                       |
| কিসের জন্য ব্যবহার করো?            | multiple ফিল্ড একসাথে যাচাই, cross-validation, নতুন ফিল্ড যোগ ইত্যাদি |

🔸 Django এর ভিতরের আচরণ (Internals): | Method | cleaned*data আগে থেকে থাকে? | কোন ফিল্ডের জন্য
available? | return না দিলে কি হয়? | | ----------------- | ---------------------------- |
--------------------------- | ---------------------- | | `__init__()` | ❌ না | কিছুই থাকে না |
error হতে পারে | |
`clean*<field>()`| ✔️ শুধু ওই ফিল্ড | অন্য ফিল্ড নাও থাকতে পারে | ফিল্ড বাদ যেতে পারে | |`clean()` |
✔️ সব ফিল্ড | সব ফিল্ড | আগের cleaned_data ধরে |

🔸 উদাহরণ Diagram (Flow Summary):

```pgsql

⬇️ User Input Form
        ⬇️
is_valid() ➡️ Form._clean_fields()
        ⬇️
১. Field built-in validation
২. clean_<field>() ➡️ return cleaned value
        ⬇️
৩. Form.clean() ➡️ full cleaned_data modify/check
        ⬇️
✔️ form.cleaned_data ➡️ Final cleaned values

```

---

### 🎯 3. Form Submission Handling (POST)

```python
if request.method == 'POST':
    form = MyForm(request.POST)
    if form.is_valid():
        # data = form.cleaned_data
        ... # process data
else:
    form = MyForm()

return render(request, 'form.html', {'form': form})
```

🔸 `form.is_valid()` false হলে cleaned_data পাওয়া যায় না। তাই form.errors দেখতে হয়।

---

### 🎯 4. `cleaned_data` vs `clean` method

| বিষয়                | `cleaned_data`                               | `clean()` method (form-level validation)                     |
| ------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| 📌 কী               | valid field গুলোর ডিকশনারি                   | form এর সব ফিল্ড একসাথে যাচাই করার জন্য method               |
| 🔍 পাওয়া যায় কখন    | `form.is_valid()` সফল হলে                    | `form.is_valid()` এর সময়ই call হয়                            |
| 📥 কী রিটার্ন করে   | dictionary → `{field_name: value}`           | সাধারণত `super().clean()` এর result return করা উচিত          |
| 📄 Validation Scope | শুধু field level validation এর পরে পাওয়া যায় | একাধিক ফিল্ডের মধ্যে সম্পর্ক যাচাই করার জন্য use হয়          |
| 💥 Error Handling   | এখানে error থাকে না (form.errors এ থাকে)     | এখানে error raise করতে হয় বা `self.add_error()` দিয়ে দিতে হয় |
| ✅ ব্যবহার উদাহরণ   | `form.cleaned_data['email']`                 | password এবং confirm_password মিল আছে কিনা চেক করা           |

---

### 🎯 5. `self.add_error()` vs `raise ValidationError`

| বিষয়                     | `self.add_error()`                                                                                                    | `raise ValidationError()`                                                      |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **প্রকৃতি**              | Form বা ModelForm এর method, validation error যুক্ত করার জন্য ব্যবহার হয়                                              | Exception যা validation error হিসেবে উঠানো হয়                                  |
| **ব্যবহার ক্ষেত্র**      | সাধারণত `clean()` method বা `clean_<fieldname>()` method এর মধ্যে নির্দিষ্ট ফিল্ড বা পুরো ফর্মে error যুক্ত করার জন্য | field-level বা form-level validation এ error ঘটলে exception হিসেবে উঠাতে হয়    |
| **প্যারামিটার**          | ২টি প্যারামিটার নেয়: (field_name (string বা None), error_message)                                                     | সাধারণত error message বা error list নেয়                                        |
| **Error target**         | নির্দিষ্ট field এর error হিসেবে অথবা পুরো ফর্মের error হিসেবে যুক্ত করতে পারে (`field_name=None` দিলে ফর্ম error)     | সাধারণত পুরো form এর validation error হিসাবে বিবেচিত হয়                        |
| **Form validation flow** | error যোগ করলেও form এর validation process চলতে থাকে, আপনি একাধিক error add করতে পারেন                                | ValidationError উঠানো হলে validation তৎক্ষণাৎ থেমে যায়, পরের কোড execute হয় না |
| **Template এ access**    | form.errors এ যুক্ত হয়, নির্দিষ্ট ফিল্ডের errors হিসেবে দেখা যায়                                                      | form.errors এ আসে, সাধারণত form-level error হিসেবে দেখা যায়                    |
| **কখন ব্যবহার করবেন?**   | একাধিক field এর জন্য error যোগ করতে চান, validation চলাকালীন একাধিক error দেখতে চান                                   | একক critical error পেলে validation থামিয়ে দিতে চান                             |

---

### 🎯 6. `self.method()` vs `super().method()`

- `self.method()` → নিজের method আগে খুঁজবে, না পেলে parent-এ যাবে।
- `super().method()` → সরাসরি parent-এর method কল করে।

**Form এর ক্ষেত্রে:**

```python
def clean(self):
    data = super().clean()  # super দিয়ে parent clean() call
```

---

### 🎯 7. Form Widget Customize

👉🏿Modelform

```python
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Product Name',
        }

```

👉 customform

```pthon
class MyForm(forms.Form):
    name = forms.CharField(labels='Product Name',widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Name'
    }))
```

### 🎯 8. BoundField এবং `form['field']`

🔸 `form['field']` → BoundField object return করে।

🔸 BoundField object এর `__str__` method আছে যা template এ `<input ...>` element render করে।

🔸 তাই template এ `{{ form.field }}` বা `{{ form.field.errors }}` লিখলেই কাজ হয়।

🔸 যখন টেম্পলেট এ অবজেক্ট বা dict কল করা হয় তখন পাইথন অটোমেটিক তার str মেথড কল করে ফর্ম এর ক্ষেত্রে
এর **str** মেথড as_table method call করে তাই আমরা {{form}} লিখলে এটা তার str কল হয়ে as_table আকারে
রেন্ডার হয়।বাস্তবে form বা form.field হলো boundre_field object যেখানে অনেক প্রপার্টি ও মেথড থাকে
যেমন form.field.error একটা প্রপার্টি form.field.label_tag একটা property .

---

### 🎯 9. `form.fields`

🔸 এটা একটা Dictionary যা `{ field_name: Field object }` আকারে থাকে। 🔸 শুধুমাত্র raw Field Object
(CharField, IntegerField etc) access এর জন্য। 🔸 এটা Template এ ইউজ হয় না; template এ আমরা
`form[field_name]` ইউজ করি।

---

### 🎯 10. Form Internal Structure Summary:

```python
form = MyForm()
form.fields         # dict of {name: Field instance}
form['name']        # BoundField object (renderable)
form.cleaned_data   # validated data dict (after is_valid())
form.errors         # dict of errors (after is_valid())
```

```python
# BoundField এর মূলত এটা
class BoundField:
    def __str__(self):
        return self.as_widget()
```

---

### 🎯 11. Dunder Method `__getitem__`

```python
class Form:
    def __getitem__(self, name):
        return BoundField(self, self.fields[name], name)
```

🔸 এজন্য আমরা form\['field_name'] লিখলে সে BoundField return করে।

---

### 🎯 12. Template rendering & Styling

🔸 Custom HTML form এ Bootstrap সহ styling করতে চাইলে:

```html
<form method="POST">
  {% csrf_token %}
  <div class="mb-3">{{ form.name.label_tag }} {{ form.name }} {{ form.name.errors }}</div>
</form>
```

---

### 🎯 13. Form Rendering Process:

| Step | Action                                                                                             |
| ---- | -------------------------------------------------------------------------------------------------- |
| 1    | Request আসে form page এ                                                                            |
| 2    | GET হলে blank form render করে                                                                      |
| 3    | POST হলে `MyForm(request.POST)` instantiate করে                                                    |
| 4    | `is_valid()` call হয়                                                                               |
| 5    | Valid হলে `cleaned_data` dict আসে এরপর সেভ দিলে তা model.object.create() চালিয়ে অবজেক্ট ক্রিটে করে |
| 6    | Template এ BoundField এর মাধ্যমে render হয়                                                         |
| 7    | Error হলে error dict `form.errors` render হয়                                                       |

---

## 🔚 Conclusion:

এই handnote টিতে Django Form Handling এর almost সব গুরুত্বপূর্ণ বিষয় আলোচনার ভিত্তিতে লিপিবদ্ধ করা
হয়েছে। Future এ একবার পড়লেই সব clear হবে, এবং এটা রিভিশনের জন্য পারফেক্ট।

## 🍪 ✅ Day 7: Authentication System

- Session authentication
- Django built-in auth
- Register, Login, Logout view
- login_required, messages

### 🧠 ১. Cookie কীভাবে কাজ করে?

### ✅ Server থেকে Cookie set:

```http
HTTP/1.1 200 OK
Set-Cookie: sessionid=abc123xyz; Path=/; HttpOnly
```

➡️ ব্রাউজার বুঝে যায় এটি একটি কুকি এবং সেটি তার internal cookie store-এ সেভ করে।

### ✅ পরবর্তী Request এ:

```http
GET /dashboard HTTP/1.1
Host: example.com
Cookie: sessionid=abc123xyz
```

➡️ ব্রাউজার সেই কুকি সার্ভারে পাঠিয়ে দেয়।

### ✅ Cookie পাঠানোর শর্ত:

| শর্ত         | ব্যাখ্যা                                       |
| ------------ | ---------------------------------------------- |
| Domain match | কুকি যেই ডোমেইন থেকে এসেছে, সেই ডোমেইনে পাঠাবে |
| Path match   | কুকি যেই path এর জন্য সেট, সেই path-এ পাঠাবে   |
| Secure       | শুধুমাত্র HTTPS এর জন্য পাঠাবে                 |
| HttpOnly     | JavaScript access করতে পারবে না                |

### 🔐 ২. Cookie দিয়ে Session কীভাবে কাজ করে?

1. **User Login করলে**, Django একটা `sessionid` কুকি সেট করে।
2. এই কুকি ব্রাউজার সেভ করে এবং পরবর্তী রিকোয়েস্টে পাঠায়।
3. Django এই কুকি দেখে বুঝে ফেলে user কে।
4. Django backend-এ `/sessions/` table বা Redis-এ session data রাখে।

---

### 🔐 Django Authentication System

### 🧾 ৩. Built-in Auth Views

### ✅ Registration View:

```python
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')
```

### ✅ Login View:

```python
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Session শুরু হয় এখানে
            return redirect('dashboard')
    return render(request, 'login.html')
```

### ✅ Logout View:

```python
from django.contrib.auth import logout

def user_logout(request):
    logout(request)  # reuest এর জন্য sessionid নিয়ে ওই ইউসার এর  Session Destroy করে django এর সেশন ডিবি থেকে এন্ড ব্রমের এর sessionid cookey null/remove  করে দেয়
    return redirect('login')
```

---

### 🗂️ ৪. Session Authentication

✅ Django session-based authentication ব্যবহার করে।

| ধাপ | ব্যাখ্যা                                  |
| --- | ----------------------------------------- |
| 1   | Login করলে session তৈরি হয়                |
| 2   | Django কুকিতে `sessionid` পাঠায়           |
| 3   | ব্রাউজার সেই কুকি পাঠায় প্রতি request এ   |
| 4   | Django সেই sessionid দেখে user সনাক্ত করে |

---

🔄 Diagram (সংক্ষিপ্ত)

```text
User Login → login(request, user)
              ↓
           session.save() → DB/session backend as {sessionid:xyz,user_id,abc, authentication_backend:"your auth backend setup"}
              ↓
           Set-Cookie: sessionid=xyz ← to browser

→ User sends next request
     ↓
   Cookie: sessionid=xyz ← comes with request
     ↓
  SessionMiddleware gets session object from sesson DB by this sessionid cookey
     ↓
  AuthenticationMiddleware →
 get user object by sesson object user_id property and set
request.user = User instance

```

## 🛑 ৫. @login_required,@user_passes_test Decorator and lamda

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

➡️ এই ডেকোরেটর check করে user logged in কিনা। না থাকলে login page এ রিডাইরেক্ট করে।

## 🧠 `lambda` & `@user_passes_test` in Django (Handnote)

---

### ✅ `lambda` in Python

#### 🔹 কী?

`lambda` হলো Python-এর anonymous (নামহীন) এক লাইনের ফাংশন।

#### 🔹 Syntax:

```python
lambda arguments: expression
```

#### 🔹 উদাহরণ:

```python
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8
```

#### 🔹 ব্যবহার:

- ছোট ফাংশন বা expression
- `map()`, `filter()`, `sorted()`, `decorator`, ইত্যাদির মধ্যে
- কোথায় একবারের জন্যো ফাংশন লাগলে

#### 🔹 Practical Example:

```python
squared = list(map(lambda x: x * x, [1, 2, 3]))
# Output: [1, 4, 9]
```

---

### ✅ `@user_passes_test` in Django

#### 🔹 কী?

`@user_passes_test` হচ্ছে Django এর একটা **decorator** যার মাধ্যমে আপনি নির্দিষ্ট test দিয়ে **view
access control** করতে পারেন।

#### 🔹 Syntax:

```python
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def my_view(request):
    ...
```

#### 🔹 lambda u: u.is_superuser

এখানে:

- `u` হলো `request.user`
- এটি check করে user superuser কি না

#### 🔹 বিকল্পভাবে (function দিয়ে):

```python
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def dashboard(request):
    ...
```

---

### 📌 কোথায় ব্যবহার করব?

- যেসব view-তে আপনি চান **শুধু logged in user বা specific user type (admin/staff)** access করুক
- Example:

  - `@user_passes_test(lambda u: u.is_authenticated)`
  - `@user_passes_test(lambda u: u.is_staff)`
  - `@user_passes_test(lambda u: u.is_superuser)`
  - `@user_passes_test(lambda u: u.is_active)`

---

### 🚫 Access না পেলে কী হয়?

Default-ভাবে user শর্ত না মানলে তাকে **login page এ redirect** করা হয়। তুমি চাইলে custom redirect
URL ও দিতে পারো:

```python
@user_passes_test(lambda u: u.is_superuser, login_url='/no-access/')
```

---

### 🦾 সংক্ষিপ্ত মনে রাখার নিয়ম:

| বিষয়               | কাজ              | ব্যবহার             |
| ------------------- | ---------------- | ------------------- |
| `lambda`            | এক লাইনের ফাংশন  | Python & callback   |
| `@user_passes_test` | User কে test করে | Django view control |

---

### ✅ Common Example:

```python
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_authenticated)
def profile_view(request):
    ...
```

---

## 🖚 শেষ কথা:

- **`lambda`** → ছোট ফাংশনের শর্টকার্ট
- **`@user_passes_test`** → view কে protect করার tool
- দুটোই powerful & Pythonic 🐍

---

## 💬 ৬. Django Messages Framework

### ✅ উদাহরণ:

```python
from django.contrib import messages
from django.shortcut import redirect

def login_view(request):
    if request.method == 'POST':
        # ...
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect("messages")

        else:
            messages.error(request, 'Invalid credentials')
            return redirect("messages")
```

### ✅ template এ দেখাতে:

```html
{% for message in messages %}
<div class="alert">{{ message }}</div>
{% endfor %}
```

---

### `✅ সব মেথড + কমান্ড এবং এগুলার কাজ`

| বিষয়                                                            | কাজ                                                                                                                                                                                                                                                                                                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cookie                                                          | ব্রাউজার এবং সার্ভারের মধ্যে ডেটা সংরক্ষণের মাধ্যম                                                                                                                                                                                                                                                                 |
| Set-Cookie                                                      | Server -> Browser: কুকি সেট করার কমান্ড                                                                                                                                                                                                                                                                            |
| Cookie header                                                   | Browser -> Server: কুকি পাঠানোর জন্য                                                                                                                                                                                                                                                                               |
| Session                                                         | Server-side storage, user কে track করতে সাহায্য করে                                                                                                                                                                                                                                                                |
| login()                                                         | Django session শুরু/make করে, কুকি সেট করে set_cookey দিয়া এবং sesssion middleware প্রতি রিকোয়েস্ট অনুযায়ী তার মধ্যে ব্রাউসার থেকে পাঠানো sessionid কুকি অনুযায়ী django sesson ডিবি হতে ইউসার fetch করে request.user এ সেই user অবজেক্ট পাঠায় তাই আমরা template এ request.user.username দিলে লগইন ইউসার এর নাম পাই |
| logout(request)                                                 | request অবজেক্ট এ থাকা sessionid এর জন্য যেই ইনস্ট্যান্স সেশন এ আচে সেই Session অবজেক্ট destroy করে। করে                                                                                                                                                                                                           |
| authenticate(request,username="something",password="something") | authenticate করে যদি এই ইনফরমেশন এ কোন ইউসার পায় তাহলে User object return করে না হলে none return করে                                                                                                                                                                                                               |
| @login_required(login_url="loginpage")                          | Authenticated user না হলে redirect করে login_url এ যেই ইউআরএল thake সেখানে রিডাইরেক্ট করে।                                                                                                                                                                                                                         |
| messages                                                        | User feedback display করতে flash মেসেজ পাঠায় রিটার্ন পেজ এ যা একবার এর জন্য দেখায় এন্ড এটা সেশন বেসড তাই রিকোয়েস্ট অবজেক্ট পাঠাতে হয় একবার শো করলে সেশন থেকে ডেস্ট্রয় হয় আর সীন না করা পর্যন্ত রিফ্রেশ করলেও মেসেজ থেকেই যায়।                                                                                      |

---

# ✅ Django Custom User Model Handnote (Day 08)

## 🔰 Custom User Model কেন ব্যবহার করব?

Django-এর default user model অনেক সময় আমাদের প্রয়োজন অনুযায়ী field (যেমন: phone_number,
profile_image ইত্যাদি) রাখার সুযোগ দেয় না। তাই আমরা custom user model ব্যবহার করি যাতে user model
নিজের মতো modify করা যায়।

---

## 🔹 AbstractUser vs AbstractBaseUser

| Topic           | AbstractUser                           | AbstractBaseUser                   |
| --------------- | -------------------------------------- | ---------------------------------- |
| Inherits        | Django's built-in User model           | Only Base user class               |
| Fields          | Default fields (username, email, etc.) | Must define all fields manually    |
| Easier to use?  | ✅ হ্যাঁ (prebuilt features পেয়ে যাব)  | ❌ না (সব manually define করতে হয়) |
| Password System | Built-in আছে                           | নিজে implement করতে হয়             |

---

## 🔹 Custom User Model এ কী কী থাকতে হবে?

1. AbstractUser থেকে extend করা Model:

```python
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
```

2. Custom Manager তৈরি করতে হবে:

```python
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, email, password, **extra_fields)
```

3. Custom User Model এ Manager যুক্ত করতে হবে:

```python
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    objects = CustomUserManager()  # Custom Manager যুক্ত করা হলো
```

4. settings.py এ জানাতে হবে:

```python
AUTH_USER_MODEL = 'yourapp.CustomUser'
```

---

## Django Profile Page

````markdown
# Django Profile Page তৈরির গাইড (request.user ব্যবহার করে)

## ভূমিকা

এই গাইডে শেখানো হবে কিভাবে Django এর built-in `request.user` অবজেক্ট ব্যবহার করে একজন লগইনকৃত
ইউজারের প্রোফাইল পেজ তৈরি করা যায়।

---

## ১. URL Configuration

প্রথমে তোমার `urls.py` ফাইলে প্রোফাইল পেজের URL এন্ট্রি দিতে হবে:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
]
```
````

---

## ২. View Function

`views.py` ফাইলে `profile_view` ফাংশন তৈরি করো:

```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # নিশ্চিত করবে ইউজার লগইন আছে
def profile_view(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)
```

---

## ৩. Template ফাইল (profile.html)

`templates` ফোল্ডারে `profile.html` তৈরি করো:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>{{ user.username }} এর প্রোফাইল</title>
  </head>
  <body>
    <h1>প্রোফাইল পেজ</h1>
    <p><strong>নাম:</strong> {{ user.get_full_name }}</p>
    <p><strong>ইমেইল:</strong> {{ user.email }}</p>
    <p><strong>ইউজারনেম:</strong> {{ user.username }}</p>
    <!-- প্রয়োজনমতো আরও ফিল্ড যোগ করতে পারো -->
  </body>
</html>
```

---

## ৪. Authentication Setup

- নিশ্চিত করো তোমার settings.py-তে `LOGIN_URL` সঠিক আছে (যেমন: `/accounts/login/`)
- লগইন ছাড়া কেউ প্রোফাইল পেজে যেতে না পারে এজন্য `@login_required` ডেকোরেটর ব্যবহার করা হয়েছে।

---

### হ্যান্ডনোট (Handnote)

```html
<div style="border:1px solid #ccc; padding:10px; background:#f9f9f9; position: relative;">
  <h3>Quick Tips</h3>
  <pre id="handnote-text" style="white-space: pre-wrap; word-wrap: break-word;">
1. প্রোফাইল পেজ শুধুমাত্র লগইন করা ইউজারের জন্য।
2. request.user দিয়ে সহজেই ইউজারের ডাটা পাওয়া যায়।
3. @login_required ডেকোরেটর ইউজারকে লগইন করাতে বাধ্য করে।
4. user.get_full_name() নাম দেখানোর জন্য ব্যবহৃত হয়।
5. ইমেইল, ইউজারনেম সব প্রপার্টি পাওয়া যায় request.user থেকে।
</pre
  >
  <button
    id="copy-btn"
    style="position: absolute; top: 10px; right: 10px; padding: 4px 10px; cursor: pointer;"
  >
    Copy
  </button>
</div>

<script>
  document.getElementById('copy-btn').addEventListener('click', function () {
    const text = document.getElementById('handnote-text').innerText
    navigator.clipboard
      .writeText(text)
      .then(() => {
        alert('Handnote copied!')
      })
      .catch(() => {
        alert('Copy failed, please copy manually.')
      })
  })
</script>
```

---

## 🔹 Model.objects.create vs Model()

| Model.objects.create                   | Model() + save()                     |
| -------------------------------------- | ------------------------------------ |
| Object তৈরি ও সাথে সাথে DB-তে save করে | Object তৈরি হয়, পরে `save()` দিতে হয় |
| Internal call করে `.save()`            | Manually `obj.save()` দিতে হয়        |

---

## 🔹 set_password() কোথা থেকে আসে?

- এটি `AbstractBaseUser` এর instance method।
- এর মাধ্যমে password hashed করে save করা হয়।

---

## 🔹 extra_fields কাজ কী করে?

```python
extra_fields = {"is_superuser": True, "is_staff": True}
```

- `user = self.model(username, email, **extra_fields)` → এর মানে:

  ```python
  user = self.model(username=username, email=email, is_superuser=True, is_staff=True)
  ```

- এটি dictionary spread করে additional fields assign করে।
- Python এ `**kwargs` → keyword arguments dict আকারে নেয়।

---

## 🔹 extra_fields.setdefault()

- Python dictionary এর built-in method

```python
extra_fields.setdefault('is_superuser', True)
```

- যদি key `is_superuser` না থাকে তবে `True` set করবে।

---

## 🔹 ValueError কোথা থেকে আসে?

- Python built-in exception। Import করার দরকার নাই।

```python
raise ValueError("Users must have an email address")
```

---

## 🔹 model manager / object manager কি?

- প্রতিটি Model এর সাথে `objects` নামে default manager থাকে:

```python
User.objects.all()
User.objects.filter()
```

- আমরা চাইলে Custom Manager তৈরি করে `.objects` override করতে পারি।
- Custom Query behaviors define করতে পারি।
- Manager override করার উদাহরণ:

```python
class ActiveUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
```

---

## 🔹 UserCreationForm extend করার কারণ?

- `UserCreationForm` Django এর built-in form যেটা automatic কিছু validation (`clean_username`,
  `clean_password2`, etc) provide করে।
- Custom User Form তৈরি করার সময় এটি inherit করলে default validation system active থাকে।

---

## 🔹 USERNAME_FIELD vs REQUIRED_FIELDS

| Field           | কাজ                                                      |
| --------------- | -------------------------------------------------------- |
| USERNAME_FIELD  | কোন field দিয়ে user authenticate হবে (default: username) |
| REQUIRED_FIELDS | createsuperuser চলাকালে যে fields চাই তা define করা      |

```python
USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username']
```

---

## 🔹 Authentication Backend সেট করা:

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
```

---

### ✅ আপনি কি বুঝেছেন?

- CustomUser কেন দরকার
- Manager কি ও কেন override করতে হয়
- Model vs Model.objects.create পার্থক্য
- set_password এর পেছনের কাহিনী
- extra_fields কীভাবে কাজ করে
- CustomUserManager কি ও কেন দরকার
- AUTH_USER_MODEL কোথায় সেট করতে হয়

---

---

## ✅ Day 9: Middleware & Decorator

- Custom middleware কী এবং কিভাবে বানানো যায়
- Custom Decorator কী এবং কিভাবে বানানো যায়
- Decorator ও Permission based view

### ✅ Part 1: Middleware

#### 🧠 Middleware কী?

Middleware হলো Django-এর এমন এক সিস্টেম যেখানে তুমি HTTP request এবং response এর মাঝখানে **extra কাজ
(logic)** করতে পারো।

> 🎯 মনে রাখো: Middleware = Request & Response এর মাঝখানে দাঁড়িয়ে নিয়ন্ত্রণ করা।

---

#### 🧩 Django Middleware কখন চলে?

1. **Request আসলে** → Middleware আগে চলে → তারপর View ফাংশনে যায়
2. **Response রিটার্ন হলে** → Middleware আবার কাজ করে → তারপর Client এ পাঠায়

---

#### 🔧 কেন Middleware দরকার?

তুমি View-এ অনেক কাজ করতে পারো ঠিক, কিন্তু Middleware এর কিছু Extra সুবিধা:

| সুবিধা                              | কারণ                                  |
| ----------------------------------- | ------------------------------------- |
| Request আসার আগেই check করা যায়     | যেমন user authenticated কিনা          |
| View execute হওয়ার আগেই কাজ করা যায় | IP blacklist করা, custom logging      |
| Response modify করা যায়             | HTML footer যোগ করা, CORS header দেয়া |
| সব View-র আগেই বা পরে কাজ করে       | common কাজ বারবার না লিখতে            |

---

### 🏗️ Custom Middleware বানানো (Function-Based)

### ✅ Step-by-step:

```python
# myapp/middleware.py

def my_middleware(get_response):
    print("👉 Middleware Initialized")

    def middleware(request):
        print("🔹 Request Middleware: view-এর আগে")
        response = get_response(request)
        print("🔸 Response Middleware: view-এর পরে")
        return response

    return middleware
```

#### 🔍 কী কী ব্যবহার হলো?

| জিনিস                              | কাজ                                                     |
| ---------------------------------- | ------------------------------------------------------- |
| `get_response`                     | এটা হলো সেই function যেটা request নিয়ে View-কে call করে |
| `request`                          | HTTP request object                                     |
| `response = get_response(request)` | View function কে call করে, তার result ধরে               |
| return response                    | Client কে response পাঠায়                                |

---

#### ⚠️ যদি `get_response(request)` না দিতাম?

View কখনোই execute হতো না। তোমার middleware শুধু request পেত, কিন্তু response রিটার্ন করতো না —
Server হ্যাং হয়ে যেত।

---

#### 🔗 settings.py-তে যুক্ত করো:

```python
MIDDLEWARE = [
    ...
    'myapp.middleware.my_middleware',
]
```

---

### 🏗️ Custom Middleware (Class-Based)

#### ✅ Syntax:

```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("👉 Middleware Initialized")

    def __call__(self, request):
        print("🔹 Request Middleware: view-এর আগে")
        response = self.get_response(request)
        print("🔸 Response Middleware: view-এর পরে")
        return response
```

#### 🧠 ব্যাখ্যা:

| Method         | কাজ                                     |
| -------------- | --------------------------------------- |
| `__init__`     | middleware setup হয় যখন Django start হয় |
| `get_response` | View কে call করার function              |
| `__call__`     | প্রতিবার request এ middleware চালায়     |
| `request`      | HTTPRequest object                      |
| `response`     | View এর return                          |

---

#### ❓ কেন `__call__()` লাগে?

Django middleware instance কে function-এর মতো call করে: `middleware_instance(request)` `__call__` না
দিলে, middleware request handle করতে পারতো না।👉 Middleware class এর **call** হল python এর বিল্ড ইন
একটি special dunder method যেটা class এর instance কে function-এর মতো call করার ক্ষমতা দেয়।instance
কে ফাংশনের মতো call করলে **call**() method execute হয়। যা একটা ভিউ function রিটার্ন করে ডেকোরেটর
যেমন করে কারণ আমরা জানি যে middleware এক ধরণের বিশেষ ডেকোরেটর যার স্পেশাল কিছু behave/power আছে।

---

#### 📌 কোথায় কোন কোড চলে?

| জায়গা                   | কাজ                                                |
| ----------------------- | -------------------------------------------------- |
| `__init__()`            | Django server start করার সময় চলে (একবার)           |
| `__call__()`            | প্রতিবার request আসলে চলে                          |
| `get_response(request)` | View কে call করে, তারপর view শেষ হলে বাকি code চলে |

---

#### 🎁 Bonus: Middleware Hook গুলো

Class-based middleware-এ আরও কিছু hook থাকে:

| Method                        | কখন চলে                          | কাজ                          |
| ----------------------------- | -------------------------------- | ---------------------------- |
| `process_view()`              | view function execute হওয়ার আগে | view check, arguments change |
| `process_exception()`         | যদি exception হয়                 | error handle                 |
| `process_template_response()` | template response modify         |                              |

> ⚠️ এগুলো শুধু old style middleware-এ use হয়, Django 1.10+ এ নতুন style হচ্ছে `__init__`,
> `__call__`

---

---

### ✅ Part 2: Decorator

## 🧠 Decorator কী?

Decorator হচ্ছে Python-এর একটা ফিচার, যা **function-এর উপরে আরেকটা function "লেপে" দেয়**, যেন কিছু
অতিরিক্ত কাজ হয়।

---

## 🎯 Django-তে কেন Decorator দরকার?

- একটা view-র আগে/পরে কাজ করতে
- User login check করতে
- Permission check করতে
- Custom logic add করতে

---

## 🧩 Custom Decorator বানানো (Step by Step)

### ✅ Basic Structure:

```python
from functools import wraps

def my_decorator(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print("🔹 View এর আগে কিছু করলাম")
        response = view_func(request, *args, **kwargs)
        print("🔸 View এর পরে কিছু করলাম")
        return response
    return wrapper
```

### 🔍 ব্যাখ্যা:

| জিনিস                      | কাজ                                          |
| -------------------------- | -------------------------------------------- |
| `@wraps(view_func)`        | মূল function-এর নাম ও docstring বজায় রাখে    |
| `request, *args, **kwargs` | Django view function-এ সব argument ধরার জন্য |
| `view_func(request)`       | মূল view কে call করে                         |
| return response            | response ক্লায়েন্টে পাঠায়                    |

---

### ✅ Custom Decorator Use করার নিয়ম:

```python
@my_decorator
def my_view(request):
    return HttpResponse("Hello from view")
```

---

#### ❓Decorator ছাড়া কি সম্ভব?

হ্যাঁ, কিন্তু প্রতিটা view-তে একই code বারবার লিখতে হতো। DRY (Don't Repeat Yourself) ভাঙত।

✅ কখন my_decorator() চলে, কখন wrapper() চলে?

| ফাংশন            | কখন চলে                                                           |
| ---------------- | ----------------------------------------------------------------- |
| `my_decorator()` | যখন Python তোমার view কে decorate করে (server start-এর সময় একবার) |
| `wrapper()`      | যখন user request করে এবং decorated view call হয়                   |

#### Server start হলে

- তোমার view কে decorate করে (server start-এর সময় একবার)
- Django তোমার সব middleware read করে (settings.py → MIDDLEWARE list থেকে)

- প্রতিটি middleware কে call করে একবার → middleware_instance = middleware(get_response)

- এর মানে প্রতিটি middleware get_response কে wrap করে নতুন একটা callable return করে।

➡️ সব middleware একটার ভেতরে আরেকটা nested হয়।

### 🌀 Middleware vs Decorator: পার্থক্য

| দিক                         | Middleware                           | Decorator                              |
| --------------------------- | ------------------------------------ | -------------------------------------- |
| ব্যবহৃত হয়                  | Django core request/response cycle-এ | শুধুমাত্র view ফাংশনের উপর             |
| কে apply করে                | Django নিজেই (server start-এ)        | তুমি নিজে কোডে `@decorator` দিয়ে       |
| Scope                       | global (সব view-তে)                  | local (নির্দিষ্ট view-এ)               |
| Request/Response handle করে | হ্যাঁ                                | না, শুধুমাত্র view-এর আগে/পরে          |
| Initialization সময়          | Django চলার সময়                      | Python runtime-এ (function define সময়) |

### Middleware chaining (View wrapping)

Middleware গুলো এরকম কাজ করে:

```python
# middlewares = ["middleware1", "middleware2", "middleware3"]
final_view = middleware1(
                  middleware2(
                      middleware3(
                          original_view
                      )
                  )
              )
```

এখানে “server run হলে view = middleware(view)”

### Decorator ব্যবহার করলে কী হয়?

```python
@my_decorator
def my_view(request):
    ...

```

➡️ Python internally করে:

```python
my_view = my_decorator(my_view)
```

### দুইটায় একসাথে use করলে (middleware,decoretor)

```python
# middlewares = ["middleware1", "middleware2", "middleware3"]
# @mydecorator
# def original_view;

final_view = middleware1(
                  middleware2(
                      middleware3(
                          my_decorator(original_view)
                      )
                  )
              )
```

#### 🔄 Execution Order (console output):

```pgsql

middleware1 before view
decorator before view
Inside view
decorator after view
middleware1 after view


```

| বিষয়                          | Summary                                                   |
| ----------------------------- | --------------------------------------------------------- |
| **Middleware**                | Request/Response এর মাঝখানে বসে কাজ করে; সব view-তে চালায় |
| **Decorator**                 | View-এর আগে/পরে আলাদা কাজ করে; শুধু ওই view-তেই           |
| **Function-based Middleware** | Simple function যা request নিয়ে response ফেরত দেয়         |
| **Class-based Middleware**    | Full control দেয়, Django এর নতুন স্ট্যান্ডার্ড            |
| **Custom Decorator**          | View এর আগে/পরে নিজস্ব logic চালায়                        |

---

## `Middleware is actually a special kind of decorator.`

### ✅ Part 3 : Decorator ও Permission based view

#### 🔹 ১. Decorator কী?

`Decorator` হলো Python-এর এক ধরনের ফাংশন যা অন্য একটি ফাংশন বা ভিউ-কে modify বা enhance করতে ব্যবহৃত
হয়।

Django-তে ব্যবহৃত common decorators:

- `@login_required`
- `@permission_required`
- `@user_passes_test`

---

#### 🔹 ২. কেন Decorator ব্যবহার করি?

✅ View কে protected করতে ✅ কোন ভিউতে শুধু logged-in user access করতে পারবে তা নির্ধারণ করতে ✅
Custom condition apply করতে (যেমন: শুধু staff user, শুধু superuser)

---

## 🔹 ৩. `@login_required` ব্যবহার

#### ✅ উদ্দেশ্য:

যদি user লগ ইন না করে থাকে, তাহলে তাকে login পেজে redirect করবে।

#### ✅ ব্যবহার:

```python
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login/')
def dashboard(request):
    return render(request, 'dashboard.html')
```

#### 🔹 ৪. @permission_required ব্যবহার

#### ✅ উদ্দেশ্য:

User-এর নির্দিষ্ট permission আছে কিনা তা যাচাই করে। না থাকলে 403 Forbidden দিবে।

#### ✅ ব্যবহার:

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app_label.permission_codename', raise_exception=True)
def my_view(request):
    return render(request, 'secure_page.html')

```

🔍 বুঝে নেন:

- 'app_label.permission_codename' = eg: 'products.add_product'

- raise_exception=True দিলে login না থাকা বা permission না থাকলে 403 দিবে।

#### 🔹 ৫. @user_passes_test দিয়ে Custom Check

#### ✅ Example:

```python
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin.html')
```

#### 🔹 ৬. Model Permission নাম গুলো কীভাবে তৈরি হয়?

- Model: Product

| কাজ            | Permission Codename |
| -------------- | ------------------- |
| Add product    | `add_product`       |
| Change product | `change_product`    |
| Delete product | `delete_product`    |
| View product   | `view_product`      |

Format: 'app_label.codename'

#### 🔹 ৭. Permission Add করার নিয়ম (admin panel থেকে)

Admin panel → User → Permissions → ✅ Select required permissions → Save

🧠 Bonus: Custom Permission তৈরি (Model Meta ক্লাসে)

```
class Product(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_publish", "Can Publish Product"),
        ]

```

#### 🔹 ৮. Function-based View (FBV) vs Class-based View (CBV) এ Decorator

##### ✅ CBV এ login_required ব্যবহার:

```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')
```

| Decorator              | কাজ                                           |
| ---------------------- | --------------------------------------------- |
| `@login_required`      | Login ছাড়া ভিউ access করতে দিবে না            |
| `@permission_required` | নির্দিষ্ট permission ছাড়া view access দিবে না |
| `@user_passes_test`    | Custom logic check                            |
| Custom Decorator       | নিজের মতো করে কোন logic enforce করা           |

---

## ✅ Day 10: blog backend based website by django done

---

- DRF install & config

- APIView দিয়ে JSON Response

- API vs Web Page

## ✅ Day 11: DRF Setup & First API

### 🧱 Part 1: DRF Install & Configuration

#### 🔹 Step 1: DRF Install

```bash
pip install djangorestframework
```

🔸 কেন করলাম?

> DRF (Django REST Framework) ইনস্টল না করলে আমরা Django দিয়ে API বানাতে পারতাম না। এটা Django এর
> ওপর বসানো একটা শক্তিশালী extension।

---

#### 🔹 Step 2: settings.py তে যোগ করো

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

🔸 কেন করলাম?

> Django-কে জানাতে হবে যে আমরা DRF ব্যবহার করব। না করলে Django এটা চিনতে পারবে না।by-deafalut drf
> একটা app এর মতো কাজ করে আমরা জানি একটা apps বানালে তা আমাদের settings.py তে অ্যাড করতে হয় না হলে
> সেই app কে django চিনতে পারে না তাই আমাদের add করতে হয়েছে।

---

#### ✅ Part 2: APIView দিয়ে JSON Response - Step by Step

#### 🔹 Step 1: Model তৈরি করো

```python
# blog/models.py
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

🔸 কেন করলাম?

> আমরা ডেটা কোথা থেকে আনব? Model মানে হচ্ছে ডেটাবেইসের কাঠামো।এই ডাটাবেস থেকে আমরা ডাটা নিবো যা api
> এর maddhome ফ্রন্টএন্ড apps কে পাঠাবো।

---

#### 🔹 Step 2: Serializer তৈরি করো

```python
# blog/serializers.py
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
```

🔸 কেন করলাম?

> Model কে JSON এ রূপান্তর করার জন্য serializer দরকার। না করলে API ডেটা পাঠাতে পারবে না। serializer
> অনেক টা django এর ফর্ম এর মতো ফর্ম যেমন মডেল অবজেক্ট ফিল্ডস বা কাস্টম ফিল্ডস কে টেম্পলেট এ কনভার্ট
> এন্ড ডাটা ভ্যালিডেশন করে। তেমনি serializer ও মডেল অবজেক্ট ফিল্ডস বা কাস্টম ফিল্ডস কে পাইথন
> dictionary তে কনভার্ট করে এবং ফিল্ড ভ্যালিডেশন করে। এরপর সেই পাইথন dictionary কে পরবর্তী ভিউ তে
> response json এ কনভার্ট করে সেই জেসন এর সাথে প্রয়োজনীয় সব মেটা ডাটা হেডার স্টেটাস যুক্ত করে
> ফ্রন্টএন্ড apps কে পাঠিয়ে দেয়।

---

#### 🔹 Step 3: APIView তৈরি করো

```python
# blog/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True) #many=true না  দিলে মডেল এর একাধিক অবজেক্ট কে ভ্যালিডেট করে  লিস্ট অফ মডেল  অবজেক্ট  ডিক্ট  বানাতো না একটা অবজেক্ট ধরে নিতো dict  এর লিস্ট না বানিয়ে জাস্ট একটা dict বানাতো।
        return Response(serializer.data)
```

🔸 কেন করলাম?

> APIView হলো DRF-এর class-based view, যেটা দিয়ে আমরা GET/POST ইত্যাদি method ব্যবহার করতে পারি।যার
> একটা মেথড আছে as_view এই মেথড রিকোয়েস্ট এর মেথড (post,get,put,patch,delete) অনুযায়ী apiview এর
> view মেথড এক্সিকিউট করে।APIView নিজেই as_view() মেথড দিয়ে HTTP মেথড (get, post, put, patch,
> delete) অনুযায়ী ক্লাসের সংশ্লিষ্ট মেথড (get(), post(), put()...) এক্সিকিউট করে। আমরা viewset এর
> ক্ষেত্রে as_view() class মেথড কে আর্গুমেন্ট পাস করে বলে দিতে পারি কোন রিকোয়েস্ট মেথড এ কোন ক্লাস
> মেথড ভিউ এক্সিকিউট হবে APIview.as_view({

    "get":list,"post":create,"put":update

}) এই কাজ তা মূলত deafaltrouter() করে urlpatterent লিস্ট বানায় এটা viewset ,modelviewset এর বেলায়
তবে সেটা apiview এ কাজ করে না ।

#### APIview vs viewset

| বিষয়                   | APIView                           | ViewSet / ModelViewSet                   |
| ---------------------- | --------------------------------- | ---------------------------------------- |
| HTTP মেথড হ্যান্ডলিং   | ক্লাসের get/post/put ইত্যাদি মেথড | `as_view()`-এ মেথড-ম্যাপিং ডিকশনারি দিয়ে |
| `as_view()` আর্গুমেন্ট | নেয় না                            | নেয় (মেথড-ম্যাপিং ডিকশনারি)              |
| URL প্যাটার্ন          | ম্যানুয়ালি লিখতে হয়               | Router দিয়ে অটোমেটিক তৈরি হয়             |

---

#### 🔹 Step 4: URL যুক্ত করো

```python
# blog/urls.py
from django.urls import path
from .views import BlogListAPIView

urlpatterns = [
    path('api/blogs/', BlogListAPIView.as_view(), name='api-blogs'),
]
```

🔸 কেন করলাম?

> URL ছাড়া আমরা ব্রাউজার বা অ্যাপ থেকে এই API-তে রিকোয়েস্ট পাঠাতে পারতাম না।

---

#### 🔹 এখন ব্রাউজারে এই লিংক ভিজিট করো:

```
http://127.0.0.1:8000/api/blogs/
```

🔸 তুমি JSON format-এ ডেটা দেখতে পাবে।

---

### 🔹 Bonus: POST দিয়ে নতুন Blog তৈরি

```python
class BlogCreateAPIView(APIView):
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

🔸 কেন করলাম?

> শুধু GET করলে ডেটা দেখানো যায়। POST করলে নতুন ডেটা যোগ করা যায়।

---

### 📊 Part 3: API vs Web Page

| বিষয়                    | Web Page            | API                 |
| ----------------------- | ------------------- | ------------------- |
| Format                  | HTML                | JSON                |
| Viewer                  | মানুষ (User)        | অ্যাপ বা JavaScript |
| উদ্দেশ্য                | দেখানো              | ডেটা পাঠানো/নেওয়া   |
| কী থাকে?                | Text, Image, Design | কাঁচা ডেটা          |
| Mobile App ব্যবহার করে? | না                  | হ্যাঁ               |

---

### 🧠 উপসংহার:

- Web Page = মানুষের জন্য
- API = অ্যাপ ও কম্পিউটারের জন্য
- APIView দিয়ে DRF এ JSON Response পাঠানো যায়
- Serializer ছাড়া JSON বানানো যেত না,validation করা যেত না
- URL ছাড়া API এক্সেস করা যেত না

---

## ✅ Day 12: Serializers (Basic)

এই Handnote টা ৩টা গুরুত্বপূর্ণ Django DRF topic কভার করবে:

- Manual Serializer Class
- ModelSerializer
- Serializer Validation

সাথে তুলনামূলক আলোচনা থাকবে Django Forms এর সাথে:

- Forms vs Serializers
- ModelForm vs ModelSerializer

---

### 1. Manual Serializer Class

#### 🔹 কী?

Manual serializer class হচ্ছে DRF-এর serializer যেটা `serializers.Serializer` থেকে ইনহেরিট করে
বানানো হয়। এটা একদম Django Form এর মতো কাজ করে, কিন্তু JSON data এর জন্য।

#### ✅ কেন ব্যবহার করবো?

যখন আপনি নিজের মতো করে ফিল্ড, ভ্যালিডেশন কাস্টমাইজ করতে চান এবং Model এর সাথে সরাসরি সম্পর্ক নাই।

#### 🔧 কোড:

```python
from rest_framework import serializers

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, label="Blog Title")
    content = serializers.CharField()

    def validate_title(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError("Title must contain 'django'")
        return value

    def validate(self, data):
        if data['title'] == data['content']:
            raise serializers.ValidationError("Title and content must be different")
        return data

# External validator function
from rest_framework.validators import ValidationError

def no_hello(value):
    if 'hello' in value.lower():
        raise ValidationError("'hello' is not allowed")

class SampleSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[no_hello])
```

### 🧠 মিল Django Form এর সাথে:

| Manual Serializer                | Django Form                    |
| -------------------------------- | ------------------------------ |
| `Serializer` থেকে ইনহেরিট        | `forms.Form` থেকে ইনহেরিট      |
| ফিল্ড define করতে হয়             | ফিল্ড define করতে হয়           |
| `.is_valid()`, `.validated_data` | `.is_valid()`, `.cleaned_data` |
| `.validate_<field>()` method     | `clean_<field>()` method       |
| `.validate()` method             | `clean()` method               |

### ❌ অমিল:

| Manual Serializer                                              | Django Form                                                                                                                                                                                         |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| JSON Data handle করে                                           | HTML form data handle করে                                                                                                                                                                           |
| API request/response format                                    | Template rendering and user input                                                                                                                                                                   |
| `.save()` method নাই                                           | `.save()` method নাই (form এ থাকে শুধু ModelForm এ)                                                                                                                                                 |
| DRF নিজে validate\_<field>(self,value) এ ফিল্ডের value পাঠায়   | Form এ clean\_<field>() call করার সময় cleaned_data থেকে নিজে cleaned_data[field] avabe নিতে হয়                                                                                                      |
| DRF নিজেই validate(self,data)-এ সব cleaned/validate data পাঠায় | Django Form এ parent class এর clean() manually call করতে হয় self.cleaned_data dict তৈরি করতে তারপর cleaned_data[field] এভাবে করে যতগুলা দরকার ফিল্ড এর ভ্যালু নিতে হয় json ভ্যালিডেটে এর ক্ষেত্রে । |

---

### 2. ModelSerializer

#### 🔹 কী?

`serializers.ModelSerializer` এমন এক serializer যেটা Django এর Model এর উপর ভিত্তি করে অটো ফিল্ড
তৈরি করে দেয়।

#### ✅ কেন ব্যবহার করবো?

যখন আপনার ডেটা সরাসরি Model এর সাথে সম্পর্কিত।

#### 🔧 কোড:

```python
from rest_framework import serializers
from .models import Blog

# Custom validator
from rest_framework.validators import ValidationError

def no_forbidden(value):
    if "forbidden" in value.lower():
        raise ValidationError("You can't use the word 'forbidden'")

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        extra_kwargs = {
            'title': {
                'label': "Blog Title",
                'validators': [no_forbidden]
            },
            'content': {
                'label': "Content Body"
            }
        }

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title is too short")
        return value

    def validate(self, data):
        if data['title'] == data['content']:
            raise serializers.ValidationError("Title and content cannot be the same")
        return data
```

#### 🧠 মিল ModelForm এর সাথে:

| ModelSerializer             | ModelForm                   |
| --------------------------- | --------------------------- |
| Model এর উপর ভিত্তি করে     | Model এর উপর ভিত্তি করে     |
| `Meta` class ব্যবহার করে    | `Meta` class ব্যবহার করে    |
| ফিল্ড অটো তৈরি হয়           | ফিল্ড অটো তৈরি হয়           |
| `.save()` method থাকে       | `.save()` method থাকে       |
| Validation override করা যায় | Validation override করা যায় |

#### ❌ অমিল:

| ModelSerializer        | ModelForm             |
| ---------------------- | --------------------- |
| JSON data process করে  | HTML Form process করে |
| Template render করে না | Template render করে   |
| API-based              | Form-based            |

---

### 3. Serializer Validation vs Form Validation

#### 🧩 ফিল্ড-লেভেল Validation:

| Serializer                          | Form                          |
| ----------------------------------- | ----------------------------- |
| `validate_<field>()`                | `clean_<field>()`             |
| Raise `serializers.ValidationError` | Raise `forms.ValidationError` |

#### 🧩 Object-লেভেল Validation:

| Serializer                          | Form                          |
| ----------------------------------- | ----------------------------- |
| `validate(self, data)`              | `clean(self)`                 |
| Raise `serializers.ValidationError` | Raise `forms.ValidationError` |

#### 🧩 Built-in Field Validation:

| Serializer                                 | Form                                       |
| ------------------------------------------ | ------------------------------------------ |
| `CharField(required=True, max_length=...)` | `CharField(required=True, max_length=...)` |

#### 🧩 Custom Validator Function:

| Serializer                          | Form                          |
| ----------------------------------- | ----------------------------- |
| `validators=[my_func]`              | `validators=[my_func]`        |
| Raise `serializers.ValidationError` | Raise `forms.ValidationError` |

---

#### 🧩 Error কোথায় store হয়?

| বিষয়                            | Serializer                                  | Form                                                                  |
| ------------------------------- | ------------------------------------------- | --------------------------------------------------------------------- |
| ফিল্ড-লেভেল Error               | `serializer.errors['field']`                | `form['field'].errors`                                                |
| অবজেক্ট-লেভেল Error (non-field) | `serializer.errors['non_field_errors']`     | `form.non_field_errors()`                                             |
| ম্যানুয়ালি Error add করলে       | `raise ValidationError({'field': 'error'})` | `self.add_error('field', 'error')` বা `raise forms.ValidationError()` |

---

#### 🔄 Summary Table

| বিষয়              | Serializer                               | Form                   | মিল | অমিল                    |
| ----------------- | ---------------------------------------- | ---------------------- | --- | ----------------------- |
| ইনহেরিট           | serializers.Serializer / ModelSerializer | forms.Form / ModelForm | ✅  | ❌ DRF uses JSON        |
| ফিল্ড define      | ✅                                       | ✅                     | ✅  | ❌ HTML vs JSON         |
| Field validation  | validate\_<field>()                      | clean\_<field>()       | ✅  | Syntax আলাদা            |
| Object validation | validate()                               | clean()                | ✅  | Syntax আলাদা            |
| Custom validator  | ✅                                       | ✅                     | ✅  | Raise class আলাদা       |
| `.is_valid()`     | ✅                                       | ✅                     | ✅  | None                    |
| `.save()`         | শুধু ModelSerializer এ                   | শুধু ModelForm এ       | ✅  | Manual serializer এ নাই |
| Data format       | JSON                                     | HTML form              | ❌  | ✅                      |
| Frontend Render   | ❌                                       | ✅                     | ❌  | ✅                      |
| API Usage         | ✅                                       | ❌                     | ❌  | ✅                      |

---

### ✅ Extra Tips:

- DRF এর serializer = Django Form এর advanced version, API-centric
- শুধু frontend rendering লাগলে => Django Form
- যদি API বানাতে হয় => DRF Serializer
- Model এর সাথে কাজ করলে => ModelSerializer / ModelForm
- কাস্টম ভ্যালিডেশন লাগলে => `validate_<field>()` বা `validate()` override করো

---

## ✅ Day 13: API CRUD (GenericAPIView,mixin)

- mixin,genericapiview

- ListAPIView, CreateAPIView

- RetrieveUpdateDestroyAPIView

- Data add, edit, delete via API(genericapiview)

### 📚 DRF: GenericAPIView, Mixins, and Class-Based Views (A to Z Full Guide)

এই হ্যান্ডনোটে আমরা DRF-এর GenericAPIView, Mixins এবং Generic Views যেমন `ListAPIView`,
`CreateAPIView`, `RetrieveUpdateDestroyAPIView` — প্রতিটি বিষয় A to Z তে আলোচনা করবো। এছাড়াও, এগুলোর
Form (Django traditional form)-এর সাথে তুলনাও করবো, যেন future-এ রিভিশন দিলে সহজে মনে পড়ে যায়।

---

### 🧠 DRF এ GenericAPIView আর Mixins কেন এলো?

👉 DRF অনেক low-level থেকে কাজ করতে দেয় — যেমন APIView দিয়ে। কিন্তু সবকিছু আবার আবার লিখতে হয়
(validation, queryset, save, etc.)। তাই DRY (Don't Repeat Yourself) মেনে reusable অংশগুলোকে আলাদা
করা হয়েছে — GenericAPIView ও Mixins আকারে।

- `GenericAPIView`: এটি base class যেটি queryset, serializer_class, lookup_field এসবকে configure করে
  এবং এর মধ্যে get_queryset,get_serializer_class,filter_queryset etc মেথড থাকে যার মাদ্ধমে এর চাইল্ড
  গুলো এর কনফিগার গুলা fetch করতে পারে । এটি APIView কে extend করে যার ফলে জেনেরিক এর সব route
  apiview handle করে তার ডেফল্ট বিহেভিয়ার (get ,post ,update ,delete ) মেথড দিয়া ।
- `Mixins`: এগুলো ছোট ছোট কাজের behavior দেয় — যেমন list করা, create করা, retrieve করা ইত্যাদি।বলা
  যায় mixin রেডিমেট ডাইনামিক ভিউ বানিয়ে রাখে যে self.get_serializer(data=request.data)
  self.get_queryset() এর মাধ্যমে serializer ,queryset etc genericapiview এর কাছ থেকে তাকে এক্সটেন্ড
  এর মধ্যে থাকা মেথড গুলা use করে অপারেশন চলার জন্য যা যা লাগে সব ফেচ করে নেয় । mixin এ প্রতিটা
  oparetion এর জন্য আলাদা আলাদা ক্লাস আছে mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,mixins.DestroyModelMixin ইত্যাদি

Note: mixin ডাইরেক্ট ভাবে GenericAPIView কে এক্সটেন্ড করে না বরং ইনডাইরেক্ট ভাবে করে মানে হলো
ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView এগুলা GenericAPIView এবং তার অপারেশন এর
জন্য যে মিক্সিন লাগবে সেটা এক্সটেন্ড করে যেমন ListAPIView mixins.listModelMixin কে আবার
CreateAPIView Createmodelmixin কে তাই mixin ও ইনডাইরেক্ট ভাবে GenericAPIView কে এক্সটেন্ড করে

```python
class RetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    def get(self, request, *args, **kwargs): #apiview  এর get মেথড আর get ভিউ রেন্ডার functionaity
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs): #apiview  এর put  মেথড আর put ভিউ রেন্ডার functionaity
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):   #apiview  এর patch  মেথড আর patch  ভিউ রেন্ডার functionaity
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs): #apiview  এর delete  মেথড আর delete  ভিউ রেন্ডার functionaity
        return self.destroy(request, *args, **kwargs)

```

#### এভাবেই GenericAPIView ইনডাইরেক্ট ভাবে apiview দ্বারা রাউটিং এন্ড মেথড ভিউ রেন্ডারিং হ্যান্ডেল করে

---

### 🔎 APIView vs GenericAPIView vs ViewSet vs ModelViewSet

| Feature     | APIView              | GenericAPIView          | ViewSet            | ModelViewSet             |
| ----------- | -------------------- | ----------------------- | ------------------ | ------------------------ |
| Base Class  | `APIView`            | `GenericAPIView`        | `ViewSet`          | `ModelViewSet`           |
| Flexibility | Full control         | Semi-automated          | Fully automated    | Fully automated + CRUD   |
| Use Case    | Custom logic         | CRUD with customization | Grouped routes     | Full CRUD with less code |
| When to Use | Complex custom logic | Control + Reuse         | Router with method | Most default use cases   |

---

### 🧩 GenericAPIView + Mixins: ধাপে ধাপে

### 🧱 GenericAPIView কাজ কী?

- `queryset` : কাদের উপর কাজ হবে
- `serializer_class` : কোন serializer ইউজ হবে
- `.get_queryset()` ও `.get_serializer_class()` override করলে ডায়নামিক behavior দেওয়া যায়

### 🔧 DRF Mixins

| Mixin                | Functionality    |
| -------------------- | ---------------- |
| `ListModelMixin`     | GET list         |
| `CreateModelMixin`   | POST add         |
| `RetrieveModelMixin` | GET single item  |
| `UpdateModelMixin`   | PUT/PATCH update |
| `DestroyModelMixin`  | DELETE delete    |

**কাজের ধরন অনুযায়ী Mixins মিশিয়ে GenericAPIView থেকে নিজের ভিউ বানানো যায়।**

---

### 🧪 বিস্তারিত Generic Views

#### ✅ 1. `ListAPIView`

**ব্যবহার:** সব ডেটা লিস্ট আকারে রিটার্ন করা

```python
from rest_framework.generics import ListAPIView

class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

#### 🔁 Form দিয়ে:

```python
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'template.html', {'blogs': blogs})
```

### ✅ 2. `CreateAPIView`

**ব্যবহার:** নতুন ডেটা যুক্ত করা

```python
from rest_framework.generics import CreateAPIView

class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

#### 🔁 Form দিয়ে:

```python
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

def blog_create(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        form.save()
```

### ✅ 3. `RetrieveUpdateDestroyAPIView`

**ব্যবহার:** একটি ডেটা দেখানো, আপডেট করা বা মুছে ফেলা

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
```

#### 🔁 Form দিয়ে:

```python
def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
```

---

### ⌛ কখন কোনটা ব্যবহার করবো?

| কাজের ধরন                     | কোন View ব্যবহার করবেন     |
| ----------------------------- | -------------------------- |
| Full CRUD দরকার               | `ModelViewSet`             |
| Partial/customized CRUD দরকার | `GenericAPIView` + Mixins  |
| খুব Custom logic দরকার        | `APIView`                  |
| Nested Routing দরকার          | `ViewSet` / `ModelViewSet` |

---

### 🔁 তুলনামূলক টেবিল (Form vs DRF)

| Task     | Django Form                           | DRF GenericAPIView   |
| -------- | ------------------------------------- | -------------------- |
| List     | Query in view + Template loop         | `ListAPIView`        |
| Create   | `ModelForm`, save()                   | `CreateAPIView`      |
| Retrieve | `get_object_or_404()` + form.instance | `RetrieveModelMixin` |
| Update   | `form(instance=obj).save()`           | `UpdateModelMixin`   |
| Delete   | `obj.delete()`                        | `DestroyModelMixin`  |

---

### 🔐 Extra Notes:

- `ListAPIView` = `GenericAPIView` + `ListModelMixin`
- `CreateAPIView` = `GenericAPIView` + `CreateModelMixin`
- `RetrieveUpdateDestroyAPIView` = `GenericAPIView` + `RetrieveModelMixin`+ `updateModelMixin` +
  `updateModelMixin`

---

## ✅ Tips:

- ছোটখাটো customize করলে GenericAPIView + Mixins খুব efficient
- full CRUD দরকার হলে ModelViewSet সবচেয়ে শর্টকাট ও powerful
- highly customizable চাইলে APIView এ পুরো কন্ট্রোল রাখা যায়

---

## 📦 Bonus: Routing & URL

```python
from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [
    path('blogs/', BlogListView.as_view()),
    path('blogs/create/', BlogCreateView.as_view()),
    path('blogs/<int:pk>/', BlogDetailView.as_view()),
]
```

---

## ✅ Day 14: ViewSets & Routers

- ViewSet vs APIView
- viewsets,modelviewset,readonlyviewset
- Routers দিয়ে URL config
- ViewSet actions (list, retrieve, create, etc.)

### 🔹 1. APIView কি?

`APIView` হল Django REST Framework এর সবচেয়ে Base ক্লাস API তৈরি করার জন্য। এটি Python-এর সাধারণ
ক্লাস ভিত্তিক View-এর মতো কাজ করে।

### ✅ কেন ব্যবহার করবো?

- যখন আমাদের পুরো কাস্টমাইজড control দরকার HTTP methods এর উপর।

### 🧠 Structure:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    def get(self, request):
        return Response({"message": "GET request"})

    def post(self, request):
        return Response({"message": "POST request"})
```

---

### 🔹 2. ViewSet কি?

`ViewSet` একটি ক্লাস যেটি APIView এর উপর ভিত্তি করে তৈরি, কিন্তু এতে HTTP methods গুলো আলাদা করে না
লিখে একসাথে CRUD operations handle করা যায়। list create এর জন্য আলাদা class আবার
update,delete,retrive এর জন্য আলাদা ক্লাস লিখার দরকার হয় viewset rouder এর দ্বারা কাজ করে রাউটার
নিজে route create করতে পারে তাই আমাদের ম্যানুয়ালি ভিউসেট এর জন্য route লিখার দরকার হয় না deafalt
রাউটার এ রেজিস্টার করলে হয়। সেই সব route বানিয়ে একটা urlpattern বানিয়ে দেয়।

### ✅ কেন ব্যবহার করবো?

- যখন আমরা CRUD operation করবো এবং প্রতিবার `get`, `post`, `put`, `delete` আলাদা আলাদা ক্লাসে এরকম
  apiview এর মতো করে না লিখে shortcut এ কাজ করতে চাই।এবং নিজে ইউআরএল ম্যাপিং করতে না চাইলে আমরা
  ভিউসেট use করবো।

### 🧠 Structure:

```python
from rest_framework.viewsets import ViewSet

class MyViewSet(ViewSet):
    def list(self, request):
        return Response({"message": "List of data"})

    def retrieve(self, request, pk=None):
        return Response({"message": f"Single data {pk}"})
```

> ⚠️ এখানে `as_view()` method ব্যাবহারের দরকার নেই, DRF এর `routers` এগুলো auto-map করে দেয়।

---

### 🔹 3. ModelViewSet কি?

`ModelViewSet` হচ্ছে `ViewSet` এর subclass, যেটা মডেল এবং serializer নিয়ে পুরো CRUD automatically
handle করে। `modelviewset` mixins.CreateModelMixin, mixins.RetrieveModelMixin,
mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet কে
এক্সটেন্ড করে যার ফলে আবার genericviewset ViewSetMixin, generics.GenericAPIView কে extend করে যার
ফলে বলা যায় modelviewset ইনডাইরেক্ট ভাবে ভিউসেট কে এক্সটেন্ড করে যার ফলে মডেল ভিউসেট এর feacher
router এর সাপোর্ট পায় আর list ,create ,retrive, destry etc সব ভিউ মিক্সিন থেকে ইনহেরিট করে যার ফলে
আমাদের জাস্ট সেরিয়ালিজের আর queryset দিতে হয় agenericapiview কে তার কাছ থেকে সব serializer
,queryset,filter ,serch etc সব নেয় genericviewset এবং সেই অনুযায়ী get মেথড এ লিস্ট pk পাঠালে retrive
,post এ create টি = etc এভাবে autommatic সব হ্যান্ডেল হয়।

### ✅ কেন ব্যবহার করবো?

- মডেলের জন্য পুরো CRUD তৈরি করতে চাই খুব সহজে।

### 🧠 Structure:

```python
from rest_framework.viewsets import ModelViewSet
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

---

### 🔹 4. ReadOnlyModelViewSet কি?

`ReadOnlyModelViewSet` ও `ModelViewSet` এর মতো, কিন্তু শুধু `list` ও `retrieve` method দেয়। কোন কিছু
Create, Update, Delete করা যায় না।

### ✅ কেন ব্যবহার করবো?

- যখন শুধু data দেখতে দিবো, কিন্তু edit করতে দিবো না।

### 🧠 Structure:

```python
from rest_framework.viewsets import ReadOnlyModelViewSet

class MyReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

---

### 🔹 5. Routers দিয়ে URL Configuration

`ViewSet` বা `ModelViewSet` use করলে নিজে URL path লিখতে হয় না, `router` automatically সব URL তৈরি
করে দেয়।

### ✅ কেন ব্যবহার করবো?

- প্রতিটা route নিজে লিখার ঝামেলা থেকে বাঁচার জন্য।

### 🧠 Structure:

```python
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'myapi', MyModelViewSet, basename='myapi')
                   ।_ prefix    ।_viewclass

urlpatterns = [
    path('', include(router.urls)),
]
```

#### router internally নিচের মতো করে কাজ করে।

```python

  [
      path("prefix/",viewset.as_view({"get":"list","post":"create"}),
      path("prefix/<int:pk>/",viewset.as_view({"get":"retrive","put":"update","delete":"destroy","patch":"partial-update"}))
  ]

```

##### note: as_view() te paramitar hisabe configer viewset e pathano jay apiview e jay na.

### 👉 এটা automatically নিচের URL গুলো তৈরি করে:

- GET `/myapi/` → list() // url name-> basename-list
- GET `/myapi/<pk>/` → retrieve() // url name-> basename-retrieve
- POST `/myapi/` → create() // url name-> basename-create
- PUT `/myapi/<pk>/` → update() // url name-> basename-update
- DELETE `/myapi/<pk>/` → destroy() // url name-> basename-destroy

---

#### prefix vs name

| বিষয়        | `prefix`                                   | `basename`                                   |
| ----------- | ------------------------------------------ | -------------------------------------------- |
| কাজ         | এর ওপর ভিত্তি করে প্রতিটা URL path ঠিক করে | এর ওপর ভিত্তি করে প্রতিটা Route name ঠিক করে |
| ব্যবহার হয়  | ১ম argument হিসাবে                         | ৩য় argument হিসাবে                           |
| প্রয়োজনীয়তা | Always required                            | Optional (queryset থাকলে না দিলেও চলে)       |
| উদাহরণ      | `'books'` → `/books/`                      | `'book'` → `book-list`, `book-detail`        |

### 🔹 ViewSet এর Built-in Methods

| Method Name      | Description                 |
| ---------------- | --------------------------- |
| list()           | সব object এর লিস্ট দেখায়    |
| retrieve()       | নির্দিষ্ট একটি object দেখায় |
| create()         | নতুন object তৈরি করে        |
| update()         | পুরা object আপডেট করে       |
| partial_update() | কিছু অংশ আপডেট করে (PATCH)  |
| destroy()        | object ডিলিট করে            |

---

### 🔹 ViewSet vs APIView তুলনা

| Feature     | APIView                       | ViewSet / ModelViewSet |
| ----------- | ----------------------------- | ---------------------- |
| Control     | বেশি কাস্টমাইজড               | কম কাস্টমাইজড          |
| URL mapping | নিজে করতে হয়                  | Router auto-handle করে |
| Use case    | যখন একদম নিজে logic লিখতে চাই | যখন CRUD অটো চাই       |

---

#### 🔹 কখন কোনটা ব্যবহার করবো?

| Condition                              | Use                    |
| -------------------------------------- | ---------------------- |
| সম্পূর্ণ কাস্টম API behavior দরকার     | `APIView`              |
| Simple CRUD দরকার                      | `ModelViewSet`         |
| শুধু দেখাবো (read-only)                | `ReadOnlyModelViewSet` |
| কাস্টম method সহ CRUD control করতে চাই | `ViewSet` + `@action`  |

---

#### 🔹 Bonus: ViewSet এর Custom Action

```python
from rest_framework.decorators import action

class MyViewSet(ViewSet):
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        return Response({"msg": "This is custom action"})
```

URL: `/myviewset/<pk>/custom_action/`

---

#### 🔹 Extra: ViewSet এর ভিতরে as_view() না লাগার কারণ

`ViewSet` class এর জন্য DRF-এর router system automatically URL map করে দেয়। কিন্তু `APIView`
ব্যাবহার করলে, নিজের হাতে `.as_view()` দিতে হয়, কারণ Django বুঝে না কোন method handle করবে।

---

### ✅ Summary:

- `APIView`: বেশি কাস্টম কাজের জন্য।
- `ViewSet`: অনেক কাজ shortcut এ করতে চাইলে।
- `ModelViewSet`: CRUD খুব সহজে তৈরি করতে।
- `ReadOnlyModelViewSet`: শুধু দেখানোর জন্য।
- `router`: ViewSet URL অটো handle করে।

---

## ✅ Day 15: API Testing (Postman)

- Postman দিয়ে API GET/POST

- Header set, Auth, Params, Body

- API error handling

- Django-তে CORS allow করা

---

### 🧪 1. API Testing (Postman)

### কেন API Testing করবো?

Django-তে আমরা যখন API তৈরি করি (DRF দিয়ে), তখন চাই যে Client সঠিকভাবে request পাঠাতে পারবে এবং
Server ঠিকভাবে response দিবে। এইটা যাচাই করার জন্য আমরা Postman ব্যবহার করি।

### Postman কী?

Postman একটি GUI-based tool, যেটা দিয়ে তুমি API call (GET, POST, PUT, DELETE etc) করতে পারো — সহজে।

---

### 🔁 2. Postman দিয়ে API GET / POST

### 🔹 GET Request:

- ডেটা দেখার জন্য ব্যবহৃত হয়
- Example:
  - Endpoint: `http://127.0.0.1:8000/api/blogs/`
  - Method: `GET`
  - Postman-এ শুধু URL দিয়ে **Send** ক্লিক করলেই JSON data চলে আসবে

### 🔹 POST Request:

- নতুন ডেটা add করার জন্য
- Example:
  - Endpoint: `http://127.0.0.1:8000/api/blogs/`
  - Method: `POST`
  - Body > raw > JSON format:
    ```json
    {
      "title": "My Blog",
      "content": "This is my blog post."
    }
    ```
  - তারপর **Send**

---

### 📑 3. Headers, Auth, Params, Body

### 🔸 Headers:

Headers হল এমন তথ্য যা Client এবং Server-এর মধ্যে communication এর জন্য দরকার হয়।

#### Headers ২ প্রকার:

1. **General Headers** – Meta info দেয়
2. **Request Headers** – Client থেকে যায়
3. **Response Headers** – Server থেকে আসে

### ১ General Headers:

> HTTP General Headers মানে এমন header গুলা যা request এবং response উভয় ক্ষেত্রেই ব্যবহৃত হতে পারে।
> এই headers গুলা মূলত message-এর meta-information বহন করে — যেমন message caching, connection info,
> অথবা date/time এর মতো বিষয়।

- এগুলো এমন header যা client → server এবং server → client উভয় দিকেই যেতে পারে।
- এগুলোর কাজ হচ্ছে message-এর আচরণ ও বৈশিষ্ট্য ব্যাখ্যা করা, কিন্তু এগুলো body বা content-এর বিষয়ে
  নির্দিষ্ট কিছু বলে না।

- General Headers সব সময় message-এর body নয়, বরং message নিজেই কিভাবে handle হবে তা নির্দেশ করে।

- এগুলো content-specific নয়, যেমন content-type, content-length এগুলো entity headers বা
  representation headers এ পড়ে।

#### 🎯Most Common Built-in HTTP General Headers (Meta Info দেয়)

| Header              | কাজ                                                         | কোথায়/কেন ব্যবহার হয়                                        | না ব্যবহার করলে কী হতে পারে                           |
| ------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| `Cache-Control`     | কন্টেন্ট ব্রাউজারে কতক্ষণ ক্যাশে থাকবে তা নির্ধারণ করে      | Performance optimization, SPA বা static content এর ক্ষেত্রে | কন্টেন্ট বারবার লোড হবে → Performance slow            |
| `Connection`        | সার্ভারের সাথে কানেকশন থাকবে কিনা তা বলে (keep-alive/close) | Persistent connection এর জন্য                               | প্রতিবার request এ নতুন করে TCP connection খোলা লাগবে |
| `Date`              | রেসপন্সটি কখন জেনারেট করা হয়েছে                             | Time validation/check এর জন্য                               | Response এর সময় জানা যাবে না, sync issue হতে পারে     |
| `Transfer-Encoding` | কনটেন্ট কিভাবে ট্রান্সফার করা হচ্ছে (chunked etc.)          | Large content break করে পাঠানোর জন্য                        | বড় response পাঠাতে সমস্যা হতে পারে                    |
| `Via`               | কোন intermediate proxy/gateway হয়ে এসেছে তা জানায়           | Proxy server বা caching mechanism ব্যবহারে                  | Proxy troubleshooting কঠিন হয়ে পড়ে                    |

👉 Example General headers:

```http
GET /api/users HTTP/1.1
Host: example.com
Authorization: Bearer abc123xyz
Accept: application/json
User-Agent: Mozilla/5.0

```

### ২ Request Headers (Client → Server যায়):

> HTTP Request Headers মূলত client (যেমন browser বা Postman) যখন server-এর কাছে কোন request পাঠায়,
> তখন সাথে কিছু অতিরিক্ত তথ্য পাঠানো হয় header-এর মাধ্যমে। এগুলো server কে বলে দেয় request সম্পর্কে
> context, যেমন content format, authentication token, language preference ইত্যাদি।

#### 🎯Most Common Built-in HTTP Request Headers

| Header          | কাজ                                                       | কোথায়/কেন ব্যবহার হয়                          | না ব্যবহার করলে কী হতে পারে                 |
| --------------- | --------------------------------------------------------- | --------------------------------------------- | ------------------------------------------- |
| `Host`          | কোন ডোমেইনের জন্য রিকোয়েস্ট করা হচ্ছে                     | Server multiple site handle করলে              | সার্ভার বুঝবে না কোন site এর জন্য রিকোয়েস্ট |
| `User-Agent`    | Client-এর ব্রাউজার বা ডিভাইস info দেয়                     | Analytics, device-specific content serve করতে | Browser compatibility issue হতে পারে        |
| `Accept`        | Client কোন টাইপের content চায় (e.g., JSON, HTML)          | REST API, Content negotiation এ               | Server ভুল format পাঠাতে পারে               |
| `Authorization` | Access token বা credentials পাঠায়                         | Protected route access করতে                   | Unauthorized (401) error আসবে               |
| `Content-Type`  | Client কনটেন্টের টাইপ declare করে (e.g., JSON, form-data) | POST, PUT রিকোয়েস্টে body parse করার জন্য     | Server body বুঝতে পারবে না → Error 415      |

#### 👉 Example Request headers:

```http
GET /api/users HTTP/1.1
Host: example.com
Authorization: Bearer abc123xyz
Accept: application/json
User-Agent: Mozilla/5.0

```

#### ✅ Custom Headers:

##### Custom header গুলো সাধারনত X- দিয়ে শুরু হয়।

```http
X-Auth-Token: your_token_here
X-API-Key: abc123xyz
```

#### Header না দিলে কী সমস্যা?

- Server বুঝতে পারবে না কোন format-এ data এসেছে
- Secure API-তে Access Token না থাকলে `401 Unauthorized` error দিবে

### ৩. Response Headers (Server → Client পাঠায়)

> Django (বা যেকোনো ওয়েব ফ্রেমওয়ার্ক)-এর HTTP Response এ যে Headers থাকে, সেগুলো মূলত client
> (browser বা API consumer)-এর কাছে কিছু গুরুত্বপূর্ণ metadata পাঠানোর জন্য ব্যবহৃত হয়।এগুলো হলো
> Key-Value pair আকারে তথ্য যা ব্রাউজার বা ক্লায়েন্টকে জানায় Response-এর ধরন, Cache করতে পারবে কিনা,
> Content কী ধরনের, কত বড় ইত্যাদি।

##### ✅ Response Headers-এর ধরণ

> Response Headers কে আমরা কয়েকটি ভাগে ভাগ করতে পারি:

| ধরন                  | বর্ণনা                                   |
| -------------------- | ---------------------------------------- |
| **General Headers**  | Server এবং client উভয়ের জন্য সাধারণ তথ্য |
| **Response Headers** | Server সম্পর্কিত তথ্য                    |
| **Entity Headers**   | মূল content (body) সম্পর্কে তথ্য         |
| **Security Headers** | নিরাপত্তা নিশ্চিত করার জন্য ব্যবহৃত      |

#### 🎯Most Common Built-in HTTP Response Headers

| Header                        | কাজ                                                  | কোথায়/কেন ব্যবহার হয়                     | না ব্যবহার করলে কী হতে পারে              |
| ----------------------------- | ---------------------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `Content-Type`                | রেসপন্সের content টাইপ বলে (HTML, JSON, etc.)        | ব্রাউজার/ক্লায়েন্ট সঠিকভাবে render করতে  | ডেটা ভুলভাবে render/show হতে পারে        |
| `Content-Length`              | কনটেন্টের total byte size বলে                        | Download/file transfer/streaming এ       | Incomplete বা corrupt data আসতে পারে     |
| `Set-Cookie`                  | Cookie ক্লায়েন্টে সেট করতে                           | Session management, auth token save      | লগইন সিস্টেম কাজ করবে না                 |
| `Access-Control-Allow-Origin` | কোন origin থেকে রিকোয়েস্ট আসতে পারবে তা বলে          | Cross-origin requests (CORS) handle করতে | অন্য origin থেকে API access সম্ভব হবে না |
| `ETag`                        | কন্টেন্ট চেঞ্জ হয়েছে কিনা চেক করার জন্য version/hash | Cache validation এবং bandwidth কমাতে     | পুরোনো বা ভুল ক্যাশড ডেটা লোড হতে পারে   |

### ✅ উদাহরণ (Django view থেকে):

```python
from django.http import HttpResponse

def my_view(request):
    response = HttpResponse("Hello, World!")
    response['Content-Type'] = 'text/plain'
    response['Cache-Control'] = 'no-cache'
    response['X-Custom-Header'] = 'MyApp'
    return response

```

#### ✅ Bonus: Django Response Header দেখা যাবে কোথায়?

- Browser DevTools → Network → Headers Tab
- Postman → Response → Headers
- Python code দিয়ে:

```python
response = client.get('/some-url/')
print(response.headers)
```

### ✅ সংক্ষিপ্তভাবে (Auto bind and none bind header):

| Header টাইপ | Auto bind হয়                                     | Manually bind করতে হয়                                       |
| ----------- | ------------------------------------------------ | ----------------------------------------------------------- |
| General     | `Date`, `Connection`, `Transfer-Encoding`, `Via` | `Cache-Control`                                             |
| Request     | `Host`, `User-Agent`, `Accept`                   | `Authorization`, `Content-Type`                             |
| Response    | `Content-Length`, `ETag`                         | `Content-Type`, `Set-Cookie`, `Access-Control-Allow-Origin` |

### 🔸 Auth:

Postman-এ:

- Authorization Tab > Type: Token/Auth
- Token টাইপ দিলে Header-এ auto যোগ হয়

### 🔸 Params:

- Query parameters (URL এর শেষে ?name=value)
- Example: `/blogs/?author=monira`

### 🔸 Body:

- শুধু POST, PUT, PATCH method এ লাগে
- Postman-এ: Body > raw > JSON

---

## ❌ 4. API Error Handling

### কেন দরকার?

- Client কে বুঝানো দরকার যে request-এ কী ভুল ছিল

### Django DRF-এ Error Handling এর Step-by-Step Process:

#### ✅ Step 1: Validation error example (Serializer)

```python
def validate_title(self, value):
    if "badword" in value:
        raise serializers.ValidationError("Invalid title")
    return value
```

#### ✅ Step 2: View-এ try-except

```python
from rest_framework.response import Response
from rest_framework import status

def post(self, request):
    try:
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
```

#### ✅ Step 3: Postman-এ response দেখো

```json
{
  "title": ["Invalid title"]
}
```

#### ✅ Common Error Codes:

| Status Code | মানে                               |
| ----------- | ---------------------------------- |
| 200         | Success                            |
| 201         | Created                            |
| 400         | Bad Request (ভুল data)             |
| 401         | Unauthorized (token নাই / invalid) |
| 403         | Forbidden (permission নাই)         |
| 404         | Not Found                          |
| 500         | Server Error                       |

---

## ✅ Bonus: CORS Issue Fix (Browser Access)

### Django-তে CORS allow করতে:

1. `pip install django-cors-headers`
2. settings.py এ যোগ করো:

```python
INSTALLED_APPS = [
  ...
  'corsheaders',
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  ...
]

CORS_ALLOW_ALL_ORIGINS = True  # development time only
```

---

## 📌 Summary Checklist (Revision Time)

✅ Postman setup করেছো ✅ GET/POST করে response পেয়েছো ✅ Header, Body, Params use করতে পারো ✅
Token based Auth করেছো ✅ Error Handling implement করেছো ✅ CORS fix করেছো browser access এর জন্য

---

## ✅ Day 16: Filtering & Searching

- django-filter use
- filter_backends
- SearchFilter
- OrderingFilter
- django_filter
- filterset

---

### 🔹 1. django-filter কী?

`django-filter` হল Django REST Framework (DRF)-এর জন্য এক ধরনের Third-Party filtering library, যা
API-এর GET param এর মাধ্যমে সহজে filtering করার সুবিধা দেয়।

### ✅ Install:

```bash
pip install django-filter
```

### ✅ settings.py:

```python
INSTALLED_APPS = [
    ...
    'django_filters',
]
########################################################################
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ]
}
```

---

### 🔹 2. Filter Backend কী?

`filter_backends` একটি DRF attribute যা filtering, searching বা ordering এর জন্য backend class
নির্ধারণ করে দেয়।filter_backends DRF-এর একটা attribute, যা সাধারণত আমরা APIView, GenericAPIView,
ListAPIView, ModelViewSet ইত্যাদির মধ্যে ব্যবহার করি।

> note:Filter Backend GenericAPIView তথা ভিউ এর queryset কে মোডিফাই করে আর pagination ভিউ এর রেসপন্স
> কে মোডিফাই করে এটাই আসল কথা।

### ✅ Global Level Setup:(সব ক্লাস ভিউ এর জন্য)

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}
```

### ✅ Local Level Setup (নির্দিষ্ট View class এর ভিতরে):

```python
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_field=["name","city"]
```

এই attribute টা accept করে filter backend classes-এর list, যেগুলোর প্রত্যেকটার ভিতরে একটা method
থাকে:

```python
def filter_queryset(self, request, queryset, view):
    ...
```

🔹 কে filter_backends ব্যবহার করে?

#### ✅ GenericAPIView এই attribute টি ব্যবহার করে।

### 📌 সব ListAPIView, RetrieveAPIView, ModelViewSet এইসব ক্লাস GenericAPIView থেকে ইনহেরিট করে। তাই filter_backends আসলে GenericAPIView-এর property।

🔹 ইন্টার্নালি কীভাবে কাজ করে?

GenericAPIView এর মধ্যে একটা method আছে:

```python

def filter_queryset(self, queryset):
    for backend in list(self.filter_backends):
        queryset = backend().filter_queryset(self.request, queryset, self)
    return queryset
```

#### ⚙️ Step-by-step:

- self.filter_backends থেকে list নেওয়া হয় (যেমন: [DjangoFilterBackend, SearchFilter])
- প্রত্যেক backend class কে ইনিশিয়ালাইজ করে: backend()
- তারপর প্রত্যেকটার filter_queryset() method কল করা হয়:

```python
queryset = backend().filter_queryset(request, queryset, view)
```

- প্রতিবারে queryset modify হয়ে update হয়।
- শেষে final filtered queryset return হয়। 🔹 View-এ এই filter_queryset() কখন কিভাবে কল হয় mixin এর
  মাদ্ধমে ?

```python
def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

```

🔹 Custom filter_backend class বানাতে চাইলে?

```python
from rest_framework.filters import BaseFilterBackend

class MyCustomFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # কাস্টম লজিক
        if request.user.is_staff:
            return queryset
        return queryset.none()
```

---

### 🔹 3. django_filter FilterSet ব্যবহার

### ✅ Step-by-Step:

#### Step 1: Create filters.py

```python
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['category', 'price_min', 'price_max', 'name']

```

#### Step 2: View-এ যুক্ত করো

```python
from .filters import ProductFilter

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
```

---

#### 🔹 4. SearchFilter (Full Text Search)

`SearchFilter` allow করে search query তৈরি করতে `?search=...` param ব্যবহার করে।

### ✅ Syntax:

```python
from rest_framework import filters

class ProductListAPIView(generics.ListAPIView):
    ...
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
```

### ✅ Prefix Meaning:

- `^title` → Starts with
- `=title` → Exact match
- `@title` → Full text search (only PostgreSQL)
- `$title` → Regex match

✅ Example:

```python
search_fields = ['^name', '=category', '$description']
```

---

#### 🔹 5. OrderingFilter

API-তে order করতে `?ordering=fieldname` ব্যবহার করো।

#### ✅ Example:

```python
class ProductListAPIView(generics.ListAPIView):
    ...
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'created_at']
    ordering = ['price']  # Default ordering
```

➡️ ?ordering=price ➡️ ?ordering=-price

---

#### 🔹 6. কোনটা কবে ব্যবহার করবো?

| Feature         | Use When                                          |
| --------------- | ------------------------------------------------- |
| django_filter   | Exact field filtering, date range, etc.           |
| SearchFilter    | Full-text search/filter                           |
| OrderingFilter  | Sorting result ascending/descending               |
| filterset_class | Complex filter logic (custom class-based filters) |

---

#### 🔹 7. Internally DRF কীভাবে কাজ করে?

- View এর `filter_backends` list অনুযায়ী sequentially filtering apply করে
- প্রত্যেক filter class এ `filter_queryset(self, request, queryset, view)` method থাকে
- যেটা `request.GET` থেকে query নেয় এবং `queryset` modify করে return করে

---

#### 🔹 8. সব কিছুর সংক্ষিপ্ত সংযোগ:

```python
# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'price']

# views.py
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = ProductFilter
    filterset_field=["category","topic"]
    search_fields = ['^name', '=category']
    ordering_fields = ['price', 'created_at']
    ordering = ['price']
```

---

#### filterset_fields vs filterset_class

| পার্থক্য                  | filterset_fields                          | filterset_class                   |
| ------------------------- | ----------------------------------------- | --------------------------------- |
| কিসের জন্য ব্যবহার হয়     | Simple ফিল্ড ভিত্তিক filtering            | Complex/custom filtering logic    |
| কীভাবে কাজ করে            | DRF নিজে থেকে ফিল্ডের উপর filter তৈরি করে | তুমি নিজে filter class define করো |
| কোডের উদাহরণ              | `filterset_fields = ['field1', 'field2']` | `filterset_class = ProductFilter` |
| Custom logic support করে? | ❌ না                                     | ✅ হ্যাঁ                          |
| কোনটা বেশি flexible?      | ❌ সীমিত                                  | ✅ অনেক বেশি flexible             |

#### 🔚 Conclusion

এই হ্যান্ডনোট পড়ে তোমার এখন পুরোপুরি ক্লিয়ার হয়ে যাওয়ার কথা:

- `django-filter` দিয়ে কাস্টম ফিল্টার
- `SearchFilter` দিয়ে flexible সার্চ
- `OrderingFilter` দিয়ে ordering
- `filter_backends` কিভাবে কাজ করে
- Prefix ( ^ @ = \$ ) মানে কী

তোমার DRF প্রজেক্টে ফিল্টারিং এখন হবে একদম প্রফেশনাল লেভেলের। ✅

---

## ✅ Day 17: Pagination

- PageNumberPagination
- LimitOffsetPagination
- Custom Pagination Class

---

### 🔹 Pagination কেন দরকার?

যখন Queryset বড় হয় (১০০০+ record), তখন পুরো dataset return করলে performance খারাপ হয়। তাই আমরা
**pagination** ব্যবহার করি — অর্থাৎ **একসাথে সব না পাঠিয়ে, প্রতি বার কিছু কিছু করে পাঠানো**।

---

### 🔹 Pagination DRF-এ কিভাবে কাজ করে?

DRF-এর যেকোনো `ListAPIView`, `ModelViewSet` বা `ListModelMixin` এ pagination অটোমেটিক কাজ করে যদি
pagination class সেট করা থাকে।

Pagination class-এর মূল কাজ:

- কোন page কত item দেখাবে তা নিয়ন্ত্রণ করা
- Response format ঠিক করে দেওয়া

---

### 🔹 PageNumberPagination — (Simple Page Based)

#### ✅ ব্যবহার করো যখন:

- তুমি চাই pagination `?page=2` এর মতন হবে
- Fixed item per page চাও
- পেজ বানাতে চাও বই এর মতো যে কয়েকটা লাইন মিলে একটা পেজ বানায় আবার আবার কয়েকটা পেজ মিলে একটা বই
  বানায় এক্ষেত্রে লাইন হলো মডেল অবজেক্ট আর বই হলো queryset আমরা params এ বলে দিতে পারি যে আমরা কয়
  নম্বর পেজ এর ডাটা নিতে চাই।

#### ✅ Global Setup (settings.py):

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    "PAGE_PARMS":"p"
}
```

➡️ এখন `/api/products/?page=2` → এইরকম URL কাজ করবে

#### ✅ Local Setup (View-এ):

```python
from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 100
    page_query_param = 'mypage'
```

```python
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
```

➡️ `/api/products/?mypage=3&size=20` → এইভাবে কাজ করবে

---

### 🔹 LimitOffsetPagination — (Limit & Offset(skippeditemnumber) Based)

#### ✅ ব্যবহার করো যখন:

- তুমি চাই user বলে দিবে কয়টা skip(offset) করে কয়টা item(limit) নিবে
- URL হবে `?limit=10&offset=30`

#### ✅ Global Setup:

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10  # default limit
}
```

➡️ `/api/products/?limit=5&offset=15`

### ✅ Local Customization:

```python
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'lmt'
    offset_query_param = 'ofs'
    max_limit = 100
```

```python
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomLimitPagination
```

➡️ `/api/products/?lmt=10&ofs=20`

---

### 🔹 Custom Pagination (Fully Customized Response)

#### ✅ Custom Class বানানোর কারন:

- তুমি চাই JSON এর format পুরোপুরি নিজের মতন করো
- Custom page_size, max_limit দিতে পারো

#### ✅ উদাহরণ:

```python
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    max_page_size = 50
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
```

➡️ এখন API response হবে:

```json
{
  "total_items": 50,
  "total_pages": 10,
  "current_page": 2,
  "next": "http://...page=3",
  "previous": "http://...page=1",
  "results": [ ...data... ]
}
```

---

#### 🔹 Pagination Summary Table

| Pagination Type       | Query Format          | Use When                            |
| --------------------- | --------------------- | ----------------------------------- |
| PageNumberPagination  | `?page=2`             | Simple page-based navigation        |
| LimitOffsetPagination | `?limit=10&offset=20` | More control on data range          |
| CustomPagination      | As you design         | Need custom response / page control |

---

#### 🔹 Pagination Important Parameters

| Parameter               | কাজ কী করে                            |
| ----------------------- | ------------------------------------- |
| `page_size`             | প্রতি পেজে কয়টা item থাকবে            |
| `page_size_query_param` | client-side থেকে page_size চেঞ্জ করতে |
| `max_page_size`         | client কতো বড় page_size দিতে পারবে    |
| `page_query_param`      | default `?page=` এর নাম চেঞ্জ করতে    |
| `limit_query_param`     | default `?limit=` নাম চেঞ্জ করতে      |
| `offset_query_param`    | default `?offset=` নাম চেঞ্জ করতে     |
| `default_limit`         | initial limit মান                     |

---

#### 🔚 Conclusion

এই হ্যান্ডনোটের মাধ্যমে তুমি এখন শিখে ফেলেছো:

- DRF Pagination কিভাবে কাজ করে
- Global vs Local Pagination config
- PageNumberPagination vs LimitOffsetPagination এর পার্থক্য
- Custom Pagination কীভাবে বানাতে হয়
- pagination class এর parameter গুলোর কাজ

---

## ✅ Day 18: Permissions & Authentication

### 1️⃣ Permission কী?

Permission মানে হলো **কে কোন API endpoint অ্যাক্সেস করতে পারবে, কে পারবে না** — এই নিয়ম নির্ধারণ
করা। এটা মূলত **Authentication-এর পরবর্তী ধাপ**।

- **Authentication** → ইউজার কে (Identity চেক)
- **Permission** → এই ইউজার কী করতে পারবে (Access Control)

---

### 2️⃣ Permission কোথায় বসানো যায়?

Permission দুইভাবে বসানো যায় —

| Scope                | কীভাবে বসাবো                                      | প্রভাব                                           |
| -------------------- | ------------------------------------------------- | ------------------------------------------------ |
| **Global**           | `settings.py` এ `DEFAULT_PERMISSION_CLASSES` দিয়ে | পুরো প্রজেক্টে ডিফল্টভাবে ওই permission কাজ করবে |
| **Per View / Local** | `permission_classes` attribute দিয়ে               | শুধু ওই ভিউ বা ভিউসেটে কাজ করবে                  |

#### **Global Example** (`settings.py`)

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

#### **Local Example** (ভিউতে)

```python
from rest_framework.permissions import IsAuthenticated

class MyView(APIView):
    permission_classes = [IsAuthenticated]
```

---

### 3️⃣ DRF Built-in Permission Classes

| Permission Class                         | কাজ                                                                           | কখন ব্যবহার করবো                                                                                                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AllowAny**                             | সবাই অ্যাক্সেস করতে পারবে (লগইন লাগবে না)                                     | Public API, Login/Register page                                                                                                                                   |
| **IsAuthenticated**                      | শুধু লগইন করা ইউজার অ্যাক্সেস পাবে                                            | Protected API যেমন Dashboard                                                                                                                                      |
| **IsAdminUser**                          | শুধু `is_staff=True` ইউজার অ্যাক্সেস পাবে                                     | Admin Panel API                                                                                                                                                   |
| **IsAuthenticatedOrReadOnly**            | লগইন ইউজার = সব পারবে, লগইন না করলে = শুধু GET/HEAD/OPTIONS পারবে             | Public read + Private write API                                                                                                                                   |
| **DjangoModelPermissions**               | Django Model permission system ব্যবহার করে চেক করে                            | যখন User permissions (add, change, delete, view) মডেলে সেট করা আছে                                                                                                |
| **DjangoModelPermissionsOrAnonReadOnly** | লগইন ইউজার = Model permission অনুযায়ী কাজ করবে, লগইন না করলে = শুধু read-only | Public read, private write with model perms                                                                                                                       |
| **DjangoObjectPermissions**              | Object-level permission (guardian বা custom) ব্যবহার করে চেক করে              | Row-level security দরকার হলে যেমন যার পোস্ট সে যেন শুধু সেই পোস্টটি retrive,update,delete করতে পারে এমন permissions এর ক্ষেত্রে DjangoObjectPermissions দরকার হয়। |

---

### 4️⃣ Permission কাজের Flow (Internally)

DRF যখন **APIView / GenericAPIView** চালায়, তখন এর মধ্যে এই প্রসেস হয়:

1. ভিউ কল হওয়ার আগে → `APIView.dispatch()` → `self.check_permissions(request)` কল হয়
2. `check_permissions` → লুপ চালিয়ে সব `permission_classes` এর `has_permission(request, view)` চেক
   করে
3. যদি `has_permission` **False** দেয় → `PermissionDenied` exception তুলে দেয় (HTTP 403)
4. যদি object-level permission লাগে (Retrieve/Update/Delete) →
   `check_object_permissions(request, obj)` কল হয়
5. `check_object_permissions` → প্রতিটি `permission_classes` এর
   `has_object_permission(request, view, obj)` চেক করে
6. Fail হলে → `PermissionDenied`

### 🎯 Permission কাজের ডায়াগ্রাম

```pgsql

        ┌────────────────────────────────┐
        │  Request আসে (APIView / GenericAPIView) │
        └────────────────────────────────┘
                         │
                         ▼
           ┌──────────────────────────┐
           │  dispatch() কল হয়        │
           └──────────────────────────┘
                         │
                         ▼
      ┌────────────────────────────────────┐
      │  self.check_permissions(request)   │
      └────────────────────────────────────┘
                         │
         ┌───────────────────────────────────────────┐
         │  Loop করে প্রতিটি permission_classes চেক করে │
         │  has_permission(request, view)              │
         └───────────────────────────────────────────┘
                         │
       ┌──────────────┐              ┌──────────────┐
       │ True হলে →   │              │ False হলে →  │
       │ পরের স্টেপে  │              │ PermissionDenied│
       │ যাবে         │              │ (HTTP 403)    │
       └──────────────┘              └──────────────┘
                         │
                         ▼
       ┌────────────────────────────────────────────┐
       │  যদি Object-level permission দরকার হয়       │
       │  (Retrieve / Update / Delete এর সময়)        │
       └────────────────────────────────────────────┘
                         │
                         ▼
   ┌─────────────────────────────────────────────┐
   │  self.check_object_permissions(request, obj)│
   └─────────────────────────────────────────────┘
                         │
         ┌──────────────────────────────────────────┐
         │  Loop করে প্রতিটি permission_classes চেক করে│
         │  has_object_permission(request, view, obj) │
         └──────────────────────────────────────────┘
                         │
       ┌──────────────┐              ┌──────────────┐
       │ True হলে →   │              │ False হলে →  │
       │ ভিউ চলবে    │              │ PermissionDenied│
       │ (সাকসেস)    │              │ (HTTP 403)    │
       └──────────────┘              └──────────────┘
```

---

### 5️⃣ Method: `has_permission()` vs `has_object_permission()`

| Method                                            | কবে কল হয়                                                 | প্যারামিটার        | কী return করবে                      |
| ------------------------------------------------- | --------------------------------------------------------- | ------------------ | ----------------------------------- |
| `has_permission(self, request, view)`             | ভিউ অ্যাক্সেসের আগে                                       | request, view      | **True** (Allow) / **False** (Deny) |
| `has_object_permission(self, request, view, obj)` | নির্দিষ্ট object অ্যাক্সেসের সময় (Retrieve/Update/Delete) | request, view, obj | True / False                        |

---

### 6️⃣ Custom Permission বানানো

#### Example: শুধু owner data দেখতে পারবে

```python
from rest_framework.permissions import BasePermission

class IsOwnerOnly(BasePermission):
    def has_permission(self, request, view):
        # শুধু authenticated ইউজারকে allow করবো
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Object র owner হলে allow করবো বা একটা ব্লগ /post  এর owner এ শুধু retrive /delete /আপডেট করতে পারবে।
        return obj.owner == request.user
```

**Use in view:**

```python
class MyDetailView(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOnly]
    queryset = MyModel.objects.all()
```

---

### 7️⃣ Table — সব Permission এর Summary

| Class                                | Login দরকার? | Admin লাগবে? | Object level? | Public Read? |
| ------------------------------------ | ------------ | ------------ | ------------- | ------------ |
| AllowAny                             | ❌           | ❌           | ❌            | ✅           |
| IsAuthenticated                      | ✅           | ❌           | ❌            | ❌           |
| IsAdminUser                          | ✅           | ✅           | ❌            | ❌           |
| IsAuthenticatedOrReadOnly            | Optional     | ❌           | ❌            | ✅           |
| DjangoModelPermissions               | ✅           | ❌           | ❌            | ❌           |
| DjangoModelPermissionsOrAnonReadOnly | Optional     | ❌           | ❌            | ✅           |
| DjangoObjectPermissions              | ✅           | ❌           | ✅            | ❌           |

---

### 8️⃣ বাস্তবে কোনটা কবে ব্যবহার করবো?

- **Public API** → `AllowAny`
- **Login প্রয়োজন** → `IsAuthenticated`
- **শুধু Admin ইউজার** → `IsAdminUser`
- **Public Read + Private Write** → `IsAuthenticatedOrReadOnly`
- **Django admin perms control** → `DjangoModelPermissions`
- **Public read + model perms write** → `DjangoModelPermissionsOrAnonReadOnly`
- **Owner / Row-level control** → Custom permission + `has_object_permission`

---

### 9️⃣ Shortcut কোড — Global + Local Example

```python
# settings.py (Global)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# views.py (Local Override)
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

class PublicView(APIView):
    permission_classes = [AllowAny]

class MixedView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
```

---

### 🔟 গুরুত্বপূর্ণ কথা

- **Permission সবসময় Authentication-এর পরে চেক হয়**
- **Permission fail করলে DRF 403 Forbidden রিটার্ন করে**
- **Custom permission বানালে True/False return করতেই হবে**
- Object level permission শুধু detail views এ চেক হয়, list view-তে না
- একাধিক permission দিলে → সবগুলো **AND condition** হয়।

---
