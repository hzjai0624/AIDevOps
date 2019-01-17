# Model Training
 機械学習・深層学習を用いて、予測モデルを作成します。トレーニングの環境としては、様々な選択肢があります。

### 1. Microsoft-Hosted Agent
Azure DevOpsにて提供しているHosted agentは下記になります。
    - Ubuntu 16.04
    - Visual Studio 2017 on Windows Server 2016
    - macOS 10.13
    - Windows Server 1803 for funning Windows containers
    - Visual Studio 2015 on Windows Server 2012R2

### 2. Machine Learning Compute  
Azure Machine Learning serviceで提供しているPaaS型のVM環境になります。使いたいときに簡単に構築することが出来るので、最適なコストでハイパフォーマンスを実現することができます。

   ※Azure Machine Learning Computeについては、こちらの[ドキュメント](https://docs.microsoft.com/ja-jp/azure/machine-learning/service/how-to-set-up-training-targets#amlcompute)をご参照ください。

### 3. Self-hosted Agent
ユーザでVMを準備して利用する形態をさします。詳しい設定方法については、こちらの[サイト](https://qiita.com/taminami/items/9f44e8cb72e70b783c1b)をご参照ください。