import speedtest
import requests

try:
    response = requests.get("https://api.ipify.org/")
    print('========== SPEED TEST ==========')
    if response.status_code == 200:
        print('le serveur repond correctement')
        ip = response.text
        print(f"votre adresse ip est: {ip} (cette adresse ip est l'adresse ip publique).")
    else:
        print(f'le serveur ne repond pas correctement veuiller ressayer ({response.status_code})')

except requests.exceptions.ConnectionError:
    print(" Impossible de se connecter au serveur.")


test = speedtest.Speedtest()

test.get_best_server()


print(f"Votre ping est de : {test.results.ping}ms")
print(f"votre vitesse de download: {round(test.download() / 1000 / 1000, 1)} Mbit/s")
print(f"votre vitesse de upload: {round(test.upload() / 1000 / 1000, 1)} Mbit/s")
print("================================")