from runtime.errors.runtime_errors import *
from runtime.runtime_types import *
import runtime.interpreter as runtime
import runtime.environment as environment
""" 
format:
! = bang
? = qmark
[ = lbrack
] = rbrack
{ = lbrace
} = rbrace
( = lparen
) = rparen
"""

def fn_bang_qmark(arg: MLType, *_):
    print(arg)

def get_type(val: any):
    if isinstance(val, int) or isinstance(val, float):
        return RuntimeNumber(val)
    if isinstance(val, str):
        return RuntimeString(val)
    if isinstance(val, bool):
        return RuntimeBoolean(val)
    if isinstance(val, callable):
        return BuiltinFunction(val)

std_funcs = {
    '!?': BuiltinFunction(lambda arg, *_: print(arg)),
    '+': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg.value + x.value)), False),
    '*': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg.value * x.value)), False),
    '-': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg.value - x.value)), False),
    '/': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg.value / x.value)), False),
    '%': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg.value % x.value)), False),
    '=': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg == x)), False),
    '>': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg > x)), False),
    '<': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg < x)), False),
    '≠': BuiltinFunction(lambda arg, *_: BuiltinFunction(lambda x, *_: get_type(arg != x)), False),
    
}