from cdqa.utils.download import download_squad, download_model, download_bnpp_data
from cdqa.pipeline import QAPipeline
from cdqa.utils.filters import filter_paragraphs
from cdqa.retriever import BM25Retriever

## Importing base packages
import pandas as pd
from ast import literal_eval
import ast, os

import pandas as pd
from ast import literal_eval
from cdqa.pipeline import QAPipeline
import preprocess_data

preprocess_data.get_excel('./data/downloads/rental_1.json', './data/downloads/rental_1.xlsx')

df = pd.read_excel('./data/downloads/rental_1.xlsx', 'Sheet1')
df['paragraphs'] = df['paragraphs'].apply(lambda x: ast.literal_eval(x))
# df = pd.read_csv('./data/processed/sample_7.xlsx', converters={'paragraphs': literal_eval})

cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib') # use 'distilbert_qa.joblib' for DistilBERT instead of BERT
cdqa_pipeline.fit_retriever(df=df)

print(cdqa_pipeline.predict(query='The house rental contract is between?'))