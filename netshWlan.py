import os
import subprocess

def findCode():
    networks = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)

    networks = networks.stdout.split("\n")

    networks = list(filter(lambda x: x.startswith("SSID"), networks))
    neuronio = ""
    for net in networks:
        if "blips-" in net:
            neuronio = net[-17:]
            result = subprocess.run(['netsh', 'wlan', 'connect', f'name={neuronio}'], capture_output=True, text=True, check=True,)
            return neuronio

print(findCode())