import random
import string
from antlr4 import *
from MINICLexer import MINICLexer
from MINICParser import MINICParser
from MINICListener import MINICListener
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class IDCollector(MINICListener):
    def __init__(self, parser):
        self.ids = set()
        self.parser = parser

    def visitTerminal(self, node):
        if node.symbol.type == self.parser.ID:
            self.ids.add(node.getText())

def obfuscate_ids(input_code):
    input_stream = InputStream(input_code)
    lexer = MINICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MINICParser(token_stream)
    tree = parser.program()

    collector = IDCollector(parser)
    walker = ParseTreeWalker()
    walker.walk(collector, tree)

    id_list = list(collector.ids)
    print(id_list)

    def generate_random_name(length=5):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    rename_map = {id_: generate_random_name() for id_ in id_list}

    rewriter = TokenStreamRewriter(token_stream)

    for token in token_stream.tokens:
        if token.type == parser.ID:
            original = token.text
            if original in rename_map:
                rewriter.replaceSingleToken(token,' ' + rename_map[original])

    return rewriter.getDefaultText(), rename_map

def execute():
    with open("example.txt", "r") as f:
        code = f.read()

    obfuscated_code, id_map = obfuscate_ids(code)

    with open("output.txt", "w") as f:
        f.write(obfuscated_code)

    print("Obfuscation done.")
