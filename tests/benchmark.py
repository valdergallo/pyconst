# encoding: utf-8
from __future__ import unicode_literals
import random
import string
from pyconst import PyConst

CHAR_SET = string.ascii_uppercase

def rand_text(max_length=6):
    return ''.join(random.sample(CHAR_SET*max_length, max_length))


def test_add_one_time(benchmark):
    permissions = PyConst()
    text = rand_text(max_length=6)

    @benchmark
    def add_one_with_six_digits():
        permissions.add(text)

def test_add_one_time_big_text(benchmark):
    permissions = PyConst()
    text = rand_text(max_length=1000)

    @benchmark
    def add_one_with_six_digits():
        permissions.add(text)


def test_add_thousand_time(benchmark):
    texts = []
    for i in range(1000):
        texts.append(rand_text(max_length=6))

    @benchmark
    def add_thousand_with_six_digits():
        permissions = PyConst()
        for i in range(1000):
            permissions.add(texts[i])


def test_add_hundred_time(benchmark):
    texts = []
    for i in range(100):
        texts.append(rand_text(max_length=6))

    @benchmark
    def add_hundred_with_six_digits():
        permissions = PyConst()
        for i in range(100):
            permissions.add(texts[i])


def test_get_item_from_thousand(benchmark):
    permissions = PyConst()
    for i in range(1000):
        permissions.add(rand_text(max_length=6))

    @benchmark
    def get_permission():
        permissions[888]
