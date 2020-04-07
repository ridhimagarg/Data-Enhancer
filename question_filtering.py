# -*- coding: utf-8 -*-
#title           :question_filtering.py
#description     :This will filter the question whose information is not present in any document of business.
#author          :ridhima.garg
#date            :07-Apr-2020
#version         :2.0
#usage           :python question_filtering.py
#notes           :
#python_version  :3.6.4


import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
import re, os, random, ast


from utils import download, basic_utils


MODEL_DIR = 'models/tfhub_model'
DATA_FILENAME = './data/data.xlsx'


def USE_embeddings(features: list):
    """
    Parameters
    ----------

    features: list of sentences, for generating sentences embedding for each sentence.

    Returns
    -------
    list of list, each sublist represents the 125-dimensional vector

    """


    if os.path.exists(MODEL_DIR):
        print("Loading Model ....")
        print(os.path.join(MODEL_DIR+ str("/TFModel_1.0")))
        embed = hub.Module(os.path.join(MODEL_DIR+ str("/TFModel_1.0")))
    
    else:
        download.download_model(MODEL_DIR)
        print("Loading Model ....")
        embed = hub.Module(os.path.join(MODEL_DIR+ str("/TFModel_1.0")))

    print("Loaded successfully!")
    with tf.Session() as sess:
        sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
        embeddings =sess.run(embed(features))


    return embeddings



def calculating_similarity(QUESTIONS_DIC, data_filename = DATA_FILENAME):

    """
    Parameters
    ----------

    QUESTIONS_DIC: Dic of questions(Loaded json question dictionary)

    data_filename: DATA Processed file (contains title, paragraphs)


    Returns
    --------

    Score of similarity betwwen question and paragraphs i.e, Dot product of question and each sentence embedding 
  
    """

    print("Calculating similarity...")

    ## Creating list for flattening all the sentences/questions
    data = []
    questions = []

    ## Reading data and questions
    df = pd.read_excel(DATA_FILENAME, 'Sheet1')
    df['paragraphs'] = df['paragraphs'].apply(lambda x: ast.literal_eval(x))

    questions_dic = QUESTIONS_DIC

    for _ , value in questions_dic.items():
        questions.extend(value)

    for _ , row in df.iterrows():
        data.extend(row["paragraphs"])

    # print(data)
    # print(questions)

    data_use_embedding = USE_embeddings(data)
    question_use_embedding = USE_embeddings(questions)

    # print(np.dot(question_use_embedding, data_use_embedding.T))
    
    return np.dot(question_use_embedding, data_use_embedding.T)


def discard_question(question_data_array):
    """
    
    Parameters
    ----------

    question_data_array: Score of similarity betwwen question and paragraphs i.e, Dot product of question and each sentence embedding 
  
    
    Return
    ------
    Question and Paragrah Id: Question id which contains information the paragraph id
    
    """


    ques_para_id = []

    for ques_id , x in enumerate(question_data_array):

        para_id = np.where(x>= 0.5)[0]

        if para_id.size != 0:
            ques_para_id.append((ques_id, list(para_id)))

    print(ques_para_id)

    return ques_para_id

def filtered_questions(QUESTIONS_DIC):

    """
    Main function which return the questions and paragraph id

    Parameters
    ----------
    QUESTION_DIC : dictionary loaded from json which contains questions according to company

    Returns
    --------

    Question and Paragraph Id

    """

    question_data_array = calculating_similarity(QUESTIONS_DIC)
    filtered_questions = discard_question(question_data_array)

    return filtered_questions




