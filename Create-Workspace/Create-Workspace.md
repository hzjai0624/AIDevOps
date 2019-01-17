# Create Workspace
Azure Machine Learning service のWorkspaceを設定します。

1. Azure Machine Learning serviceのリソース情報をconfig.jsonに記載する
2. config.jsonからWorkspaceの情報を読み取る
3. 該当のリソースがない場合、新規作成する。該当リソースがある場合は、その環境をロードする

## config.json
下記のように記載します。
{
    "subscription_id": "ff18d7a8-962a-406c-858f-49acd23d6c01",
    "resource_group": "DevOps_AzureML_Demo",
    "workspace_name": "AzureML_Demo_ws",
    "location": "southcentralus"
}
## Code ##
[00-Workspace.py](../code/aml_service/00-WorkSpace.py)

### 実装例

新規Workspace作成
```python
ws = Workspace.create(
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
            



