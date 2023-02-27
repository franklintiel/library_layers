def load_manager(*args, **kwargs):
    """
    layer function to translate the default execute manager
    """
    import sys
    from django.core.management import execute_manager

    try:
        file = kwargs.get('file', __file__)
        from core import settings
        return settings, execute_manager
    except ImportError:
        sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. If appears you've customized things.\nYou'll have to run django-admin.py passing it your seetings module.\n(If the file settings.py does indeed exists, it's causing an ImportError somehow.)\n" % file)
        sys.exit(1)

def include(*args, **kwargs):
    """
    function layer to translate the code useed in the defaults.include()
    """
    from django.conf.urls.defaults import include as default_include
    return default_include(*args, **kwargs)

def patterns(*args,  **kwargs):
    """
    function layer to translate the code used in the defaults.patterns()
    """
    from django.conf.urls.defaults import patterns as default_patterns
    return default_patterns(*args, **kwargs)

def url(*args, **kwargs):
    """
    function layer to translate the code used in the defaults.url()
    """
    from django.conf.urls.defaults import url as default_url
    return default_url(*args, **kwargs)

