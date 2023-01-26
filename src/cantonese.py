"""
    Created at 2021/1/16 16:23
    The interpreter for Cantonese    
"""
import cmd
import re
import sys
import os
import argparse

from can_error import 濑啲咩嘢
from stack_vm import *
from can_lexer import *
from can_compile import *
from can_lib import *

from can_web_parser import *
from can_asm_parser import *
from can_codegen import *

_version_ = "Cantonese 1.0.3 Copyright (C) 2020-2023 StepfenShawn"

dump_ast = False
dump_lex = False
to_js = False
to_cpp = False
_S = False
mkfile = False
TO_PY_CODE = ''

def cantonese_run(code : str, is_to_py : bool, file : str, 
                    REPL = False, get_py_code = False) -> None:
    
    global dump_ast
    global dump_lex
    global TO_PY_CODE
    global variable

    tokens = cantonese_token(code, keywords)
    # TODO: update for v1.0.3
    if dump_lex:
        for token in tokens:
            print("line " + str(token[0]) + ": " + str(token[1]))

    stats = can_parser.StatParser(tokens).parse_stats()
    code_gen = Codegen(stats, file)

    if dump_ast:
        for stat in stats:
            print(stat)
    
    TO_PY_CODE = ''
    for stat in stats:
        TO_PY_CODE += code_gen.codegen_stat(stat)


    if to_js:
        import Compile
        js, fh = Compile.Compile(stats, "js", file).ret()
        f = open(fh, 'w', encoding = 'utf-8')
        f.write(js)
        sys.exit(1)
        
    if _S:
        import Compile
        code, fh = Compile.Compile(stats, "asm", file).ret()
        # f = open(fh, 'w', encoding = 'utf-8')
        # f.write(code)
        print(code)
        sys.exit(1)
        
    cantonese_lib_init()
    if is_to_py:
        print(TO_PY_CODE)

    if mkfile:
        f = open(file[: len(file) - 10] + '.py', 'w', encoding = 'utf-8')
        f.write("###########################################\n")
        f.write("#        Generated by Cantonese           #\n")
        f.write("###########################################\n")
        f.write("# Run it by " + "'cantonese " + file[: len(file) - 10] + '.py' + " -build' \n")
        f.write(TO_PY_CODE)
    
    if debug:
        import dis
        print(dis.dis(TO_PY_CODE))
    else:
        import traceback
        try:
            c = TO_PY_CODE
            if REPL:
                TO_PY_CODE = "" # reset the global variable in REPL mode
            if get_py_code:
                return c
            exec(TO_PY_CODE, variable)
        except Exception as e:
            print("濑嘢!" + "\n".join(濑啲咩嘢(e)))

class 交互(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = '> '
    
    def var_def(self, key):
        pass
    
    def run(self, code):
        if code in variable.keys():
            print(variable[code])
        try:
            exec(code, variable)
        except Exception as e:
            print("濑嘢!" + "\n".join(濑啲咩嘢(e)))

    def default(self, code):
        
        global kw_exit_1
        global kw_exit_2
        global kw_exit

        if code is not None:
            if code == kw_exit or code == kw_exit_2 or code == kw_exit_1:
                sys.exit(1)
            c = cantonese_run(code, False, '【标准输入】', 
                REPL = True, get_py_code = True)
            if len(c) == 0:
                c = code
            self.run(c)


def 开始交互():
    global _version_
    print(_version_)
    import time
    交互().cmdloop(str(time.asctime(time.localtime(time.time()))))

def cantonese_run_with_vm(code : str, file : bool) -> None:
    tokens = cantonese_token(code, keywords)
    stats = can_parser.StatParser(tokens).parse_stats()

    if dump_ast:
        for stat in stats:
            print(stat)
    if dump_lex:
        print(tokens)
    gen_op_code = []
    stmt = make_stmt(stats, [])
    run_with_vm(stmt, gen_op_code, True, path = file)
    code = Code()
    code.ins_lst = gen_op_code
    if debug:
        for j in gen_op_code:
            print(j)
    cs = CanState(code)
    cs._run()

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file", nargs = '?', default = "")
    arg_parser.add_argument("other", nargs = '?', default = "")
    arg_parser.add_argument("-to_py", action = "store_true", help = "Translate Cantonese to Python")
    arg_parser.add_argument("-讲翻py", action = "store_true", help = "Translate Cantonese to Python")
    arg_parser.add_argument("-to_js", action = "store_true", help = "Translate Cantonese to JS")
    arg_parser.add_argument("-to_cpp", action = "store_true", help = "Translate Cantonese to C++")
    arg_parser.add_argument("-to_asm", action = "store_true", help = "Translate Cantonese to assembly")
    arg_parser.add_argument("-to_web", action = "store_true")
    arg_parser.add_argument("-倾偈", action = "store_true")
    arg_parser.add_argument("-compile", action = "store_true")
    arg_parser.add_argument("-讲白啲", action = "store_true")
    arg_parser.add_argument("-build", action = "store_true")
    arg_parser.add_argument("-stack_vm", action = "store_true")
    arg_parser.add_argument("-ast", action = "store_true")
    arg_parser.add_argument("-lex", action = "store_true")
    arg_parser.add_argument("-debug", action = "store_true")
    arg_parser.add_argument("-v", "-verison", action = "store_true", help = "Print the version")
    arg_parser.add_argument("-mkfile", action = "store_true")
    arg_parser.add_argument("-S", action = "store_true")
    arg_parser.add_argument("-s", action = "store_true")
    args = arg_parser.parse_args()

    global dump_ast
    global dump_lex
    global to_js
    global to_cpp
    global _S
    global debug
    global mkfile
    global _version_

    if args.v:
        print(_version_)
        sys.exit(1)

    if not args.file:
        sys.exit(开始交互())

    try:
        with open(args.file, encoding = "utf-8") as f:
            code = f.read()
            # Skip the comment
            code = re.sub(re.compile(r'/\*.*?\*/', re.S), ' ', code)
            is_to_py = False
            if args.build:
                cantonese_lib_init()
                exec(code, variable)
                exit()
            if args.to_py or args.讲翻py:
                is_to_py = True
            if args.to_web or args.倾偈:
                if args.compile or args.讲白啲:
                    cantonese_web_run(code, args.file, False)
                else:
                    cantonese_web_run(code, args.file, True)
            if args.ast:
                dump_ast = True
            if args.lex:
                dump_lex = True
            if args.debug:
                debug = True
            if args.stack_vm:
                cantonese_run_with_vm(code, args.file)
                sys.exit(1)
            if args.to_js:
                to_js = True
            if args.to_cpp:
                to_cpp = True
            if args.S or args.s:
                _S = True
            if args.mkfile:
                mkfile = True
            if args.to_asm:
                Cantonese_asm_run(code, args.file)
            cantonese_run(code, is_to_py, args.file)
    except FileNotFoundError:
        print("濑嘢!: 揾唔到你嘅文件 :(")

if __name__ == '__main__':
    main()
