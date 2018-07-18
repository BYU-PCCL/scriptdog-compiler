grammar Scriptdog;

/*

A simple grammar for scriptdog.

*/

//
// ==================================================================
//
// PARSER RULES
//

program
    : ( named_state_definition | named_utterance_definition )*
    ;

named_state_definition
    : LST ID parameter_list? GRT LBRACE state_op_list RBRACE
    ;

named_utterance_definition
    : LSBRACE GLOBAL? ID RSBRACE LBRACE utterance_op_list RBRACE
    ;

//precompiler_directive
//    : BANG INCLUDE filename
//    ;

// ---------------------------------------------

state_op_list :  state_op* ;

utterance_op_list :  utterance_op* ;

// ---------------------------------------------

state_op
    : expect_statement
    | set_statement
    | clear_statement
    | opt_statement
    | if_statement
    | return_statement
    | named_state
    ;

utterance_op
    : LSBRACE utterance_innards_list RSBRACE 
    | LSBRACE utterance_innards_list RSBRACE LBRACE state_op_list RBRACE        
    | LSBRACE utterance_innards_list RSBRACE RTARROW named_state
    | LSBRACE ELSE RSBRACE RTARROW named_state
    | LSBRACE ELSE RSBRACE LBRACE state_op_list RBRACE
    ;

utterance_innards_list: utterance_innard+ ;

utterance_innard
    : else_uop
    | idref_uop
    | regexv_uop
    | assgn_uop
    | varref_uop        
    ;

else_uop : ELSE; // this is the utterance version, not the <if> statement version...
idref_uop : ID QUES?;
regexv_uop: STRING QUES?;
assgn_uop: ID EQ ID QUES?;
varref_uop: LBRACE ID RBRACE QUES?; // I don't think the QUES makes sense here...

// ---------------------------------------------


named_state
    : NUMBER? LST ID argument_list? GRT
    ;

expect_statement
    : NUMBER? LST EXPECT GRT LBRACE utterance_op_list RBRACE
    ;

set_statement
    : NUMBER? LST BANGSET argument_list? GRT
    ;

clear_statement
    : NUMBER? LST BANGCLEAR ID GRT
    ;

opt_statement
    : NUMBER? LST OPT GRT LBRACE state_op_list RBRACE
    ;

return_statement
    :  NUMBER? LST RETURN GRT
    ;

if_statement
    : NUMBER? LST IF LBRACE ID RBRACE GRT LBRACE state_op_list RBRACE elseif_statement_list? else_statement?
    ;

elseif_statement_list : elseif_statement+ ;

elseif_statement
    : LST ELSEIF LBRACE ID RBRACE GRT LBRACE state_op_list RBRACE
    ;
        
else_statement
    :  LST ELSE GRT LBRACE state_op_list RBRACE
    ;

// ---------------------------------------------

parameter_list
    : ( ID )+
    ;

argument_list
    : ( ID | STRING | NUMBER | varref )+
    ;

varref  : LBRACE expr RBRACE ;
expr    : ( ID | STRING | NUMBER | varref )+ ;

filename : STRING;

//
// ==================================================================
//

// these are groups of operators that have equivalent precedences

/*

g1	: ( NEQ | DOUBLE_EQ | GRTE | GRT | LSTE | LST );
g2	: ( PLUS | MINUS );
g3	: ( LEFTDIV | RIGHTDIV | TIMES | EL_LEFTDIV | EL_RIGHTDIV | EL_TIMES );
g4	: ( EXP | EL_EXP );

expression : e0 -> ^(EXPRESSION e0);

e0	: e1;

e1	: e2 (LOG_OR^ e2)*;
e2	: e3 (LOG_AND^ e3)*;
e3	: e4 (BIN_OR^ e4)*;
e4	: e5 (BIN_AND^ e5)*;
e5	: e6 (g1^ e6)*;
e6	: e7 (COLON^ e7)*;
e7	: e8 (g2^ e8)*;
e8	: e9 (g3^ e9)*;
e9	: prefix_operator^ e9 | e10;
e10	: e11 (g4^ e11)*; // note: in matlab, exponentiation is left-associative
e11	: unary_expression postfix_operator^?;

unary_expression
        : base_expression -> ^(base_expression)
        | LPAREN expression RPAREN -> ^( PARENS expression )
        ;

base_expression
        : INT
        | FLOAT
        | STRING
        ;

*/

//
// ==================================================================
//
// LEXER RULES
//

RTARROW : '->';
QUES    : '?';
BANG    : '!';

//
// language keywords
//

GLOBAL  : 'global';
EXPECT  : 'expect';
INCLUDE : 'include';
OPT     : 'opt';
RETURN  : 'return';
BANGSET : '!set';
BANGCLEAR : '!clear';

IF      : 'if';
ELSE    : 'else';
ELSEIF  : 'elseif';

TRUE    : 'true';
FALSE   : 'false';

//
// operators and assignments
//

LST     : '<';
GRT     : '>';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LSBRACE : '[';
RSBRACE : ']';

EQ      : '=';

PIPE    : '|';
DOUBLE_EQ       : '==';
LOG_OR  : '||';
LOG_AND : '&&';
LSTE    : '<=';
GRTE    : '>=';
NEQ     : '~=';
PLUS    : '+';
MINUS   : '-';
NEG     : '~';
TIMES   : '*';
LEFTDIV : '/';
EXP     : '^';

//
// identifiers, strings, numbers, whitespace
//

BOOLEAN : ( TRUE | FALSE ) ;

ID      : ('a'..'z'|'A'..'Z'|'0'..'9'|'_')+ ;

NUMBER  : ( INT | FLOAT ) ;

INT     : '0'..'9'+ ;

FLOAT
        : ('0'..'9')+ '.' ('0'..'9')* EXPONENT?
        | '.' ('0'..'9')+ EXPONENT?
        | ('0'..'9')+ EXPONENT
        ;

STRING
        : '"' ( ESC_SEQ | ~('"') )* '"'  // not sure why this is a problem... |'\"'
        ;

fragment
EXPONENT
        : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;

fragment
HEX_DIGIT
        : ('0'..'9'|'a'..'f'|'A'..'F') ;

fragment
ESC_SEQ
        : '\\' ('b'|'t'|'n'|'f'|'r'|'\''|'\\'|'"')  // not sure why this throws a warning... |'\"'
        | UNICODE_ESC
        | OCTAL_ESC
        ;

fragment
OCTAL_ESC
        : '\\' ('0'..'3') ('0'..'7') ('0'..'7')
        | '\\' ('0'..'7') ('0'..'7')
        | '\\' ('0'..'7')
        ;

fragment
UNICODE_ESC
        : '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
        ;

//WS: [ \n\t\r]+ -> channel(HIDDEN);

//
// comments and whitespace
//

ML_COMMENT      : '/*' ( . | EOL )*? '*/' -> skip;
WS              : [ \t] -> skip;
EOL             : [\r\n] -> skip;
SL_COMMENT      : '//' ( . )*? EOL -> skip;
SL2_COMMENT     : '#' ( . )*? EOL -> skip;
