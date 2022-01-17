"""
@author: xiongbiao
@date: 2022-01-17 23:27
"""

from components import Register

class Instruction:
    def __init__(self, ins, src, dest=None):
        self.ins = ins
        self.src = src
        self.dest = dest


class InstructionDecoder:

    def parse(self, instruction):
        ins = instruction.ins
        src  = instruction.src
        dest = instruction.dest

        if ins == 'halt':
            return 0x00

        if ins == 'nop':
            return 0x10

        if ins == 'rrmovq':
           src_code = Register.get_id(src.replace('%', ''))
           dest_code = Register.get_id(dest.replace('%', ''))
           return 0x20 << 8 | src_code << 4 | dest_code


ins = Instruction('rrmovq', '%rax', '%rbx')
decoder = InstructionDecoder()
print(decoder.parse(ins))