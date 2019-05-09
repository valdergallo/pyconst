# encoding: utf-8
from __future__ import unicode_literals
import unicodedata
import re


def to_string(input_str):
    try:
        return unicode(input_str)
    except:
        return str(input_str)


def slugify(input_str):
    input_str = to_string(input_str)
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('utf-8')
    only_string = re.findall('\w+', only_ascii)
    return '_'.join(only_string)


def slugify_attr(input_str):
    input_str = to_string(input_str)
    if input_str.isdigit():
        input_str = '_' + input_str
    return slugify(input_str)
