import torch
import torch.nn as nn

class LinearModel(nn.Module):
    def __init__(self, input_features, out_features, hidden_dim_1, hidden_dim_2):
        super().__init__()

        self.layer = nn.Sequential(
            nn.Linear(in_features= input_features, out_features=hidden_dim_1),
            nn.ReLU(),
            nn.Linear(in_features= hidden_dim_1, out_features= hidden_dim_2),
            nn.ReLU(),
            nn.Linear(in_features= hidden_dim_2, out_features= out_features)
        )
        
    def forward(self, x):
        x = self.layer(x)
        
        return x