class ImageGeneratedEvent:
    def __init__(self, image):
        self.image = image

    def notify(self):
        print("Image generated")
        # Aqui você pode adicionar o código para notificar outras partes do sistema
