# Generated from Scriptdog.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import re
from . ScriptdogParser import ScriptdogParser
from antlr4.Token import CommonToken    
    

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01a8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00d4\n\24\3")
        buf.write("\24\3\24\5\24\u00d8\n\24\3\24\5\24\u00db\n\24\5\24\u00dd")
        buf.write("\n\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*")
        buf.write("\3+\3+\5+\u0115\n+\3,\6,\u0118\n,\r,\16,\u0119\3-\3-\5")
        buf.write("-\u011e\n-\3.\6.\u0121\n.\r.\16.\u0122\3/\6/\u0126\n/")
        buf.write("\r/\16/\u0127\3/\3/\7/\u012c\n/\f/\16/\u012f\13/\3/\5")
        buf.write("/\u0132\n/\3/\3/\6/\u0136\n/\r/\16/\u0137\3/\5/\u013b")
        buf.write("\n/\3/\6/\u013e\n/\r/\16/\u013f\3/\5/\u0143\n/\3\60\3")
        buf.write("\60\3\60\7\60\u0148\n\60\f\60\16\60\u014b\13\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u0153\n\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\7\62\u015c\n\62\f\62\16\62\u015f")
        buf.write("\13\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63\u0168\n")
        buf.write("\63\3\63\6\63\u016b\n\63\r\63\16\63\u016c\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\5\65\u0175\n\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\5\66\u0180\n\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\38\68\u018a\n8\r8\168\u018b\3")
        buf.write("9\39\79\u0190\n9\f9\169\u0193\139\3:\3:\3:\3:\7:\u0199")
        buf.write("\n:\f:\16:\u019c\13:\3;\3;\5;\u01a0\n;\3;\5;\u01a3\n;")
        buf.write("\3;\3;\5;\u01a7\n;\3\u015d\2<\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62")
        buf.write("c\63e\2g\2i\2k\2m\2o\2q\2s\2u\2\3\2\n\6\2\62;C\\aac|\3")
        buf.write("\2$$\4\2\f\f\16\17\4\2GGgg\4\2--//\5\2\62;CHch\n\2$$)")
        buf.write(")^^ddhhppttvv\4\2\13\13\"\"\2\u01c1\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\3w\3\2\2\2\5y\3\2\2\2\7{\3\2\2\2")
        buf.write("\t~\3\2\2\2\13\u0080\3\2\2\2\r\u0082\3\2\2\2\17\u0089")
        buf.write("\3\2\2\2\21\u0090\3\2\2\2\23\u0098\3\2\2\2\25\u009f\3")
        buf.write("\2\2\2\27\u00a6\3\2\2\2\31\u00ab\3\2\2\2\33\u00b2\3\2")
        buf.write("\2\2\35\u00b5\3\2\2\2\37\u00ba\3\2\2\2!\u00c1\3\2\2\2")
        buf.write("#\u00c6\3\2\2\2%\u00cc\3\2\2\2\'\u00dc\3\2\2\2)\u00e0")
        buf.write("\3\2\2\2+\u00e2\3\2\2\2-\u00e4\3\2\2\2/\u00e6\3\2\2\2")
        buf.write("\61\u00e8\3\2\2\2\63\u00ea\3\2\2\2\65\u00ec\3\2\2\2\67")
        buf.write("\u00ee\3\2\2\29\u00f0\3\2\2\2;\u00f2\3\2\2\2=\u00f4\3")
        buf.write("\2\2\2?\u00f7\3\2\2\2A\u00fa\3\2\2\2C\u00fd\3\2\2\2E\u0100")
        buf.write("\3\2\2\2G\u0103\3\2\2\2I\u0106\3\2\2\2K\u0108\3\2\2\2")
        buf.write("M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010e\3\2\2\2S\u0110\3")
        buf.write("\2\2\2U\u0114\3\2\2\2W\u0117\3\2\2\2Y\u011d\3\2\2\2[\u0120")
        buf.write("\3\2\2\2]\u0142\3\2\2\2_\u0144\3\2\2\2a\u0152\3\2\2\2")
        buf.write("c\u0156\3\2\2\2e\u0165\3\2\2\2g\u016e\3\2\2\2i\u0174\3")
        buf.write("\2\2\2k\u017f\3\2\2\2m\u0181\3\2\2\2o\u0189\3\2\2\2q\u018d")
        buf.write("\3\2\2\2s\u0194\3\2\2\2u\u019d\3\2\2\2wx\7<\2\2x\4\3\2")
        buf.write("\2\2yz\7.\2\2z\6\3\2\2\2{|\7/\2\2|}\7@\2\2}\b\3\2\2\2")
        buf.write("~\177\7A\2\2\177\n\3\2\2\2\u0080\u0081\7#\2\2\u0081\f")
        buf.write("\3\2\2\2\u0082\u0083\7i\2\2\u0083\u0084\7n\2\2\u0084\u0085")
        buf.write("\7q\2\2\u0085\u0086\7d\2\2\u0086\u0087\7c\2\2\u0087\u0088")
        buf.write("\7n\2\2\u0088\16\3\2\2\2\u0089\u008a\7g\2\2\u008a\u008b")
        buf.write("\7z\2\2\u008b\u008c\7r\2\2\u008c\u008d\7g\2\2\u008d\u008e")
        buf.write("\7e\2\2\u008e\u008f\7v\2\2\u008f\20\3\2\2\2\u0090\u0091")
        buf.write("\7k\2\2\u0091\u0092\7p\2\2\u0092\u0093\7e\2\2\u0093\u0094")
        buf.write("\7n\2\2\u0094\u0095\7w\2\2\u0095\u0096\7f\2\2\u0096\u0097")
        buf.write("\7g\2\2\u0097\22\3\2\2\2\u0098\u0099\7e\2\2\u0099\u009a")
        buf.write("\7j\2\2\u009a\u009b\7q\2\2\u009b\u009c\7k\2\2\u009c\u009d")
        buf.write("\7e\2\2\u009d\u009e\7g\2\2\u009e\24\3\2\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3")
        buf.write("\7w\2\2\u00a3\u00a4\7t\2\2\u00a4\u00a5\7p\2\2\u00a5\26")
        buf.write("\3\2\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7#\2\2\u00aa\30\3\2\2\2\u00ab\u00ac")
        buf.write("\7e\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7#\2\2\u00b1\32")
        buf.write("\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7h\2\2\u00b4\34")
        buf.write("\3\2\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\36\3\2\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be")
        buf.write("\7g\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7h\2\2\u00c0 \3")
        buf.write("\2\2\2\u00c1\u00c2\7V\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4")
        buf.write("\7w\2\2\u00c4\u00c5\7g\2\2\u00c5\"\3\2\2\2\u00c6\u00c7")
        buf.write("\7H\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7u\2\2\u00ca\u00cb\7g\2\2\u00cb$\3\2\2\2\u00cc\u00cd")
        buf.write("\7f\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7h\2\2\u00cf&\3")
        buf.write("\2\2\2\u00d0\u00d1\6\24\2\2\u00d1\u00dd\5o8\2\u00d2\u00d4")
        buf.write("\7\17\2\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d8\7\f\2\2\u00d6\u00d8\4\16\17")
        buf.write("\2\u00d7\u00d3\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00db\5o8\2\u00da\u00d9\3\2\2\2\u00da\u00db")
        buf.write("\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00d0\3\2\2\2\u00dc")
        buf.write("\u00d7\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\b\24\2")
        buf.write("\2\u00df(\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1*\3\2\2\2\u00e2")
        buf.write("\u00e3\7@\2\2\u00e3,\3\2\2\2\u00e4\u00e5\7*\2\2\u00e5")
        buf.write(".\3\2\2\2\u00e6\u00e7\7+\2\2\u00e7\60\3\2\2\2\u00e8\u00e9")
        buf.write("\7}\2\2\u00e9\62\3\2\2\2\u00ea\u00eb\7\177\2\2\u00eb\64")
        buf.write("\3\2\2\2\u00ec\u00ed\7]\2\2\u00ed\66\3\2\2\2\u00ee\u00ef")
        buf.write("\7_\2\2\u00ef8\3\2\2\2\u00f0\u00f1\7?\2\2\u00f1:\3\2\2")
        buf.write("\2\u00f2\u00f3\7~\2\2\u00f3<\3\2\2\2\u00f4\u00f5\7?\2")
        buf.write("\2\u00f5\u00f6\7?\2\2\u00f6>\3\2\2\2\u00f7\u00f8\7~\2")
        buf.write("\2\u00f8\u00f9\7~\2\2\u00f9@\3\2\2\2\u00fa\u00fb\7(\2")
        buf.write("\2\u00fb\u00fc\7(\2\2\u00fcB\3\2\2\2\u00fd\u00fe\7>\2")
        buf.write("\2\u00fe\u00ff\7?\2\2\u00ffD\3\2\2\2\u0100\u0101\7@\2")
        buf.write("\2\u0101\u0102\7?\2\2\u0102F\3\2\2\2\u0103\u0104\7\u0080")
        buf.write("\2\2\u0104\u0105\7?\2\2\u0105H\3\2\2\2\u0106\u0107\7-")
        buf.write("\2\2\u0107J\3\2\2\2\u0108\u0109\7/\2\2\u0109L\3\2\2\2")
        buf.write("\u010a\u010b\7\u0080\2\2\u010bN\3\2\2\2\u010c\u010d\7")
        buf.write(",\2\2\u010dP\3\2\2\2\u010e\u010f\7\61\2\2\u010fR\3\2\2")
        buf.write("\2\u0110\u0111\7`\2\2\u0111T\3\2\2\2\u0112\u0115\5!\21")
        buf.write("\2\u0113\u0115\5#\22\2\u0114\u0112\3\2\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115V\3\2\2\2\u0116\u0118\t\2\2\2\u0117\u0116")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011aX\3\2\2\2\u011b\u011e\5[.\2\u011c")
        buf.write("\u011e\5]/\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("Z\3\2\2\2\u011f\u0121\4\62;\2\u0120\u011f\3\2\2\2\u0121")
        buf.write("\u0122\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\\\3\2\2\2\u0124\u0126\4\62;\2\u0125\u0124\3\2\2")
        buf.write("\2\u0126\u0127\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012d\7\60\2\2\u012a")
        buf.write("\u012c\4\62;\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2")
        buf.write("\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0131\3")
        buf.write("\2\2\2\u012f\u012d\3\2\2\2\u0130\u0132\5e\63\2\u0131\u0130")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0143\3\2\2\2\u0133")
        buf.write("\u0135\7\60\2\2\u0134\u0136\4\62;\2\u0135\u0134\3\2\2")
        buf.write("\2\u0136\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u013b\5e\63\2\u013a")
        buf.write("\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0143\3\2\2\2")
        buf.write("\u013c\u013e\4\62;\2\u013d\u013c\3\2\2\2\u013e\u013f\3")
        buf.write("\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0143\5e\63\2\u0142\u0125\3\2\2\2\u0142")
        buf.write("\u0133\3\2\2\2\u0142\u013d\3\2\2\2\u0143^\3\2\2\2\u0144")
        buf.write("\u0149\7$\2\2\u0145\u0148\5i\65\2\u0146\u0148\n\3\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148\u014b\3")
        buf.write("\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014c\u014d\7$\2\2\u014d")
        buf.write("`\3\2\2\2\u014e\u0153\5o8\2\u014f\u0153\5q9\2\u0150\u0153")
        buf.write("\5s:\2\u0151\u0153\5u;\2\u0152\u014e\3\2\2\2\u0152\u014f")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0155\b\61\3\2\u0155b\3\2\2\2\u0156")
        buf.write("\u0157\7\61\2\2\u0157\u0158\7,\2\2\u0158\u015d\3\2\2\2")
        buf.write("\u0159\u015c\13\2\2\2\u015a\u015c\t\4\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0160\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u0160\u0161\7,\2\2\u0161\u0162\7")
        buf.write("\61\2\2\u0162\u0163\3\2\2\2\u0163\u0164\b\62\3\2\u0164")
        buf.write("d\3\2\2\2\u0165\u0167\t\5\2\2\u0166\u0168\t\6\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016a\3\2\2\2")
        buf.write("\u0169\u016b\4\62;\2\u016a\u0169\3\2\2\2\u016b\u016c\3")
        buf.write("\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016df")
        buf.write("\3\2\2\2\u016e\u016f\t\7\2\2\u016fh\3\2\2\2\u0170\u0171")
        buf.write("\7^\2\2\u0171\u0175\t\b\2\2\u0172\u0175\5m\67\2\u0173")
        buf.write("\u0175\5k\66\2\u0174\u0170\3\2\2\2\u0174\u0172\3\2\2\2")
        buf.write("\u0174\u0173\3\2\2\2\u0175j\3\2\2\2\u0176\u0177\7^\2\2")
        buf.write("\u0177\u0178\4\62\65\2\u0178\u0179\4\629\2\u0179\u0180")
        buf.write("\4\629\2\u017a\u017b\7^\2\2\u017b\u017c\4\629\2\u017c")
        buf.write("\u0180\4\629\2\u017d\u017e\7^\2\2\u017e\u0180\4\629\2")
        buf.write("\u017f\u0176\3\2\2\2\u017f\u017a\3\2\2\2\u017f\u017d\3")
        buf.write("\2\2\2\u0180l\3\2\2\2\u0181\u0182\7^\2\2\u0182\u0183\7")
        buf.write("w\2\2\u0183\u0184\5g\64\2\u0184\u0185\5g\64\2\u0185\u0186")
        buf.write("\5g\64\2\u0186\u0187\5g\64\2\u0187n\3\2\2\2\u0188\u018a")
        buf.write("\t\t\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cp\3\2\2\2\u018d")
        buf.write("\u0191\7%\2\2\u018e\u0190\n\4\2\2\u018f\u018e\3\2\2\2")
        buf.write("\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3")
        buf.write("\2\2\2\u0192r\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0195")
        buf.write("\7\61\2\2\u0195\u0196\7\61\2\2\u0196\u019a\3\2\2\2\u0197")
        buf.write("\u0199\n\4\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bt\3\2\2")
        buf.write("\2\u019c\u019a\3\2\2\2\u019d\u019f\7^\2\2\u019e\u01a0")
        buf.write("\5o8\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a6")
        buf.write("\3\2\2\2\u01a1\u01a3\7\17\2\2\u01a2\u01a1\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a7\7\f\2\2")
        buf.write("\u01a5\u01a7\4\16\17\2\u01a6\u01a2\3\2\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7v\3\2\2\2!\2\u00d3\u00d7\u00da\u00dc\u0114")
        buf.write("\u0119\u011d\u0122\u0127\u012d\u0131\u0137\u013a\u013f")
        buf.write("\u0142\u0147\u0149\u0152\u015b\u015d\u0167\u016c\u0174")
        buf.write("\u017f\u018b\u0191\u019a\u019f\u01a2\u01a6\4\3\24\2\b")
        buf.write("\2\2")
        return buf.getvalue()


class ScriptdogLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    RTARROW = 3
    QUES = 4
    BANG = 5
    GLOBAL = 6
    EXPECT = 7
    INCLUDE = 8
    CHOICE = 9
    RETURN = 10
    SETBANG = 11
    CLEARBANG = 12
    IF = 13
    ELSE = 14
    ELSEIF = 15
    TRUE = 16
    FALSE = 17
    DEF = 18
    NEWLINE = 19
    LST = 20
    GRT = 21
    LPAREN = 22
    RPAREN = 23
    LBRACE = 24
    RBRACE = 25
    LSBRACE = 26
    RSBRACE = 27
    EQ = 28
    PIPE = 29
    DOUBLE_EQ = 30
    LOG_OR = 31
    LOG_AND = 32
    LSTE = 33
    GRTE = 34
    NEQ = 35
    PLUS = 36
    MINUS = 37
    NEG = 38
    TIMES = 39
    LEFTDIV = 40
    EXP = 41
    BOOLEAN = 42
    ID = 43
    NUMBER = 44
    INT = 45
    FLOAT = 46
    STRING = 47
    SKIP_ = 48
    ML_COMMENT = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "','", "'->'", "'?'", "'!'", "'global'", "'expect'", 
            "'include'", "'choice'", "'return'", "'set!'", "'clear!'", "'if'", 
            "'else'", "'elseif'", "'True'", "'False'", "'def'", "'<'", "'>'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "'='", "'|'", "'=='", 
            "'||'", "'&&'", "'<='", "'>='", "'~='", "'+'", "'-'", "'~'", 
            "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "RTARROW", "QUES", "BANG", "GLOBAL", "EXPECT", "INCLUDE", "CHOICE", 
            "RETURN", "SETBANG", "CLEARBANG", "IF", "ELSE", "ELSEIF", "TRUE", 
            "FALSE", "DEF", "NEWLINE", "LST", "GRT", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LSBRACE", "RSBRACE", "EQ", "PIPE", "DOUBLE_EQ", 
            "LOG_OR", "LOG_AND", "LSTE", "GRTE", "NEQ", "PLUS", "MINUS", 
            "NEG", "TIMES", "LEFTDIV", "EXP", "BOOLEAN", "ID", "NUMBER", 
            "INT", "FLOAT", "STRING", "SKIP_", "ML_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "RTARROW", "QUES", "BANG", "GLOBAL", "EXPECT", 
                  "INCLUDE", "CHOICE", "RETURN", "SETBANG", "CLEARBANG", 
                  "IF", "ELSE", "ELSEIF", "TRUE", "FALSE", "DEF", "NEWLINE", 
                  "LST", "GRT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LSBRACE", "RSBRACE", "EQ", "PIPE", "DOUBLE_EQ", "LOG_OR", 
                  "LOG_AND", "LSTE", "GRTE", "NEQ", "PLUS", "MINUS", "NEG", 
                  "TIMES", "LEFTDIV", "EXP", "BOOLEAN", "ID", "NUMBER", 
                  "INT", "FLOAT", "STRING", "SKIP_", "ML_COMMENT", "EXPONENT", 
                  "HEX_DIGIT", "ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC", "SPACES", 
                  "COMMENT", "COMMENT2", "LINE_JOINING" ]

    grammarFileName = "Scriptdog.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.NEWLINE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:


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

               
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[18] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


