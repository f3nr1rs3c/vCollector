#!/usr/bin/env python3
import ssl
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

# SSL doğrulamasını devre dışı bırak
ctx = ssl._create_unverified_context()

# vCenter veya ESXi sunucusuna bağlan
si = SmartConnect(
    host="10.5.2.111",
    user="administrator@telecore.ad",
    pwd="August1990password",
    sslContext=ctx
)

# İçerik nesnesini al
content = si.RetrieveContent()

# Tüm sanal makineleri listele
container_view = content.viewManager.CreateContainerView(
    content.rootFolder,
    [vim.VirtualMachine],
    True
)

for vm in container_view.view:
    try:
        ip = vm.guest.ipAddress
    except:
        ip = "N/A"

    if not ip and vm.guest.net:
        try:
            ip = vm.guest.net[0].ipConfig.ipAddress[0].ipAddress
        except:
            ip = "N/A"

    print(f"VM: {vm.name}")
    print(f"Power: {vm.runtime.powerState}")
    print(f"OS: {vm.config.guestFullName}")
    print(f"Tools: {vm.guest.toolsStatus}")
    print(f"IP: {ip}")
    print(f"Notes: {vm.config.annotation}\n")

# Bağlantıyı sonlandır
Disconnect(si)
