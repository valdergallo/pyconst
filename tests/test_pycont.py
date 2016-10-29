# encoding: utf-8
from __future__ import unicode_literals
import unittest
from pyconst import Const


class TestConsts(unittest.TestCase):

    def setUp(self):
        self.const = Const()

    def test_slugify(self):
        self.const.add('caça vovó')
        self.assertEqual(self.const.caca_vovo, 'caca_vovo')

    def test_add_item(self):
        self.const.add('update item')
        self.assertEqual(self.const.update_item, 'update_item')

    def test_inter_pyconst(self):
        self.const.add('update item')
        for value in self.const:
            self.assertEqual(value, ('update_item', 'update item'))

    def test_set_init_values(self):
        const = Const(
            'add user',
            'create user',
            'delete user',
        )

        self.assertEqual(const.add_user, 'add_user')
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
        self.assertEqual(const.add_user, 'add_user')

    def test_add_attribute(self):
        self.const.add('Update item (new)', 'update_item')
        self.assertEqual(self.const.update_item, 'update_item')
        self.assertEqual(self.const.update_item.label, 'Update item (new)')

    def test_get_value_in_order(self):
        const = Const(
            'Add User',
            'Create User',
            'Delete User',
        )

        self.assertEqual(const[0], ('add_user', u'Add User'))

    def test_get_multiple_value_in_order(self):
        const = Const(
            ('Add User', 'add_user'),
            ('Create User', 'create_user'),
            ('Delete User', 'delete_user'),
        )

        self.assertEqual(const[0], ('add_user', u'Add User'))

    def test_get_multiple_kwargs_value_in_order(self):
        const = Const(**{'Add User': 'add_user'})
        self.assertEqual(const[0], ('add_user', u'Add User'))

    def test_slug_index_error(self):
        const = Const()
        const.add(['Add User'])
        self.assertEqual(const[0], ('add_user', u'Add User'))


if __name__ == '__main__':
    unittest.main()
