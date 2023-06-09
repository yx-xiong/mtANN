# Ensemble of multiple references for single-cell RNA sequencing data annotation and unseen cell-type identification

mtANN is a novel cell-type annotation framework
that integrates ensemble learning and deep learning
simultaneously, to annotate cells in a new query dataset with the help of multiple well-labeled reference datasets. It takes multiple well-labeled reference datasets and a query dataset that needs to be annotated as input. It begins with generating a series of subsets for each reference dataset by adopting various gene selection methods. Next, for each reference subset, a base classification model is trained based on neural networks. Then, mtANN annotates the cells in the query dataset by integrating the prediction results from all the base classification models. Finally, it identifies cells that may belong to cell types not observed in the reference datasets according to the uncertainty of the predictions.

![Figure1](Figure1.png)

## System Requirements

Python support packages: pandas, numpy, scanpy, scipy, sklearn, torch, giniclust3, rpy2

<<<<<<< HEAD
R support packages: limma, Seurat, parallel

=======
>>>>>>> 72453049c5c54617b0d1fca69290eae901d86269
## Versions the software has been tested on

### Environment 1
- System: Ubuntu 18.04.5
- Python: 3.8.8
- Python packages: pandas = 1.2.3, numpy = 1.19,2, scanpy=1.9.0, scipy = 1.6.1, sklearn = 0.24.1, torch = 1.9.1, giniclust3 = 1.1.0, rpy2 = 3.5.2
<<<<<<< HEAD
- R: 3.6.1
- R packages: limma = 3.42.2, Seurat = 3.1.1, parallel = 3.6.1

### Environment 2
- System: Windows 10
- Python: 3.8.15
- Python packages: pandas = 2.0.0, numpy = 1.23.5, scanpy=1.9.3, scipy = 1.10.1, sklearn = 1.1.3, torch = 1.10.0, giniclust3 = 1.1.2, rpy2 = 3.4.1
- R: 4.1.2
- R packages: limma = 3.50.3, Seurat = 4.2.0, parallel = 4.1.2

# Installation

`pip install mtANN==0.1.0`

# Useage
The mtANN repository includes the mtANN code files in the `mtANN` folder and provides a usage example which specifically shows the format of the input data and the usage of the main function. The data used in the example can be downloaded at [https://doi.org/10.5281/zenodo.7922657](https://doi.org/10.5281/zenodo.7922657). 

The input data considered by the current version of mtANN is in `csv` format, where rows are samples and columns are features. In addition, its cell type information is stored in another csv file, and its naming format is the name of the dataset + `_label`.
=======

# Installation

`pip install -i https://test.pypi.org/simple/ mtANN==0.0.0`

# Useage

`example1` shows data loading and mtANN annotation of query dataset on the Pancreas dataset collection. 

`example2` shows the simulation of unseen cell type and mtANN annotation of query dataset on the PBMC dataset collection. 
>>>>>>> 72453049c5c54617b0d1fca69290eae901d86269

 
# Contact

Please do not hesitate to contact Miss Yi-Xuan Xiong ([xyxuana@mails.ccnu.edu.cn](xyxuana@mails.ccnu.edu.cn)) or Dr. Xiao-Fei Zhang ([zhangxf@ccnu.edu.cn](zhangxf@ccnu.edu.cn)) to seek any clarifications regarding any contents or operation of the archive.



