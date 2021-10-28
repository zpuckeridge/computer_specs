import os
import socket
import subprocess

# grab operating system


def get_os():
    os_name = os.name
    if os_name == 'nt':
        return 'Windows'
    elif os_name == 'posix':
        return 'Linux'
    else:
        return 'Mac'

# grab hostname
def get_hostname():
    return socket.gethostname()

# grab ip address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((socket.gethostname(), 0))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

# grab network link speed in GBPS
def get_link_speed():
    if os.name == 'nt':
        link_speed = subprocess.check_output(
            ['wmic', 'path', 'Win32_PerfRawData_Tcpip_NetworkInterface', 'get', 'CurrentBandwidth'])
        return link_speed.decode('utf-8')
    elif os.name == 'posix':
        link_speed = subprocess.check_output(['ethtool', 'enp0s3'])
        return link_speed.decode('utf-8')

# grab windows or linux mac address
def get_mac():
    if os.name == 'nt':
        mac_info = subprocess.check_output(['getmac'])
        return mac_info.decode('utf-8')
    elif os.name == 'posix':
        mac_info = subprocess.check_output(['ifconfig'])
        return mac_info.decode('utf-8')

# grab windows or linux cpu info
def get_cpu():
    if os.name == 'nt':
        cpu_info = subprocess.check_output(['wmic', 'cpu', 'get', 'name'])
        return cpu_info.decode('utf-8')
    elif os.name == 'posix':
        cpu_info = subprocess.check_output(['lscpu'])
        return cpu_info.decode('utf-8')

# grab windows or linux cpu info
def get_ram():
    if os.name == 'nt':
        ram_info = subprocess.check_output(
            ['wmic', 'OS', 'get', 'FreePhysicalMemory'])
        return ram_info.decode('utf-8')
    elif os.name == 'posix':
        ram_info = subprocess.check_output(['free', '-m'])
        return ram_info.decode('utf-8')

# grab windows or linux gpu info
def get_gpu():
    if os.name == 'nt':
        gpu_info = subprocess.check_output(
            ['wmic', 'path', 'Win32_VideoController', 'get', 'name'])
        return gpu_info.decode('utf-8')
    elif os.name == 'posix':
        gpu_info = subprocess.check_output(['lspci', '-vnn'])
        return gpu_info.decode('utf-8')

# grab windows or linux motherboard info
def get_motherboard():
    if os.name == 'nt':
        motherboard_info = subprocess.check_output(
            ['wmic', 'path', 'Win32_BaseBoard', 'get', 'Manufacturer,Product'])
        return motherboard_info.decode('utf-8')
    elif os.name == 'posix':
        motherboard_info = subprocess.check_output(
            ['dmidecode', '-t', 'baseboard'])
        return motherboard_info.decode('utf-8')

# grab windows or linux disk info
def get_disk():
    if os.name == 'nt':
        disk_info = subprocess.check_output(
            ['wmic', 'logicaldisk', 'get', 'Name,Size,FreeSpace'])
        return disk_info.decode('utf-8')
    elif os.name == 'posix':
        disk_info = subprocess.check_output(['df', '-h'])
        return disk_info.decode('utf-8')


# print computer specifications
print('Operating System:', get_os())
print('Hostname:', get_hostname())
print('IP:', get_ip())
print('Link Speed:', get_link_speed())
print('MAC:', get_mac())
print('CPU:', get_cpu())
print('Memory:', get_ram())
print('GPU:', get_gpu())
print(get_motherboard())
print(get_disk())
