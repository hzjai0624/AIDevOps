# モデルの評価
import os, json
from azureml.core import Workspace
from azureml.core import Experiment
from azureml.core.model import Model
import azureml.core
from azureml.core import Run

run_id = ""   # failするrun id を記載
   
# Workspaceの取得
ws = Workspace.from_config()

# 最新のrun, Experimentの取得 
with open("aml_config/run_id.json") as f:
    config = json.load(f)
new_model_run_id = config["run_id"]
experiment_name = config["experiment_name"]
exp = Experiment(workspace = ws, name = experiment_name)

fail_run = Run(exp,run_id=run_id)

fail_run.fail()
