
#### BRD -> business requirement document;
  - Projenin tüm isterlerini, özelliklerini, gereklerini yazdığımız doküman. Projedeki ana kaynak. 
  - Projeye başlamadan önce dizayn kısmında, tasarım kısmında hazırlanır.
  - Software Development Life Cycle (SDLC) İlk aşama gerekliliklerin toplanması, projenin dizayn edilmesi, kurgulanması, isterlerin biraraya getirilmesi.
  - Poje ile ilgili herşey yazar, projenin imkan/özellikleri, hangi tip kullanıcılar olacak?, normal user/admin/başka roller, her kullanıcı rolü için yetkiler, bu dokümanda bulunur.
  
- Projeye başlanacağı zaman Agile kavramından hatırlarsanız proje isterlerinin hepsi task olarak product backlog lara alınıyor. Daha sonra sprintler halinde sprint backlog lara gerekli task lar halinde atılıyor, ve ilgili developer lara assign ediliyor. Böyle devam ediliyor.
- Bir projeye başlarken bu kısımlara zaman ayırıp en ince detayına kadar planlanıp, belirlenmesi gerekiyor.

#### ERD -> Entity Relationship Diagram
  - db tablolarını şekillendirmek, bir diyagrama dökmek. 


## TASLAK_V01

- swagger
- redoc
- __debug__/
- settings -> deveopment/production
- logging 
- postgresql



- Temel Yapı
- Flight
- User

- register/login/logout
- crud operations for flights
- crud operations for reservations


- SDLC Software Development Life Cycle ->
  - Requirements analysis -> BRD, SRS, FRD/FRS
    - BRD stands for Business Requirements Document
      - BRD stands for Business Requirements Document, which is a document that outlines the business requirements for a software development project. It typically includes information about the project's goals, scope, stakeholders, and budget. 
    - SRS stands for Software Requirements Specification
      - SRS stands for Software Requirements Specification, which is a document that outlines the functional and non-functional requirements for a software development project. It typically includes information about the system's features, user interface, data structures, and performance requirements. The SRS is used by the development team to guide the software development process and ensure that the software meets the requirements of the stakeholders. 
    - FRD stands for Functional Requirements Document
      - FRD stands for Functional Requirements Document, which is a document that outlines the functional requirements for a software development project. It typically includes information about the specific features and functionalities that the software must have to meet the needs of the end-users. 
    - FRS stands for Functional Requirements Specification
      - FRS stands for Functional Requirements Specification, which is a document that outlines the detailed functional requirements for a software development project. It typically includes information about the specific inputs, processes, and outputs required for each feature or functionality of the software. The FRS is used by the development team to guide the software development process and ensure that the software meets the functional requirements of the stakeholders. 
  - Design -> Teknik/altyapı design, ERD, Pattern Design, Structure Design, Planlama 
  - Development -> Yazılım kısmı
  - Testing -> System, Unit, Functional/UI/UX, Test edilebilir seviyedeki yazılımların testi
  - Maintenance


### Django proje kurulumu:

```py
- python -m venv env
- ./env/Scripts/activate 
- pip install djangorestframework
- pip install python-decouple
- pip freeze > requirements.txt
- django-admin startproject core .
- python manage.py runserver 
```


### Repodan çektiğimiz bir projeyi requirements deki indirilen paket/versiyonları ile birlikte install etmek için kullanılacak komut ->
```py
- python -m venv env
- ./env/Scripts/activate 
- pip install -r requirements.txt
```

- .gitignore dosyalasını oluştur. 
(Terminalden 
```powershell
cat > .gitignore "yapıştır"
```
)

- Add "rest_framework", your INSTALLED_APPS setting -> 

settings.py ->

```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # 3rd_party_packages
    'rest_framework',
    # my_apps
]
```

```powershell
- python manage.py migrate
- python manage.py createsuperuser 
- python manage.py runserver 
```


### Redoc
- API için
- G2A nın dışarıdan erişilebilir public API servisi. Bu da dokümanı. Bu servisi kullanacaksan, buradaki prosedürü izle.  
https://www.g2a.com/integration-api/documentation/import/v3/


### Swagger
- Dokümantasyon için kullanılır, backend de oluşturduğumuz endpointlerin daha doğrusu API nin dokümantasyonu. Aynı zamanda bir API test ortamı da sağlar.
- Swagger, 2010 yılında bir girişim tarafından başlatılan açık kaynaklı bir projedir. Amaç, bir framework uygulamaktır.kod ile senkronizasyonu korurken, geliştiricilerin API'leri belgelemesine ve tasarlamasına olanak sağlamaktır.
- Bir API geliştirmek, düzenli ve anlaşılır dokümantasyon gerektirir.
- API'leri Django rest frameworküyle belgelemek ve tasarlamak için gerçek oluşturan drf-yasg kullanacağız.
- Bir Django Rest Framework API'sinden Swagger/Open-API 2.0 belirtimleri. belgeler burada bulabilirsin

- Biz drf-yasg kullanacağız. Özelliği; Swagger ile birlikte Redoc (Read the Docs) da oluşturuyor. Tek bir modül ile hem dokümantasyon tarafını hem de swagger tarafını halledeceğiz.
- drf-yasg -> django rest_framework yet another swagger generator
- Django REST Swagger kullanırsak sadece swagger kuruluyor.

#### Swagger -> Document + Test (swagger->ortam, redoc->dokuman)
  - çok kullanılan bir tool, yazdığımız backend api, bunu frontend de bizim takım arkadaşlarımız da kullanabilir, veya dışarıya da servis edebiliriz. Bunun için yani servisin nasıl kullanılacağına dair bir klavuz hazırlanması gerekir.
  - end pointler için doküman oluşturur
  - swagger->ortam, redoc->document
  - Nasıl ekleniyor? ->
    - pip install drf-yasg şeklinde install ettikten sonra, drf_yasg ile third party package ile ekledik,
    - main urls.py da schema_view ve endpointlerini ekledik.

#### Swagger installation

https://drf-yasg.readthedocs.io/en/stable/readme.html#installation

```powershell
- pip install drf-yasg
- pip freeze > requirements.txt
```

- add drf-yasg to INSTALLED_APPS -> 'drf_yasg'
- Ayrıca 'django.contrib.staticfiles', ın INSTALLED_APPS de ekli olması gerekiyor.
```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # 3rd_party_packages
    'rest_framework',
    'drf_yasg',
    # my_apps
]
```

- swagger ve redoc için core/urls.py da path lerimizi yazıyoruz, swaggera permission ayarı da yapılabilir, mesela kullanıcı girişi yapanlar erişebilsin. Şimdilik herkes erişebilir diyoruz.
- Başlık, version, açıklama, email adres kısımlarını dolduruyoruz.

core/urls.py ->

```py
# -----------------------------------------------
# Swagger + Redoc
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Flight API",
      default_version='v1',
      description="Flight API Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="umitarat8098@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

```powershell
- py manage.py runserver
- py manage.py migrate 
```

- http://127.0.0.1:8000/swagger.json
- http://127.0.0.1:8000/swagger.yaml


- swagger ı kurduk, urls.py daki ayarlarını da yaptık, http://127.0.0.1:8000/swagger/  endpointine istek attığımızda swagger ana sayfasını gördük.


### Debug Toolbar

#### Debug_Toolbar -> Documentation 
- Development aşamasında projemizi geliştirirken bize ekstra kabiliyetler kazandırıyor.
- Nasıl ekleniyor? ->
    - pip install django-debug-toolbar şeklinde install ettikten sonra, drf_toolbar ile third party package ile ekledik, daha sonra dev settings ayarlarına aldık.
    - sonra MIDDLEWARE e en üst kısma "debug_toolbar.middleware.DebugToolbarMiddleware" ekledik, daha sonra development settings ayarlarına aldık.
    - sonra INTERNAL_IPS a da ayarını ekledik, daha sonra development settings ayarlarına aldık.
    - urls.py da bir de debug_toolbar ın   path('__debug__/', include('debug_toolbar.urls')),     şeklinde bir endpointi var, onu ekliyoruz.
    - En son migrate komutunu çalıştırdık.


- The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content
  https://django-debug-toolbar.readthedocs.io/en/latest/
(Django Hata Ayıklama Araç Çubuğu, çeşitli hata ayıklama bilgilerini görüntüleyen yapılandırılabilir bir panel kümesidir. geçerli istek/yanıt ve tıklandığında panel içeriği hakkında daha fazla ayrıntı görüntüler)
- Arka planda dönen işin teknik detaylarını bu debug tool bar sayesinde inceleyebiliyoruz.

#### Install Debug Toolbar

- Install the package

```powershell
- pip install django-debug-toolbar
- pip freeze > requirements.txt
```

- Bizden settings.py' da INSTALLED_APPS' de 
  'django.contrib.staticfiles', 
  ve 
  STATIC_URL = "static/" 
  olmasını istiyor.

- Add "debug_toolbar" to your INSTALLED_APPS setting -> "debug_toolbar"

settings.py ->

```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # 3rd party packages
    # ....
    'debug_toolbar',
]
```

- Add django-debug-toolbar’s URLs to your project’s URLconf
 
urls.py ->
```py
from django.urls import path, include

urlpatterns += [ 
    # ... 
    path('__debug__/', include('debug_toolbar.urls')), # django-debug-toolbar 
] 
```

- Add the middleware to the top (en üste):

settings.py ->

```py
MIDDLEWARE = [ 
    "debug_toolbar.middleware.DebugToolbarMiddleware", 
    # ... 
] 
```

- Add configuration of internal IPs to "settings.py":

settings.py ->

```py
# DebugToolBar
INTERNAL_IPS = [ 
    "127.0.0.1", 
]
```

- test edelim çalışacak mı?

```powershell
- py manage.py runserver
```

- çalıştı,   http://127.0.0.1:8000/   endpointine istek atınca gelen sayfanın sağ tarafında bir tool DjDT açılıyor.

  
### Seperate Dev and Prod Settings (Development ve Product ayarlarını ayırma)

- Şu ana kadar yaptığımız projelerde tüm projede geçerli olan ayarları settings.py altında topluyorduk. Ancak ideal bir ortamda çok tavsiye edilen bir durum değil. 
- Projenin bulunduğu safhaya göre settings.py ayarları değişeceği için, her ortam için ayrı bir settings.py oluşturulur. 
- Dokümanda görüldüğü gibi bir structure oluşturup, 

```text
settings/
    |- __init__.py
    |- base.py
    |- ci.py
    |- local.py
    |- staging.py
    |- production.py
    |- qa.py
```

    Yukarıdaki örnekteki gibi tek bir yerde hepsinin toplanmasından sa ayrı ayrı dosyalar oluşturup, mesela tüm projede geçerli olan ortak ayarları base.py içerisine almış, ci->Continuous integrations, qa->test gibi setting.py ı parçalara ayırıyoruz.
    
    Biz şuanda temel olarak hemen hemen her projede olan developer ve produc ortamını birbirinden ayıracağız.

- Bir modül'ü package'a çevirmek için içine boş bile olsa "__init__.py " dosyası oluşturmak yeterli. 

- core klasörü içerisine settings klasörü create et. Bu şu anda basit bir klasör. Bunu modüler bir yapıya çavirmemiz için  içerisine boş bile olsa "__init__.py" dosyası oluşturuyoruz. Artık bu settings klasörü basit bir klasör değil, bir modül/package oldu. Yani core içerisindeki wsgi içinde, "core.settings" çağırdığı zaman artık bizim settings klasörümüz çağrılabilir oldu.
- wsgi'ın settings'i çağırması demek aslında "__init__.py" 'ı çalıştırması demektir. Burada da development.py içeriğini import edersek, development içindeki settings ayarlarını çalıştır demektir bu.
  - __init__.py  # burasının bir python modül/package olduğunu gösterir. Bu sayede wsgi.py içerisinde, settings için bakılacak modül/package olarak burayı kullan diye belirtiyoruz.
  - base.py   
  - development.py   
  - production.py   


- core/settings
  - __init__.py
  - base.py 
  - development.py 
  - production.py    

- core içerisindeki settings.py içeriğini, yeni oluşturulan settings/base.py içerisine kopyalıyoruz.

- core/settings/__init__.py dosyasının içerisinde base.py ın içeriğini import ediyoruz;

core/settings/__init__.py
```py
from .base import *
```

- Normalde bizim settings ayarlarımız core klasörü içerisindeydi. Artık settings ayarlarımız core/settings/base.py'a yani bir alt klasöre taşındı. Bu yüzden settings ayarları içerisinde BASE_DIR ayarında bir değişiklik yapmamız, bir "parrent" daha eklememiz gerekiyor. Yoksa core klasörü altında da bir db.sqlite3 oluşturur. Bu da istenmeyen bir durumdur.

core/settings/base.py
```py
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```

- Artık core/settings.py dosyası silinebilir.

- Şimdi artık başlangıçta settings.py daki ayarlarımızı core/settings/ içerisinde 
  - base.py, 
  - development.py, 
  - production.py 
olarak  ayırmaya başlıyoruz, ->

- .env create edip, içeriğini yazıyoruz;

- core/settings/base.py daki SECRET_KEY 'i config ile .env ye ekleyip, gizliyoruz.

core/settings/base.py
```py
from decouple import config
SECRET_KEY = config('SECRET_KEY')
```

.env
```py
SECRET_KEY =django-insecure-&2_9wl^*c1v&z-x0g121-qceca2nm&tys+=a_!$9(6x28vech&
```


##### core/settings/development.py settings ayarları ->
development.py
```py
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    # Extras for Debug
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# DebugToolBar
INTERNAL_IPS = [
    "127.0.0.1", 
]

```


##### core/settings/production.py settings ayarları ->
production.py
```py
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    ]

INSTALLED_APPS += []

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Şimdilik sqlite3 kalsın, birazdan postgresql'e geçicez.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

```


##### core/settings/base.py settings ayarları ->
base.py
```py
"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
## DEBUG = True

## ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd_party_packages
    'rest_framework',
    'drf_yasg',
    ## 'debug_toolbar',
    # my_apps
]

MIDDLEWARE = [
    # Extras for Debug
    ## "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

## DATABASES = {
##     'default': {
##         'ENGINE': 'django.db.backends.sqlite3',
##         'NAME': BASE_DIR / 'db.sqlite3',
##     }
## }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

## AUTH_PASSWORD_VALIDATORS = [
##     {
##         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
##     },
##     {
##         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
##     },
##     {
##         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
##     },
##     {
##         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
##     },
## ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / STATIC_URL
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / MEDIA_URL

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DebugToolBar
## INTERNAL_IPS = [ 
##     "127.0.0.1", 
## ]

```


##### core/settings/__init__.py settings ayarları ->
__init__.py
```py
from decouple import config

ENVIRONMENT = config('ENV')

if ENVIRONMENT == 'development':
    from .development import *
else:
    from .production import *
```


##### .env ayarları ->
.env
```py
ENV = development

SECRET_KEY = django-insecure-0clw50l%vdp7jejgu6vlnjmx$s#z8-srm+__s7ggkw!i94z8+x

```



### Logging

#### Logger -> işlem geçmişimizi tutmaya yarayan kullanışlı bir tool.
- Bu bir şablon şeklinde, tekrardan yazmıyoruz, bu şekilde kullanıyoruz. 
  - En alttan başlıyoruz bakmaya,  
  - loggers da handlers kısmında loglarımızı hem console a yazdır, hem de file oluştur demişiz.
  
  - level kısmına INFO demişiz, hangi level de tutabileceğini belirleyebiliyoruz.
  ( DEBUG: Low level system information for debugging purposes
    INFO: General system information
    WARNING: Information describing a minor problem that has occurred.
    ERROR: Information describing a major problem that has occurred.
    CRITICAL: Information describing a critical problem that has occurred.)

  - belirttiğimiz console ve file ayarlarını da hemen üstte handlers ta configüre ediyoruz, console a yazarken ki ayarlar, file a yazarkenki ayarlar.. Dikkat edilmesi gereken formatter kısmı -> 
    - console da standart, 
    - file da verbose demişiz.
  
  - formatter a da bir yukarıda bakıyoruz, standart, verbose, simple ile yani logların hangi formatta nasıl tutulacağını burada belirliyoruz.
  - belirlediğimiz formatları aşağıda handlers kısmında seçebiliyoruz, handlers ları da bir alttaki loggers kısımda seçebiliyoruz, ikisini de seçmişiz ayrıca  logger seviyesini de level ile seçebiliyoruz.(level ı config ile .env ye aktarabiliriz. Buradan env ortamını değiştirebildiğimiz gibi debug level ını da değiştirebiliriz.)

https://docs.djangoproject.com/en/4.0/topics/logging/#logging

- logging işlemi restframework ile beraber geldiği için ekstra bir modüle ihtiyacımız yok. Sadece ayarlarını belirtiyoruz. 

- Python programcıları, kodlarında hızlı ve kullanışlı bir hata ayıklama aracı olarak genellikle print() öğesini kullanır. 
- logging framework (günlük kaydı çerçevesi) kullanmak  bundan biraz daha fazla çaba gerektirir, ancak çok daha zarif ve esnektir. 
- Günlüğe kaydetme, hata ayıklama için yararlı olmanın yanı sıra uygulamanızın durumu ve sağlığı hakkında size daha fazla - ve daha iyi yapılandırılmış - bilgi de sağlayabilir.
- Django, sistem günlük kaydı gerçekleştirmek için Python'un yerleşik günlük modülünü kullanır ve genişletir. 
- Bu modül Python'un kendi belgelerinde ayrıntılı olarak ele alınmıştır; bu bölüm hızlı bir genel bakış sunar.

- "disable_existing_loggers": True -> mevcut log ayarlarını devre dışı bırak ve aşağıdakileri kullan.
  
- Dokümandaki LOGGING kodunu alıp core/settings/development.py da en sona ekliyoruz.

development.py
```py
# LOGGING
# https://docs.djangoproject.com/en/4.0/topics/logging/#logging
'''
    DEBUG: Hata ayıklama amaçlı düşük seviyeli sistem bilgisi.
    INFO: Genel sistem bilgisi.
    WARNING: Küçük çaplı hataların bilgisi.
    ERROR: Büyük çalplı hataların bilgisi.
    CRITICAL: Kritik hataların bilgisi.
'''
LOGGING = { 
    "version": 1, 
    # is set to True then all loggers from the default configuration will be disabled. 
    "disable_existing_loggers": True, 
    # Formatters describe the exact format of that text of a log record.  
    "formatters": { 
        "standard": { 
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s" 
        }, 
        'verbose': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        }, 
        'simple': { 
            'format': '{levelname} {message}', 
            'style': '{', 
        }, 
    }, 
    # The handler is the engine that determines what happens to each message in a logger. 
    # It describes a particular logging behavior, such as writing a message to the screen,  
    # to a file, or to a network socket. 
    "handlers": { 
        "console": { 
            "class": "logging.StreamHandler", 
            "formatter": "standard", 
            "level": "INFO", 
            "stream": "ext://sys.stdout", 
            }, 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "verbose", 
            'filename': './debug.log', 
            'level': 'INFO', 
        }, 
    }, 
    # A logger is the entry point into the logging system. 
    "loggers": { 
        "django": { 
            "handlers": ["console", 'file'], 
            # log level describes the severity of the messages that the logger will handle.  
            # "level": config("DJANGO_LOG_LEVEL", "INFO"), # .env ye alıyoruz.
            "level": config("DJANGO_LOG_LEVEL"), 
            'propagate': True, 
            # If False, this means that log messages written to django.request  
            # will not be handled by the django logger. 
        }, 
    }, 
} 
```

NOT: import datetime yapıp, 'filename': './debug_20320520.log', -> bu bilgiyi (2023 05 20) datetime dan çekersiniz, her gün için ayrı log yazar. Normalde tek dosya şişirilmez. Ama bazen de tek dosyada da kaydedilirler.

- Logging ayarlarına baktığımızda baktığımızda formatters, handlers, loggers bölümleri var. linkteki dokümantasyonda mevcut.
  https://docs.djangoproject.com/en/4.0/topics/logging/#logging

- "formatters" -> Bir şablon ayarlıyoruz. standart şablonu, verbose şablonu, simple şablonu. Bu şablonlarda hangi bilgiler olacak, hangi stilde olacak (verbose ve simple da '{' style ında olsun denmiş.) onları belirtiyoruz. Template yapıyoruz yani.
- "handlers" -> yakalama ortamı.

- loggers kısmının;
  - level kısmında -> Hangi seviyede log tutacak isek onu belirtiyoruz -> INFO (DEBUG, INFO, WARNING, ERROR, CRITICAL) (Minimum ayarı belirtiyoruz. Mesela Info seçili ise, INFO dan daha düşük olan DEBUG lar gösterilmeyecek. INFO ve üzeri gösterilecek/kaydedilecek.)
  
  - handlers (topluyor, tutuyor) kısmında -> console, file belirtilmiş. Bunlar da hemen üstte detayları var;
        console; stream çıktıyı düzenli bir akış ile terminale console a veriyor.
            level; INFO
            formatter; hemen biraz üstte standart, verbose, simple olarak belirtilmiş olanlardan standart seçili.
        file; bulunduğu yerdeki ./debug.log isimli bir dosyaya kaydediyor.
            level; INFO
            formatter; hemen biraz üstte belirtilmiş olanlardan verbose seçili.


- level ile -> neleri loglayacak, bunu belirtiyoruz, 
- formatter ile -> loglanan şeylerin ne kadar detayını alacak bunu belirtiyoruz, 
  
- çalıştıryoruz; 
- debug.log isimli bir dosya oluşturulmuş olduğunu ve logging de belirttiğimiz kayıtların olduğunu gördük.

- log işlemi yapıyorsa, her yaptığımız işlemde özellikle INFO belirttiysek, backend de gerçekleşen her işlemi bir yere yazması lazım. Eğer WARNING yazarsak, dosyaya sadece WARNING ve üzeri bilgilerileri kaydeder. vb.


- "formatters" , "handlers" ,  "loggers" diye yapılarımız var.

- hangi seviyede tutacağım? -> "level": config("DJANGO_LOG_LEVEL", "INFO"),

- neleri tutacağım/handle edeceğim? -> "handlers": ["console", 'file'],
  
- handle ediyorsam nerede saklayacağım? -> 'filename': './debug.log',

- formatter a da bir yukarıda bakıyoruz, standart, verbose, simple ile yani logların hangi formatta nasıl tutulacağını burada belirliyoruz.
  - belirlediğimiz formatları aşağıda handlers kısmında seçebiliyoruz, handlers ları da bir alttaki loggers kısımda seçebiliyoruz, ikisini de seçmişiz ayrıca  logger seviyesini de level ile seçebiliyoruz.(level ı config ile .env ye aktarabiliriz. Buradan env ortamını değiştirebildiğimiz gibi log level ını da değiştirebiliriz.)

- development.py' a eklediğimiz LOGGING kodunu core/settings/production.py 'a da en sona ekliyoruz. Ardından production için ayarları yapalım. development ve production kısımlarında ayrı loglama yapacağız. production için "loggers" kısmında istediğimiz ayarları yapıyoruz. (mesela "handlers" dan "console" u kaldırıyoruz.)

production.py
```py
# LOGGING
# https://docs.djangoproject.com/en/4.0/topics/logging/#logging
'''
    DEBUG: Hata ayıklama amaçlı düşük seviyeli sistem bilgisi.
    INFO: Genel sistem bilgisi.
    WARNING: Küçük çaplı hataların bilgisi.
    ERROR: Büyük çalplı hataların bilgisi.
    CRITICAL: Kritik hataların bilgisi.
'''
LOGGING = { 
    "version": 1, 
    # is set to True then all loggers from the default configuration will be disabled. 
    "disable_existing_loggers": True, 
    # Formatters describe the exact format of that text of a log record.  
    "formatters": { 
        "standard": { 
            "format": "[%(levelname)s] %(asctime)s %(name)s: %(message)s" 
        }, 
        'verbose': { 
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}', 
            'style': '{', 
        }, 
        'simple': { 
            'format': '{levelname} {message}', 
            'style': '{', 
        }, 
    }, 
    # The handler is the engine that determines what happens to each message in a logger. 
    # It describes a particular logging behavior, such as writing a message to the screen,  
    # to a file, or to a network socket. 
    "handlers": { 
        "console": { 
            "class": "logging.StreamHandler", 
            "formatter": "standard", 
            "level": "INFO", 
            "stream": "ext://sys.stdout", 
            }, 
        'file': { 
            'class': 'logging.FileHandler', 
            "formatter": "verbose", 
            'filename': './debug.log', 
            'level': 'INFO', 
        }, 
    }, 
    # A logger is the entry point into the logging system. 
    "loggers": { 
        "django": { 
            "handlers": ['file'], 
            # log level describes the severity of the messages that the logger will handle.  
            "level": config("DJANGO_LOG_LEVEL", "WARNING"), 
            'propagate': True, 
            # If False, this means that log messages written to django.request  
            # will not be handled by the django logger. 
        }, 
    }, 
}
```


- logların level ını .env de tutacağız. Kurarken level olarak 'INFO' belirledik tamam, ama bu ayarı .env de tutarak oradan değiştireceğiz.
    "level": config("DJANGO_LOG_LEVEL") yazıp,
    .env de de -> 
        DJANGO_LOG_LEVEL=INFO  olarak kaydederek log level seçeneğini .env ye taşımış oluruz.

- "level": config("DJANGO_LOG_LEVEL", "INFO"), # .env ye alıyoruz. Eğer .env de DJANGO_LOG_LEVEL belirtmez isek, bu sefer parantez içindeki default değerleri kullanıyor.
  "level": config("DJANGO_LOG_LEVEL"), 

.env
```py
ENV=development
# ENV = production

SECRET_KEY=django-insecure-0clw50l%vdp7jejgu6vlnjmx$s#z8-srm+__s7ggkw!i94z8+x

DJANGO_LOG_LEVEL=INFO
```

- Herhangi bir hatada veya server ın nasıl çalıştığını izleyebilmek için, bu logları tutuyoruz. Bu loglardaki trafiği takip ederek bazı kararlar alabiliyoruz. Mesela bir endpoint e bir çok istek var, demekki birisi birşeyler deniyor.
- Burada önemli olan husus logları hangi seviyede tutacağız?, neleri handle edeceğiz?, handle ediyorsak nerede saklayacağız? bunları belirtiyoruz.


### PostgreSQL setup

- pgAdmin de bir db oluşturup, 
- oluşturduğumuz db ayarlarını production.py kısmına yazıyoruz,
- gizlenmesi gereken verileri config ile .env ye aktarıyoruz.

- base(ortak ayarlar), dev(development ayarları), prod(production ayarları)


- pgAdmin açıp yeni bir db oluşturalım;
- Python'un Postgres ile çalışmasını sağlamak için “psycopg2” modülünü kurmanız gerekecek.

```powershell
- pip install psycopg2
- pip install psycopg2-binary # for macOS
- pip freeze > requirements.txt
```


- .env dosyasına gidip;
```py
SQL_DATABASE=Flight_App_API_CH-13
SQL_USER=postgres
SQL_PASSWORD=postgres 
SQL_HOST=localhost 
SQL_PORT=5432
```

- production.py daki settings ayarlarına gidip, dbsqlite3 olan kısmı kendi postgresql db ayarlarımızla değiştiriyoruz.
production.py
```py
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Şimdilik sqlite3 kalsın, birazdan postgresql'e geçicez.

DATABASES = { 
    "default": { 
        "ENGINE": "django.db.backends.postgresql_psycopg2", 
        "NAME": config("SQL_DATABASE"), 
        "USER": config("SQL_USER"), 
        "PASSWORD": config("SQL_PASSWORD"), 
        "HOST": config("SQL_HOST"), 
        "PORT": config("SQL_PORT"), 
        "ATOMIC_REQUESTS": True,
    }
} 
```
NOT: "ATOMIC_REQUESTS": True, -> django birden fazla sql kodu gönderirse eğer, bütün kodları bekle, kodları hepsini birden çalıştır. Mesela 10 ayrı sql kodu geldi ise 10 ayrı işlem yapma, tek işlemde 10 kodu da çalıştır.

- .env'ye gidip, ENV değişkenini production olarak değiştirelim.

```powershell
- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver
```

##### CSSler gelmez ise

- Eğer admin paneli açtığımızda Css ler gelmez ise! ->
- Niçin böyle birşey olur? -> Biz artık canlıya çıktık, artık django development ortamında olmadığımızı biliyor, dosyaları olması gereken yerde istiyor.
- Tüm static dosyalarını olması gereken yer olan root directory deki static folder ının içerisinde toplama komutu olan "py manage.py collectstatic" çalıştırarark, topluyoruz.
- Bunu da zaten settings.py da (base.py) belirtmiştik.

```powershell
- python manage.py collectstatic
```

- Eğer yine çalışmaz ise -> Aşağıdaki yöntem denenebilir.

- Debug=False yani production/canlı ortamda güvenli bağlantı istiyor (https gibi). Ancak biz şuan development yaparken localhost kullanırken https (SSL sertifikası) kullanamıyoruz. Bu yüzden CSS gibi static dosyalarını görüntülemiyor. Django güvenli bir sunucu istiyor. Onu bile düşünmüş. 

- Bu nedenle lochalhost ta production/canlı ortamda çalıştırabilmek için  "python manage.py runserver --insecure" ile çalıştırmak gerekiyor. Yani "güvenliği lütfen kafana takmadan çalış" gibi birşey... Güvenli olmayan bir ortamda da çalışabilirsin! Yoksa biz bir hata yapmadık yani.

```py
- python manage.py runserver --insecure
```


NOT: 
- STATIC_ROOT = BASE_DIR / STATIC_URL   ayarı ile tek bir yer belirleyebiliyoruz.

- Ancak django static dosyalarını farklı farklı yerde saklayabilirsin diyerek şöyle bir ayar getirmiş, onun için farklı farklı yerler de belirtebiliyoruz.
```py
# STATIC_ROOT = BASE_DIR / STATIC_URL
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "var/www/static/",
  ]
```

- Bu şekilde de yazabiliriz. Ayrıca , ile ayırıp farklı bir yer de belirtebiliriz. django hepsine gidip tek tek bakacaktır.
```py
# STATIC_ROOT = BASE_DIR / STATIC_URL
STATICFILES_DIRS = [
    BASE_DIR / STATIC_URL,
    "var/www/static/",
  ]
```

#### Taslak olarak kullanmak;

- Şimdi bunu taslak olarak kullanıp bu taslak üzerine projeler oluşturabiliriz.
- Bunu repomuza push layıp, 
- repomuza pushladık, repoya girdik, settings, template repository seç, -> yeni bir repository dediğimiz zaman yeni oluşturacağımız repoyu bu taslağa alır ve o şekilde oluşturur. Yani bu taslak üzerinden devam edebilirsiniz, tekrar tekrar paket kurmanıza gerek kalmaz.



## TASLAK_V02 - AUTH

```powershell
- echo ENV=development > .env  # > içine şunu yazarak dosya oluştur!
- echo SECRET_KEY=ghjg398434qf2j >> .env  # >> içine şunu yaz mevcut olan dosyanın!
```

### User App oluşturuyoruz Authentication işlemleri için;

```powershell
- py manage.py startapp user
```

- Add users app to INSTALLED_APPS in your django settings.py ->
settings/base.py ->
```py
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # 3rd_party_packages
    'rest_framework',
    'drf_yasg',
    ## 'debug_toolbar',
    # my_apps
    'user',
]
```

- core/urls.py dan oluşturacağımız user/urls.py yönlendirme yapıyoruz,
core/urls.py ->
```py
urlpatterns = [
    path("user/", include("user.urls")),
]
```


- create urls.py in user app

```py
from django.urls import path, include
  
urlpatterns = [ 
]
```


- Ayrıca core/urls.py da url pattern in hemen altına static/media paternlerini ekliyoruz. 
```py
# STATIC/MEDIA:
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



#### User authentication işlemleri (register, login, logout...)->

- 1- login, logout, password change vb. işlemler için dj_res_auth paketini kullanacağız.
- 2- Biz register için kendimiz view,serializer,urls yazacağız,


##### 1- Authentication (login, logout, password_change, password_reset) işlemleri -> 

- Kullanıcı login, logout,
- TokenAuthentication 

- Daha önceki derste login logout işlemlerini rest_framework.authtoken kullanmıştık,  view için obtain_auth_token kullanmıştık,

###### 3rd party package -> dj-rest-auth 

###### login, logout

- Ancak burada login ve logout işlemleri için third party packages lardan biri olan, oldukça yaygın bir şekilde kullanılan django-rest-auth / dj-rest-auth paketini kullanacağız.
  
- registration özelliği de sunuyor fakat allauth paketini de yüklemek gerekiyor. Biz registration ı kendimiz yazacağız.

- Bu paket çok kapsamlı bir paket, çok fazla özellikleri var. Dokümanına gidiyoruz, 
  
  https://dj-rest-auth.readthedocs.io/en/latest/index.html

- registration için allauth paketi kurmamızı istiyor demiştik, biz kurmayıp registration ı kendimiz yazacağız.

- eğer allauth u yüklersek social authentication imkanı da var. neler bunlar? facebook, google, twitter, github, bunlarla nasıl authentication işlemleri yapılacağını buradan inceleyebilirsiniz. 
- biz django-rest-auth paketinin sadece login, logout özelliğini kullanacağız.

- installation ->
- django-rest-auth paketini yüklüyoruz;

```powershell
- pip install dj-rest-auth
- pip freeze > requirements.txt
```

- settings klasörü içindeki settings.py (base.py) da INSTALLED_APPS kısmına "rest_framework.authtoken" paketi ile birlikte "dj_rest_auth" paketini ekliyoruz. 

settings/base.py (settings.py) ->
```py
INSTALLED_APPS = [
    .....
    'rest_framework.authtoken',
    'dj_rest_auth',
]
```

- Ayrıca TokenAuthentication kullanacağımız için base.py da en alt kısma ekliyoruz;
settings/base.py -> 
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 20,
}
```

- Şimdi login, logout için kullanacağımız dj-rest-auth paketimizin pathini users app imizin urls.py ına ekliyoruz.

users/urls.py ->
```py
from django.urls import path, include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
```

- Biz dokümanda belirtilen paketin path ismini uzun bulduk ve auth/ olarak kısaltıyoruz.

- Bu endpoint bize paketin birtakım özelliklerini sunacak.

- Son olarak migrate istiyor db miz için

```powershell
- py manage.py migrate
```

- Browser a gidip endpointimizle (http://localhost:8000/user/auth//) istek attığımızda bize sağladığı endpointleri de görüyoruz;
(
users/ auth/ password/reset/ [name='rest_password_reset']
users/ auth/ password/reset/confirm/ [name='rest_password_reset_confirm']
users/ auth/ login/ [name='rest_login']
users/ auth/ logout/ [name='rest_logout']
users/ auth/ user/ [name='rest_user_details']
users/ auth/ password/change/ [name='rest_password_change']
)

- Biz buradan sadece login ve logout kullanacağız. Paketin özelliklerinden olan  "password/change/", "password/reset/" için frontend ile birlikte yapılması gereken özellikler olduğu için sadece backend kısmı ile gösterildiğinde havada kalabiliyor. 

- paketin dokümanındaki, frontend i react, backend i django ile yazılmış demo projeyi repodan indirip dokümandak adımları izleyerek kurup, bu paket ile yapılmış özellikleri (password reset, password change) inceleyebilirsiniz.
  https://dj-rest-auth.readthedocs.io/en/latest/demo.html

- Burada şimdi login ve logout işlemlerini paketten kullanacağız.

- Paketimizi kurduk, ayarlarını yaptık;
   http://localhost:8000/user/auth/login/ 
  endpointine istek attığımızda, paketin login özelliği olarak bize bir login page sunuyor. 

- Biz zaten admin ile login olmuş olduğumuz için username ve password dolu bir şekilde bize bir form dönüyor, 

- Dokümandan bakıyoruz, API endpoints kısmından,
  https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
  Biz username ve password yazıp form ile POST isteği attımızda bize token dönüyor.

- Ayrıca admin panelden Token tablosunun create edildiğini ve token oluşturulduğunu gördük.

- Şimdi endpointine istek atalım;
  http://127.0.0.1:8000/users/auth/logout/
evet, gelen page de post methodu ile istek attığımızda  Succesfully logged out mesajı ile logout edildiğimizi gördük.
  
- admin panele gidip browser ımızı refresh ettiğimizde logout olduğumuzu görüyoruz. Tekrar login oluyoruz ve Token tablomuzda login olurken oluşturulmuş token ın hala durduğunu görüyoruz. Neden? Çünkü logout yaparken token bilgisinin de gönderilmesi gerekiyor ki, gelen tokena sahip user ı logout yaparken tokenını da Token tablosundan silsin. Eğer modheader ile logout endpointine POST methodu ile istek atarken token verisi de gönderirsek bu sefer user ı logout edince Token tablosundan da tokenı siliyor. Ancak Modheader biraz zahmetli. Bu yüzden endpoint testlerinde Postman kullanıyoruz.
- Normalde biz postmanden istek atsaydık bu token ı silecekti ama browserdan istek attığımız için token ı silmiyor. Deneyelim bakalım postmanden logout için istek atalım; Evet logout/ yapınca token silindi, login/ yapınca token oluştu. Bu yüzden development aşamasında postman kullanıyoruz.

- Artık sadece third party package olan dj-rest-auth paketini yükleyip installation ayarlarını yaparak ve TokenAuthentication kullanarak bize sağladığı endpoint ile login ve logout yapmış olduk. Bizim için login olduğumuzda token üretiyor ve logout olduğumuzda token ı siliyor.

- Şimdi email ile login olmayı deneyelim;
- Normalde default olarak django bizden username ve password ile login olmamızı bekliyor. Ancak bu paketin sağladığı avantajlardan birisi email ve password ile de login olabilmek.
- Test ettik postmanden çalıştı.
- Bu paket sayesinde çok hızlı bir şekilde login ve logout işlemleri yapabiliyoruz.
- Ayrıca pasword change endpointinden de login olmuş olan user ın password ünü değiştirmesini de test ettik çalışıyor.
- Bir de yine bu paket sayesinde auth/user endpointi ile login olmuş user kendi user bilgilerini get/put/patch yapabiliyor. test ettik çalıştı.



###### 2- Authentication register işlemleri -> 

- User register yapısını ise ikiye ayıracağız;
  - 1- Admin user tarafıdan user oluşturulması ve var olan user ların bilgilerinin update edilmesi, 
  - 2- Dışarıdan, userların kendilerinin register olabilmesi. 

1. Kısım registration (Admin user tarafıdan user oluşturulması)->
- Admin kullanıcı, tüm diğer user ları yönetebiliyor, yeni user da create edebiliyor.

- settings.py da global olarak DEFAULT_AUTHENTICATION_CLASSES kısmına TokenAuthentication yazıyoruz,
- Default_Permission_Class -> IsAdminUser tanımlayarak bu sistemde admin olmayan user işlemi yapamaz, yazıyoruz. (Normalde permissions lar views.py da tanımlanır.)
- 
base.py
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication'],
    # 'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAdminUser'],
}
```


###### Sadece admin userlar için registration (create, update, delete) işlemleri;

- user app imizin içinde serializers.py create edip,
- User için ModelSerializer dan inherit ederek bir UserSerializer class ımızı yazmaya başlıyoruz.
- djangonun default/yerleşik User modelimizi kullanacağımız için import ediyoruz.

user/serializer.py
```py 
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = []       
``` 

- Bu yazdığımız serializer' ı kullanacak view imizi de yazalım;
- UserView class ımızı ModelViewSet den inherit ederek yazıyoruz,

user/views.py
```py 
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    User, UserSerializer,
)

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
``` 

- Bu view imizi çalıştıracak endpoint/url imizi yazalım;
- view imizi ModelViewSet den inherit ederek oluşturduğumuz için router yapısı kullanacağız,


user/urls.py
```py
from django.urls import path, include
  
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import UserView

router = DefaultRouter()
router.register('', UserView)

urlpatterns += router.urls
``` 

- Test ediyoruz, http://127.0.0.1:8000/user/  endpointine gidiyoruz.
- Post methodu ile şu veriler ile yeni kullanıcı create ediyoruz, çalıştı.
```json
{
    "username": "user1",
    "password": "use123456"
}
```

- Ancak user1'in password ü şifrelenmemiş bir şekilde db'ye kaydedilmiş olduğunu gördük.

  - password şifrelenmemiş olarak kaydediliyor.
  - password confirmi yapılmıyor.
  - user create edildikten sonra password datası da dönen veri içinde açık olarak görünüyor.

- Bu sorunları serializer ve views de çözebiliriz. Ancak serializer da çözmek best practice.
- Bir userı create/update/delete/list maksatlı kullandığımız view için yazmış olduğumuz serializerın kaynak kodunu (ModelSerializer) incelediğimizde ModelSerializer -> Serializer içinde sanki bu işler için özel olarak override edilmek için hazırlanmış def validate() methodunu görüyoruz. Ayrıca validate işlemi hem create ederken hem de update ederken kullanılıyor. Dolayısıyla buradaki  def validate() methodunu override edersek, yani passwordümü şifrele dersek bizim için yeterli olur.

- Yani serializerda validate() methodunu override ederek; ey django, sen hem create yaparken hem de update yaparken mutlaka sana gönderdiğimiz veriyi bir validasyondan geçiriyorsun, bu veriyi validasyondan geçirirken password ümüzü hem kontrol edip hem de şifrele!

- Önce  validate_password (passwordü validasyondan geçiriyor) ve make_password (passwordü şifreliyor) fonksiyonlarını import edip,
- attrs içinden password ü çekip, validasyondan geçiriyoruz,
- daha sonra update ederken de şifreli hale getiriyoruz. 
- En son super içerisindeki validate attrs ı return ediyoruz.

- password create/update

serializers.py
```py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = [
            # "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
    
    def validate(self, attrs):
        from django.contrib.auth.password_validation import validate_password # doğrulama fonksiyonu
        from django.contrib.auth.hashers import make_password # şifreleme fonksiyonu
        password = attrs['password'] # Password al.
        validate_password(password) # Validation'dan geçir.
        attrs.update(
            {
                'password': make_password(password) # Password şifrele ve güncelle.
            }
        )
        return super().validate(attrs) # Orjinal methodu çalıştır.
```

- Test ediyoruz, http://127.0.0.1:8000/user/2/   endpointine istek atarak, 2 nolu id li user ın verisini çekiyoruz ve passwordünün şifresiz olduğunu görüyoruz.
- Hiç verisine dokunmadan PUT ile update ediyoruz ve artık password verisinin şifrelenmiş olduğunu görüyoruz.

- Ayrıca postmanden de http://127.0.0.1:8000/user/  endpointine, Post methodu ile, 
```json
{
    "username": "user2",
    "password": "use123456"
}
```
datası ile istek attığımızda yeni bir user create edildiğini görüyoruz.

- user register (create/update/delete/list) yapabiliyoruz.


###### password girmeden user datasını güncelleme. ()

- Admin userlar için, normal userların datasını o userın passwordü olmadan güncelleyebilmesi için ->
- password field ını zorunlu alan olmaktan çıkarıp, sadece create ederken kullanılabilen bir alan yapıyoruz.
- validate() methoduna if condition ile attrs dict inin içinden "password" ü al, yoksa False döndür diyerek, aşağısındaki password validation/şifreleme işlemini pass geçerek, userın diğer datalarını update edebiliyoruz.
- dictionary den veriyi almanın iki yolu var; biri attrs.get('password') methodu, diğeri attrs['password'] . Burada if attrs.get('password', False) ile password verisi varsa ver, yoksa False dön. aşağısını çalıştırma. Böylelikle password verisi göndermeden user datasını güncelleyebildik.

user/serializer.py 
```py
 class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        required = False,
        write_only = True,
    )

    class Meta:
        model = User
        exclude = [
            "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
    
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password # doğrulama fonksiyonu
            from django.contrib.auth.hashers import make_password # şifreleme fonksiyonu
            password = attrs['password'] # Password al.
            validate_password(password) # Validation'dan geçir.
            attrs.update(
                {
                    'password': make_password(password) # Password şifrele ve güncelle.
                }
            )
        return super().validate(attrs) # Orjinal methodu çalıştır.
```


###### email fieldını zorunlu ve unique yapılması;

- email field ını baştan tanımlıyoruz,
- zorunlu hale getiriyoruz,
- UniquValidators dan geçiriyoruz,
- 
user/serializer.py 
```py
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )
```

- Test ediyoruz, tarayıcıdan   http://127.0.0.1:8000/user/ endpointine post isteği ile email fieldını doldurmadan user create etmeye çalışıyoruz bize email in zorunlu olduğu hatası dönüyor.
- Artık biz "username" (default unique), "email" (unique), "password" datası ile user create edebiliyoruz.


////////////////////////////////////////
////////////////////////////////////////
- Ancak henüz register ile create edilen user sadece  http://localhost:8000/user/auth/login/   endpointine, Post methodu ile, 
```json
{
    "username": "user2",
    "email": "user2@gmail.com",
    "password": "use123456"
}
```
datası ile istek attığında login olabiliyor.

- Bunu ilerde user register olur olmaz onun için aynı zamanda token create edilsin, ve token verisi ile user verisi de dönecek şekilde ayarlayıp login olmuş bir user haline getireceğiz. 
- Ayrıca şu anda sadece username, email ve password ile register olabiliyor.
- Biz bunu email, password1 ve password2 ile register olabilmesi için ayarlayacağız. 
////////////////////////////////////////
////////////////////////////////////////


- Buraya kadar register işlemlerini sadece adminuser'ın yapabildiği, yeni user create/update/delete işlemi yapabildiği kısmı bitirdik. 
- Bundan sonra diğer tüm kullanıcılar için register/kayıt olabilecekleri bir sistem kurmalıyız. Bunun için de yeni bir view yazıp, permission olarak da herkesin erişebilmesini sağlamalıyız. 

------------


2. Kısım registration (Dışarıdan, userların kendilerinin register olabilmesi)->
- Genel kullanım için, yani dışarıdan, userların kendilerinin register/kayıt olabilmesi. 

###### Genel/Anonymous userlar için registration (sadece create) işlemi;

- Tüm kullanıcıların register olabilmeleri için bir view yazacağız. Bu view imizi de sadece create işlemi (yeni kullanıcı kaydı) için kullanacağımız için Generic views lerden CreateModelMixin 'den inherit ederek yazıyoruz ve permission olarak da local de AllowAny diyerek de bu view i herkesin kullanabilmesini sağlıyoruz. Ayrıca mixin ler tekbaşlarına çalışamayıp, çalışabilmek için başka bir class'a ihtiyaç duydukları için GenericViewSet class ını da import edip inherit ederek argüman olarak yazıyoruz.

user/views.py
```py
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    User, UserSerializer,
)

# ----------------------------------
# UserView -> Full Control for permissions.IsAdminUser
# ----------------------------------
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser] # Default: IsAdminUser settings.py da global olarak belirtildi.


# ----------------------------------
# UserCreateView -> Only CreateUser for permissions.AllowAny
# ----------------------------------
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
```

- Sadece yeni kullanıcı kaydı yapabilen bir view olan CreateModelMixin view inden ve de GenericViewSet ten inherit ederek yazdığımız bu view imizin endpointi olan urls'sini yazıyoruz.
- user/urls.py  a gidip router yapısında (GenericViewSet olduğu için) register ediyoruz. Burada ince bir detay var; 'create' i en üstte register ediyoruz ki çalışabilsin. Yoksa çalışmaz. Neden çalışmaz? 'create',  '' ın altında kalırsa, önce '' ı çalıştıracak, 'create' a hiç sıra gelmeyecek. Ama üste yazarsak, url isteğinde önce eğer varsa 'create' li kısım çalışacak, ama url isteğinde 'create' yoksa normal '' çalışacak. 

user/urls.py
```py
from django.urls import path, include
  
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import UserView, UserCreateView

router = DefaultRouter()
router.register('create', UserCreateView) # permissions.AllowAny
router.register('', UserView) # permissions.IsAdminUser

urlpatterns += router.urls
```

- Test ediyoruz, sadece yeni kullanıcı oluşturmak için genel kullanıma açık yazdığımız view imiz ve url miz çalışıyor. postmanden aşağıdaki veriler ile http://127.0.0.1:8000/user/create/ endpointine post ile istek attığımızda yeni kullanıcı oluşturuyor. Ancak login etmiyor.
```json
{
    "password": "use123456",
    "email": "user7@gmail.com",
    "username": "user7",
}
```

- Kullanıcı register olur olmaz login olmuş olsun -> 
- Bunun için de UserCreateView inin create() methodunu override ediyoruz;
- view imizi inherit ettiğimiz CreateModelMixin içerisindeki create() methodunu kopyalayıp, view imize yapıştırıyoruz, serializer ın kaydedildiği kısma müdahale edip orada, serializer kaydedilince yani yeni bir user oluşturunca  git Token tablosunda bu kullanıcıya bir token oluştur, bu token ı da serializer.data içerisine yaz ve çıktıda göster.

user/views.py
```py
class UserCreateView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # <--- User.save() & Token.create() --->
        user = serializer.save()
        data = serializer.data
        token = Token.objects.create(user=user)
        data['key'] = token.key
        # </--->
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

```

- Test ediyoruz, postmanden aşağıdaki veriler ile http://127.0.0.1:8000/user/create/ endpointine post ile istek attığımızda yeni kullanıcı oluşturuyor, dönüş datasına da token ı ekleyerek, oluşturduğu kullanıcıyı login ediyor.
```json
{
    "password": "use123456",
    "email": "user7@gmail.com",
    "username": "user7",
}
```
Dönüş ->
```json
{
    "id": 20,
    "email": "user8@gmail.com",
    "is_superuser": false,
    "username": "user8",
    "first_name": "",
    "last_name": "",
    "is_staff": false,
    "is_active": false,
    "key": "34e92de4574623ef0d56f530f87abc1400fb97c2"
}
```

- Eğer adminuser tarafından bir user create/register edilecekse -> create edilir edilmez user ın login olmasına gerek yok.
- Ancak user kendisi register olacak ise register olur olmaz login olması daha iyi olur.

- Test ediyoruz, evet eğer user admin tarafından create edilirse  http://127.0.0.1:8000/user/  aynı anda token create edilmiyor/dönmüyor (login edilmiyor), Ancak user kendisi register olursa  http://127.0.0.1:8000/user/create/   aynı anda token create ediliyor/dönüyor (login ediliyor). 


----------------

- Şu anda user ister adminuser isterse de user ın kendisi tarafından create/register olmuş olsun iki türlü de login endpointine username/email/password ile login olduğunda sadece token key dönüyor. 

- Ancak biz istiyoruz ki user kendisi register olduğunda dönen datanın içerisinde user bilgilerinin de token key ile birlikte dönmesini sağlayalım. Kullanıcı datasını çekmek için tekrardan istek atmak zorunda olmasın.

- token, token tablosunda kayıtlı, biz db den veri çekip frontend e aktarırken serializer dan geçirip aktarıyoruz. Aynı bunun gibi token tablosundan token ı alıp frontend e aktarırken de arka tarafta bir serializer dan (TokenSerializer) geçiriliyor.

- O TokenSerializer ına ulaşıp içine user datasını da koyacağız.
  https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#login-serializer 

- LOGIN_SERIALIZER biz views.LoginView kısmında da customize edebilirdik ama biz LoginSerializer ını customize edeceğiz.

- serializers.py a gidiyoruz;

- dj_rest_auth.serializers  dan TokenSerializer ı import ediyoruz,
    from dj_rest_auth.serializers import TokenSerializer

- source koduna gidiyoruz, çok basit olarak class Meta sında TokenModel kullanarak sadece key field ını dönüyor. işte biz buraya user datasını da koymak istiyoruz.

- Bu TokenSeriaizer class ını alıp, inherit ederek kendimiz bir class yazacağız. İnheritance neydi tüm özellikleri ile beraber aynısını almış olduk. Bunun üzerine kendimize göre bir iki değişiklik yapacağız.
  class UserTokenSerializer(TokenSerializer):

- Bu TokenSerializer dan inherit ederek oluşturduğumuz UserTokenSerializer da, TokenSerializer'ın class Meta sını da inherit etmek isitiyoruz. Çünkü içerisinde TokenModel kullanarak sadece 'key' fieldını dönüyor. Biz tekrardan TokenModel import etmeyelim diye class Meta(TokenSerializer.Meta) -> class Meta sını almak için bu yapıyı kullanmamız gerekiyor. class Meta sını da inherit edip, 'key' fieldının yanına 'user' fieldımızı ekliyoruz.
  class Meta(TokenSerializer.Meta):

- Şimdi fields ını belirliyoruz. Bu fields içine user da koyacağız. Ancak bize user'ın id sini dönecektir. Biz user field'ını yeniden tanımlayarak;
    user = UserSerializer()
user field'ına UserSerializer dan gelen datayı koyuyoruz.       

user/serializer.py 
```py
class UserSerializer(serializers.ModelSerializer):
    ...
    ....

# ------- TokenSerializer -------
# ---- Kullanıcı login olurken token key ile birlikte user datası da dönsün! ----
from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(TokenSerializer):
    user = UserSerializer()
    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")
```

- Normal TokenSerializer ı aldık, bunu inherit ederek yeni bir serializer (UserTokenSerializer) oluşturduk, TokenSerializer sadece "key" dönüyordu. Biz bunun class metasını tekrardan çektik ve "key" in yanına "user" koyduk . Ancak user field ımız yoktu, Bunun için User modelinden bir serializer yazdık ve onu user a tanımladık.

- Ancak biz şimdi TokenSerializer ı buraya çekip inherit ederek yeni bir serializer yazdık ama, pakete bu bizim yazdığımız CustomTokenSerializer serializer ı kullan dememiz lazım, yoksa o hala kendi TokenSerializer serializer ını kullanıyor olacaktır. Pakete buraya bir CustomTokenSerializer serializer yazdım, bunu kullan dememiz lazım. Bunu da ;
- settings/base.py içerisinde belirtiyoruz. Yani TOKEN_SERIALIZER olarak users app imin içindeki serializers içindeki CustomTokenSerializer ı kullan diyoruz. Bu da zaten paketin sağladığı serializer ı inherit ederek oluşturduğumuz bir serializer.

```py
REST_AUTH = {
    'TOKEN_SERIALIZER': 'user.serializers.UserTokenSerializer',
}
```

- Test ediyoruz, postmanden aşağıdaki veriler ile http://localhost:8000/user/auth/login/ endpointine post ile istek attığımızda, token key verisi ile user verisi dönüyor. login ediyor.
```json
{
    "username": "user4",
    "email": "user4@gmail.com",
    "password": "use123456"
}
```
Dönüş ->
```json
{
    "key": "45c8c7bcf3ec8baa63e38a71f39034b727f71369",
    "user": {
        "id": 40,
        "email": "user4@gmail.com",
        "is_superuser": false,
        "username": "user4",
        "first_name": "",
        "last_name": "",
        "is_staff": false,
        "is_active": true
    }
}
```

----------------

- Son durum -> User sistemi;
  - Admin, kullanıcı ekleme, kullanıcıların verilerini update, silme, güncelleme yapabiliyor.
    - Dikkat, eğer admin kullanıcı bir user create ederken, o create edilen kullanıcıların active olması sağlanmalı, yoksa login olamıyorlar!
    - Eğer adminuser bir user create ederse otomatik olarak user login edilmiyor. Gerek yok çünkü.
  
  - Normal user lar kendileri register olabiliyorlar, register olur olmaz da login olabiliyorlar.
   
  - dj_rest_auth ile login, logout, password...
  
  - Kullanıcı login olduğunda, kullanıcıya token ile birlikte kullanıcı verisi de dönüyor.



## TASLAK_V03 - STOCK_APP

- LOGGING kısmında config ile .env den çekilen level değişkeni çalışmıyor.
- Flight_App projesinin taslakları üzerinden devam ediyoruz;
- Frontend için corsheaders install edip base/settings'e ekliyoruz. Cors headers ayarlarını base/settings de yapıyoruz.
- djangofilter install edip base/settings'ekliyoruz.
- global olarak tanımlanmış permissions ve paginations ayarlarını yoruma alıyoruz.
- core/urls.py da "user" olan url path'ini account olarak değiştiriyoruz.

#### django-cors-headers Ayarları ->
- Bir django projesine dışarıdan bağlanabilmek için buna dair izinler vermemiz gerekiyor. Bunu da django-cors-headers ile yapıyoruz. Burada bir doküman var, buna bakılabilir. 
  https://dzone.com/articles/how-to-fix-django-cors-error

cors-headers ın kendi dokümanı burada ; github hesabından da incelenebilir.
https://pypi.org/project/django-cors-headers/


https://pypi.org/project/django-cors-headers/

- Python ile yazılmış backendin, react ile yazılmış frontend ile konuşmasını sağlayacak paket ve ayarları ->

```bash
- pip install django-cors-headers
- pip freeze > requirements.txt
```

- settings.py da INSTALLED_APPS e ekle, MIDDLEWARE' de en üst kısma ekle, CORS_ALLOWED_ORIGINS (Kabaca izin verilen server ların bir listesi)
  - Burada 3 seçenek var;
    - CORS_ALLOWED_ORIGINS -> İzin verilen serverların listesi,
    - CORS_ALLOWED_ORIGIN_REGEXES -> Belli regex ler ile izin verme,
    - CORS_ALLOW_ALL_ORIGINS -> Tüm serverlara izin ver, (Eğitim amaçlı kullanılır, Normalde izin verilen serverların listesi yazılacak yukarıdakine. Örnekleri dokümanda var.)
  - CORS_ALLOW_METHODS -> Frontendin göndereceği requestleri sınırlayabiliriz. Belli methodları kısıtlama, mesela buraya sadece GET yazarsak eğer karşı taraftaki server sadece GET request gönderebilir.

core/settings/base.py
```py
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...,
    "django.middleware.common.CommonMiddleware",
    ...,
]
```


- Aşağıdaki üç ayardan birini yapılandırmamız gerekiyor;
    CORS_ALLOWED_ORIGINS
    CORS_ALLOWED_ORIGIN_REGEXES
    CORS_ALLOW_ALL_ORIGINS

- Daha sonra CORS_ALLOWED_...  ile izinleri düzenliyoruz;
  - Yukarıdaki opsiyonları inceledikten sonra biz bu projemizde CORS_ALLOW_ALL_ORIGINS=True (tüm istek urllerine cevap ver.) seçeneğini kullanıyoruz.

- İsteklerin methodlarını da belirlememiz/tanımlamamız gerekiyor.

core/settings/base.py
```py

CORS_ALLOW_ALL_ORIGINS=True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
```

#### filter ekleme (django-filter package);

- Category view imize bir de filtreleme özelliği eklemek istiyoruz.
- Dokümanda 
  https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
linkinden bakıyoruz,
- pip install django-filter ile paketi install edip ister settings.py da global olarak, istersek de view bazında filtreleme özelliği kazandırabiliriz viewimize.

```bash
- pip install django-filter
- pip freeze > requirements.txt
```

- add INSTALLED_APPS

main/settings.py
```py
INSTALLED_APPS = [
    ...
    'django_filters',
    ...
]
```

- Biz filtreleme özelliğini global değil de view bazında eklemek istiyoruz. İmportlarımızı yapıp view imize ekleyeceğiz.

- Stock_App
- flight app i create ediyoruz,

```bash
- py manage.py startapp stock
```
- INSTALLED_APPS ' e ekliyoruz.
- urls configurasyonunu yapıyoruz,

core/urls.py
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('stock/', include('stock.urls')),
]
```

stock/urls.py -> şimdilik boş.
```py
from django.urls import path, include
  
urlpatterns = [
]
```


- stock app için modellerimizi, serializerlarımızı, viewlerimizi ve url lerimizi oluşturacağız. Önce serializer.py dosyamızı create ediyoruz,

- Modellerimizi yazmaya başlıyoruz, FixModel kullanıyoruz ve diğer modellerimizi de ondan inherit ederek oluşturacağız. user, created, updated fieldlarımız tüm modellerimizde olacak.
- Brand image'ını UrlField olarak ekleyeceğiz.

stock/models.py
```py
from django.db import models
from django.contrib.auth.models import User

# ---------------------------------
# FixModel
# ---------------------------------

class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# ---------------------------------
# Models
# ---------------------------------
class Category(FixModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Brand(FixModel):
    name = models.CharField(max_length=64, unique=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(FixModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_products')
    name = models.CharField(max_length=128, unique=True)
    stock = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.category} - {self.brand} - {self.name} # {self.stock}'


class Firm(FixModel):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'
    

class Purchase(FixModel):
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name='firm_purchases')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_purchases')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.product} [+{self.quantity}]'


class Sale(FixModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sales')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.product} [-{self.quantity}]'

```


- admin.py da modellerimizi register ediyoruz,
stock/admin.py
```py
from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Purchase,
    Sale,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Purchase)
admin.site.register(Sale)
```


- serializer.py da modellerimiz için kullanacağımız serializer larımızı yazmaya başlıyoruz.
- Serializerımızda FixSerializer da kullanacağız. Diğer tüm serializerları bu FixSerializer dan inherit ederek oluşturuyoruz. user'ı string olarak göster, user_id'yi ise her yeni kayıtta o anki user'ın id'sini user_id olarak tanımla.
- Category 'de, her bir categorye bağlı product sayısını veren bir product_count fieldını MethodField olarak ekledik. 
- Brand 'de, her bir brande bağlı product sayısını veren bir product_count fieldını MethodField olarak ekledik.
- price_total fieldını read_only olarak tanımlıyoruz. Bu field hesaplanarak kaydedilecek bir field olduğu için sadece read ederken gösterilecek bir field.
- Purchase ve Sale ' de category fieldı ekledik, MethodField kullanarak;
  - Product objelerinden, id'si Purchase objesinin id'si ile aynı olanları filtrele, (filteleme bize liste olarak döneceği için,)
  - listenin ilk elemanının category_id'sini al,
  - Category objelerinden, id'si category_id si ile aynı olanları filtrele, (bunu da liste'ye çevirip return et!)  
  - !!!! Burası biraz karışık geldi bana.!!!!
 
stock/serializers.py
```py
from rest_framework import serializers
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Purchase,
    Sale,
)

# ---------------------------------
# FixSerializer
# ---------------------------------
class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)

# ---------------------------------
# Serializers
# ---------------------------------


class CategorySerializer(FixSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = []

    # Her bir objedeki ürün sayısı:
    def get_product_count(self,obj):
        return Product.objects.filter(category_id=obj.id).count()


class BrandSerializer(FixSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        exclude = []

    # Her bir objedeki ürün sayısı:
    def get_product_count(self,obj):
        return Product.objects.filter(brand_id=obj.id).count()


class ProductSerializer(FixSerializer):
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()

    class Meta:
        model = Product
        exclude = []


class FirmSerializer(FixSerializer):

    class Meta:
        model = Firm
        exclude = []


class PurchaseSerializer(FixSerializer):
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Purchase
        exclude = []
        read_only_fields = ['price_total']

    # Üründen kategori bilgisini ver:
    def get_category(self, obj):
        products = Product.objects.filter(id=obj.product_id).values()
        category_id= products[0]['category_id']
        return list(Category.objects.filter(id=category_id).values())


class SaleSerializer(FixSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        exclude = []
        read_only_fields = ['price_total']

    # Üründen kategori bilgisini ver:
    def get_category(self, obj):
        products = Product.objects.filter(id=obj.product_id).values()
        category_id= products[0]['category_id']
        return list(Category.objects.filter(id=category_id).values())
```


- view lerimizi yazmaya başlıyoruz;

- view lerimizde de ModelViewSet den inherit ederek FixView kullanıyoruz. Bu fixView imizde search ve filter için kullandığımız motorları, filter_backends olarak SearchFilter ve DjangoFilterBackend kullanıyoruz. search_fields ve filterset_fields parametrelerini her view de ayrı olarak tanımladık.
  
- Djangoyu rest_framework olarak kullandığımızda,  default olarak sunduğu bazı ayarları kullanamayabiliyoruz. Mesela DjangoModelPermissions
- Userlar için Admin panelden oluşturduğumuz gruplar ve gruplara veya teker teker userlara tanımlayabildiğimiz permission ayarlarının aktif olabilmesi için rest_framework.permissions dan DjangoModelPermissions'ı import edip, FixView imizde permission_classes=[DjangoModelPermissions] şeklinde tanımlyoruz. Böylelikle Admin panelden yaptığımız permissions ayarlarını kullanabileceğiz. Ancak şimdilik yoruma alıyoruz, projeyi kurarken permission hataları almayalım diye. 

- Diğer viewlerimizi de FixView den inherit ederek oluşturuyoruz.
- Modellerimizi ve bu modeller için yazdığımız serializer ları da import ediyoruz.

stock/views.py ->
```py
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    Category, CategorySerializer,
    Brand, BrandSerializer,
    Product, ProductSerializer,
    Firm, FirmSerializer,
    Purchase, PurchaseSerializer,
    Sale, SaleSerializer,
)

# ---------------------------------
# FixView
# ---------------------------------
class FixView(ModelViewSet):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # permission_classes = [DjangoModelPermissions]

# ---------------------------------
# Views
# ---------------------------------

class CategoryView(FixView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']


class BrandView(FixView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    search_fields = ['name']


class ProductView(FixView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    filterset_fields = ['category', 'brand']


class FirmView(FixView):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    search_fields = ['name']


class PurchaseView(FixView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_fields = ['firm', 'brand','product']


class SaleView(FixView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filterset_fields = ['brand','product']
```


- yazdığımız viewleri çalıştıracak endpointleri/url leri yazıyoruz.
- ModelViewSet kullandığımız için router yapısı kullanıyoruz.
- Viewlerimizi de import ediyoruz.

stock/urls.py ->
```py
# ---------- Router ----------
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryView,
    BrandView,
    ProductView,
    FirmView,
    PurchaseView,
    SaleView,
)
router = DefaultRouter()
router.register('categories', CategoryView)
router.register('brands', BrandView)
router.register('products', ProductView)
router.register('firms', FirmView)
router.register('purchases', PurchaseView)
router.register('sales', SaleView)
urlpatterns = router.urls
```

- Test ediyoruz, admin panelden tablolarımızı gördük.

- Projede bizden istenen user rollerini gruplandırıp onlara permission tanımlamak için admin panelden gruplarımız oluşturalım,
  - Product Manager: 
    - CRUD-> Category, Band, Firm, Product 
    - Read-> Purchase, Sale
  - Finance: 
    - CRUD-> Purchase, Sale 
    - Read-> Category, Band, Firm, Product
  - Read only -> Authorized only read operations in all tables

- Tablolarımıza admin panelden veri girişi yapalım.

#### stock projesinin özü-1 burası.
- Purchase(satınalma) and Sale(satış) tablolarında işlem yaptığımızda, yapılan miktar(quantity), Purchase veya Sale tablomuzdaki price fieldı ile çarpımından elde ettiğimiz sonuç price total fieldı olarak tanımlansın.
- Bu işlemi signals kullanarak yapacağız.
  https://docs.djangoproject.com/en/4.2/topics/signals/
  
- Bu işlemi modelde de yapabiliriz. Normalde mecbur kalmadıkça (django için de böyle, db için de böyle (db deki karşılığı triger'dır/tetikleyiciler'dir.)) performans açısından bir tetikleyici kullanmamak en güzeli.    

- @receiver decorator -> amacı yakalamak, sender=Purchase ile Purchase tablosundaki bir değişikliği (yeni kayıt/güncelleme) takip ediyor, pre_save ile bu değişikliğin öncesinde, aşağıdaki fonksiyonu çalıştır. Bir de post_save var. 
- Aşağıdaki fonksiyonda da instance(Purchase yada Sale tablosundaki yapılan değişiklik ile oluşan obje) 'ın quantity'si çarpı price'ı sonucunun price_total olarak tanımlanması.

- stock app inin içinde signals.py oluşturuyoruz.
- oluşturduğumuz signal.py daki signal'in çalışması için stock/apps.py da ready() fonksiyonuyla import etmemiz gerekli.

stock/signals.py
```py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchase, Sale

# https://docs.djangoproject.com/en/4.2/topics/signals/

'''
@receiver(pre_save, sender=Purchase)
def calculate_total_price(sender, instance, **kwargs):
    # Toplam fiyat hesapla:
    instance.price_total = instance.quantity * instance.price


@receiver(pre_save, sender=Sale)
def calculate_total_price(sender, instance, **kwargs):
    # Toplam fiyat hesapla:
    instance.price_total = instance.quantity * instance.price
'''

@receiver(pre_save, sender=Purchase)
@receiver(pre_save, sender=Sale)
def calculate_total_price(sender, instance, **kwargs):
    # Toplam fiyat hesapla:
    instance.price_total = instance.quantity * instance.price
```

stock/apps.py
```py
class StockConfig(AppConfig):
    ...

    def ready(self):
        import stock.signals
```


#### Categoryleri, altındaki productları ile birlikte görüntüleme;

- Normalde category viewimizde categoryler listelenirken altlarındaki productlar görünmez.
- Biz categorylerin altlarındaki productlar ile  görünmesini sağlayan yeni bir serializer yazarak, 
- bu serializerı da CategoryView imizde get_serializer_class() methodunu override ederek, eğer urlden /categories den sonra /products query'si gelirse  yeni oluşturduğumuz CategoryProductsSerializerı çalıştır,
- gelmezse CategorySerializerı çalıştır. 

stock/serializer.py
```py
# ---------------------------------
# Extra Serializers
# ---------------------------------
# Kategoriye bağlı ürünleri göster (realeted_name):
class CategoryProductsSerializer(CategorySerializer):
    category_products = ProductSerializer(many = True)
```

- yeni serializerımızı yazdık şimdi bunu kullanacak Category viewimizde get_serializer_class() methodunu override ederek, eğer urlden /categories den sonra /products query'si gelirse  yeni oluşturduğumuz CategoryProductsSerializerı çalıştır, gelmezse CategorySerializerı çalıştır. 

stock/views.py
```py
from .serializers import (
    # Extras:
    CategoryProductsSerializer,
)

class CategoryView(FixView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['name']

    # Kategori içinde ürünler göster/gösterme: (url/?products=1)
    def get_serializer_class(self):
        if self.request.query_params.get("products", False):
            return CategoryProductsSerializer
        else:
            return super().get_serializer_class()


```

- Şimdi;
   http://127.0.0.1:8000/stock/categories/ 
   endpointine istek atıldığında view'de CategorySerializer kullanılacak, 

   http://127.0.0.1:8000/stock/categories/?products=1
   endpointine istek atıldığında bu sefer CategoryProductsSerializer kullanılarak, productları ile birlikte ctegoryler gelecek.

   http://127.0.0.1:8000/stock/categories/1/?products=1
   endpointine istek atıldığında ise bu sefer CategoryProductsSerializer kullanılarak, id'si 1 olan category'nin altındaki productlar ile birlikte gelecek.



#### stock projesinin özü-2 burası.

- Purchase(satınalma) and Sale(satış) tablolarında işlem yaptığımızda, yapılan miktar(quantity), Product tablomuzdaki stock fieldını artırsın yada azaltsın.

- Bir özelliğin hem django tarafında hem de api tarafında etkin olmasını istiyorsak onu modelde yazmamız gerekiyor. Çünkü modeller django ve rest_framework de önemli bir yere sahipler.

- Products tablosundaki stock miktarını serializer yada view'de create/update/delete methodlarını override ederek stock field daki miktarı artırıp/azaltabiliriz. Ancak bu işlemi serializer yada view de yaptığımızda admin panelde çalışmayacaktır.

- Admin panelde de çalışmasını istiyorsak bunu modelde yapmamız lazım. 
  (Misal signal hem djangoda default olarakçalışır yani admin panelde çalışır, hem de rest_framework'te yani api kısmında çalışır.)
  (Ancak DjangoModelPermissions django default'ta yani admin panelde çalışır, rest_framework'te/api kısmında çalışması için import edilip viewde belirtilmesi gerekir.)

##### Purchse create/update - Satın alma sonrası / satın almanın güncellenmesi sonrasında stock miktarının hesaplanması;

- Peki şimdi modelde nasıl yapacağız.
- Modelde insert/update işlemini yapan method, arka planda çalışan save() methodudur. Bunu override edeceğiz.
- Önce Purchase modelinden başlayalım;
  - Model'in source code'nda save() methodu var, onu override edeceğiz. Araya kaydetmeden önce stock fieldını artır/azalt diyeceğiz.

- Source code da çalışan;
    def save(self, *args, **kwargs):
        ...
        ...
        return super().save(*args, **kwargs)
  save() methodunu alıp, arasına kendi logic'imizi kuracağız.

- Önce güncelleme yapacağımız Product modelindeki instance'ı/ürün objesini çağırıyoruz. Bunu da ForeignKey olarak ilişkili olduğu product field'ının id'si ile yapıyoruz;
  (id=self.product_id)
- İlgili ürünü/product'ı yakaladık, şimdi onun stock miktarını yapılan işleme göre değiştireceğiz;
  - Şimdi bu save methodu hem güncelleme hemde create ettiği için bir ayrım yapmamız gerekiyor. Bunu nasıl yapacağız? 
    - Yeni kayıt yapılırken instance'ın id'si olmaz,
    -  Ancak update yapılırsa instance'ın id'si olur, Çünkü var olan bir instance'ın güncellemesi yapılabiliri olmayan bir instance'ın güncellemesi olmaz. 
  Buradan yola çıkarak bir condition yazarak;  
    - Eğer self.id'si varsa yani if True olursa, demekki burada bir instance'ın (satın alma işlemi)'nin update işlemi vardır, yani var olan bir instance'ın güncellemesini yapacağım;
      - Öncelikle update/güncelleme yapacağımız instance'ın (satın alma) quantity'sini yakalayıp, old_quantity değişkenine tanımlıyoruz,
        old_quantity = Purchase.objects.get(id=self.id).quantity
      - eski miktar ile update/güncellemek istediğimiz miktar arasındaki farkı bulup new_quantity değişkenine tanımlıyoruz.
      - Misal biz 10 satınalma instance'ı create etmiştik, şimdi bu 10'u 8 olarak güncellersek -> product.stock düşecektir, 12 olarak güncellersek -> product.stock artacaktır.
      - Daha sonra product.stock += new_quantity yaparak product stock'unu yeni miktar kadar artır/azalt, product.save() ile kaydet.

    - Eğer self.id'si yoksa (else) yani, demek ki burada bir create/insert (satın alma işlemi) işlemi vardır, yani bir instance'ın (satın alma işlemi) ilk kaydını/insert/create yapacağım;
      - self.quantity verisini new_quantity değişkenine tanımla, product.stock += new_quantity yaparak product stock'unu yeni miktar kadar artır, product.save() ile kaydet.

stock/models.py
```py
class Purchase(FixModel):
    ...
   
    # insert/update:
    def save(self, *args, **kwargs):

        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        
        if (self.id): # update/product miktarı güncelleme işlemi
            old_quantity = Purchase.objects.get(id=self.id).quantity
            new_quantity = self.quantity - old_quantity
        else: # insert/yeni satın alma işlemi
            new_quantity = self.quantity
                
        # Ürün stok bilgi güncelle:
        product.stock += new_quantity
        # Ürün kaydet:
        product.save()
        
        return super().save(*args, **kwargs)
```

##### Purchse delete - Satın alma sonrası, yapılan satın alma işleminin silinmesi sonrasında stock miktarının hesaplanması;

- Purchase (satınalma) silinmesi ile Product stock'uğun azalması.
- Product tablosundan ilgili product'ı yakala,
- ilgili product'ın stock'uğundan silinen purchase/satın alma kadar miktarı çıkar.
- product'ı save() et.

stock/models.py
```py
class Purchase(FixModel):
    ...
   
    # delete:
    def delete(self, *args, **kwargs):
        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        # Ürün stok bilgi güncelle:
        product.stock -= self.quantity
        # Ürün kaydet:
        product.save()
        return super().delete(*args, **kwargs)
```

- Test ettik, hem postmanden, hem de browsable API den çalıştı. Yani;
  - purchase create edince stock arttı,
  - purchase update edince stock arttı/azaldı,
  - purchase delete edince stock azaldı.



##### Sale create/update - Satış sonrası / satışın güncellenmesi sonrasında stock miktarının hesaplanması;

- Yukarıdaki Purchase işleminde olduğu gibi; bu işlemi de yine modelde yaparak, hem API tarafından hem de django/admin panelden kullanılabilmesini sağlamak için model kısmında save() methodunu override ederek yapıyoruz.
- Purchase işlemindeki kodları kullanıyoruz. Sadece yapılan işlem satış olduğu için, satış sonrası stock azalacağı için matematiksel işlemi + dan -'ye çeviriyoruz, delete işleminde de -'den +'ya çeviriyoruz.
- Ayrıca stock tan fazla satış yapmayı engellemek için, bir if condition'ı yazıp, 
  - Eğer product.stock >= self.quantity(sale.quantity): bu işlemleri yap, 
  - değilse, yani stock miktarı, satış yapılmak istenen miktardan küçük ise -> validation error raise etsin.


stock/models.py
```py
    # insert/update:
    def save(self, *args, **kwargs):

        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        
        # Miktar yeterli mi?
        if (product.stock >= self.quantity):
            if (self.id): # update/product miktarı güncelleme işlemi
                old_quantity = Sale.objects.get(id=self.id).quantity
                new_quantity = self.quantity - old_quantity
            else: # insert/yeni satın alma işlemi
                new_quantity = self.quantity
                
            # Ürün stok bilgi güncelle:
            product.stock -= new_quantity
            # Ürün kaydet:
            product.save()
        
            return super().save(*args, **kwargs)
        
        else:
            from django.core.exceptions import ValidationError
            raise ValidationError(f'Dont have enough stock. Current stock is {product.stock}')
    
    # delete:
    def delete(self, *args, **kwargs):
        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        # Ürün stok bilgi güncelle:
        product.stock += self.quantity
        # Ürün kaydet:
        product.save()
        return super().delete(*args, **kwargs)

```

- Test ettik, hem postmanden, hem de browsable API den çalıştı. Yani;
  - sale create edince stock azaldı,
  - sale update edince stock azaldı/arttı,
  - sale delete edince stock arttı.
  

- Ayrıca admin panelden/django dan stock'taki miktardan fazla sale create etmeye çalışınca hata raise ediyor. 
- Fakat rest_framework/API tarafından stock'taki miktardan fazla sale create etmeye çalışınca program çöküyor. Bunu handle etmek için;
- SaleSerializer'ın validate() methodunu override ederek;
- Eğer serializer'a gelen data daki quantity, product stock'undan büyük ise ValidationError raise ettiriyoruz. 

stock/serializers.py
```py
class SaleSerializer(FixSerializer):
    ...
    ...
    # Stokta yeteri kadar yoksa satış yapma:
    def validate(self, data):
        product = Product.objects.get(id=data.get('product_id'))
        if data.get('quantity') > product.stock:
            raise serializers.ValidationError(f'Dont have enough stock. Current stock is {product.stock}')
        return data
```

- Test ettik, hem postmanden, hem de browsable API den çalıştı. Yani artık;
  - admin panelden stock miktarından fazla sale create edince bize hata mesajı raise ediyordu,hala ediyor.
  - rest_framework/API tarafından stock miktarından fazla sale create edince bize hata mesajı raise ediyor.


## pythonanywhere deployment

- Projeyi github a push layın. reponun görünürlüğünü Public olarak ayarlayın. (push larken dbsqlite3'yi de pushluyorum. Db boş olmasın diye.)
- pythonanywhere sign up oluyoruz.
- pythonanywhere free account içinde sadece 1 app konulabiliyor. Birden çok app konulacaksa, birden fazla e-mail ile birden fazla free account oluşturulup ve herbir free account a 1 app konulabilir.
- pythonanywhere default olarak olarak sql3 db sunuyor. free account ta postgresql için para ödemek gerekiyor.
  
- repoda bir değişiklik olduğunda deploy edilmiş app a değişiklikler otomatik yansımıyor. (pipline) Değişiklikleri repoya pushladıktan sonra, pythonanywhere e gidip, terminalden yapılan değişiklikler tekrardan çekilip!!, app i reload etmek gerekiyor.

- pythonanywhere -> dashboard -> New console -> $Bash yeni sekmede açıyoruz.
- pythonanywhere deki bash terminalde;
- rm -rf ....   ile eskilerini siliyoruz. (README.txt kalıyor.)
```bash
rm -rf klkf.txt
```

- github taki deploye edeceğimiz reponun url ini kopyalıyoruz (clonelar gibi)
- pythonanywhere deki bash terminale;

```bash
git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Flight_App.git
```

- project imizi pythonanywhere clonladık.
- terminalde ls komutuyla dosyaları görüyoruz,
- projemizin içine, manage.py dosyasıyla aynı seviyeye geliyoruz (cd komutuyla), yani ls komutunu çalıştırdığımızda manage.py ı görmemiz lazım.

- Türkiyede cloud platformlar çok kullanılmıyor, genelde Dedicated Server lar üzerinden işlemler yapılıyor. Tüm proje o server içerisinde oluyor. Servera girip, projeyi clonlama işlemi yapılıyor, veya pipeline kuruluyor (localde bir değişiklik yapıldı, github a pushlandı, merge oldu, development server ından bu değişikliğin algılanıp canlıda değişiklik yapılması...). Bunun için github hook ları var, bu hooklar ile işlem yapılıyor.  Bir değişiklik olduğunda github hookları takip ediliyor, değişiklik olduğunda trigger ediyor, o trigger ile server ınızda otomatik git pull yapıyor, değişiklikleri çekiyor, projeyi yeni şekliyle ayağa kaldırıyor.

- Localde iken yapmamız gereken işlemlerin aynısını yapıyoruz;
    - virtual environment oluşturuyoruz,
    - bazı eski versiyonlarda python 2. versiyonu gelebiliyor. Önce "python --version" ile kontrol edilip, eğer 2. versiyon geliyorsa "python3 --version" ile bir daha kontrol edip bu sefer 3. versiyonun geldiğini görüp, "python3 -m venv env" ile virtual environment oluşturuyoruz.
    - "source env/bin/activate" komutu ile env yi aktif hale getiriyoruz.(Bu ortam linux ortamı olduğu için windows kullanıcıları da ancak bu komutla env aktif hale getirebilir.)
    - projenin dependency lerini (bağımlılıklarını) kuruyoruz.

```bash
- python --version
- python3 --version
- python3 -m venv env  # python -m venv env 
- source env/bin/activate
- pip install -r requirements.txt
```

  - pythonanywhere -> dashboard -> Web -> Add a new web app -> next -> Manual configuration (including virtualenvs) -> Python 3.10 (python versionu) -> next
        All done! Your web app is now set up. Details below. 
        (Hepsi tamam! Web uygulamanız artık kuruldu. Detaylar aşağıda.)
  - Artık app kuruldu ve app ile ilgili bir dashboard sundu bize. Burada manuel configurations lar yapacağız. 
        Bu site 28 Temmuz 2024 Pazar günü devre dışı bırakılacaktır. Buradan 3 ay daha app i çalıştırmak için bir button var.

- Şimdi yapacağımız işlemler -> 
  - Code:
        Source code: -> source codumuzu koyduğumuz yeri yazacağız.
        Working directory: -> source code ile aynı oluyor, bu directory de çalışacaksın diyoruz.  
        WSGI configuration file: -> manuel olarak update edeceğiz.
  - Virtualenv:
        Enter path to a virtualenv, if desired -> env nin nerede olduğunu göstereceğiz, yolunu vereceğiz.


- Source code: -> bash terminalde app in olduğu klasör içerisinde iken, "pwd" yazıp klasörün yolunu görebiliyoruz.
        /home/umit8098/Project_Django_Rest_Framework_Flight_App
- Working directory: -> Source code kısmına yazdığımız yolu buraya da yazıyoruz.
        /home/umit8098/Project_Django_Rest_Framework_Flight_App
- WSGI configuration file: Manuel configuration yaptığımız için bu WSGY (Web Server Gateway Interface) configuration u da kendimiz yapacağız. django application ile server arasındaki iletişimi sağlayan gateway. Bunda ayarlar yapmalıyız. sağ tıklayıp new tab ile yeni pencerede açıyoruz, Default olarak farmeworklerin ayar template leri var. 74-89 satırları arasında django kısmı var. Bunun haricindeki herşeyi siliyoruz, sadece django ile ilgili kısım kalıyor. İlk iki satır hariç yorumdan kurtarıyoruz.

```py
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/umit8098/mysite/mysite/settings.py'
# and your manage.py is is at '/home/umit8098/mysite/manage.py'
path = '/home/umit8098/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```

- path kısmında bize manage.py ın yolunu vermemizi istiyor. Aslında source code umuzun olduğu path, biraz önce "pwd" ile almıştık, "/home/umit8098/Project_Django_Rest_Framework_Flight_App". Bunu path değişkenine tanımlıyoruz. Yani manage.py ımız bu klasörün içinde bunu söylüyoruz.

```py
path = '/home/umit8098/Project_Django_Rest_Framework_Flight_App'
```

- os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'  -> settings klasörümüzün bulunduğu yeri belirtiyoruz. Bizim settings klasörümüz main in altında. buraya 'main.settings' yazıyoruz.

```py
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
```


- save ediyoruz.

- Virtualenv: env yolunu vermemiz lazım. Tekrar console a geri dönüyoruz, 
  - env nin olduğu dizne gidiyoruz. (ls yaptığımızda env yi görüyoruz.) 
  - "cd env/" ile env nin dizinine giriyoruz. 
  - pwd yazıp env nin path'ini yani yolunu kopyalıyoruz.
  - kopyaladığımız path i Virtualenv kısmındaki bölüme yazıp tik e tıklıyoruz. env miz de hazır.

```py
/home/umit8098/Project_Django_Rest_Framework_Flight_App/env
```


- Genel olarak ayarlarımız tamam ama birkaç ayar daha kaldı.
  - SECRET_KEY, DEBUG, ENV_NAME, DJANGO_LOG_LEVEL=INFO (bu projeye özel)
  - Bunları ayarlayacağımız yer Source code kısmındaki Go to directory. sağ tıklayarak yeni sekmede açıyoruz,
  - projemizde bu verileri tuttuğumuz yer .env file ı idi. Açılan sekmede Files kısmına .env yazıp New File oluşturuyoruz. bize .env isminde yeni bir file oluşturdu. manage.py, requirements.txt ile aynı seviyede.
  - Eğer dev, prod şeklinde env mizi ayırmadıysak sadece .env deki değişkenleri tanımlamamız yeterli.
  - Ancak env miz dev ve prod olarak ayrılmış ise -> 
    - SECRET_KEY tanımladık, 
    - DEBUG=True  (Önce True yazıyoruz, hataları görebilmek için. daha sonra False a çekebiliriz.)
    - settings klasörünün __init__.py daki env değişkeninin ismine ne verdiysek onu alıp .env file ında değişken ismi olarak kullanıyoruz. ENV_NAME
    - ENV_NAME=dev  
        - prod ayarlarımızda db olarak postgresql var. bizim dev ayarlarını kullanmamız daha iyi. 
        - Ayrıca dev ayarlarını kullanırken de; debug.toolbar sadece localhost ta çalışıyor. Bu yüzden debug.toolbar ayarları ile development çalıştırılırsa hata verecektir. Bu hatayı almamak için dev.py daki debug.toolbar ayarlarını yoruma alıyoruz.
    - Bir de DJANGO_LOG_LEVEL=INFO ayarımız vardı onu da .env file ımıza ekliyoruz.

settings/dev.py
```py
from .base import *

# THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

# INSTALLED_APPS += THIRD_PARTY_APPS

# THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]
```


- .env dosyamızın en son hali -> 

.env
```py
SECRET_KEY=o_zoo)sc$ef3bbctpryhi7pz!i)@)%s!ffg_zsxd^n+z+h5=7i
DEBUG=True
ENV_NAME=dev
DJANGO_LOG_LEVEL=INFO
```

- bash console a gidip db mizdeki tablolarımız oluşturacağız.
- (Biz projemizi github'a pushlarken db.sqlite3' yi de pushlamıştık. Yani db miz var. Eğer db'siz olarak github'a pushlayıp, oradan pythonanywhere'e deploye ediyorsak o zaman migrate ve superuser yapmamız gerekiyor.) 
- bash console da manage.py file ının bulunduğu dizine gidip db miz deki tablolarımızı oluşturuyoruz, superuser oluşturuyoruz,

```bash
python manage.py migrate
python manage.py createsuperuser
```

- dashboard a gidip Reload butonuna tıklıyoruz. Tüm değişiklikleri algılayacaktır. Daha sonra hemen bir üstte verdiği link ile projemizi pythonanywhere de yeni sekmede çalıştırıyoruz. 
- Bazen ALLOWED_HOSTS hatası veriyor. pythonanywher'e yüklediğimiz projenin settings.py'ına gidip ALLOWED_HOSTS = ['*'] şeklinde update/save ediyoruz ve tekrardan reload ediyoruz.
- admin panele giriyoruz,
- statics ler olmadan, css ler olmadan sayfamız geldi. 
- statics lerin görünmemesinin sebebi; django admin panel bir application ve bunun static file ları env içerisinde duruyor. Bunu localhost ta çalıştırdığımız zaman sıkıntı yaşamıyoruz ama canlı servera aldığımız zaman static root diye bir directory belirtmemiz gerekiyor. Static root, bütün environment ta olan static file ları veya application içerisinde varsa static file larımızı (css, javascript, image)  bunların hepsini tek bir klasör altında topluyor ve canlıdayken oradan çekiyor. Bu static ayarı nı yapmamız gerekiyor. Nasıl yapacağız;
- dashboadr -> Cource code -> Go to directory -> main -> settings -> base.py  içine STATİC_URL = 'static' altına STATIC_ROOT = BASE_DIR / 'static' yazıyoruz.

settings/base.py
```py
STATİC_URL = 'static'
STATIC_ROOT = BASE_DIR / 'static'
```

- base directory altında static isminde bir klasör oluştur, tüm static file ları bu static folder içerisinde topla demek için şu komutu (collectstatic) bash console da çalıştırıyoruz;

```bash
python manage.py collectstatic
```
- bu komut çalıştırıldıktan sonra; 197 adet static file kopyalandı ve belirttiğimiz folder altında toplandı.
" 197 static files copied to '/home/umit8098/Project_Django_Rest_Framework_Flight_App/main/static'. "

- Şimdi dashboarda gidip, web kısmında Static files: kısmında URL altında URL ini (/static/),  ve Directory altında path ini giriyoruz. (path ini zaten bize vermişti -> 197 static files cop..... kısmının sonunda. (/home/umit8098/Project_Django_Rest_Framework_Flight_App/main/static))
- girdikten sonra ✔ işareti ile kaydetmeliyiz.
  
```py
/static/
/home/umit8098/Project_Django_Rest_Framework_Flight_App/main/static
```

- Bu işlemi yaptıktan sonra değişikliklerin algılanması için tekrardan Reload butonuna tıklıyoruz. Artık sayfalarımızın statics leri de geliyor.

 - Şuanda backend projesi deploye edildi. Eğer bu backend için bir frontend yazılmış ise deploye edilmiş projenin endpointlerine istek atması gerekir. Mesela frontend kısmı React ile yazılmışsa istek atılacak endpointler düzenlenip netlify'a deploye edilip, oradan çalıştırılması daha uygun olur. 