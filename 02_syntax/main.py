import sys
import argparse
from lexer import lexer
from syntax_check import parser

# Command-line argument parsing
def parse_arguments():
    parser = argparse.ArgumentParser(description="PostHaste Syntax Checker")
    parser.add_argument("-f", "--file", help="filename to process")
    parser.add_argument('--who', action='store_true', help='print out student IDs and NAMEs of authors')
    parser.add_argument("-d", "--debug", action="store_true", help="activate debug mode in PLY")
    return parser.parse_args()

# Main function
def main():
    args = parse_arguments()

    if args.who:
        # Print student IDs and NAMES
        print('152103143 Minh Hoang')
        return

    if args.file:
        # Read input file
        with open(args.file, "r") as file:
            input_data = file.read()

        # Tokenize and parse input
        lexer.input(input_data)
        parser.parse(input_data, lexer=lexer)

if __name__ == "__main__":
    main()
