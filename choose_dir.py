import os
import glob
import model
from PIL import Image
import torch

def choose_dir(dir_path:str):
    img_exts = ['jpg', 'jpeg', 'png']
    with open("captions.txt", "w") as caption_file:
        for image_ext in img_exts:
            for img_path in glob.glob(os.path.join(dir_path, f"*.{image_ext}")):

                # load your image
                img = Image.open(img_path).convert("RGB")

                # inputs
                inputs = model.processor(images = img, return_tensors = 'pt').to(model.device)

                # generate a caption for the image
                with torch.no_grad():
                    outputs = model.model.generate(**inputs, max_length = 50)

                caption = model.processor.decode(outputs[0], skip_special_tokens = True)

                caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")
                print(f"Processed: {img_path}")
    return "captions.txt"

caption_created = choose_dir("/Users/tinonturjamajumder/Pictures/paper_graph")
print(f"Captions saved to: {caption_created}")