# その他
## Machine Learning Compute (計算環境)の作成
```python
compute_name = ""  # クラスタ名 

# This example uses CPU VM. For using GPU VM, set SKU to STANDARD_NC6
vm_size = os.environ.get("BATCHAI_CLUSTER_SKU", "STANDARD_D2_V2")

# compute_min_nodes : 最小ノード数
# compute_max_nodes : 最大ノード数

compute_min_nodes = 0
compute_max_nodes = 2
provisioning_config = AmlCompute.provisioning_configuration(
                              vm_size = vm_size,
                              min_nodes = compute_min_nodes, 
                              max_nodes = compute_max_nodes) 
# ML Computeの作成
print(‘ 新しい計算環境の作成中 ...s ')
compute_target = ComputeTarget.create(ws, compute_name, provisioning_config)
```

## クラウドへのデータアップロード
様々な方法でクラウドのストレージ(Blob, FileShare)にデータをアップロードする方法がありますが、ここではAzure ML service Python SDKを使う方法を示します。

```python
# note that while loading, we are shrinking the intensity values (X) from 0-255 to 0-1 so that the model converge faster.
X_train = load_data('./data/train-images.gz', False) / 255.0 
y_train = load_data('./data/train-labels.gz', True).reshape(-1)

X_test = load_data('./data/test-images.gz', False) / 255.0 
y_test = load_data('./data/test-labels.gz', True).reshape(-1)
```