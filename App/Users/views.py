from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv
import numpy as np
from django.contrib.auth.models import User

# Try importing your models
try:
    from .models import Prediction, UserFeatureData
except ImportError:
    Prediction = None
    UserFeatureData = None


# ======================
# 🔹 GCN Model Definition
# ======================
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


# ======================
# 🔹 Load Trained Model
# ======================
INPUT_DIM = 40
HIDDEN_DIM = 64
OUTPUT_DIM = 40  # Adjust based on your dataset's number of labels

model = GCNModel(INPUT_DIM, HIDDEN_DIM, OUTPUT_DIM)
try:
    model.load_state_dict(torch.load('model/nsl-kdd/gcn_model.pth', map_location='cpu'))
    model.eval()
except Exception as e:
    print(f"⚠️ Warning: Could not load model — {e}")


# ======================
# 🔹 Prediction View
# ======================
def userpredict(request):
    prediction_result = None
    error = None

    LABEL_MAP = {
        0: "Normal Activity ✅",
        1: "Suspicious Behavior ⚠️",
        2: "Data Exfiltration 🚫",
        3: "Unauthorized Access 🚷",
        4: "Privilege Escalation 🔐",
        5: "Policy Violation 🧾",
        6: "Account Misuse 🔄",
        7: "Phishing Attempt 🎣",
        8: "Network Reconnaissance 🌐",
        9: "Brute Force Attack 💥",
        10: "Malware Infection 🦠",
        11: "Denial of Service ⛔",
        12: "Credential Theft 🧠",
        13: "Data Corruption 🧩",
        14: "Critical Insider Threat 🚨",
        15: "Unknown / Unclassified ❓"
    }

    if request.method == 'POST':
        hash_link = request.POST.get('hash_link', '').strip()
        if not hash_link:
            error = "Please provide a hash link."
        else:
            try:
                if UserFeatureData is None:
                    error = "Model or UserFeatureData not found."
                else:
                    uf = UserFeatureData.objects.get(hash_link=hash_link)
                    features = uf.get_vector()

                    # Ensure exactly 40 features
                    if len(features) < 40:
                        features += [0.0] * (40 - len(features))
                    elif len(features) > 40:
                        features = features[:40]

                    input_tensor = torch.tensor(features, dtype=torch.float).unsqueeze(0)
                    edge_index = torch.tensor([[0, 0], [0, 0]], dtype=torch.long)

                    with torch.no_grad():
                        output = model(input_tensor, edge_index)
                        pred_class = output.argmax(dim=1).item()

                    predicted_label = LABEL_MAP.get(pred_class, f"Class {pred_class}")

                    if Prediction:
                        Prediction.objects.create(
                            user=request.user if request.user.is_authenticated else None,
                            user_input=hash_link,
                            predicted_label=predicted_label
                        )

                    prediction_result = predicted_label

            except UserFeatureData.DoesNotExist:
                error = "⚠️ Hash link not found in database."
            except Exception as e:
                error = f"⚠️ Error during prediction: {str(e)}"

    return render(request, 'user/userpredict.html', {
        'prediction_result': prediction_result,
        'error': error
    })


# ======================
# 🔹 User Home View
# ======================
@login_required(login_url='/Users/userlogin/')
def userhome(request):
    return render(request, 'user/userhome.html', {'user': request.user})


# ======================
# 🔹 User Registration
# ======================
def userregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password:
            messages.error(request, "All fields are required.")
            return redirect('userregister')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('userregister')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('userlogin')

    return render(request, 'user/userregister.html')


# ======================
# 🔹 User Login
# ======================
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('userhome')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'user/userlogin.html')


# ======================
# 🔹 User Logout
# ======================
def userlogout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('userlogin')
# ======================
# 🔹 View All User Data + Predictions
# ======================
@login_required(login_url='/Users/userlogin/')
def userdata(request):
    from .models import UserFeatureData, Prediction

    # Get all user feature records
    users_data = UserFeatureData.objects.all().order_by('-created_at')

    # Get recent predictions (if exist)
    predictions = {p.user_input: p.predicted_label for p in Prediction.objects.all()}

    # Merge both into one clean structure for the template
    user_rows = []
    for u in users_data:
        preview = ', '.join(u.feature_vector.split(',')[:5]) + "..."  # show first few features
        user_rows.append({
            'hash_link': u.hash_link,
            'feature_preview': preview,
            'predicted_label': predictions.get(u.hash_link, 'No Prediction Yet'),
            'created_at': u.created_at
        })

    return render(request, 'user/userdata.html', {'user_rows': user_rows})
