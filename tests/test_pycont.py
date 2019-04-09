# encoding: utf-8
from __future__ import unicode_literals
import unittest
from pyconst import Const


class TestConsts(unittest.TestCase):

    def setUp(self):
        self.const = Const()

    def test_slugify(self):
        self.const.add('caça vovó')
        self.assertEqual(self.const.caca_vovo, 'CACA_VOVO')

    def test_add_item(self):
        self.const.add('update item')
        self.assertEqual(self.const.update_item, 'UPDATE_ITEM')

    def test_inter_pyconst(self):
        self.const.add('update item')
        for value in self.const:
            self.assertEqual(value, ('UPDATE_ITEM', 'update item'))

    def test_set_init_values(self):
        const = Const(
            'add user',
            'create user',
            'delete user',
        )

        self.assertEqual(const.add_user, 'ADD_USER')
        self.assertEqual(len(const), 3)

    def test_get_value(self):
        const = Const(
            'Add User',
            'Create User',
            'Delete User',
        )

        self.assertEqual(const.add_user.label, 'Add User')

    def test_slug_stranger_characteres(self):
        const = Const(
            'Add - User',
        )
        self.assertEqual(const.add_user, 'ADD_USER')

    def test_add_attribute(self):
        self.const.add('Update item (new)', 'update_item')
        self.assertEqual(self.const.update_item, 'UPDATE_ITEM')
        self.assertEqual(self.const.update_item.label, 'Update item (new)')

    def test_get_value_in_order(self):
        const = Const(
            'Add User',
            'Create User',
            'Delete User',
        )

        self.assertEqual(const[0], ('ADD_USER', u'Add User'))

    def test_get_multiple_value_in_order(self):
        const = Const(
            ('Add User', 'add_user'),
            ('Create User', 'create_user'),
            ('Delete User', 'delete_user'),
        )

        self.assertEqual(const[0], ('ADD_USER', u'Add User'))

    def test_get_multiple_kwargs_value_in_order(self):
        const = Const(**{'Add User': 'add_user'})
        self.assertEqual(const[0], ('ADD_USER', u'Add User'))

    def test_slug_index_error(self):
        const = Const()
        const.add(['Add User'])
        self.assertEqual(const[0], ('ADD_USER', u'Add User'))

    def test_number_attr(self):
        const = Const()
        const.add('First item', 1)
        self.assertEqual(const[0], ('1', u'First item'))
        self.assertEqual(const._1, '1')

    def test_set_different_attribute_and_value(self):
        const = Const()
        const.add(label='First item', attr="my_item", value=1)
        self.assertEqual(const[0], ('1', u'First item'))
        self.assertEqual(const.my_item, '1')

    def test_set_const_with_tuple_three_values(self):
        const = Const(('Label Test', 'Attr test', 'Value test'),
                      ('Label Test2', 'Attr test2', 'Value test2'),)

        self.assertEqual(const[0], ('VALUE_TEST', u'Label Test'))
        self.assertEqual(const.attr_test, 'VALUE_TEST')

    def test_set_const_with_tuple_four_values(self):
        const = Const(('Label Test', 'Attr test', 'Value test', 'Ignore Value'),
                      ('Label Test2', 'Attr test2', 'Value test2', 'Ignore Value'),)

        self.assertEqual(const[0], ('VALUE_TEST', u'Label Test'))
        self.assertEqual(const.attr_test, 'VALUE_TEST')


if __name__ == '__main__':
    unittest.main()
