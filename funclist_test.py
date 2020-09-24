import unittest
from funclist import *

class TestFuncList(unittest.TestCase):

    def test_item_count_simple(self):
        self.assertEqual(0, item_count(None))
        self.assertEqual(1, item_count(FuncList(4, None)))
        self.assertEqual(1, item_count(FuncList(122, None)))
        self.assertEqual(4, item_count(FuncList(1, FuncList(2, FuncList(3, FuncList(4,None))))))


    def test_convert_to_funclist(self):
        reglist = [1, 2, 3, 4]
        funclist = FuncList(1, FuncList(2, FuncList(3, FuncList(4,None))))

        self.assertEqual(funclist, convert_to_funclist(reglist))
        self.assertNotEqual(funclist.tail, convert_to_funclist(reglist))
        self.assertEqual(None, convert_to_funclist([]))
        self.assertEqual(FuncList(7, None), convert_to_funclist([7]))


    def test_convert_to_reglist(self):
        reglist = [1, 2, 3, 4]
        funclist = FuncList(1, FuncList(2, FuncList(3, FuncList(4,None))))

        self.assertEqual(reglist, convert_to_reglist(funclist))
        self.assertNotEqual([2, 3, 4], convert_to_reglist(funclist))
        self.assertEqual([], convert_to_reglist(None))
        self.assertEqual([7], convert_to_reglist(FuncList(7, None)))

    def test_item_count_complex(self):
        self.assertEqual(0, item_count(convert_to_funclist([])))
        self.assertEqual(950, item_count(convert_to_funclist(list(range(950)))))