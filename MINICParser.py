# Generated from MINIC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,5,0,37,8,0,10,0,12,0,40,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,
        56,8,2,10,2,12,2,59,9,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,74,8,4,1,5,1,5,1,5,1,5,3,5,80,8,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,100,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,112,8,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,125,8,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,136,8,12,1,
        12,1,12,1,12,1,13,1,13,3,13,143,8,13,1,13,1,13,1,14,1,14,5,14,149,
        8,14,10,14,12,14,152,9,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,165,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,5,15,176,8,15,10,15,12,15,179,9,15,1,16,1,16,1,16,0,1,
        30,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,4,1,0,16,17,
        1,0,18,19,1,0,20,25,1,0,26,28,192,0,38,1,0,0,0,2,43,1,0,0,0,4,52,
        1,0,0,0,6,60,1,0,0,0,8,73,1,0,0,0,10,75,1,0,0,0,12,83,1,0,0,0,14,
        88,1,0,0,0,16,92,1,0,0,0,18,101,1,0,0,0,20,107,1,0,0,0,22,119,1,
        0,0,0,24,130,1,0,0,0,26,140,1,0,0,0,28,146,1,0,0,0,30,164,1,0,0,
        0,32,180,1,0,0,0,34,37,3,2,1,0,35,37,3,8,4,0,36,34,1,0,0,0,36,35,
        1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,
        40,38,1,0,0,0,41,42,5,0,0,1,42,1,1,0,0,0,43,44,3,32,16,0,44,45,5,
        30,0,0,45,47,5,1,0,0,46,48,3,4,2,0,47,46,1,0,0,0,47,48,1,0,0,0,48,
        49,1,0,0,0,49,50,5,2,0,0,50,51,3,28,14,0,51,3,1,0,0,0,52,57,3,6,
        3,0,53,54,5,3,0,0,54,56,3,6,3,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,
        1,0,0,0,57,58,1,0,0,0,58,5,1,0,0,0,59,57,1,0,0,0,60,61,3,32,16,0,
        61,62,5,30,0,0,62,7,1,0,0,0,63,74,3,10,5,0,64,74,3,12,6,0,65,74,
        3,16,8,0,66,74,3,18,9,0,67,74,3,20,10,0,68,74,3,22,11,0,69,74,3,
        24,12,0,70,74,3,26,13,0,71,74,3,28,14,0,72,74,5,4,0,0,73,63,1,0,
        0,0,73,64,1,0,0,0,73,65,1,0,0,0,73,66,1,0,0,0,73,67,1,0,0,0,73,68,
        1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,
        74,9,1,0,0,0,75,76,3,32,16,0,76,79,5,30,0,0,77,78,5,5,0,0,78,80,
        3,30,15,0,79,77,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,4,0,
        0,82,11,1,0,0,0,83,84,5,30,0,0,84,85,5,5,0,0,85,86,3,30,15,0,86,
        87,5,4,0,0,87,13,1,0,0,0,88,89,5,30,0,0,89,90,5,5,0,0,90,91,3,30,
        15,0,91,15,1,0,0,0,92,93,5,6,0,0,93,94,5,1,0,0,94,95,3,30,15,0,95,
        96,5,2,0,0,96,99,3,8,4,0,97,98,5,7,0,0,98,100,3,8,4,0,99,97,1,0,
        0,0,99,100,1,0,0,0,100,17,1,0,0,0,101,102,5,8,0,0,102,103,5,1,0,
        0,103,104,3,30,15,0,104,105,5,2,0,0,105,106,3,8,4,0,106,19,1,0,0,
        0,107,108,5,9,0,0,108,111,5,1,0,0,109,112,3,10,5,0,110,112,3,12,
        6,0,111,109,1,0,0,0,111,110,1,0,0,0,112,113,1,0,0,0,113,114,3,30,
        15,0,114,115,5,4,0,0,115,116,3,14,7,0,116,117,5,2,0,0,117,118,3,
        8,4,0,118,21,1,0,0,0,119,120,5,10,0,0,120,121,5,1,0,0,121,122,5,
        33,0,0,122,124,5,3,0,0,123,125,5,11,0,0,124,123,1,0,0,0,124,125,
        1,0,0,0,125,126,1,0,0,0,126,127,5,30,0,0,127,128,5,2,0,0,128,129,
        5,4,0,0,129,23,1,0,0,0,130,131,5,12,0,0,131,132,5,1,0,0,132,135,
        5,33,0,0,133,134,5,3,0,0,134,136,3,30,15,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,137,1,0,0,0,137,138,5,2,0,0,138,139,5,4,0,0,139,25,1,
        0,0,0,140,142,5,13,0,0,141,143,3,30,15,0,142,141,1,0,0,0,142,143,
        1,0,0,0,143,144,1,0,0,0,144,145,5,4,0,0,145,27,1,0,0,0,146,150,5,
        14,0,0,147,149,3,8,4,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,
        0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,5,
        15,0,0,154,29,1,0,0,0,155,156,6,15,-1,0,156,157,5,1,0,0,157,158,
        3,30,15,0,158,159,5,2,0,0,159,165,1,0,0,0,160,165,5,30,0,0,161,165,
        5,31,0,0,162,165,5,32,0,0,163,165,5,29,0,0,164,155,1,0,0,0,164,160,
        1,0,0,0,164,161,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,177,
        1,0,0,0,166,167,10,8,0,0,167,168,7,0,0,0,168,176,3,30,15,9,169,170,
        10,7,0,0,170,171,7,1,0,0,171,176,3,30,15,8,172,173,10,6,0,0,173,
        174,7,2,0,0,174,176,3,30,15,7,175,166,1,0,0,0,175,169,1,0,0,0,175,
        172,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,
        31,1,0,0,0,179,177,1,0,0,0,180,181,7,3,0,0,181,33,1,0,0,0,15,36,
        38,47,57,73,79,99,111,124,135,142,150,164,175,177
    ]

class MINICParser ( Parser ):

    grammarFileName = "MINIC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "'='", "'if'", 
                     "'else'", "'while'", "'for'", "'scanf'", "'&'", "'printf'", 
                     "'return'", "'{'", "'}'", "'*'", "'/'", "'+'", "'-'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'int'", 
                     "'char'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "ID", "INT", "CHAR", "STRING", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_params = 2
    RULE_param = 3
    RULE_statement = 4
    RULE_declaration = 5
    RULE_assignment = 6
    RULE_assigninfor = 7
    RULE_ifStatement = 8
    RULE_whileStatement = 9
    RULE_forStatement = 10
    RULE_scanfCall = 11
    RULE_printfCall = 12
    RULE_returnStatement = 13
    RULE_block = 14
    RULE_expr = 15
    RULE_type = 16

    ruleNames =  [ "program", "function", "params", "param", "statement", 
                   "declaration", "assignment", "assigninfor", "ifStatement", 
                   "whileStatement", "forStatement", "scanfCall", "printfCall", 
                   "returnStatement", "block", "expr", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    BOOL=29
    ID=30
    INT=31
    CHAR=32
    STRING=33
    WS=34
    COMMENT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MINICParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MINICParser.FunctionContext)
            else:
                return self.getTypedRuleContext(MINICParser.FunctionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MINICParser.StatementContext)
            else:
                return self.getTypedRuleContext(MINICParser.StatementContext,i)


        def getRuleIndex(self):
            return MINICParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MINICParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1543534416) != 0):
                self.state = 36
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 34
                    self.function()
                    pass

                elif la_ == 2:
                    self.state = 35
                    self.statement()
                    pass


                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(MINICParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MINICParser.TypeContext,0)


        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(MINICParser.BlockContext,0)


        def params(self):
            return self.getTypedRuleContext(MINICParser.ParamsContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = MINICParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.type_()
            self.state = 44
            self.match(MINICParser.ID)
            self.state = 45
            self.match(MINICParser.T__0)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0):
                self.state = 46
                self.params()


            self.state = 49
            self.match(MINICParser.T__1)
            self.state = 50
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MINICParser.ParamContext)
            else:
                return self.getTypedRuleContext(MINICParser.ParamContext,i)


        def getRuleIndex(self):
            return MINICParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = MINICParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.param()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 53
                self.match(MINICParser.T__2)
                self.state = 54
                self.param()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MINICParser.TypeContext,0)


        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def getRuleIndex(self):
            return MINICParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MINICParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.type_()
            self.state = 61
            self.match(MINICParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MINICParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MINICParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MINICParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MINICParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MINICParser.ForStatementContext,0)


        def scanfCall(self):
            return self.getTypedRuleContext(MINICParser.ScanfCallContext,0)


        def printfCall(self):
            return self.getTypedRuleContext(MINICParser.PrintfCallContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MINICParser.ReturnStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(MINICParser.BlockContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MINICParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.declaration()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.assignment()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.ifStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.whileStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.forStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.scanfCall()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.printfCall()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.returnStatement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 9)
                self.state = 71
                self.block()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 10)
                self.state = 72
                self.match(MINICParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MINICParser.TypeContext,0)


        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = MINICParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.type_()
            self.state = 76
            self.match(MINICParser.ID)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 77
                self.match(MINICParser.T__4)
                self.state = 78
                self.expr(0)


            self.state = 81
            self.match(MINICParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = MINICParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(MINICParser.ID)
            self.state = 84
            self.match(MINICParser.T__4)
            self.state = 85
            self.expr(0)
            self.state = 86
            self.match(MINICParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigninforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_assigninfor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigninfor" ):
                listener.enterAssigninfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigninfor" ):
                listener.exitAssigninfor(self)




    def assigninfor(self):

        localctx = MINICParser.AssigninforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assigninfor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MINICParser.ID)
            self.state = 89
            self.match(MINICParser.T__4)
            self.state = 90
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MINICParser.StatementContext)
            else:
                return self.getTypedRuleContext(MINICParser.StatementContext,i)


        def getRuleIndex(self):
            return MINICParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = MINICParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MINICParser.T__5)
            self.state = 93
            self.match(MINICParser.T__0)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.match(MINICParser.T__1)
            self.state = 96
            self.statement()
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(MINICParser.T__6)
                self.state = 98
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(MINICParser.StatementContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = MINICParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(MINICParser.T__7)
            self.state = 102
            self.match(MINICParser.T__0)
            self.state = 103
            self.expr(0)
            self.state = 104
            self.match(MINICParser.T__1)
            self.state = 105
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def assigninfor(self):
            return self.getTypedRuleContext(MINICParser.AssigninforContext,0)


        def statement(self):
            return self.getTypedRuleContext(MINICParser.StatementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(MINICParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MINICParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = MINICParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MINICParser.T__8)
            self.state = 108
            self.match(MINICParser.T__0)
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27, 28]:
                self.state = 109
                self.declaration()
                pass
            elif token in [30]:
                self.state = 110
                self.assignment()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 113
            self.expr(0)
            self.state = 114
            self.match(MINICParser.T__3)
            self.state = 115
            self.assigninfor()
            self.state = 116
            self.match(MINICParser.T__1)
            self.state = 117
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanfCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MINICParser.STRING, 0)

        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def getRuleIndex(self):
            return MINICParser.RULE_scanfCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanfCall" ):
                listener.enterScanfCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanfCall" ):
                listener.exitScanfCall(self)




    def scanfCall(self):

        localctx = MINICParser.ScanfCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_scanfCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MINICParser.T__9)
            self.state = 120
            self.match(MINICParser.T__0)
            self.state = 121
            self.match(MINICParser.STRING)
            self.state = 122
            self.match(MINICParser.T__2)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 123
                self.match(MINICParser.T__10)


            self.state = 126
            self.match(MINICParser.ID)
            self.state = 127
            self.match(MINICParser.T__1)
            self.state = 128
            self.match(MINICParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MINICParser.STRING, 0)

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_printfCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintfCall" ):
                listener.enterPrintfCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintfCall" ):
                listener.exitPrintfCall(self)




    def printfCall(self):

        localctx = MINICParser.PrintfCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_printfCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MINICParser.T__11)
            self.state = 131
            self.match(MINICParser.T__0)
            self.state = 132
            self.match(MINICParser.STRING)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 133
                self.match(MINICParser.T__2)
                self.state = 134
                self.expr(0)


            self.state = 137
            self.match(MINICParser.T__1)
            self.state = 138
            self.match(MINICParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MINICParser.ExprContext,0)


        def getRuleIndex(self):
            return MINICParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = MINICParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MINICParser.T__12)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063682) != 0):
                self.state = 141
                self.expr(0)


            self.state = 144
            self.match(MINICParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MINICParser.StatementContext)
            else:
                return self.getTypedRuleContext(MINICParser.StatementContext,i)


        def getRuleIndex(self):
            return MINICParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MINICParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MINICParser.T__13)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1543534416) != 0):
                self.state = 147
                self.statement()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(MINICParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MINICParser.ExprContext)
            else:
                return self.getTypedRuleContext(MINICParser.ExprContext,i)


        def ID(self):
            return self.getToken(MINICParser.ID, 0)

        def INT(self):
            return self.getToken(MINICParser.INT, 0)

        def CHAR(self):
            return self.getToken(MINICParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(MINICParser.BOOL, 0)

        def getRuleIndex(self):
            return MINICParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MINICParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 156
                self.match(MINICParser.T__0)
                self.state = 157
                self.expr(0)
                self.state = 158
                self.match(MINICParser.T__1)
                pass
            elif token in [30]:
                self.state = 160
                self.match(MINICParser.ID)
                pass
            elif token in [31]:
                self.state = 161
                self.match(MINICParser.INT)
                pass
            elif token in [32]:
                self.state = 162
                self.match(MINICParser.CHAR)
                pass
            elif token in [29]:
                self.state = 163
                self.match(MINICParser.BOOL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = MINICParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 167
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MINICParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 170
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 171
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MINICParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 173
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 174
                        self.expr(7)
                        pass

             
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MINICParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = MINICParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




