import win32crypt
import binascii
import os

rdpUser = "cx"
server_ip = "127.0.0.1"

pwdHash = win32crypt.CryptProtectData("1".encode("utf8"),'psw',None,None,None,0)
rdpPwd = str(binascii.hexlify(pwdHash).decode("utf8")).upper()

rdpTemp = open("rdp.txt").read()

rdpTemp += f"\nusername:s:{rdpUser}"
rdpTemp += f"\npassword 51:b:{rdpPwd}"
rdpTemp += f"\nfull address:s:{server_ip}"

theRdpFile = open('theRdp.rdp', 'w', encoding="utf8")
theRdpFile.write(rdpTemp)
theRdpFile.close()
os.system("mstsc theRdp.rdp /f")