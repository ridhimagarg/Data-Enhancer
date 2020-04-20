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
import ast, os, time, multiprocessing

## Our defined packages
import question_filtering 
from utils.basic_utils import *
import preprocess_data

##------------------------ Variables ---------------------------##

## Defining the variables
MODEL_DIR = './models/'
# DATA_FILENAME = 'data.xlsx'
QUESTION_FILENAME = './data/dictionary/questions_for_keys.json'
CACHING_DIR = './data/caching'
DATA_RAW_DIR = './data/raw/'
DATA_PROCESSED_DIR = './data/processed/'
RESPONSE_DIR = './data/response/'


##--------------------------- Question generation according to Organization Name ---------------------------##


# def get_dataframe():


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

    manager = multiprocessing.Manager()
    final_predictions = manager.dict()
    start_time = time.time()

    preprocess_data.get_excel(os.path.join(DATA_RAW_DIR,DATA_FILENAME), os.path.join(DATA_PROCESSED_DIR, (DATA_FILENAME.split('.json')[0]+'.xlsx')))

    df = pd.read_excel(os.path.join(DATA_PROCESSED_DIR, (DATA_FILENAME.split(".json")[0]+'.xlsx')), 'Sheet1')
    df['paragraphs'] = df['paragraphs'].apply(lambda x: ast.literal_eval(x))

    # print(df)
    organization_name = df.loc[0,'title']

    ## Reading original/common question for keys file
    ques_dic = read_json(QUESTION_FILENAME)
    
    
    ## Generating the question for that business and reading that json 
    questions_acc_business(organization_name, ques_dic)
    ques_dic = read_json(os.path.join(str(CACHING_DIR),str(organization_name)+".json"))
    ques_flat_list = [(key, item) for key, sublist in ques_dic.items() for item in sublist]
    ## Filtering out the questions for that business
    ques_para_id = question_filtering.filtered_questions(ques_dic, os.path.join(DATA_PROCESSED_DIR, (DATA_FILENAME.split(".json")[0]+'.xlsx')))
    
    ## Fitting the model pipeline
    cdqa_pipeline = QAPipeline(reader=MODEL_DIR+str(model_name))
    retriever = cdqa_pipeline.fit_retriever(df=df)


    ## Iterating over each question and paragraph id for getting predictions
    processes = []
    for q_p_id in ques_para_id:

        p = multiprocessing.Process(target=multiprocess_ques_predict, args=(q_p_id,ques_flat_list, cdqa_pipeline, final_predictions))
        processes.append(p)
        p.start()
        
        for process in processes:
            process.join()

    print(final_predictions)    
    for key_ques in ques_flat_list:
        if key_ques[0] not in final_predictions.keys():
            final_predictions[key_ques[0]] = None

    for key, values in final_predictions.items():
        if values != None:
            final_predictions[key] = list(set(values))

    final_predictions["name"] = [organization_name]


    print(final_predictions)
    save_json(os.path.join(RESPONSE_DIR, DATA_FILENAME), final_predictions)

    print('That took {} seconds'.format(time.time() - start_time))

    return final_predictions


def multiprocess_ques_predict(q_p_id, ques_flat_list, cdqa_pipeline, final_predictions):

    # final_predictions = {}

    key, ques = ques_flat_list[q_p_id[0]][0] , ques_flat_list[q_p_id[0]][1]
        
    #print(q_p_id)
    print("Key:", key)
    print("Ques:", ques)
    query = str(ques)
    prediction = cdqa_pipeline.predict(query)
    prediction = (prediction)
    print("Paragraph id by cdqa:", prediction[2])
    # print(prediction[0][2])
    print("Paragraphs id by TFhub:",q_p_id[1])
    if prediction[2] in q_p_id[1]:
        print("Prediction arry by cdqa:", prediction)
        if key not in final_predictions.keys():
            final_predictions[key] = [prediction[0]]
        else:
            final_predictions[key].append(prediction[0])

    return final_predictions


if __name__ == '__main__':
    main("sample_8.json")




















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