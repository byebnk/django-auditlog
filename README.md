# Django-auditlog

1. Add auditlog to your INSTALLED_APPS settings like these:

```python
INSTALLED_APPS = [
    ...,
    "auditlog",
]
```

2. Run ``python manage.py migrate`` to create the models.

## Important

Due to ``pgtrigger`` this package is only meant to be used with a postgres backend
