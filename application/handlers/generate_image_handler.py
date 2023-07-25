from domain.model.image_generator import ImageGenerator


class GenerateImageHandler:
    def __init__(self, image_generator: ImageGenerator):
        self.image_generator = image_generator

    def handle(self, command):
        return self.image_generator.generate(command.text)