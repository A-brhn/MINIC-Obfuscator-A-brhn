# Generated from MINIC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MINICParser import MINICParser
else:
    from MINICParser import MINICParser

# This class defines a complete listener for a parse tree produced by MINICParser.
class MINICListener(ParseTreeListener):

    # Enter a parse tree produced by MINICParser#program.
    def enterProgram(self, ctx:MINICParser.ProgramContext):
        pass

    # Exit a parse tree produced by MINICParser#program.
    def exitProgram(self, ctx:MINICParser.ProgramContext):
        pass


    # Enter a parse tree produced by MINICParser#function.
    def enterFunction(self, ctx:MINICParser.FunctionContext):
        pass

    # Exit a parse tree produced by MINICParser#function.
    def exitFunction(self, ctx:MINICParser.FunctionContext):
        pass


    # Enter a parse tree produced by MINICParser#params.
    def enterParams(self, ctx:MINICParser.ParamsContext):
        pass

    # Exit a parse tree produced by MINICParser#params.
    def exitParams(self, ctx:MINICParser.ParamsContext):
        pass


    # Enter a parse tree produced by MINICParser#param.
    def enterParam(self, ctx:MINICParser.ParamContext):
        pass

    # Exit a parse tree produced by MINICParser#param.
    def exitParam(self, ctx:MINICParser.ParamContext):
        pass


    # Enter a parse tree produced by MINICParser#statement.
    def enterStatement(self, ctx:MINICParser.StatementContext):
        pass

    # Exit a parse tree produced by MINICParser#statement.
    def exitStatement(self, ctx:MINICParser.StatementContext):
        pass


    # Enter a parse tree produced by MINICParser#declaration.
    def enterDeclaration(self, ctx:MINICParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MINICParser#declaration.
    def exitDeclaration(self, ctx:MINICParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MINICParser#assignment.
    def enterAssignment(self, ctx:MINICParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MINICParser#assignment.
    def exitAssignment(self, ctx:MINICParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MINICParser#assigninfor.
    def enterAssigninfor(self, ctx:MINICParser.AssigninforContext):
        pass

    # Exit a parse tree produced by MINICParser#assigninfor.
    def exitAssigninfor(self, ctx:MINICParser.AssigninforContext):
        pass


    # Enter a parse tree produced by MINICParser#ifStatement.
    def enterIfStatement(self, ctx:MINICParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MINICParser#ifStatement.
    def exitIfStatement(self, ctx:MINICParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MINICParser#whileStatement.
    def enterWhileStatement(self, ctx:MINICParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MINICParser#whileStatement.
    def exitWhileStatement(self, ctx:MINICParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MINICParser#forStatement.
    def enterForStatement(self, ctx:MINICParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MINICParser#forStatement.
    def exitForStatement(self, ctx:MINICParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MINICParser#scanfCall.
    def enterScanfCall(self, ctx:MINICParser.ScanfCallContext):
        pass

    # Exit a parse tree produced by MINICParser#scanfCall.
    def exitScanfCall(self, ctx:MINICParser.ScanfCallContext):
        pass


    # Enter a parse tree produced by MINICParser#printfCall.
    def enterPrintfCall(self, ctx:MINICParser.PrintfCallContext):
        pass

    # Exit a parse tree produced by MINICParser#printfCall.
    def exitPrintfCall(self, ctx:MINICParser.PrintfCallContext):
        pass


    # Enter a parse tree produced by MINICParser#returnStatement.
    def enterReturnStatement(self, ctx:MINICParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MINICParser#returnStatement.
    def exitReturnStatement(self, ctx:MINICParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MINICParser#block.
    def enterBlock(self, ctx:MINICParser.BlockContext):
        pass

    # Exit a parse tree produced by MINICParser#block.
    def exitBlock(self, ctx:MINICParser.BlockContext):
        pass


    # Enter a parse tree produced by MINICParser#expr.
    def enterExpr(self, ctx:MINICParser.ExprContext):
        pass

    # Exit a parse tree produced by MINICParser#expr.
    def exitExpr(self, ctx:MINICParser.ExprContext):
        pass


    # Enter a parse tree produced by MINICParser#type.
    def enterType(self, ctx:MINICParser.TypeContext):
        pass

    # Exit a parse tree produced by MINICParser#type.
    def exitType(self, ctx:MINICParser.TypeContext):
        pass



del MINICParser