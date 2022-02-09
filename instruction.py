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
        # instruction.pos += 0x100
        if ins == 'halt':
            return 0x00, 1

        if ins == 'nop':
            return 0x10, 1

        if ins == 'rrmovq':
           src_code = Register.get_id(src.replace('%', ''))
           dest_code = Register.get_id(dest.replace('%', ''))
           return 0x20 << 8 | src_code << 4 | dest_code, 2

        if ins == 'irmovq':
            src_code = int(src.replace('$', ''))
            dest_code = Register.get_id(dest.replace('%', ''))
            return 0x30 << 72 | 0xF << 68 | dest_code << 64 | self.to_little_endian(src_code), 10

        if ins == 'rmmovq':
            src_code = Register.get_id(src.replace('%', ''))
            imm, dest_code = re.match(r'(.*)\((.*)\)', dest).groups()
            dest_code = Register.get_id(dest_code.replace('%', ''))
            return 0x40 << 72 | src_code << 68 | dest_code << 64 | self.to_little_endian(int(imm, 16)), 10

        if ins == 'mrmovq':
            imm, src_code = re.match(r'(.*)\((.*)\)', src).groups()
            src_code = Register.get_id(src_code.replace('%', ''))
            dest_code = Register.get_id(dest.replace('%', ''))
            return 0x50 << 72 | src_code << 68 | dest_code << 64 | self.to_little_endian(int(imm, 16)), 10

        if ins[-1] == 'q' and len(ins) == 4:
            ins_code = 0x60
            src_code = Register.get_id(src.replace('%', ''))
            dest_code = Register.get_id(dest.replace('%', ''))
            if ins[:4] == 'add':
                ins_code = 0x60
            elif ins[:4] == 'sub':
                ins_code = 0x61
            elif ins[:4] == 'and':
                ins_code = 0x62
            elif ins[:4] == 'xor':
                ins_code = 0x63
            return ins_code << 8 | src_code << 4 | dest_code, 2

        if ins[0] == 'j':
            ins_code = 0x70
            dest_code = dest
            sub_code = ins[1:]
            if sub_code == 'mp':
                pass
            elif sub_code == 'le':
                ins_code += 0x01
            elif sub_code == 'l':
                ins_code += 0x02
            elif sub_code == 'e':
                ins_code += 0x03
            elif sub_code == 'ne':
                ins_code += 0x04
            elif sub_code == 'ge':
                ins_code += 0x05
            elif sub_code == 'g':
                ins_code += 0x06

            return ins_code << 64 | self.to_little_endian(dest_code), 9

        if ins[:4] == 'cmov':
            ins_code = 0x20
            src_code = Register.get_id(src.replace('%', ''))
            dest_code = Register.get_id(dest.replace('%', ''))
            sub_code = ins[4:]
            if sub_code == 'le':
                ins_code += 0x01
            elif sub_code == 'l':
                ins_code += 0x02
            elif sub_code == 'e':
                ins_code += 0x03
            elif sub_code == 'ne':
                ins_code += 0x04
            elif sub_code == 'ge':
                ins_code += 0x05
            elif sub_code == 'g':
                ins_code += 0x06

            return ins_code << 8 | src_code << 4 | dest_code, 2

    def to_little_endian(self, num):
        mask = 0xff
        little = 0x0
        for i in range(8):
            bits = num & mask
            num >>= 8
            little |= bits
            if i != 7:
                little <<= 8
        return little

# ins = Instruction('rrmovq', '%rbx', '%rcx')
# ins = Instruction('irmovq', '$15', '%rbx')
# ins = Instruction('rmmovq', '%rsp', '0x123456789abcd(%rdx)')
# ins = Instruction('mrmovq',  '0x123456789abcd(%rdx)', '%rsp')
# ins = Instruction('rmmovq', '%rcx', '-3(%rbx)')
ins = Instruction('addq', '%rbx', '%rcx')
decoder = InstructionDecoder()
print(hex(decoder.parse(ins)))