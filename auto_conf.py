#!/usr/bin/python3

"""
SSH Auto Device Configurator

"""

from netmiko import ConnectHandler
import config

connection = 0

for device in config.all_devices:
    print("[{}] Connecting to device: {}\n".format(connection, device['ip']))
    net_connect = ConnectHandler(**device)
    for cmd in config.command_list["box{}".format(connection)]:
        print("[{}] Sending command: {}".format(connection, cmd))
        output = net_connect.send_command(cmd)
        print("[{}] Response: {}\n".format(connection, output))
    connection += 1
