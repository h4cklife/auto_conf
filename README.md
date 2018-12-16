#SSH Auto Device Configurator

Automatically configure devices over SSH using Netmiko. This script only sends 'show' commands 
and is not capable of sending 'configuration change commands'. That is because this script is mainly focused on remote 
configuration of Linux devices and has no focus on 'switch' configuration.

Read more @ https://github.com/ktbyers/netmiko

## Installation

Install the full requirements provided in requirements.txt

```bash
$ pip3 install netmiko
```

## Usage

Edit the config.py as needed.

```python
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
```

Then, change the file's mode and execute the script.

```bash
$ chmod +x auto_conf.py
$ ./auto_conf.py
```