import torch
from transformers import AutoProcessor, BlipForConditionalGeneration
from choose_url import get_the_page
from torchvision import transforms
from PIL import Image
import io
import pandas as pd
import requests

# get the device
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

model_name = "Salesforce/blip-image-captioning-base"
processor = AutoProcessor.from_pretrained(model_name, use_fast = True)
model = BlipForConditionalGeneration.from_pretrained(model_name, tie_word_embeddings = False).to(device)

def generate_caption(url):
    
    try:
        results = []
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
        images_urls = get_the_page(url)
        for img_url in images_urls:
            response = requests.get(img_url,headers = headers, timeout = 10)
            response.raise_for_status()

            # open image
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            inputs = processor(images = image, text = "This image of ", return_tensors = 'pt').to(device)
            with torch.no_grad():
                outputs = model.generate(**inputs, max_length = 50)
                caption = processor.decode(outputs[0], skip_special_tokens = True)
            results.append({
                "image_url": img_url,
                "caption": caption
            }
            )
        return results
    except Exception as e:
        return f"The following error has showed up {e}"
    
    