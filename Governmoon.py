__Author__ = "0verflowSec/xMs_UwU_sMx"
__Tools__ = "Governmoon"

import os
if os.system('Windows'):
    os.system('cls')
elif os.system('Linux'):
    os.system('clear')

from sys import stdout
import random
import string
from cryptography.fernet import Fernet
import base64


try:
    def banner():
        print()
        stdout.write('╔═════════════════════════════════╗\n')
        stdout.write('║       01110010 01101110         ║\n')
        stdout.write('║       01000111 01101111         ║\n')
        stdout.write('║       01110110 01100101         ║\n')
        stdout.write('╠═════════════════════════════════╣\n')
        stdout.write('║                                 ║\n')
        stdout.write('║ Author : 0verflowSec[OCT]       ║\n')
        stdout.write('║ Team : OasisCyberTeam           ║\n')
        stdout.write('║                                 ║\n')
        stdout.write('╚═════════════════════════════════╝\n')
        print()
    banner()
    __ofile__ = input("File to obfsucate : ")
    __author__ = input("What is your name or nickname : ")
    __out__ = input("Output file name without .py : ")
    file = open(__ofile__, 'r')
    secret = file.read()


    def encrypt(sec):
        data =''
        for i in sec:
            b = 256
            data += '/x' + str(ord(i) ^ b)
        return data


    def generate_key(length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))


    def random_letter(length):
        randata = '"'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",'+' "'+''.join(random.choice(string.ascii_letters) for i in range(length))+'==",\n\t'
        return randata

    def special():
        repeat = 0
        data = str()
        num = random.randint(500, 1000)
        while repeat < num:
            data += random_letter(6)
            repeat += 1
            if repeat == 1000:
                break
            else:
                continue
        return data


    key = base64.b64encode(Fernet.generate_key()).decode('utf8')
    data = Fernet(base64.b64decode(key)).encrypt(b"PUlQMlRBRk1XQ1pNVk1GUE1UMjJVVUJPTkxVQUhINUlDM1Q0RUNKTFNCNFdHUkpMRTNWR1ZNSktORFpHSFVWS1RTNE1GNVpLMkNaT0ZLSlBOMlJFV0ZCTkwzVkVITlZLU1NTTUVESk1HQzNLVlM1S09TMlNWWUVKUUpVQ0c0Vk5YS1dNVURKTVBDWllXTFZHS0NNS1ZRSkpLVFVRRURKRzJTVlVFVlpLUlJVSVZRVkpXQ1c2VTRGSkhDWkNEWUlHWjI0QVhZVUpKRDJXV0lCT1FEM0lXQlJOU0pXR0hMSk5OMjJVRlhGS1VDNENEUk5LSUxWR1ZZNE5RUlVVRTJWTlRTNlNVV0ZNUEMyTVZNWklLS1ZLV1VKSUtMVUlFSjVLRTNWVUU1RkxPVFVVSExGTVlMM0dGRVJOTExaT0VTVktaUzNNRllJS0xEMjJXS0JKTUxWS1dMWkpLTFdDVEtSS0JMVE1GTVZLWUM0TVZTVkdETFJVVjNaS0tMVFNHSlpOUktOQUhMUk1URFpZV0xCT0tDTUtWUVJOT1RVUUVXVktOS05HV1lZSw==")


    payload = ('''# Obfuscated with Governmoon 1.0 > 0verflowSec : Special for dragonforce.io
# This code created by {4}
try:
    x=getattr(__import__(print.__class__.__name__[:7]+().__class__.__eq__.__class__.__name__[10]), [].__class__.__name__[0]+().__class__.__name__[-1]+print.__class__.__name__[6])('\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f\\x5f');y='{0}';getattr(__import__(True.__class__.__name__[1]+[].__class__.__name__[2]),().__class__.__eq__.__class__.__name__[:2]+().__iter__().__class__.__name__[6:9])(1, getattr(__import__(True.__class__.__name__[0]+().__class__.__eq__.__class__.__name__[2]+().__class__.__eq__.__class__.__name__[-8]+float.__class__.__name__[-1]+'6'+'4'),True.__class__.__name__[0]+'64'+exec.__class__.__name__[-1]+float.__class__.__name__[-1]+{{}}.__class__.__name__[2]+True.__class__.__name__[2]+{{}}.__class__.__name__[0]+str.__class__.__name__[-1])('u4iLlR2bjBSZoRHIsxWY0NnbpVmcgI3bg4WahdWYgUGZvNGIzlGa0BSZ0F2YzVnZi9WZSpQIyVWbtFmcn9mcwBSYgUHIltWYtBCdu92dgQXakVmcjBSZoRHIlZ3btVmU'[::-1])+b'\\n\\n') if not open(__file__.split('\\\\')[-1], 'r').read().__contains__(getattr(__import__(True.__class__.__name__[0]+().__class__.__eq__.__class__.__name__[2]+().__class__.__eq__.__class__.__name__[-8]+float.__class__.__name__[-1]+'6'+'4'),True.__class__.__name__[0]+'64'+exec.__class__.__name__[-1]+float.__class__.__name__[-1]+{{}}.__class__.__name__[2]+True.__class__.__name__[2]+{{}}.__class__.__name__[0]+str.__class__.__name__[-1])('vlmLlNmcvZmbvdWYyRGIy9mZgwWYpNWZwNFI6AyYlN1dvxmZyVmdwAiPgAjLxAibv9WbuJXZ292RggGdpdHIkVGdhN2c1ZmYPByI'[::-1]).decode('utf8')) else getattr(__import__(exec.__class__.__name__[:7]+().__class__.__eq__.__class__.__name__[10]),float.__class__.__name__[3:4]+'\\x76'+().__class__.__eq__.__class__.__name__[2]+False.__class__.__name__[3])(getattr(__import__(exec.__class__.__name__[:7]+().__class__.__eq__.__class__.__name__[10]),{{}}.__class__.__name__[2]+True.__class__.__name__[1]+abs.__class__.__name__[-6:-5]+().__class__.__name__[2]+[].__class__.__name__[1]+False.__class__.__name__[-1]+().__class__.__name__[-1])(''.join([chr(int(c)-x%int(c)) for c in y.split('\\x2f\\x78')[1:]]),'Governmoon',().__class__.__name__[-1]+'x'+float.__class__.__name__[-1]+{{}}.__class__.__name__[2]))
    {8}=False
    data = [{1}{2}]
    import base64;from cryptography.fernet import Fernet;import zlib as __________;import marshal as ____;import base64 as ______;key=base64.b64decode("{5}");nothing="{6}";__Governmoon__=Fernet(key).decrypt(nothing)
    if {8}:
        {7} = "{3}"
    else:
        {7} = key
except Exception as e:
    print(e)
    ''').format(encrypt(secret), # 0
                '\n\t"XHg0Nw==", "XHg2Zg==", "XHg3Ng==", "XHg2NQ==", "XHg3Mg==", "XHg2ZQ==", "XHg2ZA==", "XHg2Zg==", "XHg2Zg==", "XHg2ZQ==",\n\t', # 1
                special() + '"G", "O", "V", "E", "R", "N", "M", "O", "O", "N"', # 2
                generate_key(159), # 3
                __author__, # 4
                key, # 5
                data.decode('utf8'), # 6
                generate_key(6), # 7
                generate_key(8) # 8
                )

    getattr(__import__(True.__class__.__name__[0]+().__class__.__eq__.__class__.__name__[2]+().__class__.__eq__.__class__.__name__[-8]+float.__class__.__name__[-1]+'6'+'4'),True.__class__.__name__[0]+'64'+exec.__class__.__name__[-1]+float.__class__.__name__[-1]+{}.__class__.__name__[2]+True.__class__.__name__[2]+{}.__class__.__name__[0]+str.__class__.__name__[-1])('vlmLlNmcvZmbvdWYyRGIy9mZgwWYpNWZwNFI6AyYlN1dvxmZyVmdwAiPgAjLxAibv9WbuJXZ292RggGdpdHIkVGdhN2c1ZmYPByI'[::-1])

    newfile = open(__out__+'.py', 'w')
    newfile.write(payload)

    print('\nSuccess!\n')
except Exception as e:
    print(f"\n{e}\n")
