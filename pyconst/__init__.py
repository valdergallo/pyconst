# encoding: utf-8
from __future__ import unicode_literals, absolute_import

__version__ = (1, 0, 6)
__author__ = 'valdergallo@gmail.com'

from .const import Const
from .slug import slugify

def get_version():
    return '.'.join(map(str, __version__))

__all__ = [
    'Const',
    'slugify',
]
