import os
import subprocess

networks = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)

networks = networks.stdout.split("\n")

networks = list(filter(lambda x: x.startswith("SSID"), networks))

for net in networks:
    print(net)