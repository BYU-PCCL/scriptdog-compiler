# Generated from Scriptdog.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ScriptdogParser import ScriptdogParser
else:
    from ScriptdogParser import ScriptdogParser

# This class defines a complete generic visitor for a parse tree produced by ScriptdogParser.

class ScriptdogVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScriptdogParser#program.
    def visitProgram(self, ctx:ScriptdogParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#named_state_definition.
    def visitNamed_state_definition(self, ctx:ScriptdogParser.Named_state_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#named_utterance_definition.
    def visitNamed_utterance_definition(self, ctx:ScriptdogParser.Named_utterance_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#state_op_list.
    def visitState_op_list(self, ctx:ScriptdogParser.State_op_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#utterance_op_list.
    def visitUtterance_op_list(self, ctx:ScriptdogParser.Utterance_op_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#state_op.
    def visitState_op(self, ctx:ScriptdogParser.State_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#utterance_op.
    def visitUtterance_op(self, ctx:ScriptdogParser.Utterance_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#utterance_innards_list.
    def visitUtterance_innards_list(self, ctx:ScriptdogParser.Utterance_innards_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#utterance_innard.
    def visitUtterance_innard(self, ctx:ScriptdogParser.Utterance_innardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#else_uop.
    def visitElse_uop(self, ctx:ScriptdogParser.Else_uopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#idref_uop.
    def visitIdref_uop(self, ctx:ScriptdogParser.Idref_uopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#regexv_uop.
    def visitRegexv_uop(self, ctx:ScriptdogParser.Regexv_uopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#assgn_uop.
    def visitAssgn_uop(self, ctx:ScriptdogParser.Assgn_uopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#varref_uop.
    def visitVarref_uop(self, ctx:ScriptdogParser.Varref_uopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#named_state.
    def visitNamed_state(self, ctx:ScriptdogParser.Named_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#expect_statement.
    def visitExpect_statement(self, ctx:ScriptdogParser.Expect_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#set_statement.
    def visitSet_statement(self, ctx:ScriptdogParser.Set_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#clear_statement.
    def visitClear_statement(self, ctx:ScriptdogParser.Clear_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#opt_statement.
    def visitOpt_statement(self, ctx:ScriptdogParser.Opt_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#return_statement.
    def visitReturn_statement(self, ctx:ScriptdogParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#if_statement.
    def visitIf_statement(self, ctx:ScriptdogParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#elseif_statement_list.
    def visitElseif_statement_list(self, ctx:ScriptdogParser.Elseif_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#elseif_statement.
    def visitElseif_statement(self, ctx:ScriptdogParser.Elseif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#else_statement.
    def visitElse_statement(self, ctx:ScriptdogParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#parameter_list.
    def visitParameter_list(self, ctx:ScriptdogParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#argument_list.
    def visitArgument_list(self, ctx:ScriptdogParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#varref.
    def visitVarref(self, ctx:ScriptdogParser.VarrefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#expr.
    def visitExpr(self, ctx:ScriptdogParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptdogParser#filename.
    def visitFilename(self, ctx:ScriptdogParser.FilenameContext):
        return self.visitChildren(ctx)



del ScriptdogParser