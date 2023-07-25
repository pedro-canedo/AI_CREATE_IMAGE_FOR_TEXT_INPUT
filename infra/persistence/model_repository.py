import torch


class ModelRepository:
    def __init__(self, path):
        self.path = path

    def save_model(self, model):
        torch.save(model.state_dict(), self.path)

    def load_model(self, model):
        model.load_state_dict(torch.load(self.path))
        model.eval()
        return model