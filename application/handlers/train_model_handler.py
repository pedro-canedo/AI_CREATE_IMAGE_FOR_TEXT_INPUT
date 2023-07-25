

from domain.model.image_generator import ImageGenerator
from domain.model.training_data import TrainingData


class TrainModelHandler:
    def __init__(self, image_generator: ImageGenerator, training_data: TrainingData):
        self.image_generator = image_generator
        self.training_data = training_data

    def handle(self, command):
        dataloader = self.training_data.load(command.data_path)
        self.image_generator.train(dataloader, command.epochs)