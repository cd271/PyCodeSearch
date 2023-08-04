# Semantic Code Search Engine

Semantic code search engine allows user to input a code snippet or natural language query for searching with fine-tuned `UniXcoder` model.

## Prerequisites & Installation

In your virtual environment, run:

```sh
pip install -r requirements.txt
```

Or you can directly install in the search engine notebook.

The above commands will install `cpu-only` version of the `PyTorch` package. Please refer to [PyTorch website](https://pytorch.org/get-started/locally/) for instructions on how to install other versions of `PyTorch`.

## Usage

The Code Search Engine User Interface `CodeSearchEngine.ipynb` can be find in folder `notebook`, where you can find a demo with 20 search examples for both `Code-To-Code` and `Text-To-Code` paradigms.

Notice: our demo takes "https://github.com/keno/algorithms" as an example repository database to search, thus the searching code snippets results all come from the source code in this repository. So, the searching result maybe irrelevant whenever there is no target code snippet in the database.

<br/>

<br/>

<br/>

<br/>


Supervisor: Rosa Filgueira

Student: 220017269

Date: 04/08/2023
