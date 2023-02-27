#!/usr/bin/env python
from library_layers.libraries.django.functions import load_manager

settings, execute_manager = load_manager(file=__file__)


if __name__ == "__main__":
    execute_manager(settings)

