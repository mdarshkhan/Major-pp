# MITIGATING INSIDER THREAT: A NEURAL NETWORK APPROACH FOR ENHANCED SECURITY

> **IEEE Major Project**  
> A machine-learning-based cybersecurity application for detecting and mitigating insider threats using network-security data and neural-network techniques.

---

## 📌 Project Overview

**Mitigating Insider Threat: A Neural Network Approach for Enhanced Security** is a cybersecurity project that applies machine-learning and neural-network techniques to identify potentially malicious or anomalous activity in network environments.

The project combines:

- **Django** for the web application
- **Python** for backend and machine-learning implementation
- **PyTorch** for neural-network/model execution
- **PyTorch Geometric** for graph-based machine learning
- **NSL-KDD** network-security datasets for experimentation
- **SQLite** for application data storage
- HTML, CSS and JavaScript for the web interface

The project provides a web-based interface through which users can interact with the application and its security-analysis functionality.

---

## 🎯 Objectives

The main objectives of the project are:

1. Detect potentially malicious network activity.
2. Apply neural-network techniques to cybersecurity data.
3. Analyze network-security datasets for insider-threat-related patterns.
4. Provide a web-based interface for interacting with the system.
5. Explore graph-based machine-learning approaches for security analysis.
6. Improve the detection of abnormal or suspicious activity.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Django | Web application framework |
| PyTorch | Neural-network / deep-learning framework |
| PyTorch Geometric | Graph neural-network functionality |
| NumPy | Numerical processing |
| Pandas | Dataset processing |
| SciPy | Scientific computing |
| Scikit-learn | Machine-learning utilities |
| NetworkX | Graph/network processing |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Pillow | Image processing |
| SQLite | Application database |
| HTML/CSS/JavaScript | Frontend |
| Git/GitHub | Version control |

---

## 📂 Project Structure

```text
MITIGATING INSIDER THREAT A NEURAL NETWORK APPROACH
FOR ENHANCED SECURITY/
│
├── App/
│   ├── Admins/
│   │   ├── migrations/
│   │   └── ...
│   │
│   ├── Backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── Users/
│   │   ├── migrations/
│   │   └── ...
│   │
│   ├── model/
│   │   └── nsl-kdd/
│   │       ├── KDDTrain+.arff
│   │       ├── KDDTrain+.txt
│   │       ├── KDDTest+.arff
│   │       ├── KDDTest+.txt
│   │       ├── dataset.csv
│   │       ├── train.csv
│   │       ├── test.csv
│   │       ├── gcn_model.pth
│   │       ├── predict.py
│   │       └── Main.ipynb
│   │
│   ├── scripts/
│   ├── static/
│   │   ├── assets/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   ├── img/
│   │   │   └── vendor/
│   │
│   ├── templates/
│   │   ├── admin/
│   │   └── user/
│   │
│   ├── db.sqlite3
│   └── manage.py
│
├── Document/
│   └── Project documentation
│
├── .gitignore
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/mdarshkhan/Major-pp.git
cd Major-pp
```

---

## 2. Open the Django Application Directory

The Django `manage.py` file is located inside the `App` directory.

### Windows

```cmd
cd App
```

Verify:

```cmd
dir manage.py
```

You should see:

```text
manage.py
```

---

# 🐍 3. Create a Virtual Environment

From inside the `App` directory:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

If activation is successful, your terminal should show something similar to:

```text
(venv)
```

---

# 📦 4. Install Python Dependencies

Install Django:

```cmd
pip install django
```

Install the main data-science and machine-learning packages:

```cmd
pip install numpy pandas scipy scikit-learn sympy mpmath tqdm networkx matplotlib seaborn pillow
```

Install PyTorch:

```cmd
pip install torch torchvision torchaudio
```

Install PyTorch Geometric:

```cmd
pip install torch-geometric
```

> **Note:** PyTorch Geometric's optional compiled packages can depend on the installed PyTorch and Python versions. If the project raises an import error for packages such as `torch-scatter`, `torch-sparse`, `torch-cluster`, or `pyg-lib`, install the compatible wheels for your specific PyTorch version.

---

# 🔍 5. Verify the Installation

Run:

```cmd
python -c "import django; print('Django:', django.get_version())"
```

Check PyTorch:

```cmd
python -c "import torch; print('PyTorch:', torch.__version__)"
```

Check PyTorch Geometric:

```cmd
python -c "import torch_geometric; print('PyTorch Geometric:', torch_geometric.__version__)"
```

Check the main data-science packages:

```cmd
python -c "import numpy, pandas, scipy, sklearn, networkx, matplotlib, seaborn; print('Core ML/Data packages OK')"
```

---

# 🗄️ 6. Database

The repository contains:

```text
App/db.sqlite3
```

Therefore, the project currently includes its existing SQLite database.

If you need to apply Django migrations:

```cmd
python manage.py migrate
```

---

# ▶️ 7. Run the Application

From:

```text
Major-pp\App
```

run:

```cmd
python manage.py runserver
```

You should see something similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🧠 Machine Learning Component

The machine-learning resources are located in:

```text
App/model/nsl-kdd/
```

The repository contains NSL-KDD datasets and model-related files including:

```text
KDDTrain+.arff
KDDTrain+.txt
KDDTrain+_20Percent.arff
KDDTrain+_20Percent.txt
KDDTest+.arff
KDDTest+.txt
KDDTest-21.arff
KDDTest-21.txt
dataset.csv
train.csv
test.csv
target.xlsx
gcn_model.pth
predict.py
Main.ipynb
```

### Trained Model

```text
gcn_model.pth
```

contains the saved PyTorch model used by the project.

### Prediction Script

```text
predict.py
```

contains prediction-related machine-learning functionality.

### Notebook

```text
Main.ipynb
```

contains the project's notebook-based machine-learning experimentation.

---

# 🔬 Dataset

The project uses the **NSL-KDD** network-security dataset.

The dataset contains network-traffic records used for machine-learning-based security analysis and classification.

The project includes both training and testing data in multiple formats, including:

- `.arff`
- `.txt`
- `.csv`

---

# 🏗️ Application Architecture

```text
                    ┌──────────────────────┐
                    │      Web Browser      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Django         │
                    │    Web Application   │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌─────────────────┐
       │    SQLite DB    │          │ ML / Prediction │
       └─────────────────┘          └────────┬────────┘
                                             │
                                             ▼
                                  ┌────────────────────┐
                                  │ PyTorch / PyG Model│
                                  └─────────┬──────────┘
                                            │
                                            ▼
                                  ┌────────────────────┐
                                  │   NSL-KDD Dataset  │
                                  └────────────────────┘
```

---

# 🔐 Security Focus

The project focuses on identifying suspicious network behavior associated with potential insider threats.

The machine-learning component can be used to analyze security-related network records and classify activity based on learned patterns.

The overall workflow can be represented as:

```text
Network Security Data
          │
          ▼
   Data Preprocessing
          │
          ▼
 Feature / Graph Processing
          │
          ▼
 Neural Network / GCN Model
          │
          ▼
    Classification
          │
          ▼
 Security Analysis
```

---

# 🧪 Development Environment

Recommended environment:

```text
Python 3.x
Django
PyTorch
PyTorch Geometric
SQLite
Git
```

The exact PyTorch/PyTorch-Geometric versions should be kept compatible with the Python environment being used.

---

# ⚠️ Troubleshooting

### Django command not found

If:

```text
'django-admin' is not recognized
```

run:

```cmd
python -m pip install django
```

Then verify:

```cmd
python -m django --version
```

---

### PyTorch import error

Check:

```cmd
python -c "import torch; print(torch.__version__)"
```

If this fails, reinstall PyTorch in the active virtual environment.

---

### PyTorch Geometric import error

Check:

```cmd
python -c "import torch_geometric; print(torch_geometric.__version__)"
```

For errors involving compiled extensions, install the package versions compatible with your installed PyTorch version.

---

### Port 8000 already in use

Run Django on another port:

```cmd
python manage.py runserver 8080
```

Then open:

```text
http://127.0.0.1:8080/
```

---

# 📄 Project Documentation

Additional project documentation and academic materials are available inside:

```text
Document/
```

---

# 🎓 Academic Project

**Project Title:**  
**MITIGATING INSIDER THREAT: A NEURAL NETWORK APPROACH FOR ENHANCED SECURITY**

**Project Type:** Major / Academic Project

**Domain:** Cybersecurity + Machine Learning + Web Application

---

# 👨‍💻 Author

**Mohammed Arsh Khan**

B.Tech – Information Technology  
CMR Engineering College  
Batch: 2022–2026

---

# 🔗 Repository

GitHub:

https://github.com/mdarshkhan/Major-pp

---

# 📌 Important Notes

- The project is provided for academic and educational purposes.
- The included ML model and datasets are part of the project implementation.
- PyTorch Geometric dependencies may require version-specific installation depending on the Python and PyTorch versions used.
- The project should be run from the `App` directory because `manage.py` is located there.

---

## ⭐ Project Workflow

```text
Clone Repository
       │
       ▼
Create Virtual Environment
       │
       ▼
Install Dependencies
       │
       ▼
Enter App Directory
       │
       ▼
Run Django Migrations
       │
       ▼
Start Django Server
       │
       ▼
Access Web Application
       │
       ▼
Interact with ML-Based
Security Analysis
```

---

## 📜 License

This repository is primarily intended for academic and educational use.
