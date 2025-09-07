grammar MINIC;

program: (function | statement)* EOF;

function
    : type ID '(' params? ')' block
    ;

params
    : param (',' param)*
    ;

param
    : type ID
    ;

statement
    : declaration
    | assignment
    | ifStatement
    | whileStatement
    | forStatement
    | scanfCall
    | printfCall
    | returnStatement
    | block
    | ';' // empty statement
    ;

declaration
    : type ID ('=' expr)? ';'
    ;

assignment
    : ID '=' expr ';'
    ;
	
assigninfor
    : ID '=' expr
    ;

ifStatement
    : 'if' '(' expr ')' statement ('else' statement)?
    ;

whileStatement
    : 'while' '(' expr ')' statement
    ;

forStatement
    : 'for' '(' (declaration | assignment) expr ';' assigninfor ')' statement
    ;

scanfCall
    : 'scanf' '(' STRING ',' '&'? ID ')' ';'
    ;

printfCall
    : 'printf' '(' STRING (',' expr)? ')' ';'
    ;

returnStatement
    : 'return' expr? ';'
    ;

block
    : '{' statement* '}'
    ;
	
expr
    : '-' expr                
    | expr op=('+'|'-') expr
    | expr op=('*'|'/') expr
    | expr op=('=='|'!='|'<'|'>'|'<='|'>=') expr
    | '(' expr ')'
    | ID
    | INT
    | CHAR
    | BOOL
    ;


type: 'int' | 'char' | 'bool';

BOOL: 'true' | 'false';
ID  : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9]+;
CHAR: '\'' . '\'';
STRING: '"' .*? '"';

WS  : [ \t\r\n]+ -> channel(HIDDEN);
COMMENT: '//' ~[\r\n]* -> skip;
