# built-in modules
import re
import json
import pysbd
from nltk.tokenize import word_tokenize
# from create_corpus import append_new_line
import spacy
import pandas as pd
model = "en_core_web_sm"
nlp = spacy.load(model)
nlp.max_length = 20000000 
merge_nps = nlp.create_pipe("merge_noun_chunks")
nlp.add_pipe(merge_nps)
# with open("stopwords.txt") as fp:
#     stop_words = fp.readlines()

state = {'ALABAMA': 'AL', 'ALASKA': 'AK', 'ARIZONA': 'AZ', 'ARKANSAS': 'AR', 'CALIFORNIA': 'CA', 'COLORADO': 'CO', 
                    'CONNECTICUT': 'CT', 'DELAWARE': 'DE', 'FLORIDA': 'FL', 'GEORGIA': 'GA', 'HAWAII': 'HI', 'IDAHO': 'ID', 
                    'ILLINOIS': 'IL', 'INDIANA': 'IN', 'IOWA': 'IA', 'KANSAS': 'KS', 'KENTUCKY': 'KY', 'LOUISIANA': 'LA', 
                    'MAINE': 'ME', 'MARYLAND': 'MD', 'MASSACHUSETTS': 'MA', 'MICHIGAN': 'MI', 'MINNESOTA': 'MN', 
                    'MISSISSIPPI': 'MS', 'MISSOURI': 'MO', 'MONTANA': 'MT', 'NEBRASKA': 'NE', 'NEVADA': 'NV', 
                    'NEW HAMPSHIRE': 'NH', 'NEW JERSEY': 'NJ', 'NEW MEXICO': 'NM', 'NEW YORK': 'NY', 'NORTH CAROLINA': 'NC', 
                    'NORTH DAKOTA': 'ND', 'OHIO': 'OH', 'OKLAHOMA': 'OK', 'OREGON': 'OR', 'PENNSYLVANIA': 'PA', 
                    'RHODE ISLAND': 'RI', 'SOUTH CAROLINA': 'SC', 'SOUTH DAKOTA': 'SD', 'TENNESSEE': 'TN', 'TEXAS': 'TX', 
                    'UTAH': 'UT', 'VERMONT': 'VT', 'VIRGINIA': 'VA', 'WASHINGTON': 'WA', 'WEST VIRGINIA': 'WV', 
                    'WISCONSIN': 'WI', 'WYOMING': 'WY', 'UNITED STATES OF AMERICA':'USA', 'UNITED STATES':'USA'}
keys = [key for key in state.keys()]
values = [value for value in state.values()]
# helper independent functions

def read_text_file(FilePath: str) -> str:
    """
    Read .txt file and returns text data
    """
    with open(FilePath,encoding = 'utf8') as fp:
        # text = fp.read()
        text_list = fp.readlines()
    return text_list

def read_json_file(FilePath: str) -> str :
    """
    Read .json file and returns text data
    """
    # key_name = input("Enter the key that contains text data: ")
    with open(str(FilePath)) as fp:
        data = json.load(fp)
        # text = data['text']
    return data

def read_excel_file(FilePath: str):
    df = pd.read_excel(FilePath)
    return df

def create_json(data,FilePath: str):
    with open(FilePath,'w') as fp:
        json.dump(data,fp,indent=4)


################################ Used in case HTML text is found ############
def remove_html_tags(TextData:str) -> str:
    """
    Remove all the html tags from the `TextData`
    """

    pattern = re.compile('<.*?>')
    clean_text = re.sub(pattern, '', TextData)

    return clean_text

def remove_image_tags(TextData:str) -> str:
    """
    Remove the image tags from the `TextData`
    """

    pattern = re.compile('\[image:[\s]?.*?\]')
    clean_text = re.sub(pattern, '', TextData)

    return clean_text

def lower_text(text: str) -> str:
    """
    Lower the text.
    """
    return text.lower()

def clean_merged_text(TextData: str) -> str:
    """
    segregate merged <integers><string><integer> names
    """
    string = TextData
    pattern = re.compile(r'[0-9][a-zA-Z]+[0-9]')
    result = pattern.finditer(string)
    list_of_indices = []
    for i in result:
        list_of_indices.append(i.span())
    
    old_new = []
    for i1,i2 in list_of_indices:
        new = str(string[i1])+' '+str(string[(i1+1):(i2-1)])+' '+str(string[i2-1])
        old = str(string[i1:i2])
        old_new.append((old,new))
    if old_new:
        for t1,t2 in old_new:
            text = string.replace(t1,t2)
        return text
    else:
        return string
##################################################################################


####################### Refines text by removing unwanted symbols and unwanted characters ##############
def refine_text(TextData: str) -> str:
    text = TextData
    txt = TextData
    text = txt.replace('$',' $')
    symbols = '!#?:^*()_+=~|'
    for symbol in symbols:
        if symbol in text:
            text = text.replace(symbol, '')
    # pattern = re.compile(r'\\x[a-zA-Z0-9]?[0-9a-zA-Z]\\?')
    # text = re.sub(pattern,' ',text)
    text = text.replace(";","\n")
    text = re.sub(r'\\r\\n',"\n",text)
    patterns = [r'x[a-z0-9]{7}-[0-9]{4}',r'\\x[a-z0-9][a-z0-9]']
    for r in patterns:
        text = re.sub(r," ",text)
    # text = re.sub('[^A-Za-z0-9]+', ' ',text)
    text = text.replace(r'\r\n','\n')
    text = text.replace(r'\n','\n')
    text = text.replace('\\','')
    text = text.replace(' $ ',' $')
    # for word in ['b"',"b'"]:
    #     # print(word)
    #     text = text.replace(word,"")
    text = re.sub(r'\s+',' ',text)
    text = text.replace(' , ',', ')
    text = text.strip()
    # if text[-1] == " ":
    #     text = text.replace(text[-1],"")
    if text[-1] in [r"'",r'"']:
        # print("into if loop")
        text = text.replace(text[-1],".")
    text = re.sub(r'\.+', ".", text)
    text = text.replace(' . ','.')
    return text

######################### Pysbd Sentence Segmenter ###########################333
def pysbd_sent_segmenter(TextData: str) -> list:
    seg = pysbd.Segmenter(language="en", clean=False)
    segmented_sentences = seg.segment(TextData)
    sentences = []
    for sent in segmented_sentences:
        tokenized_words = word_tokenize(sent)
        if len(tokenized_words)>4:
            sentences.append(tokenized_words)
    # print(len(sentences))
    # print(len(segmented_sentences))
    sentences_2 = []
    for word_tokens in sentences:
        joined_tokens = " ".join(word_tokens)
        sentences_2.append(joined_tokens)
    # print(sentences_2)
    return sentences_2

############# sentence_selection: select only those sentences that satisfy certain conditions ##########
def sentence_selection(ListOfSentences: list) -> list:
    correct_sentences = []
    model = "en_core_web_sm"
    nlp = spacy.load(model)
    merge_nps = nlp.create_pipe("merge_noun_chunks")
    nlp.add_pipe(merge_nps)    
    for line in ListOfSentences:
        doc = nlp(line)
        pos_tags_list = [(token,token.pos_,token.dep_) for token in doc]
    #     print(pos_tags_list)
        sentence_correct = False
    # check for POS Tags
        # check for VERB,ADV,AUX Pos tags
        verbs_flag = False
        for word,pos,dep in pos_tags_list:
            if pos in ["VERB","ADV","AUX"]:
                verbs_flag = True
        # Check for NOUN,PROPN Pos tags
        noun_flag = False
        for word,pos,dep in pos_tags_list:
            if pos in ["NOUN","PROPN"]:
                noun_flag = True
        if verbs_flag == True and noun_flag == True:
    # Check for Dependencies 
        # check for Subject
            sub_flag = False
            for word,pos,dep in pos_tags_list:
                if dep in ["nsubj"]:
                    sub_flag = True
            obj_flag = False
            for word,pos,dep in pos_tags_list:
                if dep in ["dobj","pobj"]:
                    obj_flag = True
            if sub_flag == True and obj_flag == True:
                sentence_correct = True
        if sentence_correct == True:
            correct_sentences.append(line)
    return correct_sentences

def get_processed_data(TextData: str) -> list:
    refined_text = refine_text(TextData)
    segmented_sentences = pysbd_sent_segmenter(refine_text)
    selected_sentences = sentence_selection(segmented_sentences)
    return selected_sentences

############# As per Ridhima's Requirement below function takes excel data and process it ##########

def get_json(MainJsonFilePath: str, ExpectedJsonFilePath: str) -> dict:
    json_ = read_json_file(MainJsonFilePath)
    print(json_)
    title = json_['string']
    text = json_['text']
    ListOfSentences = get_processed_data(text)
    dataframe = pd.DataFrame(columns=['title', 'paragraphs'])
    dataframe.append({'title':title, 'paragraphs': ListOfSentences})
    dataframe.to_excel(ExpectedJsonFilePath, sheet_name='Sheet1')
    # data = {}
    # data['title'] = title
    # data['sentences'] = ListOfSentences
    # create_json(data,ExpectedJsonFilePath)


get_json('./data/cleaned_data/test.json', 'test.json')    


if __name__ == '__main__':
    pass
    # # with open("sample_data/SearchResultsCorpus.txt") as fp:
    # #     lines_list = fp.readlines()
    # # for line in lines_list:
    # #     t = get_preprocessed_data(line)
    # #     # print(t)
    # #     # break
    # #     append_new_line("sample_data/CleanedCorpus.txt",t)
    
    # with open("sample_data/SearchResultsCorpus.txt",encoding="utf8") as fp:
    #     paragraphs = fp.readlines()
    # for paragraph in paragraphs:
    #     try:
    #         sentences_from_each_paragraph = pysbd_sent_segmenter(paragraph)
    #         correct_sentences = sentence_selection(sentences_from_each_paragraph)
    #         for every_sentence in correct_sentences:
    #             append_new_line("sample_data/CleanedCorpus.txt",every_sentence)
    #     except:
    #         pass


