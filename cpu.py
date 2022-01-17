"""
@author: xiongbiao
@date: 2022-01-17 23:20
"""
from components import Register, ProgramCounter, ConditionCode, Status

class Cpu:
    def __init__(self):

        # Register
        rax = Register(0x12345678, 'rax', desc='return value')
        rbx = Register(0x12345678, 'rbx', desc='callee save')
        rcx = Register(0x12345678, 'rcx', desc='4th parameter')
        rdx = Register(0x12345678, 'rdx', desc='3rd parameter')
        rsi = Register(0x12345678, 'rsi', desc='2nd parameter')
        rdi = Register(0x12345678, 'rdi', desc='1st parameter')
        rbp = Register(0x12345678, 'rbp', desc='callee save')
        rsp = Register(0x12345678, 'rsp', desc='stack pointer')
        r8  = Register(0x12345678, 'r8', desc='5th parameter')
        r9  = Register(0x12345678, 'r9', desc='6th parameter')
        r10 = Register(0x12345678, 'r10', desc='caller save')
        r11 = Register(0x12345678, 'r11', desc='caller save')
        r12 = Register(0x12345678, 'r12', desc='callee save')
        r13 = Register(0x12345678, 'r13', desc='callee save')
        r14 = Register(0x12345678, 'r14', desc='callee save')

        # PC
        pc = ProgramCounter()

        # Stat
        stat = Status()

        # CC
        cc = ConditionCode()