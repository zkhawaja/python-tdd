import unittest

from codetest import *
class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(),'hello world')
    def test_1_score(self):
        self.assertEqual(scorecalculation(15,'Joseph'),'66%')
    def test_2_score(self):
        self.assertEqual(scorecalculation(33,'Marie'),'50%')
    def test_3_score(self):
        self.assertEqual(scorecalculation(60,'Marc'),'43%')
    def test_4_score(self):
        self.assertEqual(scorecalculation(28,'Ely'),'75%')



# si on n'est pas en pycharm il faut préciser qu'il s'agit d'un test en écrivant
if __name__ == '__main__':
   unittest.main()
