# DMHGAST: Dynamic Multi-hop Graph Attention Networks with Positional Encoding for Spatial Transcriptomics Analysis



## Overview
DMHGAST is designed for spatial domains recognition of spatial transcriptomics (ST) data. 

Spatial transcriptomics, a leading tech for tissue microenvironment analysis, enables high-throughput gene expression profiling while retaining spatial info, revealing cell type distribution and tissue function mechanisms. However, current analysis approaches face three critical limitations: simple concatenation of spatial coordinates and gene expression profiles leads to poor info integration and unclear spatial-gene feature interactions; existing graph-based models use static structures with fixed neighborhoods, failing to capture hierarchical spatial dependencies across biological scales; most self-supervised frameworks lack mechanisms to jointly preserve global-local features and spatial dependencies. To address these, we present DMHGAST-a dynamic multi-hop graph attention network with spatial transcriptomics-optimized positional encoding. Specifically, we design a spatial positional encoding module that employs a learnable trigonometric function-based strategy to map cellular coordinates into high dimensional interpretable feature embeddings, effectively addressing the information integration deficiency caused by simplistic concatenation of spatial coordinates with gene expression profiles in conventional approaches. Meanwhile, we construct a dynamically constructed multi-hop routing graph attention network that achieves adaptive aggregation of multi-order neighborhood information through multi-head attention mechanisms, successfully capturing hierarchical characteristics of spatial dependencies.  Additionally, we propose a self-supervised framework integrating global-local feature contrasting and adjacency-guided spatial regularization, optimizing hierarchical discrimination and spatial dependency preservation through dual-loss balancing for stable, interpretable representations. Comprehensive experimental validation demonstrates that our DMHGAST significantly outperforms existing state-of-the-art methods across multiple benchmark datasets derived from diverse technological platforms.

## Requirements
You'll need to install the following packages in order to run the codes.
* python>=3.8
* torch>=1.8.0
* cudnn>=10.2
* numpy==1.22.3
* scanpy==1.9.1
* anndata==0.8.0
* rpy2==3.4.1
* pandas==1.4.2
* scipy==1.8.1
* scikit-learn==1.1.1
* tqdm==4.64.0
* matplotlib==3.4.2
* R>=4.0.3

## Getting started
See run.py and Tutorial for STAR_clustering.py

## Software dependencies
scanpy

pytorch

pyG
