<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Rest_Framework_Stock_App</h1>


<!-- <div align="center">
  <h3>
    <a href="https://umit8103.pythonanywhere.com/">
      Demo
    </a>
     | 
    <a href="https://umit8103.pythonanywhere.com/">
      Project
    </a>
 
  </h3>
</div> -->

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [API Documentation](#api-documentation)
- [API Testing](#api-testing)
- [Overview](#overview)
- [Built With](#built-with)
- [How To Use](#how-to-use)
- [About This Project](#about-this-project)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)


## API Documentation

Projenin detaylı API dokümantasyonlarına aşağıdaki linklerden ulaşabilirsiniz:

- [Swagger Dokümantasyonu](https://umit8103.pythonanywhere.com/swagger/)
- "Swagger Dokümantasyonu Görseli": API endpoint'lerini kolayca test etmenizi sağlayan bir arayüz.
<!-- ![Swagger_Arayüzü](project_screenshot/Swagger_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Swagger_Dokümantasyonu_Görseli.png" alt="Swagger Arayüzü" width="400"/>

  
- [RedocDokümantasyonu](https://umit8103.pythonanywhere.com/redoc/)
- "Redoc Dokümantasyonu Görseli": API yapısını detaylı ve düzenli bir şekilde sunan bir dokümantasyon aracı.
<!-- ![Redoc_Arayüzü](project_screenshot/Redoc_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Redoc_Dokümantasyonu_Görseli.png" alt="Redoc Arayüzü" width="400"/>


<!-- - Bu dokümantasyonlar sayesinde API endpoint'lerini kolayca test edebilir ve yapılarını inceleyebilirsiniz. -->
**Not:** Swagger ve Redoc dokümantasyonlarına herhangi bir kullanıcı girişi yapmadan erişebilirsiniz.

- Swagger ve Redoc dokümantasyonlarıyla birlikte, API'leri test etmek için Postman koleksiyonumuzu kullanabilirsiniz. [Stock Management API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9c7e9dbb-cadb-4cb7-bb41-7399ad499c3e?action=share&creator=17531143)

## API Testing

API'leri Postman üzerinden test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Postman'i yükleyin (eğer yüklü değilse): [Postman İndir](https://www.postman.com/downloads/).
2. Bu [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9c7e9dbb-cadb-4cb7-bb41-7399ad499c3e?action=share&creator=17531143) indirin ve içe aktarın.
3. API'leri Postman üzerinden test etmeye başlayın.

**Postman Collection Linki:**  
[Flight Reservation API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9c7e9dbb-cadb-4cb7-bb41-7399ad499c3e?action=share&creator=17531143)


## Overview


- Stock_App Swagger-Redoc
![screenshot](project_screenshot/Stock_App_Swagger_Redoc.gif)

---

- Stock_App Stock Test On Postman
![screenshot](project_screenshot/Stock_App_Stock_Test.gif)

---

- Stock_App User/Authentication Test On Postman
![screenshot](project_screenshot/Stock_App_User_Test.gif)

---

- Stock_App Project ERD Diagram
![screenshot](project_screenshot/Stock_App_ERD.png)


## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Djago Rest Framework


## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framework_Stock_App_CH-13) 

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Stock_App_CH-13.git

# Install dependencies
    $ python -m venv env
    $ python -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...

# for development(dev) environments
DEBUG =True

# for production environments
SQL_DATABASE={DB_NAME}
SQL_USER={DB_USER_NAME}
SQL_PASSWORD={DB_PASSWORD}
SQL_HOST=localhost
SQL_PORT=5432

# for choices environment
ENV=development
# ENV = production

# DJANGO_LOG_LEVEL=INFO
DJANGO_LOG_LEVEL = WARNING
# DJANGO_LOG_LEVEL=ERROR
"""

# Run the app
    $ python manage.py runserver
```

## About This Project
- Stock Management Application API service.

<hr>

- Stock Management Application API service.

## Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Logging](https://docs.djangoproject.com/en/5.1/topics/logging/) - System logging modul
- [Swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation) - Environment and document modul 
- [Debug_Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - Debug Toolbar modul
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - for authentication
- [django-filter](https://django-filter.readthedocs.io/en/stable/)


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- GitHub [@Umit8098](https://github.com/Umit8098)

- Linkedin [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
