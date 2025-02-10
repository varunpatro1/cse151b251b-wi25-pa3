from util import *
from train import *
import torch.optim as optim
import torch.nn as nn
import os

from tqdm import tqdm

from shakespeare_lstm import LSTMModel
from shakespeare_rnn import RNNModel

def train(model, device, train_dataloader, val_dataloader, config):
    
    ## TODO

def eval(model, device, val_dataloader):

    ## TODO
    
    return val_loss
