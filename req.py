import requests
import jwt
import random
import math
import time
import zipfile
import io
import os

auth = jwt.encode({
  "sub": str(math.floor(random.random() * 1e6)),
  "iss": "HidroWeb-Front",
  "permissions": [
    "read",
    "write"
  ],
  "exp": int(time.time()*10e3)
}, key=r"7f-j&CKk=coNzZc0y7_4obMP?#TfcYq%fcD0mDpenW2nc!lfGoZ|d?f&RNbDHUX6HIDROWEBBACK", algorithm="HS256", headers={
  "alg": "HS256",
  "typ": "JWT"
} )


headers = {

"Cookie": '27628ed70890f724c98c0800461fb776=567ac90304fcd78e02f26c27b0eee4e0; c82026e9a6b8da54e034dc38d01ba2a4=922fdfd998f12723e51ababc3b4cccac',
"Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
"Sec-Ch-Ua-Mobile": '?0',
"Authorization": f'Bearer {auth}',
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36',
"Content-Type": 'application/x-www-form-urlencoded',
"Accept": 'application/json, text/plain, */*',
"Hidroweb-Front": f'Bearer {auth}',
"Sec-Ch-Ua-Platform": '"Linux"',
"Sec-Fetch-Site": 'same-origin',
"Sec-Fetch-Mode": 'cors',
"Sec-Fetch-Dest": 'empty',
"Referer": 'https://www.snirh.gov.br/hidroweb/serieshistoricas',
"Accept-Encoding": 'gzip, deflate, br',
"Accept-Language": 'en-US,en;q=0.9',
"Priority": 'u=1, i',
}

try:
  end_dir = os.mkdir(os.path.join(os.getcwd(), "DADOS_ESTACOES"))
except:
  end_dir = os.path.join(os.getcwd(), "DADOS_ESTACOES")

with open("lista_estacoes.txt", "r", encoding="utf-8") as f:
  for estacao in f.readlines():
    codigo = estacao.split()[0]
    print(f"Baixando {codigo}")
    r = requests.get("http://www.snirh.gov.br/hidroweb/rest/api/documento/download/files", stream=True, params={'codigoestacao': codigo, 'tipodocumento': "csv", "forcenewfiles": "Y"}, headers=headers)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    try:
      dir_estacao = os.mkdir(os.path.join(end_dir, str(codigo)))
    except:
      dir_estacao = os.path.join(end_dir, str(codigo))
    z.extractall(dir_estacao)


