import unittest

from dictionary.dictionary import generate_dictionary


class Testtest(unittest.TestCase):

    def test_dictionary(self):
        self.assertEqual(generate_dictionary(2, 15), {x: x*x for x in range(2, 15)})

    def test_dictionary_range_values(self):
        with self.assertRaises(ValueError):
            generate_dictionary('a', 'b')


if __name__ == '__main__':
    unittest.main()
