"""
@author: xiongbiao
@date: 2022-01-17 23:27
"""

from components import Register
import re

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

        if ins == 'irmovq':
            src_code = int(src.replace('$', ''))
            dest_code = Register.get_id(dest.replace('%', ''))
            return 0x30 << 64 | 0xF << 60 | dest_code << 56 | src_code

        if ins == 'rmmovq':
            src_code = Register.get_id(src.replace('%', ''))
            imm, dest_code = re.match(r'(.*)\((.*)\)', dest).groups()
            dest_code = Register.get_id(dest_code.replace('%', ''))
            return 0x40 << 64 | src_code << 60 | dest_code << 56 | int(imm, 16)

        if ins == 'mrmovq':
            imm, src_code = re.match(r'(.*)\((.*)\)', src).groups()
            src_code = Register.get_id(src_code.replace('%', ''))
            dest_code = Register.get_id(dest.replace('%', ''))
            return 0x50 << 64 | src_code << 60 | dest_code << 56 | int(imm, 16)

# ins = Instruction('rrmovq', '%rax', '%rbx')
# ins = Instruction('irmovq', '$15', '%rbx')
# ins = Instruction('rmmovq', '%rsp', '0x123456789abcd(%rdx)')
ins = Instruction('mrmovq',  '0x123456789abcd(%rdx)', '%rsp')
decoder = InstructionDecoder()
print(hex(decoder.parse(ins)))