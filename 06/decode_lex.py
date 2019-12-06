#! /bin/env python

import ply.lex as lex
import sys

tokens = (
    'LEM',
    'REM',
    'TOK'
)

t_LEM = r'<em>'
t_REM = r'</em>'
t_TOK = r'.'

t_ignore =  ' ,.'

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
