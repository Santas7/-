# Import Library
import random
import glob
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


class Cnn(nn.Module):
    pass


class Dataset(torch.utils.data.Dataset):
    """
        this class is for loading our image sets
    """
    def __init__(self, file_list, transform=None):
        self.transform = transform
        self.file_list = file_list

    # dataset length
    def __len__(self):
        self.filelength = len(self.file_list)
        return self.filelength

    # load an one of images
    def __getitem__(self, idx: int):
        img = Image.open(self.file_list[idx])
        img_transformed = self.transform(img.convert("RGB"))
        label = self.file_list[idx].split('/')[-1].split('.')[0]
        #print(self.file_list[idx], label)
        if label == os.path.join("new_dataset", "rose"):
            label = 1
        elif label == os.path.join("new_dataset", "tulip"):
            label = 0
        #print(label)
        return img_transformed, label


def сreating_and_training_neural_network():


if __name__ == '__main__':
    сreating_and_training_neural_network()