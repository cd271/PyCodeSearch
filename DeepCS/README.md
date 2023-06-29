# Deep Code Search

## Dependency
* Python 3.6
* PyTorch 
* tqdm

 ```
 pip install -r requirements.txt
 ```


## Code Structures

 - `models`: neural network models for code/desc representation and similarity measure;
 - `output`: pretrained model example;
 - `data`: download and unzip dataset from [Google Drive](https://drive.google.com/drive/folders/1GZYLT_lzhlVczXjD6dgwVUvDDPHMB6L7?usp=sharing);
 - `modules.py`: basic modules for model construction;
 - `train.py`: train and validate code/desc representation models; 
 - `repr_code.py`: encode code into vectors and store them to a file; 
 - `search.py`: perform code search;
 - `configs.py`: configurations for models defined in the `models` folder. Each function defines the hyper-parameters for the corresponding model;
 - `data_loader.py`: A PyTorch dataset loader;
 - `utils.py`: utilities for models and training;


## Usage

   ### Train

   ```bash
   python train.py --model JointEmbeder -v
   ```
   ### Code Embedding

   ```bash
   python repr_code.py --model JointEmbeder -t XXX --reload_from YYY
   ```
   where `XXX` stands for the timestamp, and `YYY` represents the iteration with the best model.

   ### Search

   ```bash
   python search.py --model JointEmbeder -t XXX --_reload_from YYY
   ```
   where `XXX` stands for the timestamp, and `YYY` represents the iteration with the best model.

   ### Configuration

   Edit hyper-parameters and settings in `config.py`

## Quick test

   A quick test with a pretrained model:

   ```
python repr_code.py -t 202306290524 --reload_from 4000000
python search.py -t 202306290524 --reload_from 4000000
   ```

   Note: pretrained model should be put in `./output/JointEmbeder/github/202306290524/models/`, which can not be uploaded to GitHub because of the file size.
