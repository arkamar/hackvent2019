#! /bin/env python

import ply.yacc as yacc
from decode_lex import tokens
import sys

'''
    expr      : expr bits
              | bits

    bits      : LEM tokens REM
              | tokens

    tokens    : tokens TOK
              | TOK
'''

def p_expr_expr_bits(p):
    'expr : expr bits'
    if p[0] == None:
        p[0] = ''
    p[0] += p[1]
    p[0] += p[2]

def p_expr_bits(p):
    'expr : bits'
    if p[0] == None:
        p[0] = ''
    p[0] += p[1]

def p_bits_ltr(p):
    'bits : LEM tokens REM'
    if p[0] == None:
        p[0] = ''
    p[0] += '1' * len(p[2])

def p_bits_tok(p):
    'bits : tokens'
    if p[0] == None:
        p[0] = ''
    p[0] += '0' * len(p[1])

def p_tokens_toktok(p):
    'tokens : tokens TOK'
    if p[0] == None:
        p[0] = ''
    p[0] += p[1]
    p[0] += p[2]

def p_tokens_tok(p):
    'tokens : TOK'
    if p[0] == None:
        p[0] = ''
    p[0] += p[1]

parser = yacc.yacc()

print(parser.parse(sys.stdin.read()))
