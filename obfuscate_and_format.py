from antlr4 import *
from MINICLexer import MINICLexer
from MINICParser import MINICParser
from MINICListener import MINICListener
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class ObfuscateArithmetic(MINICListener):
    def __init__(self, token_stream, parser):
        self.rewriter = TokenStreamRewriter(token_stream)
        self.token_stream = token_stream
        self.parser = parser

    def exitExpr(self, ctx):
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            if op == '+':
                new_expr = f"{left} - (-{right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)

            elif op == '-':
                new_expr = f"{left} + (-{right})"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)

def obfuscate_arithmetic_ops(input_code):
    input_stream = InputStream(input_code)
    lexer = MINICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MINICParser(token_stream)
    tree = parser.program()

    listener = ObfuscateArithmetic(token_stream, parser)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.rewriter.getDefaultText()
def execute():
    with open("output.txt", "r") as f:
        code = f.read()

    obfuscated_code = obfuscate_arithmetic_ops(code)

    with open("output.txt", "w") as f:
        f.write(obfuscated_code)

    print("Obfuscation of arithmetic expressions done.")
