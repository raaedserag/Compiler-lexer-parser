from parsing import parser
from lexer import Lexer

lexed = Lexer()
parsed = (parser(lexed))        # Returns Syntax Error or Succes
print(parsed)
