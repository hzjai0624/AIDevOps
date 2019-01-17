# Data Quality Check
モデル学習を開始する前に、データの特徴を理解します。既存のモデル学習時に用いたデータと、最新のデータの特性を比較することで、再学習のタイミングが判断できたり、モデル学習前のデータ処理内容の判断が可能になります。

## Code ##
[data_test.py](../code/code/testing/data_test.py)
            
### 下記の観点でデータを確認
* check_schema : データの列数
* check_missing_values : 欠損値
* check_distribution : データ分布

