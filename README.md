# Django Rest Error Codes

This Project is to manage the error response with a body by default like this:

    {
        'error_code': 'US001',
        'message': 'text for example'
    }
    
the `US001` code can be a row in the database with a message and a description. In the body response we send error_code and message, lastly, the field description is for the documentation of these exceptions.

## Installation

After installing this project, we need to have django rest framework installed.
Once installed:

`pip install django-rest-error`

### Added to settings.py


    INSTALLED_APPS = [
        ...
        'rest_framework',
        'error_codes',
    ]


By default this project add new migration.
This migration is use it by project to manage the errors


## Documentation
This documentation is very simple in terms of desing.
**To be able to use it** we need add to your project urls.py like this::

`path('error/', include('error_codes.urls')),`

And now we can visit:
`http://localhost:8000/error/docs/`

## Serializers

We can use the exception on the serializer:

    from rest_frameworks import serializers
    from error_codes.exceptions import CustomErrorException
    from error_codes.serializer import OverrideSerializer
    
    class UserSerializer(OverrideSerializer):

        username = serializers.ChardField(max_length=15)
        age = serializers.IntegerField()
    
        def validate_age(self, age):
            if age < 18:
                raise CustomErrorException('US001')



The code **US001** is saved on DB.

So, when serializer errors are fired, they will return a body response like above.


## Exceptions

We can use the exception **CustomErrorException** like any other exception.

`
raise CustomErrorException('USS02')
`

This case and the previous case return a body response like this:

    {
        'error_code': 'US002',
        'message': 'Text to display to user'
    }


## Other uses

We can add more static data, Only need that data like a dict, for example:

We want to add `{'status': False}`

`
raise CustomErrorException('USS02'. {'static': False})
`  


We can use in serializers or like any other exception


## New fields to body response

We can add new fields to body response.

We add a new filed called **path**

For it we extends from model **Error**:

models.py

    from django.db import models
    from error_codes.models import Error

    class OtherError(Error):
        path = models.ChardField(max_legth=100)

we apply migrations

Now we need add this field on **settings.py**

On settings.py:

    ERROR_MODEL_FIELDS = ['error_code', 'message', 'path']

And change the table for error:

    ERROR_MODEL = "yourapp.Error"

