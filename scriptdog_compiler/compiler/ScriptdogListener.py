# Generated from Scriptdog.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ScriptdogParser import ScriptdogParser
else:
    from ScriptdogParser import ScriptdogParser

# This class defines a complete listener for a parse tree produced by ScriptdogParser.
class ScriptdogListener(ParseTreeListener):

    # Enter a parse tree produced by ScriptdogParser#program.
    def enterProgram(self, ctx:ScriptdogParser.ProgramContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#program.
    def exitProgram(self, ctx:ScriptdogParser.ProgramContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#named_state_definition.
    def enterNamed_state_definition(self, ctx:ScriptdogParser.Named_state_definitionContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#named_state_definition.
    def exitNamed_state_definition(self, ctx:ScriptdogParser.Named_state_definitionContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#named_utterance_definition.
    def enterNamed_utterance_definition(self, ctx:ScriptdogParser.Named_utterance_definitionContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#named_utterance_definition.
    def exitNamed_utterance_definition(self, ctx:ScriptdogParser.Named_utterance_definitionContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#state_op_list.
    def enterState_op_list(self, ctx:ScriptdogParser.State_op_listContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#state_op_list.
    def exitState_op_list(self, ctx:ScriptdogParser.State_op_listContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#utterance_op_list.
    def enterUtterance_op_list(self, ctx:ScriptdogParser.Utterance_op_listContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#utterance_op_list.
    def exitUtterance_op_list(self, ctx:ScriptdogParser.Utterance_op_listContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#state_op.
    def enterState_op(self, ctx:ScriptdogParser.State_opContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#state_op.
    def exitState_op(self, ctx:ScriptdogParser.State_opContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#utterance_op.
    def enterUtterance_op(self, ctx:ScriptdogParser.Utterance_opContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#utterance_op.
    def exitUtterance_op(self, ctx:ScriptdogParser.Utterance_opContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#utterance_innards_list.
    def enterUtterance_innards_list(self, ctx:ScriptdogParser.Utterance_innards_listContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#utterance_innards_list.
    def exitUtterance_innards_list(self, ctx:ScriptdogParser.Utterance_innards_listContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#utterance_innard.
    def enterUtterance_innard(self, ctx:ScriptdogParser.Utterance_innardContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#utterance_innard.
    def exitUtterance_innard(self, ctx:ScriptdogParser.Utterance_innardContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#else_uop.
    def enterElse_uop(self, ctx:ScriptdogParser.Else_uopContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#else_uop.
    def exitElse_uop(self, ctx:ScriptdogParser.Else_uopContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#idref_uop.
    def enterIdref_uop(self, ctx:ScriptdogParser.Idref_uopContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#idref_uop.
    def exitIdref_uop(self, ctx:ScriptdogParser.Idref_uopContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#regexv_uop.
    def enterRegexv_uop(self, ctx:ScriptdogParser.Regexv_uopContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#regexv_uop.
    def exitRegexv_uop(self, ctx:ScriptdogParser.Regexv_uopContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#assgn_uop.
    def enterAssgn_uop(self, ctx:ScriptdogParser.Assgn_uopContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#assgn_uop.
    def exitAssgn_uop(self, ctx:ScriptdogParser.Assgn_uopContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#varref_uop.
    def enterVarref_uop(self, ctx:ScriptdogParser.Varref_uopContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#varref_uop.
    def exitVarref_uop(self, ctx:ScriptdogParser.Varref_uopContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#named_state.
    def enterNamed_state(self, ctx:ScriptdogParser.Named_stateContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#named_state.
    def exitNamed_state(self, ctx:ScriptdogParser.Named_stateContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#set_statement.
    def enterSet_statement(self, ctx:ScriptdogParser.Set_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#set_statement.
    def exitSet_statement(self, ctx:ScriptdogParser.Set_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#clear_statement.
    def enterClear_statement(self, ctx:ScriptdogParser.Clear_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#clear_statement.
    def exitClear_statement(self, ctx:ScriptdogParser.Clear_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#return_statement.
    def enterReturn_statement(self, ctx:ScriptdogParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#return_statement.
    def exitReturn_statement(self, ctx:ScriptdogParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#expect_statement.
    def enterExpect_statement(self, ctx:ScriptdogParser.Expect_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#expect_statement.
    def exitExpect_statement(self, ctx:ScriptdogParser.Expect_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#choice_statement.
    def enterChoice_statement(self, ctx:ScriptdogParser.Choice_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#choice_statement.
    def exitChoice_statement(self, ctx:ScriptdogParser.Choice_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#if_statement.
    def enterIf_statement(self, ctx:ScriptdogParser.If_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#if_statement.
    def exitIf_statement(self, ctx:ScriptdogParser.If_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#elseif_statement_list.
    def enterElseif_statement_list(self, ctx:ScriptdogParser.Elseif_statement_listContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#elseif_statement_list.
    def exitElseif_statement_list(self, ctx:ScriptdogParser.Elseif_statement_listContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#elseif_statement.
    def enterElseif_statement(self, ctx:ScriptdogParser.Elseif_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#elseif_statement.
    def exitElseif_statement(self, ctx:ScriptdogParser.Elseif_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#else_statement.
    def enterElse_statement(self, ctx:ScriptdogParser.Else_statementContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#else_statement.
    def exitElse_statement(self, ctx:ScriptdogParser.Else_statementContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#parameter_list.
    def enterParameter_list(self, ctx:ScriptdogParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#parameter_list.
    def exitParameter_list(self, ctx:ScriptdogParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#argument_list.
    def enterArgument_list(self, ctx:ScriptdogParser.Argument_listContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#argument_list.
    def exitArgument_list(self, ctx:ScriptdogParser.Argument_listContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#varref.
    def enterVarref(self, ctx:ScriptdogParser.VarrefContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#varref.
    def exitVarref(self, ctx:ScriptdogParser.VarrefContext):
        pass


    # Enter a parse tree produced by ScriptdogParser#expr.
    def enterExpr(self, ctx:ScriptdogParser.ExprContext):
        pass

    # Exit a parse tree produced by ScriptdogParser#expr.
    def exitExpr(self, ctx:ScriptdogParser.ExprContext):
        pass


