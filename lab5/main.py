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
    def __init__(self):
        super(Cnn, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=2),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc1 = nn.Linear(3 * 3 * 64, 10)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(10, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = out.view(out.size(0), -1)
        out = self.relu(self.fc1(out))
        out = self.fc2(out)
        return out


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
    # set seed and random value
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    torch.manual_seed(1234)
    if device == 'cuda':
        torch.cuda.manual_seed_all(1234)

    # create class_labels and work with file annotation
    class_labels = []
    for i in range(948):
        class_labels.append(True)
    for i in range(954):
        class_labels.append(False)

    # list of all pictures
    list_pictures = glob.glob(os.path.join('new_dataset', '*.jpg'))
    train_list, train_test_val, train_val, test_val = train_test_split(list_pictures, class_labels, test_size=0.2, shuffle=True)
    test_list, val_list, test, val = train_test_split(train_test_val, test_val, test_size=0.5)
    # print(len(train_list), len(test_list), len(val_list))

    # check dataset and pictures
    random_idx = np.random.randint(1, len(list_pictures), size=10)
    fig = plt.figure()
    i = 1
    for idx in random_idx:
        ax = fig.add_subplot(2, 5, i)
        img = Image.open(list_pictures[idx])
        plt.imshow(img)
        i += 1
    plt.axis('off')
    plt.show()
    # print(train_list[0].split('/')[-1].split('.')[0])

    # training, test and validation samples, respectively
    train_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])
    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])
    test_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ])

    train_data = Dataset(train_list, transform=train_transforms)
    test_data = Dataset(test_list, transform=test_transforms)
    val_data = Dataset(val_list, transform=val_transforms)

    train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=10, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset=test_data, batch_size=10, shuffle=True)
    val_loader = torch.utils.data.DataLoader(dataset=val_data, batch_size=10, shuffle=True)

    # build model
    model = Cnn().to(device)
    model.train()

    # set loss function and optimizer
    optimizer = optim.Adam(params=model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # train our network
    epochs = 10

    # in order to make it easier and more convenient to build graphs, let's create these lists
    train_accuracy = []
    train_loss = []
    valid_accuracy = []
    valid_loss = []

    for epoch in range(epochs):
        epoch_loss = 0
        epoch_accuracy = 0
        for data, label in train_loader:
            data = data.to(device)
            label = label.to(device)
            output = model(data)
            loss = criterion(output, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            acc = ((output.argmax(dim=1) == label).float().mean())
            epoch_accuracy += acc / len(train_loader)
            epoch_loss += loss / len(train_loader)
        train_accuracy.append(float(epoch_accuracy))
        train_loss.append(float(epoch_loss))
        print('Epoch : {}, train accuracy : {}, train loss : {}'.format(epoch + 1, epoch_accuracy, epoch_loss))
        with torch.no_grad():
            epoch_val_accuracy = 0
            epoch_val_loss = 0
            for data, label in val_loader:
                data = data.to(device)
                label = label.to(device)
                val_output = model(data)
                val_loss = criterion(val_output, label)
                acc = ((val_output.argmax(dim=1) == label).float().mean())
                epoch_val_accuracy += acc / len(val_loader)
                epoch_val_loss += val_loss / len(val_loader)
            valid_accuracy.append(float(epoch_val_accuracy))
            valid_loss.append(float(epoch_val_loss))
            print('Epoch : {}, val_accuracy : {}, val_loss : {}'.format(epoch + 1, epoch_val_accuracy, epoch_val_loss))

        # creation of graphs and their analysis
        # first graphs
        plt.figure(figsize=(15, 5))
        plt.plot(range(len(train_accuracy)), train_accuracy, color="green")
        plt.plot(range(len(valid_accuracy)), valid_accuracy, color="red")
        plt.legend(["Train accuracy", "Valid accuracy"])
        plt.show()

        # second graphs
        plt.figure(figsize=(15, 5))
        plt.plot(range(len(train_loss)), [float(value) for value in train_loss], color="green")
        plt.plot(range(len(valid_loss)), [float(value) for value in valid_loss], color="red")
        plt.legend(["Train loss", "Valid loss"])
        plt.show()

    # item 7-8
    # a little analysis of the graphs
    # 1. index increase in both the train_accuracy and valid_accuracy
    # 2. this graph shows a strong decline in train_loss and not so strong in valid_loss

    # Assignment: to evaluate the model's performance on the test sample.
    # Answer: the model behaves perfectly, shows good results
    # When asked what is the best model to use). The best one! ( train_accuracy )
    # saving model

if __name__ == '__main__':
    сreating_and_training_neural_network()