from .exceptions import DjangoVersionNotFound, LayersFolderDoesNotExists

class LayersLoader(object):
    """
    Custom class to manage the layers loaded for all django code
    """
    module_name = None
    layers_path = None
    django_version = None
    filename = None

    def __init__(self, filename):
        self.filename = filename
        self.set_django_version()
        self.set_layers_path()

    def set_django_version(self):
        """
        Function to set the DJANGO_VERSION global environment
        """
        import os
        from env_tools import apply_env

        apply_env()
        self.django_version = os.environ.get('DJANGO_VERSION', None)

        if not self.django_version:
            raise DjangoVersionNotFound("The DJANGO_VERSION environment was not defined.")

    def set_module_name(self):
        """
        Function to set the module name selected by django_version
        """
        self.module_name = "layers{django_version}".format(django_version=self.django_version)

    def get_module_dir(self):
        """
        Function to get the module dir
        """
        import os
        module_dir = os.path.dirname(self.filename)

        return module_dir
    
    def set_layers_path(self):
        """
        Function to set the layers_path attribute
        """
        import os

        self.set_module_name()
        module_dir = self.get_module_dir()
        self.layers_path = "{module_dir}/{module_name}".format(
                module_dir=module_dir,
                module_name=self.module_name)
        if not os.path.exists(self.layers_path):
            raise LayersFolderDoesNotExists("The Layers folder {module_name} does not exists for Django version {django_version}.".format(
                module_name=self.module_name,
                django_version=self.django_version))

