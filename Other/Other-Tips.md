# その他
## Machine Learning Compute (計算環境)の作成
```python
compute_name = "cpucluster"  # クラスタ名 

# This example uses CPU VM. For using GPU VM, set SKU to STANDARD_NC6
vm_size = os.environ.get("BATCHAI_CLUSTER_SKU", "STANDARD_D2_V2")


compute_min_nodes = 0 # 最小ノード数
compute_max_nodes = 2 # 最大ノード数
vm_size = "STANDARD_D2_V2"  # VMサイズ
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

・デフォルトのdatastoreの情報を取得  
※ Azure ML service のWorkspaceにはデフォルトのblobストレージがあります  
・ローカルのデータフォルダ、ターゲットのデータフォルダを指定し、アップロード

```python
# 
ds = ws.get_default_datastore()
print(ds.datastore_type, ds.account_name, ds.container_name) 
ds.upload(src_dir='./data', target_path='mnist', overwrite=True, show_progress=True)
```