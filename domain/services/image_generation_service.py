from application.commands.generate_image import GenerateImage


class ImageGenerationService:
    def __init__(self, generate_image_handler):
        self.generate_image_handler = generate_image_handler

    def generate_image(self, text):
        command = GenerateImage(text)
        return self.generate_image_handler.handle(command)
