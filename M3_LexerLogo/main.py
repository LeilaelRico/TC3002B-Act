"""
* Cristian Leilael Rico Espinosa
* Implementando un lexer para Logo
"""

from Lexer import *
import sys

if __name__ == '__main__':
	lexer = Lexer(".\\M4_LexerLogo\\test_cases\\prog1.txt")
	
	token = lexer.scan()
	while token.getTag() != Tag.EOF:
		print(str(token))
		token = lexer.scan()
	print("END")

