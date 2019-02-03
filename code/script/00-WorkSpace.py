# Azure Machine Learning service Workspaceへの接続情報
from azureml.core import Workspace
import os, json
import azureml.core
print("Azure ML service Python SDK Version:", azureml.core.VERSION)

# config.jsonに予め接続情報を記載
with open("aml_config/config.json") as f:
    config = json.load(f)

workspace_name = config['workspace_name']
resource_group = config['resource_group']
subscription_id = config['subscription_id']
location = config['location']
#location = 'southeastasia'
try:
    # 既存のWorkspaceを使用
    ws = Workspace.get(name = workspace_name,
                             subscription_id = subscription_id,
                             resource_group = resource_group)

except:
    # 新しいWorkspaceを作成
    ws = Workspace.create(name = workspace_name,
                             subscription_id = subscription_id,
                             resource_group = resource_group,
                             #create_resource_group=True,
                             location=location)

# Workspaceの情報 
print("Workspapce Details:", ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')