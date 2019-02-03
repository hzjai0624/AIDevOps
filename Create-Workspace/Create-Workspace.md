# Workspaceの作成
Azure Machine Learning service の Workspace を設定します。通常Workspaceは、分析テーマごとに作成します。予め接続情報を"config.json"に記載してください。

1. Azure Machine Learning serviceのリソース情報をconfig.jsonに記載する
2. config.jsonからWorkspaceの情報を読み取る
3. 該当のリソースがない場合、新規作成する。該当リソースがある場合は、その環境をロードする

## config.json
下記のように記載します
```json
{
    "subscription_id": "Azureサブスクリプション",
    "resource_group": "リソースグループ名",
    "workspace_name": "ワークスペース名",
    "location": "ロケーション名"
}
```

## コード ##
Script : [00-Workspace.py](../code/script/00-WorkSpace.py)  
Notebook : [00-Workspace.ipynb](../code/notebook/00-WorkSpace.ipynb)

### 実装例

新規Workspace作成
```python
ws = Workspace.create(
    name = "ワークスペース名",
    subscription_id = "Azureサブスクリプション",
    resource_group = resource_group,
    create_resource_group=True,
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
            



