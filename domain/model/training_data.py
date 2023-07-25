from torch.utils.data import DataLoader
from torchvision import datasets, transforms

class TrainingData:
    def __init__(self, batch_size=64):
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])
        self.batch_size = batch_size

    def load(self, path):
        dataset = datasets.ImageFolder(root=path, transform=self.transform)
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=True)
        return dataloader
