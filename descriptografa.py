## importa as bibliotecas necessarias 

import os
import pyaes


## abre os arquivo que sera criptografado

file_name = "texto.txt.criptografado"
file = open(file_name,"rb")
file_data = file.read()
file.close()

## apaga o arquivo original

os.remove(file_name)

## definindo a chave de encriptação

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## descriptografa o arquivo 


decrypto_data =  aes.encrypt(file_data)

## salva o arquivo criptografado

new_file = file_name + "texto.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypto_data)
new_file.close()
