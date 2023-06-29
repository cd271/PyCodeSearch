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
 - `modules.py`: basic modules for model construction;
 - `train.py`: train and validate code/desc representation models; 
 - `repr_code.py`: encode code into vectors and store them to a file; 
 - `search.py`: perform code search;
 - `configs.py`: configurations for models defined in the `models` folder. Each function defines the hyper-parameters for the corresponding model;
 - `data_loader.py`: A PyTorch dataset loader;
 - `utils.py`: utilities for models and training;

## Pretrained Model

   A quick test with a pretrained model:

   ```
   python repr_code.py -t 202106140524 --reload_from 4000000
   python search.py -t 202106140524 --reload_from 4000000
   ```


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
