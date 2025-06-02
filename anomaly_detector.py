import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LogESP.settings')
django.setup()

from siem.models import Log
import pandas as pd
from sklearn.ensemble import IsolationForest

logs = Log.objects.all()
df = pd.DataFrame(list(logs.values()))

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

features = df[['hour']]  # you can enhance this

model = IsolationForest(contamination=0.1)
df['anomaly'] = model.fit_predict(features)

for i, row in df.iterrows():
    log = Log.objects.get(id=row['id'])
    log.anomalous = True if row['anomaly'] == -1 else False
    log.save()

print("Anomaly detection complete.")
