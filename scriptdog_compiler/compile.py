import sys
import subprocess
import pickle
import tempfile

from antlr4 import *

from scriptdog_compiler.compiler.ScriptdogLexer import ScriptdogLexer
from scriptdog_compiler.compiler.ScriptdogParser import ScriptdogParser
from scriptdog_compiler.compiler.ScriptdogListener import ScriptdogListener
from scriptdog_compiler.compiler.ScriptdogVisitor import ScriptdogVisitor

from scriptdog.objs import (Program, State, Transition, NamedStateOp, ExpectOp,
                            SetOp, IfOp, ClearOp, ChoiceOp, ReturnOp, UtteranceOp,
                            IdrefOp, VarrefOp, RegexvOp, AssgnOp, ElseOp)

#
# ==================================================================================
#


class SimpleVisitor(ScriptdogVisitor):
    '''
    This basically translates an AST produced by ANTLR,
    which contains tokens for everything under the sun,
    including things like braces, into a higher-level AST.
    '''

    def __init__(self):
        self.depth = 0
        self.program = Program()
        self.global_ctx = None

    def dprint(self, *args):
        for i in range(self.depth):
            print("  ", end="")
        print(*args)

    def none_to_bool(self, x):
        if x == None:
            return False
        return True

    #
    # ===============================================
    #

    def visitNamed_state_definition(
            self, ctx: ScriptdogParser.Named_state_definitionContext):
        op_seq = self.visit(ctx.state_op_list())

        tmp = ctx.parameter_list()
        if tmp != None:
            param_list = self.visit(tmp)
        else:
            param_list = []

        new_state = State(
            ctx.ID().getText(), op_seq, param_list, is_implicit=False)
        self.program.add_state(new_state)

    #
    # The sequence of operations defined in a state
    #

    def visitState_op_list(self, ctx: ScriptdogParser.State_op_listContext):
        tmp = ctx.state_op()
        if tmp == None:
            return []
        op_seq = []
        for i in tmp:
            op_seq.append(self.visit(i))
        return op_seq

    def visitState_op(self, ctx: scriptdogParser.State_opContext):
        # this is a bit tricky.  indenting/dedenting requires explicit
        # NEWLINE tokens, which show up as nodes in the tree.  if
        # we're not careful, the default visitor will visit those, and
        # override whatever chunk of AST we've accumulated with a None
        # value... so here, we just visit the non-NEWLINE node
        return self.visit(ctx.getChild(0))

    def visitNamed_state(self, ctx: ScriptdogParser.Named_stateContext):
        tmp = ctx.argument_list()
        if tmp == None:
            arg_list = []
        else:
            arg_list = self.visit(tmp)

        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        return NamedStateOp(ctx.ID().getText(), arg_list, weight)

    def visitExpect_statement(self,
                              ctx: ScriptdogParser.Expect_statementContext):
        tmp = ctx.utterance_op_list()
        if tmp == None:
            op_seq = []
        else:
            op_seq = self.visit(tmp)

        # create an anonymous top-level named utterance definition.
        # by definition, it's not global
        new_trans_name = self.program.get_next_unique_trans_name()
        new_trans = Transition(new_trans_name, False, op_seq)
        self.program.add_trans(new_trans)

        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        return ExpectOp(new_trans_name, weight)

    def visitSet_statement(self, ctx: ScriptdogParser.Set_statementContext):

        tmp = ctx.argument_list()
        if tmp == None:
            arg_list = []
        else:
            arg_list = self.visit(tmp)

        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        return SetOp(arg_list, weight)

    def visitIf_statement(self, ctx: ScriptdogParser.If_statementContext):
        if self.global_ctx == None:
            self.global_ctx = ctx

        test_seq = []

        tmp = ctx.state_op_list()
        op_seq = []
        if tmp != None:
            op_seq = self.visit(tmp)
        test_seq += [[ctx.ID().getText(), op_seq]]

        if ctx.elseif_statement_list() != None:
            elseifs = self.visit(ctx.elseif_statement_list())
            test_seq += elseifs  # should return a list of lists

        # an else statement is like an elseif with a test that's always true
        if ctx.else_statement() != None:
            else_stmt = self.visit(ctx.else_statement())
            test_seq += [else_stmt]

        # "compile" the test sequences
        final_test_seq = []
        for test in test_seq:
            varref_id, op_seq = test
            if len(op_seq) > 0:
                new_state_name = self.program.get_next_unique_state_name()
                param_list = []  # should this be something else?
                new_state = State(
                    new_state_name, op_seq, param_list, is_implicit=True)
                self.program.add_state(new_state)
            else:
                new_state_name = None
            if varref_id != None:
                varref_id = "{" + varref_id + "}"  # because of the way it comes out of the lexer...
            final_test_seq.append([varref_id, new_state_name])

        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        return IfOp(final_test_seq, weight)

    def visitClear_statement(self,
                             ctx: ScriptdogParser.Clear_statementContext):

        id = ctx.ID().getText()

        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        return ClearOp(id, weight)

    def visitChoice_statement(self, ctx: ScriptdogParser.Opt_statementContext):
        op_set = self.visit(ctx.state_op_list())

        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        # to ease interpretation, each option in the op_set is
        # transformed into a globally named state that we can call
        name_set = []
        for op in op_set:
            new_state_name = self.program.get_next_unique_state_name()
            param_list = []  # should this be something else?
            new_state = State(
                new_state_name, [op], param_list, is_implicit=True)
            self.program.add_state(new_state)
            name_set.append([new_state_name, op.weight])

        return ChoiceOp(name_set, weight)

    def visitReturn_statement(self,
                              ctx: ScriptdogParser.Return_statementContext):
        if ctx.NUMBER() != None:
            weight = float(ctx.NUMBER().getText())
        else:
            weight = 1.0

        return ReturnOp(weight)

    # -----------------------------------------------------

    def visitNamed_utterance_definition(
            self, ctx: ScriptdogParser.Named_utterance_definitionContext):

        is_global = self.none_to_bool(ctx.GLOBAL())

        tmp = ctx.utterance_op_list()
        if tmp == None:
            ut_seq = []
        else:
            ut_seq = self.visit(tmp)

        new_trans = Transition(ctx.ID().getText(), is_global, ut_seq)
        self.program.add_trans(new_trans)

    def visitUtterance_op_list(self,
                               ctx: ScriptdogParser.Utterance_op_listContext):
        tmp = ctx.utterance_op()
        if tmp == None:
            return []

        op_seq = []
        for i in tmp:
            op_seq.append(self.visit(i))
        return op_seq

    def visitUtterance_op(self, ctx: ScriptdogParser.Utterance_opContext):

        # this is the sequence of utterance ops that make up the utterance
        #
        # for example, the following utterance:
        #    [YES? "(im|its|my name is|they call me|im called|call me)"? X=NAME ] {
        # would have 3 ops

        if ctx.utterance_innards_list() == None:
            innards = None
        else:
            innards = self.visit(ctx.utterance_innards_list())

        # this is the (optional) sequence of states to execute if the utterance is triggered
        op_seq = []
        if ctx.state_op_list() != None:
            op_seq = self.visit(ctx.state_op_list())
        if ctx.RTARROW() != None:
            op_seq = [self.visit(ctx.named_state())]

        # to ease interpretation, we implement a simplification: we
        # construct a new named state (with a unique name ).

        if len(op_seq) > 0:
            new_state_name = self.program.get_next_unique_state_name()
            param_list = []  # should this be something else?
            new_state = State(
                new_state_name, op_seq, param_list, is_implicit=True)
            self.program.add_state(new_state)

        else:
            new_state_name = None

        return UtteranceOp(innards, new_state_name)

    def visitUtterance_innards_list(
            self, ctx: ScriptdogParser.Utterance_innards_listContext):
        tmp = ctx.utterance_innard()
        if tmp == None:  # shouldn't happen...
            return []
        op_seq = []
        for i in tmp:
            op_seq.append(self.visit(i))
        return op_seq

    def visitIdref_uop(self, ctx: ScriptdogParser.Idref_uopContext):
        return IdrefOp(ctx.ID().getText(), self.none_to_bool(ctx.QUES()))

    def visitVarref_uop(self, ctx: ScriptdogParser.Varref_uopContext):
        varref_id = ctx.ID().getText()
        varref_id = "{" + varref_id + "}"  # because of the way it comes out of the lexer...
        return VarrefOp(varref_id, self.none_to_bool(ctx.QUES()))

    def visitRegexv_uop(self, ctx: ScriptdogParser.Regexv_uopContext):

        # the lexer helpfully gives us the actual quotes that were part of the STRING.
        regex_string = ctx.STRING().getText().lstrip('"').rstrip('"')

        return RegexvOp(regex_string, self.none_to_bool(ctx.QUES()))

    def visitAssgn_uop(self, ctx: ScriptdogParser.Assgn_uopContext):
        return AssgnOp(ctx.ID()[0].getText(),
                       ctx.ID()[1].getText(), self.none_to_bool(ctx.QUES()))

    def visitElse_uop(self, ctx: ScriptdogParser.Else_uopContext):
        return ElseOp()

    def visitParameter_list(self, ctx: ScriptdogParser.Parameter_listContext):
        arglist = []
        for i in range(ctx.getChildCount()):
            tmp = ctx.getChild(i).getText()
            if not tmp == ',':
                arglist.append(tmp)
        return arglist

    def visitArgument_list(self, ctx: ScriptdogParser.Argument_listContext):
        arglist = []
        for i in range(ctx.getChildCount()):
            tmp = ctx.getChild(i).getText()
            if not tmp == ',':
                arglist.append(tmp)
        return arglist

    def visitElseif_statement_list(
            self, ctx: ScriptdogParser.Elseif_statement_listContext):
        elselist = []
        for i in range(ctx.getChildCount()):
            elselist.append(self.visit(ctx.getChild(i)))
        return elselist

    def visitElseif_statement(self,
                              ctx: ScriptdogParser.Elseif_statementContext):
        op_seq = self.visit(ctx.state_op_list())
        return [ctx.ID().getText(), op_seq]

    def visitElse_statement(self, ctx: ScriptdogParser.Else_statementContext):
        op_seq = self.visit(ctx.state_op_list())
        # an else statement is like an elseif with a test that's always true
        return [None, op_seq]


#
# ==================================================================================
#


def compile_file(fn):

    #    new_f_obj = tempfile.NamedTemporaryFile()
    #    new_fn = new_f_obj.name

    new_fn = "/tmp/tmp_script.txt"

    # run the C pre processor to handle #include directives
    # XXX let's rip this out - we're only using it to implement #include...
    # run the C pre processor to handle #include directives
    # the -traditional-cpp flag tries to ensure that the preprocessor does not collapse whitespace (ie, by collapsing tabs to a single space)
    subprocess.run("cpp -traditional-cpp %s 2>/dev/null > %s" % (fn, new_fn), shell=True)

    stream_input = FileStream(new_fn)
    lexer = ScriptdogLexer(stream_input)
    stream = CommonTokenStream(lexer)
    parser = ScriptdogParser(stream)
    tree = parser.program()

    # translates the ANTLR AST to something more reasonable
    visitor = SimpleVisitor()
    visitor.visit(tree)

    return visitor.program


#    print(tree.toStringTree(recog=parser))
#    printer = simplePrinter()
#    walker = ParseTreeWalker()
#    walker.walk( printer, tree )


def validate_program(p):
    # want to make sure that every namedstateop references a defined state!
    # make sure that they don't re-define states or transitions
    # check their regexs - make sure they have parens around words with "?"
    pass
