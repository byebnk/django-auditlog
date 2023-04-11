# Django-auditlog

## Usage

**Important**: Due to ``pgtrigger`` this package is only meant to be used with a postgres backend

1. Add auditlog to your INSTALLED_APPS settings like these:

```python
INSTALLED_APPS = [
    ...,
    "auditlog",
]
```

2. Run ``python manage.py migrate`` to create the models.

## Development

Register this package for development
```bash
python setup.py develop
```

Running migrations
```bash
django-admin makemigrations --settings=settings
```

Running tests
```bash
django-admin test --settings=settings
```

### Reference

[Creating a django lib](http://hirokiky.org/tech/create_django_library.html)
