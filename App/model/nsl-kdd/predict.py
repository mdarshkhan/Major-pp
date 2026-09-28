import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
import numpy as np

# Define the GCN model class
class GCNModel(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, dropout_rate=0.5):
        super(GCNModel, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.fc = torch.nn.Linear(hidden_dim, output_dim)
        self.dropout_rate = dropout_rate

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.dropout(x, p=self.dropout_rate, training=self.training)
        x = F.relu(self.conv2(x, edge_index))
        x = F.dropout(x, p=self.dropout_rate, training=self.training)
        x = self.fc(x)
        return F.log_softmax(x, dim=1)

# Label mapping
target_labels = {
    16: 'neptune', 14: 'normal', 34: 'saint', 7: 'mscan', 20: 'guess_passwd',
    32: 'smurf', 15: 'apache2', 25: 'satan', 27: 'buffer_overflow', 19: 'back',
    1: 'warezmaster', 4: 'snmpgetattack', 3: 'processtable', 12: 'pod',
    23: 'httptunnel', 2: 'nmap', 6: 'ps', 35: 'snmpguess', 18: 'ipsweep',
    8: 'mailbomb', 9: 'portsweep', 30: 'multihop', 17: 'named', 24: 'sendmail',
    11: 'loadmodule', 0: 'xterm', 28: 'worm', 21: 'teardrop', 5: 'rootkit',
    22: 'xlock', 29: 'perl', 10: 'land', 13: 'xsnoop', 26: 'sqlattack',
    39: 'ftp_write', 36: 'imap', 37: 'udpstorm', 38: 'phf', 31: 'mailbomb',
    33: 'portsweep'
}

# Load the trained model
input_dim = 40  # 40 features as used during training
hidden_dim = 64
output_dim = len(target_labels)
model = GCNModel(input_dim, hidden_dim, output_dim)
model.load_state_dict(torch.load('gcn_model.pth'))
model.eval()

# Function to predict the label of custom input
def predict_custom_input(input_str):
    # Convert the input string to a tensor (exclude the last value - target)
    input_values = np.array([float(x) for x in input_str.split(',')])[:40]  # Take only the first 40 features
    input_tensor = torch.tensor(input_values, dtype=torch.float).unsqueeze(0)

    # Dummy edge index for single node prediction
    edge_index = torch.tensor([[0], [0]], dtype=torch.long)

    # Make prediction
    with torch.no_grad():
        output = model(input_tensor, edge_index)
        predicted_class = output.argmax(dim=1).item()
        predicted_label = target_labels.get(predicted_class, 'Unknown')

    return predicted_label

# Example usage
if __name__ == '__main__':
    example_input = '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,175,1,0.1,0.0,0.89,1.0,0.01,1.0,0.0,255,1,0.0,0.84,0.0,0.0,0.07,0.0,0.62,1.0,1,49,1'
    prediction = predict_custom_input(example_input)
    print(f'Predicted label: {prediction}')
