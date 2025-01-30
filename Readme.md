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

You can access the detailed API documentation of the project from the links below:

- [Swagger Documentation](https://umit8103.pythonanywhere.com/swagger/)
<!-- ![Swagger_Arayüzü](project_screenshot/Swagger_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Swagger_Dokümantasyonu_Görseli.png" alt="Swagger Arayüzü" width="400"/>
➡ Interface that allows you to easily test API endpoints.

  
- [Redoc Documentation](https://umit8103.pythonanywhere.com/redoc/)
<!-- ![Redoc_Arayüzü](project_screenshot/Redoc_Dokümantasyonu_Görseli.png) -->
<img src="project_screenshot/Redoc_Dokümantasyonu_Görseli.png" alt="Redoc Arayüzü" width="400"/>
➡ Documentation tool that presents the API structure in a detailed and organized way.


---

<!-- - Bu dokümantasyonlar sayesinde API endpoint'lerini kolayca test edebilir ve yapılarını inceleyebilirsiniz. -->
**Notes:** You can access Swagger and Redoc documentation without any user login.

**Not:** Swagger ve Redoc dokümantasyonlarına herhangi bir kullanıcı girişi yapmadan erişebilirsiniz.

- Along with Swagger and Redoc documentation, you can use our Postman collection to test APIs. 
  [Stock Management API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9c7e9dbb-cadb-4cb7-bb41-7399ad499c3e?action=share&creator=17531143)

## API Testing

To test APIs via Postman, you can follow the steps below:

1. Install Postman (if not installed): [Postman İndir](https://www.postman.com/downloads/).
2. This [Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9c7e9dbb-cadb-4cb7-bb41-7399ad499c3e?action=share&creator=17531143) Download and import.
3. Start testing APIs via Postman.

**Postman Collection Link:**  
[Stock Management App API Postman Collection](https://umit-dev.postman.co/workspace/Team-Workspace~7e9925db-bf34-4ab9-802e-6deb333b7a46/collection/17531143-9c7e9dbb-cadb-4cb7-bb41-7399ad499c3e?action=share&creator=17531143)


## Overview


- Project Swagger and Redoc Documentation Visual
<!-- ![screenshot](project_screenshot/Stock_App_Swagger_Redoc.gif) -->
<img src="project_screenshot/Stock_App_Swagger_Redoc.gif" alt="Project Swagger and Redoc Documentation Visual" width="400"/>

---

- Stock_App testing on Postman
<!-- ![screenshot](project_screenshot/Stock_App_Stock_Test.gif) -->
<img src="project_screenshot/Stock_App_Stock_Test.gif" alt="Stock_App testing on Postman" width="400"/>

---

- Stock_App User/Authentication Test On Postman
<!-- ![screenshot](project_screenshot/Stock_App_User_Test.gif) -->
<img src="project_screenshot/Stock_App_User_Test.gif" alt="Stock_App User/Authentication Test On Postman" width="400"/>

---

- Stock_App Project ERD Diagram
<!-- ![screenshot](project_screenshot/Stock_App_ERD.png) -->
<img src="project_screenshot/Stock_App_ERD.png" alt="Stock_App Project ERD Diagram" width="400"/>

- API documentation is detailed with Swagger and Redoc. You can access the relevant links via [Swagger](https://umit8103.pythonanywhere.com/swagger/) and [Redoc](https://umit8103.pythonanywhere.com/redoc/).

- Stock Management App is a modern backend application developed for users to manage the stock system and provide easy integration with API documentation.
- Provides CRUD operations specific to users and staff roles.
- Swagger and Redoc were used for API documentation.



## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework used to create REST APIs.
- [Swagger And Redoc](https://drf-yasg.readthedocs.io/en/stable/readme.html#installation) - Environment and document modul 
- [Debug_Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - Debug Toolbar modul
- [Logging](https://docs.djangoproject.com/en/5.1/topics/logging/) - System logging modul
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - for authentication 
- [django-filter](https://django-filter.readthedocs.io/en/stable/)
- PostgreSQL


## How To Use

<!-- This is an example, please update according to your application -->

- For online demo: You can take a look at the [Swagger](https://umit8103.pythonanywhere.com/swagger/) and [Redoc](https://umit8103.pythonanywhere.com/redoc/) interfaces.

- To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Rest_Framework_Stock_App_CH-13) 

- When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

- Complete the installation by uncommenting the appropriate package.

---

- Çevrimiçi demo için: [Swagger](https://umit8103.pythonanywhere.com/swagger/) veya [Redoc](https://umit8103.pythonanywhere.com/redoc/) arayüzlerine göz atabilirsiniz.

- requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

- Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin. 

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

# PostgreSQL settings for product (product) environments
SQL_DATABASE={your_database_name}
SQL_USER={your_database_user}
SQL_PASSWORD={your_database_password}
SQL_HOST=localhost
SQL_PORT=5432

# for choices environment
ENV=development
# ENV = production

# Logging level
# DJANGO_LOG_LEVEL=INFO
DJANGO_LOG_LEVEL = WARNING
# DJANGO_LOG_LEVEL=ERROR
"""

# Run the app
    $ python manage.py migrate
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
- **GitHub** [@Umit8098](https://github.com/Umit8098)

- **LinkedIn** [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->
