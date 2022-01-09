"""
@author: xiongbiao
@date: 2022-01-09 23:16
"""

from typing import Union


class Register:
    def __init__(self, value, name, desc=None):

        self.l_8  = hex(value & 0xf)
        self.l_16 = hex(value & 0xff)
        self.l_32 = hex(value & 0xffff)
        self.l_64 = hex(value)
        self.name = name
        self.desc = desc

    def __str__(self):
        if self.name in ['rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi', 'rbp', 'rsp']:
            l_32_name = self.name.replace('r', 'e')
            l_16_name = self.name.replace('r', '')
            if self.name in ['rax', 'rbx', 'rcx', 'rdx']:
                l_8_name = l_16_name.replace('x', 'l')
            else:
                l_8_name = l_16_name + 'l'
        else:
            l_32_name = self.name + 'd'
            l_16_name = self.name + 'w'
            l_8_name  = self.name + 'b'

        return "{}={}, {}={}, {}={}, {}={}, type={}".format(self.name, self.l_64, l_32_name, self.l_32, l_16_name,
                                                            self.l_16, l_8_name, self.l_8, self.desc)


rax = Register(0x12345678, 'rax', desc='return value')
rbx = Register(0x12345678, 'rbx', desc='return value')
rcx = Register(0x12345678, 'rcx', desc='return value')
rdx = Register(0x12345678, 'rdx', desc='return value')
rsi = Register(0x12345678, 'rsi', desc='return value')
rdi = Register(0x12345678, 'rdi', desc='return value')
rbp = Register(0x12345678, 'rbp', desc='return value')
rsp = Register(0x12345678, 'rsp', desc='return value')
r8  = Register(0x12345678, 'r8', desc='return value')
r9  = Register(0x12345678, 'r9', desc='return value')
r10 = Register(0x12345678, 'r10', desc='return value')
r11 = Register(0x12345678, 'r11', desc='return value')
r12 = Register(0x12345678, 'r12', desc='return value')
r13 = Register(0x12345678, 'r13', desc='return value')
r14 = Register(0x12345678, 'r14', desc='return value')
r15 = Register(0x12345678, 'r15', desc='return value')
print(rax)
print(rbx)
print(rcx)
print(rdx)
print(rsi)
print(rdi)
print(rbp)
print(rsp)
print(r8)
print(r9)
print(r10)
print(r11)
print(r12)
print(r13)
print(r14)
print(r15)

