from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_webhook():
    image_link = request.json.get('image_link')

    if image_link:
        try:
            image = Image.open(image_link)
        except Exception as e:
            return jsonify({"error": str(e)})
        
        width, height = image.size
        rgb_data = []
        
        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, y))
                r, g, b = pixel[0], pixel[1], pixel

                
