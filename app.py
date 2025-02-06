import numpy as np
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from transformers import VitsModel, AutoTokenizer
import torch
import scipy.io.wavfile
from pydantic import BaseModel
from io import BytesIO

# Charger le modèle et le tokenizer
checkpoint = "facebook/mms-tts-ewe"
model = VitsModel.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)


# Initialiser FastAPI
app = FastAPI()

@app.get('/')
def first():
    return {"Hello": "man"}

#Predict:

@app.post('/predit/')
def predict(message:str):
    output = ""
    input = tokenizer(message, return_tensors = "pt")
    with torch.no_grad():
        output = model(**input).waveform
    audio_np = output.squeeze(0).cpu().numpy()
    #print("Adio: ", audio_np, type(audio_np))
    # Enregistrer le fichier audio en mémoire
    wav_io = BytesIO()
    #scipy.io.wavfile.write(wav_io, 22050, audio_np.astype(np.float32))
    scipy.io.wavfile.write(wav_io, rate=model.config.sampling_rate, data=(audio_np * 32767).astype(np.int16))
    wav_io.seek(0)  # Rewind pour la lecture

    # Retourner les données audio sous forme de flux pour que le client puisse lire le fichier
    return StreamingResponse(wav_io, media_type="audio/wav")
    #return audio_np

