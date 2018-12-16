"""
SSH Auto Device Configurator

Edit the configuration below as needed for each device
that you wish to configure automagically.

"""

box0 = {
    'device_type': 'linux',
    'ip': '192.168.1.2',
    'username': 'user0',
    'password': 'password0'
}

box1 = {
    'device_type': 'linux',
    'ip': '192.168.1.3',
    'username': 'user1',
    'password': 'password1'
}

all_devices = [box0, box1]

command_list = {
    'box0': ['uname -a', 'hostname -I'],
    'box1': ['uname -a', 'hostname -I']
}