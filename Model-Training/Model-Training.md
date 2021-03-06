# モデル学習
機械学習・深層学習を用いて、予測モデルを作成します。本ハンズオンでは、diabeteデータを使用します。

Workspaceの取得(config.jsonから接続情報を読み込み)
```python
ws = Workspace.from_config()
```

リッジ回帰にてモデル学習
```python
reg = Ridge(alpha = alpha)
reg.fit(data['train']['X'], data['train']['y'])
preds = reg.predict(data['test']['X'])
```

メトリックの記録
```python
run.log('正規化率', alpha)
run.log('平均二乗誤差', mean_squared_error(preds, data['test']['y']))
```

## コード ##
__Microsoft-Hosted Agent を使用した例__  
Script : [10-TrainOnLocal.py](../code/script/11-TrainOnLocal.py)  
Notebook : [10-TrainOnLocal.ipynb](../code/notebook/11-TrainOnLocal.ipynb)

__Machine Learning Compute__  
Script : [13-TrainOnMLCompute.py](../code/script/13-TrainOnMLCompute.py)
Notebook : [13-TrainOnMLCompute.ipynb](../code/notebook/13-TrainOnMLCompute.ipynb)


## 参考：Azure Machine Learning service の計算環境について
トレーニングの環境としては、様々な選択肢があります。

### 1. Microsoft-Hosted Agent
Azure DevOpsにて提供しているHosted agentは下記になります。 

__Microsoft-Hosted Agent__  
    - Ubuntu 16.04  
    - Visual Studio 2017 on Windows Server 2016  
    - macOS 10.13  
    - Windows Server 1803 for funning Windows containers  
    - Visual Studio 2015 on Windows Server 2012R2  

### 2. Machine Learning Compute  
Azure Machine Learning serviceで提供しているPaaS型のVM環境になります。使いたいときに簡単に構築することが出来るので、最適なコストでハイパフォーマンスを実現することができます。

   ※Azure Machine Learning Computeについては、こちらの[ドキュメント](https://docs.microsoft.com/ja-jp/azure/machine-learning/service/how-to-set-up-training-targets#amlcompute)をご参照ください。

### 3. Self-hosted Agent
ユーザ自身でVMを準備して利用する形態をさします。詳しい設定方法については、こちらの[サイト](https://qiita.com/taminami/items/9f44e8cb72e70b783c1b)をご参照ください。

## コード ##
__Microsoft-Hosted Agent を使用した例__  
Script : [10-TrainOnLocal.py](../code/script/10-TrainOnLocal.py)  
Notebook : [10-TrainOnLocal.ipynb](../code/notebook/10-TrainOnLocal.ipynb)

__Machine Learning Compute__  
Script : [13-TrainOnMLCompute.py](../code/script/13-TrainOnMLCompute.py)
Notebook : [13-TrainOnMLCompute.ipynb](../code/notebook/13-TrainOnMLCompute.ipynb)