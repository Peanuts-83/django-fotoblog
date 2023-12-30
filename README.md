# Django - A server-side application discovery

This project is for learning purpose, testing and discovering the range of possibilities offered by Django's framework.
You can follow both OpenClassrooms courses about it from here:
- https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django
- https://openclassrooms.com/en/courses/7107341-intermediate-django

## Content

A simple application displaying photos, with authentication, upload and update capabilities to experiment CRUD operations. This is a Work In Progress app, don't expect any ready-made stuff!

*screenshot -*

![Homepage](/common_static/README_media/screenshot.png)

## Technical stack

- Python language based
- MTV - Model Template View :
    - Model : objects designing database tables with integrated ORM
    - Template : html templates for server-side rendering
    - View : the programatic "brain" part of the app where the logic belongs
- Integrated ORM - Object Relational Mapping : it gives an abstraction level tomanage database setup with Python language.
- Templating : for html rendered on server side. *(In an other project I shall explore the capability of combining Django with an angular application for full-stack app delivery)*
- CLI : Initiate, setup and drive your project with CLI. Also manage database tasks such as "makemigrations" and "migrate" commands.
- Admin interface : a very nice and automated admin interface, fully customisable.
- And tons of packages available, with a big community to discuss with. https://djangopackages.org/

## Packages

### Django Allauth

*https://docs.allauth.org/en/latest/introduction/index.html*

- **purpose :** Authentication stuff
- **contains :** account functionality, social login, rate limiting, privacy, customisation...
- **notable include :** Signals - emited at some key moments of authentication flow (https://docs.allauth.org/en/latest/account/signals.html).
Use it: in *.py file with @receiver() decorator

```python
# Signal: allauth.account.signals.email_confirmed(request, email_address)
@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
	do some stuff...
```

### Django Debug Toolbar

*https://django-debug-toolbar.readthedocs.io/en/latest/index.html*

- **purpose :** Give access to global variables/SQL requests, and so on ...
- **contains :** history navigation, HTTP request, SQL request, templates, signals and others...

*screnshots -*

![toolbar - full toolbar with HTTP request](/common_static/README_media/toolbar_req.png)
![toolbar - SQL requests](/common_static/README_media/toolbar_sql.png)
![toolbar - Signals emitted](/common_static/README_media/toolbar_sig.png)
![toolbar - navigation history](/common_static/README_media/toolbar_his.png)