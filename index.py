import win32crypt
import binascii
import os
import sys
import time

def get_argu(index: int, name: str =""):
    try:
        return sys.argv[index]
    except:
        print(f"ERROR: missing {name if len(name) > 1 else index}")
        sys.exit()

server_ip = get_argu(1, "ip")
rdpUser = get_argu(2, "username")
password = get_argu(3, "password")

base_path = ""
try:
    base_path = sys._MEIPASS
except:
    pass

pwdHash = win32crypt.CryptProtectData(password.encode("utf8"),'psw',None,None,None,0)
rdpPwd = str(binascii.hexlify(pwdHash).decode("utf8")).upper()

rdpTemp = open(os.path.join(base_path, "rdp.txt")).read()

rdpTemp += f"\nusername:s:{rdpUser}"
rdpTemp += f"\npassword 51:b:{rdpPwd}"
rdpTemp += f"\nfull address:s:{server_ip}"

theRdp_path = os.path.join(base_path, 'theRdp.rdp')
theRdpFile = open(theRdp_path, 'w', encoding="utf8")
theRdpFile.write(rdpTemp)
theRdpFile.close()
os.system(f"mstsc {theRdp_path} /f")