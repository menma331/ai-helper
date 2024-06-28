import requests

from loader import client


def download_file_from_url(url, local_filename='voice.mp3'):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


def convert_voice_to_text(url):
    voice_path = download_file_from_url(url)
    audio_file = open(voice_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text
