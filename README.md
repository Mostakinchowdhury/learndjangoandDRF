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
