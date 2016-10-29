# encoding: utf-8
__version__ = (1, 0, 0)

from .const import PyConst
from .slug import slugify

def get_version():
    return '.'.join(map(str, __version__))

__all__ = [
    'PyConst',
    'slugify',
]
