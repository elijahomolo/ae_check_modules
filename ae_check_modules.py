#!/usr/bin/env python3
import subprocess

def check_modules():
    modules = ['bridges', 'br_netfilter', 'overlay', 'ebtables', 'iptable_filter', 'iptable_nat']
    subprocess.run(["yum", "install", "lsmod"])
    missing_modules = []

    for module in modules:
        check = subprocess.check_output(["lsmod | grep {}".format(module)], shell=True)
        print(check)

    if check == 1:
        missing_modules.append(module)
        for module in missing_modules:
            print('installing {}'.format(module))
            install_module = subprocess.run(["sudo" "modprobe" "{}".format(module)],
                            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            if install_module == 1:
                print("{} does not exist".format(module))
            check_2 = subprocess.check_output(["lsmod | grep {}".format(module)], shell=True)
            print(check_2)

check_modules()
