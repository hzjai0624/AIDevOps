import pickle
from azureml.core import Workspace
from azureml.core.run import Run
import os
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import numpy as np
import json
import subprocess
from typing import Tuple, List

# メトリック記録開始
run = Run.get_context()

# データの準備 (クラウドのストレージのマウント、データダウンロードも可能)
X, y = load_diabetes(return_X_y=True)
columns = ['age', 'gender', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
data = {
    "train": {"X": X_train, "y": y_train},
    "test": {"X": X_test, "y": y_test}
}

print('モデル学習開始....')

# ハイパーパラメータの設定
alphas = np.arange(0.0, 1.0, 0.05)
alpha = alphas[np.random.choice(alphas.shape[0], 1, replace=False)][0]
print("alpha:", alpha)

reg = Ridge(alpha=alpha)
reg.fit(data['train']['X'], data['train']['y'])
preds = reg.predict(data['test']['X'])
mse = mean_squared_error(preds, data['test']['y'])
print("mse:", mse)

# メトリック記録
run.log('mse', mse)
run.log('alpha', alpha)


# モデルファイルの保存
model_name = "diabetes-remote.pkl"
os.makedirs('outputs', exist_ok=True)
joblib.dump(value=reg, filename='outputs/' + model_name)
