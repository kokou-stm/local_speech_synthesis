import requests
import io
import scipy.io.wavfile as wav

# L'URL de ton API FastAPI
url = "http://localhost:8000/predit/"

# Le message à passer au modèle
message = "Transport le wòɖo ɖe anyigba me le esia kple esia. Esi wòkpe ɖe ŋgɔ nɔnɔ la, ŋutilã, tsitsi kple doɖoɖo ɖo eŋu."

# Envoi de la requête POST avec le message
response = requests.post(url, params={"message": message})

# Vérification si la requête a réussi
if response.status_code == 200:
    # Récupérer le contenu audio de la réponse
   
    audio_data = response.content
    #audio_io = io.BytesIO(audio_data)
    with open('out.wav', 'wb') as f:
        f.write(audio_data)

    
else:
    print(f"Erreur dans la requête : {response.status_code}")
