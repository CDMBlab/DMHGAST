import os
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import torch
import anndata
from sklearn import metrics
from DMHGAST import DMHGAST
from DMHGAST.utils import clustering
seed = 8888
random.seed(seed)
np.random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

os.environ['R_HOME'] = 'D:\\Install\\R-4.2.2\\R-4.2.2'
os.environ['R_USER'] = 'D:\Install\\anaconda3\envs\py10two\Lib\site-packages\\rpy2'


save_model_file = 'D:\Code2\workwork2\work2\weights.pth'
file_path = "D:\Code2\workwork2\work2\data\STARmap\\STARmapBY3_1k.h5ad"
adata = anndata.read_h5ad(file_path)
adata.var_names_make_unique()
print(adata)


model = GAAEST.GAAEST(adata, device=device,save_model_file=save_model_file)
adata = model.train()
#
radius = 25
n_clusters =6
tool = 'mclust'
if tool == 'mclust':
   clustering(adata, n_clusters, radius=radius, method=tool, refinement=True)
elif tool in ['leiden', 'louvain']:
   clustering(adata, n_clusters, radius=radius, method=tool, start=0.1, end=2.0, increment=0.01, refinement=False)

#
# df_meta = pd.read_csv(path + '/metadata.tsv', sep='\t')
# df_meta_layer = df_meta['annot_type']
# adata.obs['ground_truth'] = df_meta_layer.values
# adata = adata[~pd.isnull(adata.obs['ground_truth'])]
#
ARI = metrics.adjusted_rand_score(adata.obs['domain'], adata.obs['ground_truth'])
NMI = metrics.normalized_mutual_info_score(adata.obs['domain'], adata.obs['ground_truth'])
print('ARI:', ARI)
print('NMI:', NMI)
#
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (4, 2)
sc.pl.embedding(adata, basis="spatial", color='domain', s=20,show=False)

#save_path = "D:\Code2\workwork2\work2\\result\Human_Breast_Cancer\\"
plt.savefig('ttest.jpg', bbox_inches='tight', dpi=600)
# #
# # adata.write_h5ad(save_path+'experiment2.h5ad')




