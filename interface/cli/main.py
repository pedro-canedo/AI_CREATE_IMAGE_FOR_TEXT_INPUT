import click
from application.handlers.generate_image_handler import GenerateImageHandler
from domain.model.image_generator import ImageGenerator
from domain.services.image_generation_service import ImageGenerationService

image_generator = ImageGenerator()
generate_image_handler = GenerateImageHandler(image_generator)
image_service = ImageGenerationService(generate_image_handler)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('text')
def generate(text):
    image = image_service.generate_image(text)
    # Imprima a imagem ou salve-a em um arquivo

if __name__ == '__main__':
    cli()
