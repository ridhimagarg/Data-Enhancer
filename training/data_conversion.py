from utils.basic_utils import *
from question_filtering import discard_question
import os
import sys
# print(sys.path)

TRAINING_FOLDER_PATH = f"../data/ridhima_requirements/"
OUTPUT_FILE_PATH = f"../data/annotator_format.json"

def convert_data_to_annotate():

    qa_data = {"version": "1.0", "data": []}

    for filename in os.listdir(TRAINING_FOLDER_PATH):
        #print(filename)
        if filename.endswith('.json'):
            data = read_json(TRAINING_FOLDER_PATH+str(filename))

            if qa_data["data"]:
                if data["company"] in [ companies["title"] for companies in qa_data["data"]]:
                    index = [index for (index, companies) in enumerate(qa_data["data"]) if companies["title"] == data["company"]]
                    for sentences in data["sentence_list"]:
                        qa_data["data"][index[0]]["paragraphs"].append({"qas": [], "context":sentences})
                

                else:                
                    qa_data["data"].append({"title": data["company"]})
                    index = [index for (index, companies) in enumerate(qa_data["data"]) if companies["title"] == data["company"]]
                    qa_data["data"][index[0]]["paragraphs"] = []
                    for sentences in data["sentence_list"]:
                        qa_data["data"][index[0]]["paragraphs"].append({"qas": [], "context":sentences})
        
            else:
                qa_data["data"].append({"title": data["company"]})
                qa_data["data"][0]["paragraphs"] = []
                for sentences in data["sentence_list"]:
                    qa_data["data"][0]["paragraphs"].append({"qas": [], "context":sentences})


    save_json(OUTPUT_FILE_PATH, qa_data)

def main():

    convert_data_to_annotate()

if __name__ == '__main__':
    main()


            
