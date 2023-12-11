class Computer:
    def __init__(self, cpu_freq, cpu_cores, ram, hdd=None, ssd=None):
        self.cpu_freq = cpu_freq
        self.cpu_cores = cpu_cores
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd

my_computer = Computer(cpu_freq=3.0e9, cpu_cores=4, ram=8e9, hdd=1e12, ssd=256e9)

print("CPU Freq:", my_computer.cpu_freq)
print("CPU Cores:", my_computer.cpu_cores)
print("RAM:", my_computer.ram)
print("HDD:", my_computer.hdd)
print("SSD:", my_computer.ssd)
