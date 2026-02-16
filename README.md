# know_your_image
Get the url of a webpage, scan all the image of that particular webpage, and tell me what the image is

## choose url file
1. Get the url of the file
2. Grab all the images of that files (request--> headers --> url)
3. include all the image types
4. exclude all other types

## model file
1. processor = AutoProcessor.from_pretrained('Salesforce/blip-image-captioning-base)
2. model = BlipforConditionalGeneration('Salesforce/blip-image-captioning-base)

## server file
1. Use 'Gradio' to create the interface
