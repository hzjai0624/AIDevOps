# 探索的モデル構築
本Notebookでは、Azure Machine Learning serviceの基本的な機能を使用して、モデル開発を効率的に実施します。

### __A_MLWorkspace.oipynb__ ###
Azure Machine Learning service Workspaceへの接続を確認します。

### __B1_TrainOnLocal.ipynb__ ###
ローカルのPython環境でモデル学習をします。メトリックの記録、モデルファイルのアップロードを行います。

### __B2_TrainOnRemote.ipynb__ ###
リモートの Machine Learning Compute環境でモデル学習をします。学習するタイミングでVMを起動するため、起動までに5分程度の時間がかかります。

### __C_Deploy_ACI.ipynb__ ###
バージョン管理されているモデルをAzure Container Instancesにデプロイします。