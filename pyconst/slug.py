# encoding: utf-8
from __future__ import unicode_literals
import unicodedata
import re

def slugify(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').lower()
    only_string = re.findall('\w+', str(only_ascii))
    return '_'.join(only_string)
