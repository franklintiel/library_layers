class DjangoVersionNotFound(BaseException):
    """
    Exception class used when the DJANGO_VERSION variable environment was not defined
    """
    pass

class LayersFolderDoesNotExists(BaseException):
    """
    Exception classs used when the layers folder to specific django version does not exists.
    """
    pass
