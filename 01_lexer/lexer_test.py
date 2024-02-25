import sys
import unittest
sys.path.append('..')  # Adjust the path if needed
import lexer

class TestLexer(unittest.TestCase):
    def test_basic_ints(self):
        data = '0\n1\n-1\n12\n-21\n123\n-123'
        lexer.lexer.input(data)
        expected_tokens = [
            ('INT_LITERAL', 0),
            ('INT_LITERAL', 1),
            ('INT_LITERAL', -1),
            ('INT_LITERAL', 12),
            ('INT_LITERAL', -21),
            ('INT_LITERAL', 123),
            ('INT_LITERAL', -123)
        ]
        self.assertLexerOutput(expected_tokens)

    def test_basic_date(self):
        data = '1582-12-11'
        lexer.lexer.input(data)
        expected_tokens = [('DATE_LITERAL', '1582-12-11')]
        self.assertLexerOutput(expected_tokens)

    def test_func_idets(self):
        data = 'Bjflasdkjfl70098'
        lexer.lexer.input(data)
        expected_tokens = [('FUNC_IDENT', 'Bjflasdkjfl70098')]
        self.assertLexerOutput(expected_tokens)

    def test_idets(self):
        data = 'nvxczcluuioe_fhsdlafh_vbhalk'
        lexer.lexer.input(data)
        expected_tokens = [('IDENT', 'nvxczcluuioe_fhsdlafh_vbhalk')]
        self.assertLexerOutput(expected_tokens)

    def test_one_letter_tokens(self):
        data = '&'
        lexer.lexer.input(data)
        expected_tokens = [('AMPERSAND', '&')]
        self.assertLexerOutput(expected_tokens)

    # Define additional test cases if needed

    def assertLexerOutput(self, expected_tokens):
        actual_tokens = []
        while True:
            tok = lexer.lexer.token()
            if not tok:
                break
            actual_tokens.append((tok.type, tok.value))
        self.assertEqual(actual_tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()
