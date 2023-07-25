from domain.model.image_generator import ImageGenerator
from flask import Flask, request, render_template
from application.handlers.generate_image_handler import GenerateImageHandler

from domain.services.image_generation_service import ImageGenerationService

app = Flask(__name__, template_folder="templates")

image_generator = ImageGenerator()

generate_image_handler = GenerateImageHandler(image_generator)

image_service = ImageGenerationService(generate_image_handler)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    image = image_service.generate_image(text)
    return render_template('generate.html', image=image)
