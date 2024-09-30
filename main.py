import os
import subprocess


networks = subprocess.run(["netsh", "wlan", "show", "networks"], capture_output=True, text=True)
networks = networks.stdout.split("\n")



networks = list(filter(lambda x: x.startswith("SSID"), networks))
neuronios = []
for net in networks:
    if "blips_" in net:
        neuronios.append(net[-12:])


for cod in neuronios:

    os.system(f"netsh wlan add profile filename=index.xml")
    os.system(f"netsh wlan connect {cod}")

print(neuronios)
