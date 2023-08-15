# Semantic Code Search Engine

## Overview

PyCodeSearch is a semantic code search engine allows both Code-To-Code and Text-To-Code search with fine-tuned `UniXcoder` model.

## Prerequisites & Installation

In your virtual environment, run:

```sh
pip install -r requirements.txt
```

Or you can directly install in the search engine notebook.

The above commands will install `cpu-only` version of the `PyTorch` package. Please refer to [PyTorch website](https://pytorch.org/get-started/locally/) for instructions on how to install other versions of `PyTorch`.

## Directory Structure
```
C:.
│  README.md
│  requirements.txt
│
├─notebook
│      CodeSearchEngine.ipynb
│      SearchEngine_with_examples.ipynb
│
└─search_engine
    │  data_prepare.py
    │  model.py
    │  unixcoder.py
    │  __init__.py
    │
    ├─Code2Code
    │  ├─Bi-Encoders
    │  │      Code2code_CodeT5_summarization.ipynb
    │  │      Code2code_UniXcoder.ipynb
    │  │
    │  └─Cross-Encoders
    │          Code2code_GraphCodeBERT.ipynb
    │
    ├─Evaluation
    │      Models_C4_Evaluation.ipynb
    │
    └─Text2Code
            Text2code_CodeT5_summarization.ipynb
            Text2code_GraphCodeBERT.ipynb
            Text2code_Unxicoder.ipynb
```

## Usage

The Code Search Engine User Interface `CodeSearchEngine.ipynb` can be find in folder `notebook`, where you can find a demo with 20 search examples for both `Code-To-Code` and `Text-To-Code` paradigms.

**Notice:** our demo takes "https://github.com/keno/algorithms" as an example repository database to search, thus the searching code snippets results all come from the source code in this repository. So, the searching result maybe irrelevant whenever there is no target code snippet in the database.
