==================
Django Error Codes
==================

Django Error Codes is a Django app to manage the error in your api. For each error,
you can have a description and code.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install dependencies:
    pip install  djangorestframework

2. Add "error_codes" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_framework',
        'error_codes',
    ]

2. Include the errors docs URLconf in your project urls.py like this::

    path('error/', include('error_codes.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a errors (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/error/docs/ to see all errors if you have errors saved in the database.