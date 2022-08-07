'''Import Modules'''
import unittest
import translator
class TestTranslatorMethods(unittest.TestCase):
    '''Translation method testing class'''
    def test_french_to_english(self):
        '''Test case takes French input, and output English'''
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

    def test_french_to_english_null_input(self):
        '''Test case takes French input, and output English for null value'''
        self.assertNotEqual(translator.french_to_english('None'), '')

    def test_english_to_french(self):
        '''Test case takes English input, and output French'''
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

    def test_english_to_french_null_input(self):
        '''Test case takes English input, and output French for null value'''
        self.assertNotEqual(translator.english_to_french('None'), '')
if __name__ == '__main__':
    unittest.main()
