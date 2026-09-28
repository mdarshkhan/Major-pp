# load_features.py (run inside manage.py shell or a script)
import pandas as pd
from Users.models import UserFeatureData

df = pd.read_csv('path/to/your_preprocessed_dataset.csv')  # ensure columns include id/hash + 40 features
for idx, row in df.iterrows():
    hash_link = str(row['hash'])  # change column name accordingly
    # take first 40 feature columns — adjust column selection as per your CSV
    features = [str(row[c]) for c in df.columns if c not in ['hash']]  # trim if needed
    # ensure exactly 40 features
    features = features[:40] + ['0'] * max(0, 40 - len(features))
    feature_string = ','.join(features)
    UserFeatureData.objects.update_or_create(hash_link=hash_link, defaults={'feature_vector': feature_string})
