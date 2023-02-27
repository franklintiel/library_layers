def load_manager(*args, **kwargs):
    """
    layer function to translate the default execute manager
    """
    import os
    import sys
    from django.core.management import execute_from_command_line
    
    try:

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

        return sys.argv, execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError("Couldn't import Django. Are you sure its installed and "
                              "available on your PYTHONPATH environment variable? Did you "
                              "forget to activate a virtual environment?")
        raise


def include(*args, **kwargs):
    """
    function layer to translate the code useed in the defaults.include()
    """
    from django.conf.urls import include as default_include
    return default_include(*args, **kwargs)


def url(*args, **kwargs):
    """
    function layer to translate the code used in the defaults.url()
    """
    from django.conf.urls import url as default_url
    return default_url(*args, **kwargs)

