# ローカル環境でのsklearnモデル学習 v2
import pickle
from azureml.core import Workspace, Experiment
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

# Workspaceの取得
ws = Workspace.from_config()

# Experimentの設定
experiment_name = 'prelab3'
exp = Experiment(workspace  = ws, name = experiment_name)
print("Workspace: " + exp.workspace.name, "Experiment: " +exp.name, sep = '\n')

# Azure ML service メトリック取得
run = exp.start_logging()

# Sklearnサンプルデータの準備
X, y = load_diabetes(return_X_y = True)
columns = ['age', 'gender', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
data = {
    "train":{"X": X_train, "y": y_train},        
    "test":{"X": X_test, "y": y_test}
}

print('Model Training Started ...')

# ランダムにハイパーパラメータを選択
alphas = np.arange(0.0, 1.0, 0.05)
alpha=alphas[np.random.choice(alphas.shape[0], 1, replace=False)][0]
print("Parameter: ", alpha)
reg = Ridge(alpha = alpha)
reg.fit(data['train']['X'], data['train']['y'])
print("Model Training Completed")

#テストデータに対する予測値出力と精度確認
preds = reg.predict(data['test']['X'])
mse = mean_squared_error(preds, data['test']['y'])
print("mse: ", mse)

# メトリック記録
run.log('alpha', alpha)
run.log('mse', mse)

# モデルファイルの保存
model_name = "prelab3.pkl"
os.makedirs('outputs', exist_ok=True)
# note file saved in the outputs folder is automatically uploaded into experiment record
with run:
    joblib.dump(value=reg, filename='outputs/' + model_name)

# run終了
run.complete()


# 今回のrun情報をrun_id.jsonに書き込み
run_id={}
run_id['run_id'] = run.id
run_id['experiment_name'] = run.experiment.name
with open('aml_config/run_id.json', 'w') as outfile:
  json.dump(run_id,outfile)