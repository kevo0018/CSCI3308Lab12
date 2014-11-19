import parts


# The Computer class is a Facade class which will simplify the computer part classes.
# You should implement this class
# This class should be able to be called by the running part
class Computer:
    def __init__(self):
        self.cpu=parts.CPU()
        self.mem=parts.Memory()
        self.hd=parts.HardDisk()
    # implement the class below this line    

    def startComputer(self):
        self.cpu.__init__()
        self.cpu.check()
        self.mem.__init__()
        self.mem.load()
        self.mem.getInfo()
        self.hd.__init__()
        self.hd.mount()
        self.hd.getInfo()
    
    def printCPUInfo(self):
        self.cpu.getInfo()

    def printMemInfo(self):
        self.mem.getInfo()
    
    def printHDInfo(self):
        self.hd.getInfo()


# The running part
# Don't modify the following code!
com=Computer()
com.startComputer()
com.printCPUInfo()
com.printMemInfo()
com.printHDInfo()
