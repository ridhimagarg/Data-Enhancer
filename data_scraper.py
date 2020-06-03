from bs4 import BeautifulSoup
import requests
import json
from importlib import resources
import re
from preprocess_data import remove_html_tags,remove_image_tags,refine_text
import os
from utils.basic_utils import *
# resources.path('webscrapers,')

INPUT_PATH = 'test/data/testinput/v2/'
OUTPUT_PATH = './data/raw/'

def get_html(url: str):
    try:
        response = requests.get(url)
        html = response.content
    except:
        html = None
    return html

def get_subpages_urls(main_url,html):
    soup = BeautifulSoup(html,'html.parser')
    body = soup.body
    subpages_urls = []
    href_content = [url_tag.get('href') for url_tag in body.find_all('a')]    
    regex = r'https?://[a-zA-Z0-9\./\-]+'
    if href_content:
        try:
            for url in href_content:
                if url != None:
                    complete_url_format = re.findall(regex,str(url))
                    if complete_url_format:
                        pass
                    else:
                        if url[0] == '/':
                            if main_url[-1] == '/':
                                url = str(main_url)[0:-1]+str(url)
                            else:
                                url = str(main_url)+str(url)
                        else:
                            if str(main_url)[-1] == '/':
                                url = str(main_url)+str(url)
                            else:
                                url = str(main_url)+'/'+str(url)
                    subpages_urls.append(url)
        except:
            pass
    return subpages_urls

def get_webpages(company_name,main_url,num_subpages):
    html = get_html(str(main_url))
    all_pages_content = {'company_name':company_name}
    if html != None:
        clean_main_page = refine_text(remove_image_tags(remove_html_tags(str(html))))
        all_pages_content['main_page'] = clean_main_page
        subpages_urls = get_subpages_urls(main_url,html)[0:num_subpages]
        for subpage_num,each_subpage_url in enumerate(subpages_urls,start = 1):
            subpage_html = get_html(each_subpage_url)
            if subpage_html != None:
                clean_subpage = refine_text(remove_image_tags(remove_html_tags(str(subpage_html))))
                all_pages_content['subpage'+str(subpage_num)] = clean_subpage
            else:
                all_pages_content['subpage'+str(subpage_num)]
    return all_pages_content

def get_all_pages_data(num_subpages:int,filename: str, request_num=None,company_name = None,FEIN_num = None,main_url = None):
    
    # if company_name !=  None:
    #     # call function corresponding to "name" parameter
    #     pass

    if FEIN_num != None:
        # call function corresponding to "FEIN Number"
        pass

    if main_url != None:
        all_pages = get_webpages(company_name,main_url,num_subpages)
    
    # return all_pages

    save_json(os.path.join(OUTPUT_PATH, filename), all_pages)

# main(3, 'www.kmgus.com')
        








if __name__ == '__main__':
    pass
############ read url and write html ######
    # with open(INPUT_PATH+'sample_urls.json') as fp:
    #     dict_ = json.load(fp)
    # url = dict_.get('goldman sachs')
    # html = get_html(url)
    # with open(INPUT_PATH+'goldman_sachs.txt','w') as fp:
    #     fp.write(html.decode('utf8'))
###########################################
    # company_link = "https://www.goldmansachs.com/"
    # with open(INPUT_PATH+'goldman_sachs.txt') as fp:
    #     html = fp.read()
    # other_pages_url = get_subpages(company_link,html)
    # print(len(other_pages_url))
    # for url in other_pages_url:
    #     print(url)
    # response = requests.get("https://www.linkedin.com/company/goldman-sachs/")
    # print(response.status_code)
    # all_pages = main(company_name='goldman sachs',num_subpages=3,main_url='https://www.goldmansachs.com/' )
    # print(json.dumps(all_pages,indent=4))
    