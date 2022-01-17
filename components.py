"""
@author: xiongbiao
@date: 2022-01-09 23:16
"""

class Register:
    def __init__(self, value, name, desc=None):

        self.l_8  = hex(value & 0xf)
        self.l_16 = hex(value & 0xff)
        self.l_32 = hex(value & 0xffff)
        self.l_64 = hex(value)
        self.name = name
        self.desc = desc

    def set_value(self, value):
        self.l_8 = hex(value & 0xf)
        self.l_16 = hex(value & 0xff)
        self.l_32 = hex(value & 0xffff)
        self.l_64 = hex(value)

    def set_name(self, name):
        self.name = name

    def set_desc(self, desc):
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

    @staticmethod
    def get_id(name):
        ids = ['rax', 'rcx', 'rdx', 'rbx', 'rsp', 'rbp', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
        return ids.index(name)

class ConditionCode:
    def __init__(self, zf=0, sf=0, of=0):
        self.zf = zf
        self.sf = sf
        self.of = of

    def set_zf(self, zf):
        self.zf = zf

    def set_of(self, of):
        self.of = of

    def set_sf(self, sf):
        self.sf = sf

    def __str__(self):
        return 'zf={}, sf={}, of={}'.format(self.zf, self.sf, self.of)

class ProgramCounter:
    def __init__(self, pc=0):
        self.pc = pc

    def __str__(self):
        return 'pc={}'.format(self.pc)

class Status:
    def __init__(self, stat=0):
        self.stat = stat

    def __str__(self):
        return 'stat={}'.format(self.stat)


