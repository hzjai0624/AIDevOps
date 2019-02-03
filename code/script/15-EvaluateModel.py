# モデルの評価
import os, json
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core.model import Model
import azureml.core
from azureml.core import Run

# Workspaceの取得
ws = Workspace.from_config()

# 最新のrun, Experimentの取得 
with open("aml_config/run_id.json") as f:
    config = json.load(f)
new_model_run_id = config["run_id"]
experiment_name = config["experiment_name"]
exp = Experiment(workspace = ws, name = experiment_name)


try:
  # 本コードは、保存されているモデルの中で最新のものが現在稼働中のモデルであるという前提
  # Workspaceに登録されているモデルのリスト
  model_list = Model.list(ws)

  # 稼働中モデルの取得
  production_model = next(filter(lambda x: x.created_time == max(model.created_time for model in model_list),  model_list))
  production_model_run_id = production_model.tags.get('run_id')

  # 稼働中モデルの学習時に記録したメトリックを取得
  production_model_run = Run(exp,run_id=production_model_run_id)
  new_model_run = Run(exp,run_id=new_model_run_id)
  
  # 稼働中モデルのmse
  production_model_mse=production_model_run.get_metrics().get('mse')
  # 新しいモデルのmse
  new_model_mse=new_model_run.get_metrics().get('mse')
  print('稼働中のモデルの平均二乗誤差 : {}, 新しいモデルの平均二乗誤差: {}'.format(production_model_mse,new_model_mse))

  promote_new_model=False
  if new_model_mse < production_model_mse:
    promote_new_model=True
    print('新しいモデルの方が精度が高いので、登録します')
except:
  promote_new_model=True
  print('最初のモデルなので登録をします')

run_id = {}
run_id['run_id'] = ''
# run idを /aml_config/run_id.json を書き込む
if promote_new_model:
  run_id['run_id'] = new_model_run_id

run_id['experiment_name'] = experiment_name
with open('aml_config/run_id.json', 'w') as outfile:
  json.dump(run_id,outfile)