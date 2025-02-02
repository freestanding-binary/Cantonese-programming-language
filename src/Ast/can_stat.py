from .ast_base import AST

class FuncCallStat(AST):
    def __init__(self, func_name : AST, args : list):
        self.func_name = func_name
        self.args = args

    def __str__(self) -> str:
        s = 'FunctoinCall:\n'
        s += "name: " + str(self.func_name) + '\n'
        s += "args: \n"
        for arg in self.args:
            for l in str(arg).split('\n'):
                if len(l):
                    s += '\t' + l + '\n'

        return s

class IfStat(AST):
    def __init__(self, if_exp : AST, if_block : list, elif_exps : list, 
                    elif_blocks : list, else_blocks : list):
        self.if_exp = if_exp
        self.if_block = if_block
        self.elif_exps = elif_exps
        self.elif_blocks = elif_blocks
        self.else_blocks = else_blocks

    def __str__(self) -> str:
        s = 'IfStat:\n'
        s += '"Exps": ' + '\n'
        for l in str(self.if_exp).split('\n'):
            s += '\t' + l + '\n'
        
        s += '"if_Blocks": ' + '\n'
        for block in self.if_block:
            for l in str(block).split('\n'):
                s += '\t' + l + '\n'

        if (self.elif_exps != [] or self.elif_blocks != []):
            s += '"Exps": ' + '\n'
            for exp in self.elif_exps:
                for l in str(exp).split('\n'):
                    s += '\t' + l + '\n'
            
            s += '"elif_Blocks": ' + '\n'
            for block in self.elif_blocks:
                for l in str(block).split('\n'):
                    s += '\t' + l + '\n'

        if (self.else_blocks != []):
            s += '"elif_Blocks": ' + '\n'
            for block in self.else_blocks:
                for l in str(block).split('\n'):
                    s += '\t' + l + '\n'

        return s

class PrintStat(AST):
    def __init__(self, args : list):
        self.args = args

    def __str__(self) -> str:
        s = 'PrintStat:\n'
        for arg in self.args:
            for l in str(arg).split('\n'):
                s += '\t' + l + '\n'

        return s

class PassStat(AST):
    def __init__(self) -> None:
        pass

    def __str__(self):
        return 'PassStat'


"""
assignstat := '讲嘢' varlist '系' explist
            | '讲嘢' '=>' '{' assignblock '}'
"""
class AssignStat(AST):
    def __init__(self, last_line : int, var_list : list, exp_list : list):
        self.last_line = last_line
        self.var_list = var_list
        self.exp_list = exp_list

    def __str__(self):
        s = 'AssignStat:\n'
        s += '"VarList": ' + '\n'
        for var in self.var_list:
            for l in str(var).split('\n'):
                if len(l):
                    s += '  ' + l + '\n'

        s += '"ExpList": ' + '\n'
        for exp in self.exp_list:
            for l in str(exp).split('\n'):
                if len(l):
                    s += '  ' + l + '\n'

        return s

class AssignBlockStat(AST):
    def __init__(self, last_line : int, var_list : list, exp_list : list):
        self.last_line = last_line
        self.var_list = var_list
        self.exp_list = exp_list

    def __str__(self):
        s = 'AssignStat:\n'
        s += '"VarList": ' + '\n'
        for var in self.var_list:
            for l in str(var).split('\n'):
                if len(l):
                    s += '  ' + l + '\n'

        s += '"ExpList": ' + '\n'
        for exp in self.exp_list:
            for l in str(exp).split('\n'):
                if len(l):
                    s += '  ' + l + '\n'

        return s

class ForStat(AST):
    def __init__(self, id : AST, from_exp : AST, to_exp : AST, blocks : list) -> None:
        self.var = id
        self.from_exp = from_exp
        self.to_exp = to_exp
        self.blocks = blocks

    def __str__(self) -> str:
        s = 'ForStat:\n'
        s += 'Var: ' + str(self.var) + '\n'
        s += 'From: ' + str(self.from_exp) +  '\n'
        s += 'To: ' + str(self.to_exp) + '\n'
        s += 'Block:\n'
        for block in self.blocks:
            for l in str(block).split('\n'):
                if len(l):
                    s += '\t' + l + '\n'

        return s

class ForEachStat(AST):
    def __init__(self, id_list : list, exp_list : list, blocks : list) -> None:
        self.id_list = id_list
        self.exp_list = exp_list
        self.blocks = blocks

    def __str__(self) -> str:
        s = 'ForEachStat:\n'
        s += 'Idlist:\n'
        for id in self.id_list:
            for l in str(id).split('\n'):
                s += '\t' + l + '\n'
        s += 'Explist:\n'
        for exp in self.exp_list:
            for l in str(exp).split('\n'):
                s += '\t' + l + '\n'
        s += "Blocks:\n"
        for block in self.blocks:
            for l in str(block).split('\n'):
                s += '\t' + l + '\n'
        return s

class WhileStat(AST):
    def __init__(self, exp : list, blocks : list) -> None:
        self.cond_exp = exp
        self.blocks = blocks

    def __str__(self) -> str:
        s = 'WhileStat:\n'
        s += 'Cond:\n'
        for l in str(self.cond_exp).split('\n'):
            if len(l):
                s += '\t' + l + '\n'
        s += 'Blocks:\n'
        for block in self.blocks:
            for l in str(block).split('\n'):
                if len(l):
                    s += '\t' + l + '\n'

        return s


class ListInitStat(AST):
    def __init__(self) -> None:
        pass

class FunctionDefStat(AST):
    def __init__(self, name_exp : AST, args : list, blocks : list,
                args_type : list = [], ret_type : list = []) -> None:
        self.name_exp = name_exp
        self.args = args
        self.blocks = blocks
        self.args_type = args_type
        self.ret_type = ret_type

    def __str__(self) -> str:
        s = 'FuncDefStat:\n'
        s += 'Name: ' + str(self.name_exp) + '\n'
        s += 'Args: ' + str(self.args) + '\n'
        s += 'Blocks: \n'
        for block in self.blocks:
            for l in str(block).split('\n'):
                if len(l):
                    s += '\t' + l + '\n'

        return s

class FuncTypeDefStat(AST):
    def __init__(self, func_name : AST, args_type : list, return_type : list) -> None:
        self.func_name = func_name
        self.args_type = args_type
        self.return_type = return_type

    def __str__(self) -> str:
        s = 'FuncTypeDefStat\n'
        s += 'Name: ' + str(self.func_name) + '\n'
        return s

class MethodDefStat(AST):
    def __init__(self, name_exp : AST, args : list, class_blocks : list) -> None:
        self.name_exp = name_exp
        self.args = args
        self.class_blocks = class_blocks

    def __str__(self) -> str:
        s = "MethodDefStat:\n"
        s += 'Name: ' + str(self.name_exp) + '\n'
        s += 'Args: ' + str(self.args) + '\n'
        s += 'Blocks:\n'
        for block in self.class_blocks:
            for l in str(block).split('\n'):
                if len(l):
                    s += '\t' + l + '\n'

        return s

class AttrDefStat(AST):
    def __init__(self, class_var_list : list, class_exp_list : list) -> None:
        self.class_var_list = class_var_list
        self.class_exp_list = class_exp_list

    def __str__(self) -> str:
        s += "AttrDefStat:\n"
        s += 'Class_var_list:\n'
        for class_var in self.class_var_list:
            for l in str(class_var).split('\n'):
                s += '\t' + l + '\n'
        s += 'Class_exp_list:\n'
        for class_exp in self.class_exp_list:
            for l in str(class_exp).split('\n'):
                s += '\t' + l + '\n'
        
        return s

class ClassInitStat(AST):
    def __init__(self, class_var_list : list) -> None:
        self.class_var_list = class_var_list

    def __str__(self) -> str:
        s = 'ClassInitStat:\n'
        for class_var in self.class_var_list:
            for l in str(class_var).split('\n'):
                s += '\t' + l + '\n'

        return s

class ClassDefStat(AST):
    def __init__(self, class_name : AST, class_extend : list, class_blocks : list) -> None:
        self.class_name = class_name
        self.class_extend = class_extend
        self.class_blocks = class_blocks

    def __str__(self) -> str:
        s = 'ClassDefStat\n'
        s += 'class_name: \n'
        for l in str(self.class_name).split('\n'):
            s += '\t' + l + '\n'
        s += 'extends: \n'
        for extend in self.class_extend:
            for l in str(extend).split('\n'):
                s += '\t' + l + '\n'
        s += 'class_blocks: \n'
        for blocks in self.class_blocks:
            for l in str(blocks).split('\n'):
                s += '\t' + l + '\n'
        
        return s

class MatchModeFuncDefStat(AST):
    def __init__(self, func_name : AST, args_list : list, block_list : list) -> None:
        self.func_name = func_name
        self.args_list = args_list
        self.block_list = block_list

    def __str__(self) -> str:
        s = "MatchModeFuncDefStat"
        s += "func_name: \n"
        for l in str(self.func_name).split('\n'):
            s += '\t' + l + '\n'
        s += "arg_list: \n"
        for arg in self.args_list:
            for l in str(arg).split('\n'):
                s += '\t' + l + '\n'
        for ret in self.block_list:
            for l in str(ret).split('\n'):
                s += '\t' + l + '\n'
        
        return s

class ImportStat(AST):
    def __init__(self, idlist : list) -> None:
        self.idlist = idlist

    def __str__(self) -> str:
        s = 'ImportStat:\n'
        for var in self.idlist:
            for l in str(var).split('\n'):
                if len(l):
                    s += '  ' + l + '\n'
        
        return s

class RaiseStat(AST):
    def __init__(self, name_exp) -> None:
        self.name_exp = name_exp

    def __str__(self) -> str:
        s = 'RaiseStat:\n'
        for exp in str(self.name_exp).split('\n'):
            s += '\t' + exp + '\n'

        return s

class TryStat(AST):
    def __init__(self, try_blocks : list, except_exps : list, 
                except_blocks : list, finally_blocks : list) -> None:
        self.try_blocks = try_blocks
        self.except_exps = except_exps
        self.except_blocks = except_blocks
        self.finally_blocks = finally_blocks

    def __str__(self) -> str:
        s = 'TryStat:\n'
        s += '"TryBlocks": ' + '\n'
        for block in self.try_blocks:
            for l in str(block).split('\n'):
                s += '\t' + l + '\n'

        if (self.except_exps != [] or self.except_blocks != []):
            s += '"ExceptExps": ' + '\n'
            for exp in self.except_exps:
                for l in str(exp).split('\n'):
                    s += '\t' + l + '\n'
            
            s += '"ExceptBlocks": ' + '\n'
            for block in self.except_blocks:
                for l in str(block).split('\n'):
                    s += '\t' + l + '\n'

        if (self.finally_blocks != []):
            s += '"elif_Blocks": ' + '\n'
            for block in self.finally_blocks:
                for l in str(block).split('\n'):
                    s += '\t' + l + '\n'

        return s 

class GlobalStat(AST):
    def __init__(self, idlist :list) -> None:
        self.idlist = idlist

    def __str__(self):
        s = 'GlobalStat:\n'
        for var in self.idlist:
            for l in str(var).split('\n'):
                if len(l):
                    s += '  ' + l + '\n'
        
        return s

class BreakStat(AST):
    def __init__(self) -> None:
        pass

    def __str__(self):
        return "BreakStat\n"

class TypeStat(AST):
    def __init__(self, exps) -> None:
        self.exps = exps

    def __str__(self) -> str:
        s = 'TypeStat:\n'
        for exp in str(self.exps).split('\n'):
            s += '\t' + exp + '\n'
        return s

class AssertStat(AST):
    def __init__(self, exps) -> None:
        self.exps = exps

    def __str__(self) -> str:
        s = 'AssertStat:\n'
        for exp in str(self.exps).split('\n'):
            s += '\t' + exp + '\n'

        return s

class ReturnStat(AST):
    def __init__(self, exps : list) -> None:
        self.exps = exps

    def __str__(self) -> str:
        s = 'ReturnStat:\n'
        for exp in self.exps:
            for l in str(exp).split('\n'):
                s += '\t' + l + '\n'

        return s

class DelStat(AST):
    def __init__(self, exps : list) -> None:
        self.exps = exps

    def __str__(self) -> str:
        s = 'DelStat:\n'
        for exp in self.exps:
            for l in str(exp).split('\n'):
                s += '\t' + l + '\n'

        return s

class CmdStat(AST):
    def __init__(self, args : list) -> None:
        self.args = args

    def __str__(self) -> str:
        s = 'CmdStat:\n'
        s += 'Args:\n'
        for arg in self.args:
            for l in str(arg).split('\n'):
                s += '\t' + l + '\n'
        
        return s

class MethodCallStat(AST):
    def __init__(self, name_exp : AST, method : AST, args : list):
        self.name_exp = name_exp
        self.method = method
        self.args = args

    def __str__(self) -> str:
        s = "MethodCallStat:\n"
        s += 'prefix_exp: ' + str(self.name_exp) + '\n'
        s += 'Method_name: ' + str(self.method) + '\n'
        s += 'Args:\n'
        for arg in self.args:
            for l in str(arg).split('\n'):
                s += '\t' + l + '\n'

        return s

class CallStat(AST):
    def __init__(self, exp : AST) -> None:
        self.exp = exp

    def __str__(self) -> str:
        s = "CallStat:\n"
        for l in str(self.exp).split('\n'):
            s += '\t' + l + '\n'

        return s

class MatchStat(AST):
    def __init__(self, match_id : AST, match_val : list, match_block_exp : list, 
                default_match_block : list) -> None:
        self.match_id = match_id
        self.match_val = match_val
        self.match_block_exp = match_block_exp
        self.default_match_block = default_match_block

    def __str__(self) -> str:
        s = "MatchStat:\n"
        s += "MatchId:\n"
        for l in str(self.match_id).split('\n'):
            s += '\t' + l + '\n'
        for val in self.match_val:
            for l in str(val).split('\n'):
                s += '\t' + l + '\n'
        for block in self.match_block_exp:
            for l in str(block).split('\n'):
                s += '\t' + l + '\n'
        for block in self.default_match_block:
            for l in str(block).split('\n'):
                s += '\t' + l + '\n'
        return s

class ExtendStat(AST):
    def __init__(self, code : str):
        self.code = code

    def __str__(self):
        return "ExtendStat\n"

class ModelNewStat(AST):
    def __init__(self, model : AST, dataset : AST):
        self.model = model
        self.dataset = dataset

    def __str__(self):
        return "ModelNewStat\n"

class TurtleStat(AST):
    def __init__(self, exp_blocks : list):
        self.exp_blocks = exp_blocks

    def __str__(self):
        return "TurtleStat\n"