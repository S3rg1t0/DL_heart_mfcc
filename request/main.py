import requests

# Define la URL de la API
url = "http://localhost:5000/predict"

# Define la ruta al archivo de audio que deseas enviar
audio_file = "set_a/set_a/artifact__201105040918.wav"
audio_file = "set_a/extrahls__201101161027.wav"
audio_file = "set_a/murmur__201108222242.wav"
# audio_file = "set_a/normal__201105021654.wav"

# Define los datos multipart/form-data para la petición
data = {
    "file": open(audio_file, "rb"),
}

# Realiza la petición POST
response = requests.post(url, files=data)

# Imprime la respuesta de la API
print(response.json()['predicted_class'])
