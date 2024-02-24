import sys
import unittest
sys.path.append('..')  # Adjust the path if needed
import lexer

class TestLexer(unittest.TestCase):
    def test_single_integer_literal(self):
        data = '123'
        lexer.lexer.input(data)
        expected_tokens = [
            ('INT_LITERAL', 123)
        ]
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
