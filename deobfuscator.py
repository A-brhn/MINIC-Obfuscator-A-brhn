from antlr4 import *
from MINICLexer import MINICLexer
from MINICParser import MINICParser
from MINICListener import MINICListener
from antlr4.TokenStreamRewriter import TokenStreamRewriter


# حذف کد مرده
class DeadCodeRemover(MINICListener):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)

    def enterIfStatement(self, ctx):
        cond = ctx.expr().getText().replace(" ", "")
        if cond == "false":
            # حذف کل if
            self.rewriter.delete("default", ctx.start.tokenIndex, ctx.stop.tokenIndex)

    def enterWhileStatement(self, ctx):
        cond = ctx.expr().getText().replace(" ", "")
        if cond == "false":
            # حذف کل while
            self.rewriter.delete("default", ctx.start.tokenIndex, ctx.stop.tokenIndex)

    def enterDeclaration(self, ctx):
        text = ctx.getText()
        if "unused" in text or "useless" in text:
            # حذف اعلان متغیر بی‌استفاده
            self.rewriter.delete("default", ctx.start.tokenIndex, ctx.stop.tokenIndex)




# ساده‌سازی عبارات ریاضی
class ArithmeticSimplifier(MINICListener):
    def __init__(self, token_stream):
        self.rewriter = TokenStreamRewriter(token_stream)

    def exitExpr(self, ctx):
        # تشخیص الگوی: a - (-b)
        if ctx.getChildCount() == 3:
            left = ctx.getChild(0).getText()
            op = ctx.getChild(1).getText()
            right = ctx.getChild(2).getText()

            # مثال: "x - (-y)"
            if op == "-" and right.startswith("(-") and right.endswith(")"):
                inner = right[2:-1]  # محتوای داخل پرانتز بعد از '-'
                new_expr = f"{left}+{inner}"
                self.rewriter.replaceRange(ctx.start.tokenIndex, ctx.stop.tokenIndex, new_expr)


# اجرای Pipeline
def deobfuscate(input_code: str) -> str:
    # مرحله 1: حذف کد مرده
    input_stream = InputStream(input_code)
    lexer = MINICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MINICParser(token_stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    dead_remover = DeadCodeRemover(token_stream)
    walker.walk(dead_remover, tree)
    code_no_dead = dead_remover.rewriter.getDefaultText()

    # مرحله 2: ساده‌سازی عبارات
    input_stream = InputStream(code_no_dead)
    lexer = MINICLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MINICParser(token_stream)
    tree = parser.program()

    walker = ParseTreeWalker()
    arith_simplifier = ArithmeticSimplifier(token_stream)
    walker.walk(arith_simplifier, tree)
    return arith_simplifier.rewriter.getDefaultText()

with open("output.txt", "r") as f:
    code = f.read()

cleaned = deobfuscate(code)

with open("cleaned.mc", "w") as f:
    f.write(cleaned)

print("Arithmetic expressions simplified successfully.")
