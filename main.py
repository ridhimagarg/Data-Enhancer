# -*- coding: utf-8 -*-
#title           :main.py
#description     :This is the main file which plugs into each module and brings final result
#author          :ridhima.garg
#date            :07-Apr-2020
#version         :2.0
#usage           :python main.py
#notes           :
#python_version  :3.6.4


## ----------------------Importing all libraries--------------------------##

## CDQA third party library
from cdqa.utils.download import download_squad, download_model, download_bnpp_data
from cdqa.pipeline import QAPipeline
from cdqa.utils.filters import filter_paragraphs
from cdqa.retriever import BM25Retriever

## Importing base packages
import pandas as pd
from ast import literal_eval
import ast, os

## Our defined packages
import question_filtering 
from utils.basic_utils import *
import preprocess_data

##------------------------ Variables ---------------------------##

## Defining the variables
MODEL_DIR = './models/'
DATA_FILENAME = './data/data.xlsx'
QUESTION_FILENAME = './data/dictionary/questions_for_keys.json'
CACHING_DIR = './data/caching'
DATA_RAW_DIR = './data/raw/'



##--------------------------- Question generation according to Organization Name ---------------------------##


def get_dataframe():


def questions_acc_business(organization_name, ques_dic):

    """
    Parameters
    ----------

    organization_name : Name of the organization for which we are scraping the data

    ques_dic: dictionary of original question/key pairs loaded from json file

    Returns 
    -------

    Saves the json file in caching directory for that organization contains modified question/key pairs.
    
    """

    print("Creating Question...")

    # data = read_json(ques_dic)
    
    for key, values in ques_dic.items():

        new_values = []
        for value in values:

            value = value.replace("organization_name", organization_name)
            new_values.append(value)
        
        ques_dic[key] = new_values

    print("Saving json..")
    save_json(os.path.join(str(CACHING_DIR),str(organization_name)+".json"), ques_dic)

    # print(ques_dic)



##--------------------------------------------- Main function -----------------------------------##
  
def main(DATA_FILENAME, model_name= 'bert_qa.joblib'):

    """
    
    Parameters
    ----------

    DATA_FILENAME(Otional): File(EXCEL SHEET) consist title and paragrahs for each document of the business
    
    modek_name(Optional): BY default its takes BERT model, if wants to change pls specifiy


    Returns
    -------
    Final predictions: Keys with thier answers if present in the document.
    
    """

    final_predictions = {}

    preprocess_data(os.path.join(DATA_RAW_DIR,DATA_FILENAME), (DATA_FILENAME+'.json'))

    df = pd.read_excel(DATA_FILENAME, 'Sheet1')
    df['paragraphs'] = df['paragraphs'].apply(lambda x: ast.literal_eval(x))

    # print(df)
    organization_name = df.loc[0,'title']

    ## Reading original/common question for keys file
    ques_dic = read_json(QUESTION_FILENAME)
    ques_flat_list = [(key, item) for key, sublist in ques_dic.items() for item in sublist]
    
    ## Generating the question for that business and reading that json 
    questions_acc_business(organization_name, ques_dic)
    ques_dic = read_json(os.path.join(str(CACHING_DIR),str(organization_name)+".json"))
    ## Filtering out the questions for that business
    ques_para_id = question_filtering.filtered_questions(ques_dic)
    
    ## Fitting the model pipeline
    cdqa_pipeline = QAPipeline(reader=MODEL_DIR+str(model_name))
    retriever = cdqa_pipeline.fit_retriever(df=df)


    ## Iterating over each question and paragraph id for getting predictions
    for q_p_id in ques_para_id:

        key, ques = ques_flat_list[q_p_id[0]][0] , ques_flat_list[q_p_id[0]][1]

        query = str(ques)
        prediction = cdqa_pipeline.predict(query)
        if prediction[0][2] in q_p_id[1]:
            # print(prediction)
            if key not in final_predictions.keys():
                final_predictions[key] = [prediction[0][0]]
            else:
                final_predictions[key].append(prediction[0][0])

    print(final_predictions)


if __name__ == '__main__':
    main()




















#####---------------------------------- Further Use --------------------------##


#retriever = BM25Retriever(ngram_range=(1, 2), max_df=0.85, stop_words='english')
#retriever.fit(df)
# best_idx_scores = retriever.predict(query='How many employees are there of Dabur?')
# print(best_idx_scores)


# def paraphrasing_questions(ques_dic):

#     ques_flat_list = [(key, item) for key, sublist in ques_dic.items() for item in sublist]

#     new_ques_dic = {}

#     for values in ques_flat_list:
#         print(values[1])
#         paraphrased = paraphrasing.Paraphrasing(str(values[1]))

#         if values[0] not in new_ques_dic.keys():
#             new_ques_dic[values[0]] = paraphrased

#         else:
#             new_ques_dic[values[0]].append(paraphrased)

#     print(new_ques_dic)

# paraphrasing_questions(ques_dic)