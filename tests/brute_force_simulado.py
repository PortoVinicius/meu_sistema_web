import requests
import time

URL = "http://localhost:5000/login"
USERNAME = "usuario_teste"
PASSWORD_ERRADA = "senha_errada"

TENTATIVAS = 20
INTERVALO = 0.5  # segundos

session = requests.Session()

for i in range(TENTATIVAS):
    response = session.post(URL, data={
        "username": USERNAME,
        "password": PASSWORD_ERRADA
    })

    print(f"Tentativa {i+1} - Status HTTP: {response.status_code}")
    time.sleep(INTERVALO)

