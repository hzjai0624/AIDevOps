# Create Workspace
Azure Machine Learning service のWorkspaceを設定します。

1. config.jsonからWorkspaceの情報を読み取る
2. 該当のリソースがない場合、新規作成する。該当リソースがある場合は、その環境をロードする。

## Code ##
[00-Workspace.py](../code/aml_service/00-Workspace.py)


### 実装例

新規Workspace作成
```python
ws = Workspace.create(
    name = workspace_name,
    subscription_id = subscription_id,
    resource_group = resource_group,
    #create_resource_group=True,
    location=location
    )
```


既存Workspaceの取得
```python
ws = Workspace.get(
    name = workspace_name,
    subscription_id = subscription_id,
    resource_group = resource_group
)
```
            



