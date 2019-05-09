# encoding: utf-8
from __future__ import unicode_literals, absolute_import

__version__ = (1, 1, 3)
__author__ = 'valdergallo@gmail.com'

from .const import Const
from .const import UpperConst
from .const import LowerConst
from .const import DefaultConst
from .slug import slugify

def get_version():
    return '.'.join(map(str, __version__))

__all__ = [
    'Const',
    'UpperConst',
    'LowerConst',
    'DefaultConst',
    'slugify',
]
