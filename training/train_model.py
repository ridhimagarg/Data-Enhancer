from cdqa.utils.download import download_squad, download_model, download_bnpp_data
from cdqa.pipeline import QAPipeline
from os import path

MODEL_DIR = '../models/'
NEW_TRAIN_MODEL_FILENAME = 'trained-model.joblib'
INPUT_DATA_PATH = '../data/annotator_format.json'

# Downloading pre-trained BERT fine-tuned on SQuAD 1.1
if not path.exists(MODEL_DIR+str('bert_qa.joblib')):
    download_model('bert-squad_1.1', dir=MODEL_DIR)

# Downloading pre-trained DistilBERT fine-tuned on SQuAD 1.1
if not path.exists(MODEL_DIR+str('distilbert_qa.joblib')):
    download_model('distilbert-squad_1.1', dir=MODEL_DIR)

cdqa_pipeline = QAPipeline(reader=MODEL_DIR+str('bert_qa.joblib')) # use 'distilbert_qa.joblib' for DistilBERT instead of BERT
cdqa_pipeline.fit_reader(INPUT_DATA_PATH)
cdqa_pipeline.dump_reader(MODEL_DIR+str(NEW_TRAIN_MODEL_FILENAME))