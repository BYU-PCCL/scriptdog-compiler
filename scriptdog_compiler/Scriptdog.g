grammar Scriptdog;

/*

A simple grammar for Scriptdog.

*/

tokens { INDENT, DEDENT }

@lexer::header {
import re
from . ScriptdogParser import ScriptdogParser
from antlr4.Token import CommonToken    
    }

@lexer::members {
    # A queue where extra tokens are pushed on (see the NEWLINE lexer rule).
    self.tokens = []

    # The stack that keeps track of the indentation level.
    self.indents = []
  
    # The amount of opened braces, brackets and parenthesis.
    self.opened = 0
      
    # The most recently produced token.
    self.lastToken = None
      
def emitToken(self,t):
#    print("Emitting token [%s]" % str(t) )
    super().emitToken(t)
    self.tokens.append(t)

def nextToken( self ):
  # Check if the end-of-file is ahead and there are still some DEDENTS expected.
  if self._input.LA(1) == ScriptdogParser.EOF and len(self.indents) > 0:
    # Remove any trailing EOF tokens from our buffer.
    while len(self.tokens) > 0 and self.tokens[-1].type == ScriptdogParser.EOF:
      self.tokens.pop()
    
    # First emit an extra line break that serves as the end of the statement.
    self.emitToken( self.commonToken(ScriptdogParser.NEWLINE, "\n") )

    # Now emit as much DEDENT tokens as needed.
    while len(self.indents) > 0:
      self.emitToken( self.createDedent() )
      self.indents.pop()

    # Put the EOF back on the token stream.
    self.emitToken( self.commonToken(ScriptdogParser.EOF, "<EOF>") )

  next = super().nextToken()

  if next.channel == Token.DEFAULT_CHANNEL:
    # Keep track of the last token on the default channel.
    self.lastToken = next

  if len( self.tokens ) == 0:
    return next
  else:
    # dequeue the first item from list
    return self.tokens.pop(0)

def createDedent( self ):
  dedent = self.commonToken( ScriptdogParser.DEDENT, "" )
  dedent.line = self.lastToken.line
  return dedent

def commonToken( self, _type, text ):
  stop = self.getCharIndex() - 1
  if len(text) == 0:
    start = stop
  else:
    start = stop - len(text) + 1
  return CommonToken( self._tokenFactorySourcePair, _type, self.DEFAULT_TOKEN_CHANNEL, start, stop )

    
  # Calculates the indentation of the provided spaces, taking the
  # following rules into account:
  #
  # "Tabs are replaced (from left to right) by one to eight spaces
  #  such that the total number of characters up to and including
  #  the replacement is a multiple of eight [...]"
  #
  #  -- https://docs.python.org/3.1/reference/lexical_analysis.html#indentation
def getIndentationCount( self, spaces ):
  count = 0
  for ch in spaces:
    if ch == '\t':
      count += 8 - (count % 8)
    else:
      # A normal space char.
      count += 1

  return count

def atStartOfInput( self ):
  return ( super().column == 0 ) and ( super().line == 1 )
}

//
// ==================================================================
//
// PARSER RULES
//

program
    : ( NEWLINE | named_state_definition | named_utterance_definition )* EOF
    ;

named_state_definition
    : 'def' ID '(' parameter_list? ')' ':' NEWLINE INDENT state_op_list DEDENT
    ;

named_utterance_definition
    : 'def' GLOBAL? '[' ID ']' ':' NEWLINE INDENT utterance_op_list DEDENT
    ;

// ---------------------------------------------

state_op_list :  state_op* ;

utterance_op_list :  utterance_op* ;

// ---------------------------------------------

state_op
    : expect_statement  // these are compound statements that end with dedents
    | choice_statement
    | if_statement
    | set_statement NEWLINE // regular one-liners end with newlines
    | clear_statement NEWLINE
    | return_statement NEWLINE
    | named_state NEWLINE
    ;

utterance_op
    : LSBRACE utterance_innards_list RSBRACE NEWLINE
    | LSBRACE utterance_innards_list RSBRACE ':' NEWLINE INDENT state_op_list DEDENT
    | LSBRACE utterance_innards_list RSBRACE RTARROW named_state NEWLINE
    | LSBRACE ELSE RSBRACE RTARROW named_state NEWLINE
    | LSBRACE ELSE RSBRACE ':' NEWLINE INDENT state_op_list DEDENT
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
    : NUMBER? ID '(' argument_list? ')'
    ;

set_statement
    : NUMBER? SETBANG '(' argument_list? ')'
    ;

clear_statement
    : NUMBER? CLEARBANG '(' ID ')'
    ;

return_statement
    : NUMBER? RETURN argument_list?
    ;

// ---------------------------------------------

expect_statement
    : NUMBER? EXPECT ':' NEWLINE INDENT utterance_op_list DEDENT
    ;

choice_statement
    : NUMBER? CHOICE ':' NEWLINE INDENT state_op_list DEDENT
    ;

if_statement
    : NUMBER? IF ID ':' NEWLINE INDENT state_op_list DEDENT elseif_statement_list? else_statement?
    ;

elseif_statement_list : elseif_statement+ ;

elseif_statement
    : ELSEIF ID ':' NEWLINE INDENT state_op_list DEDENT
    ;
        
else_statement
    :  ELSE ':' NEWLINE INDENT state_op_list DEDENT
    ;

// ---------------------------------------------

parameter_list
    : ID ( ',' ID )*
    ;

argument_list
    : ( ID | STRING | NUMBER | varref ) ( ',' ( ID | STRING | NUMBER | varref ) )*
    ;

varref  : LBRACE expr RBRACE ;
expr    : ( ID | STRING | NUMBER | varref )+ ;

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
CHOICE  : 'choice';
RETURN  : 'return';
SETBANG : 'set!';
CLEARBANG : 'clear!';

IF      : 'if';
ELSE    : 'else';
ELSEIF  : 'elseif';

TRUE    : 'True';
FALSE   : 'False';

DEF     : 'def';


NEWLINE
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
   )
   {

newLine = re.sub( "[^\r\n\f]+", "", self.text )
spaces = re.sub( "[\r\n\f]+", "", self.text )

next = self._input.LA(1)
#print( "next = [%s]" % str(next) )
if next == ScriptdogParser.EOF:
  chr_next = -1
else:
  chr_next = chr( next )
    
if self.opened > 0 or chr_next == '\r' or chr_next == '\n' or chr_next == '\f' or chr_next == '#':
  # If we are inside a list or on a blank line, ignore all indents,
  # dedents and line breaks.
  self.skip()

else:

  self.emitToken( self.commonToken(ScriptdogParser.NEWLINE, newLine) )
  indent = self.getIndentationCount(spaces)

  if len( self.indents ) == 0:
      previous = 0
  else:
      previous = self.indents[-1]

#  print( "indent=%d, previous=%d (from [%s])" % ( indent, previous, spaces ) )
          
  if indent == previous:
    # skip indents of the same size as the present indent-size
    self.skip()
  elif indent > previous:
    self.indents.append(indent)
    self.emitToken( self.commonToken(ScriptdogParser.INDENT, spaces) )
  else:
    # Possibly emit more than 1 DEDENT token.
    while len(self.indents) > 0 and self.indents[-1] > indent:
      self.emitToken( self.createDedent() )
      self.indents.pop()

   }
 ;


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


//
// comments and whitespace
//

SKIP_
 : ( SPACES | COMMENT | COMMENT2 | LINE_JOINING ) -> skip
 ;

ML_COMMENT : '/*' ( . | [\r\n\f])*? '*/' -> skip;

//ML_COMMENT      : '/*' ( . | EOL )*? '*/' -> skip;
//SL_COMMENT      : '//' ( . )*? EOL -> skip;
//SL2_COMMENT     : '#' ( . )*? EOL -> skip;


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

fragment SPACES
 : [ \t]+
 ;

fragment COMMENT
 : '#' ~[\r\n\f]*
 ;

fragment COMMENT2
 : '//' ~[\r\n\f]*
 ;

fragment LINE_JOINING
 : '\\' SPACES? ( '\r'? '\n' | '\r' | '\f')
 ;
