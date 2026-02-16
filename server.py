import gradio as gr
from model import generate_caption

def generate_caption_ui(url):

    results = generate_caption(url)

    if isinstance(results, str):
        return results

    formatted = ""
    for item in results:
        formatted += f"Image: {item['image_url']}\nCaption: {item['caption']}\n\n"

    return formatted


gr.Interface(
    fn=generate_caption_ui,
    inputs=gr.Textbox(label="Enter webpage URL"),
    outputs=gr.Textbox(label="Captions"),
    title="Webpage Image Caption Generator"
).launch()
