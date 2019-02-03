# ローカル環境でのsklearnモデル学習 v1
from azureml.core.runconfig import RunConfiguration
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core import ScriptRunConfig
import os, json

# Workspaceの取得
ws = Workspace.from_config()

# Experimentの設定
experiment_name = 'devops0201'
exp = Experiment(workspace  = ws, name = experiment_name)
print(exp.name, exp.workspace.name, sep = '\n')

# 実行構成
run_config_user_managed = RunConfiguration()
run_config_user_managed.environment.python.user_managed_dependencies = True

# モデル学習コードの指定
src = ScriptRunConfig(source_directory = './code', script = 'training/train.py', run_config = run_config_user_managed)
print("モデル学習の実施")
run = exp.submit(src)

# 出力
run.wait_for_completion(show_output = True)

run_id={}
run_id['run_id'] = run.id
run_id['experiment_name'] = run.experiment.name
with open('aml_config/run_id.json', 'w') as outfile:
  json.dump(run_id,outfile)
