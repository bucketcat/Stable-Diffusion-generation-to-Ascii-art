import sys
import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import subprocess

url = "http://127.0.0.1:7860"

# Use command-line arguments for prompt and steps
prompt = sys.argv[1]
steps = int(sys.argv[2])

payload = {
    "prompt": prompt,
    "steps": steps
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()

for i in r['images']:
    image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

    png_payload = {
        "image": "data:image/png;base64," + i
    }
    response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

    pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text("parameters", response2.json().get("info"))
    image.save('output.png', pnginfo=pnginfo)

    subprocess.run(['python', 'convertTransform.py', 'output.png', '--output-file=ascii.txt'])