import random
from antlr4 import *
from MINICLexer import MINICLexer
from MINICParser import MINICParser
from MINICListener import MINICListener
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class DeadCodeInserter(MINICListener):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)

    def enterBlock(self, ctx):
        insert_code = random.choice([
            "int unused = 1234;",
            "if (false) { int dummy = 0; }",
            "while (false) { int nothing = 0; }"
        ])

        lbrace_token = ctx.getChild(0).getSymbol() 
        self.rewriter.insertAfterToken(lbrace_token, f"\n    {insert_code}")

def insert_dead_code(input_code):
    input_stream = InputStream(input_code)
    lexer = MINICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MINICParser(token_stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    listener = DeadCodeInserter(token_stream)
    walker.walk(listener, tree)

    return listener.rewriter.getDefaultText()

def execute():
    with open("output.txt", "r") as f:
        code = f.read()

    modified_code = insert_dead_code(code)

    with open("output.txt", "w") as f:
        f.write(modified_code)

    print("Dead code inserted successfully.")
