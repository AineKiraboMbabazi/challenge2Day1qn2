from dictionary import dictionary
import unittest


class Testtest(unittest.TestCase):

    def test_dictionary(self):
        self.assertEqual(dictionary(2,15), {x:x*x for x in range(2,15)})
        
        
          
    def test_dictionary_range_values(self):
       with self.assertRaises(ValueError):
        dictionary('a','b')



if __name__ == '__main__':
    unittest.main()