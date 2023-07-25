import unittest
import translator
class TestTranslate(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour') self.assertEqual(translator.englishToFrench('welcome my love'), 'mon amour
    def test_f2e(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') self.assertEqual(translator.frenchToEnglish('mon amour'), 'welcome my love

if __name__ == '_main_':
    unittest.main()