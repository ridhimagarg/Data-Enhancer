# Data Enhancer using Q&A approach

The following diagram shows the full approach -:

<img src = "./data/downloads/Data Enhancer Q&A pipeline.jpg">

### 1. Scraped Data

```
{
    "id": 72,
    "sId": 15,
    "key": "b'7A01983E-487D-E311-9665-005056A838B3'",
    "string": "Goldman Sachs",
    "url": "b'https://www.charitynavigator.org/index.cfm?bay=search.profile&ein=010797982'",
    "text": "Goldman Sachs businesses in India serve leading corporate and institutional clients across the country. Following a ten-year joint venture, Goldman Sachs established an onshore business presence in Mumbai in 2006. The Bengaluru office opened in 2004.At Goldman Sachs, we turn ideas into reality for our clients and communities in 30 countries. Our people come from a variety of academic and professional backgrounds including finance, engineering, science, technology and the humanities to make things possible. Goldman Sachs have 20,000 developers all over the world. Goldman Sachs has around 38,300 employees working. The Goldman Sachs Group, Inc., is an American multinational investment bank and financial services company headquartered in New York City. It offers services in investment management, securities, asset management, prime brokerage, and securities underwriting.The bank is one of the largest investment banking enterprises in the world, and is a primary dealer in the United States Treasury security market and more generally, a prominent market maker. The group also owns Goldman Sachs Bank USA, a direct bank. Goldman Sachs was founded in 1869 and is headquartered at 200 West Street in Lower Manhattan with additional offices in other international financial centers. Goldman Sachs was founded in New York in 1869 by Marcus Goldman. In 1882, Goldman's son-in-law Samuel Sachs joined the firm. It has total revenue of US $36.546 billion and capitalization of US $8.466 billion. Richard Gnodde is a COO of company."
}
```
<br><br>

### 2. Processed Data

| title         | paragraphs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Goldman Sachs | ['Goldman Sachs businesses in India serve leading corporate and institutional clients across the country .', 'Following a ten-year joint venture , Goldman Sachs established an onshore business presence in Mumbai in 2006 .', 'The Bengaluru office opened in 2004.At Goldman Sachs , we turn ideas into reality for our clients and communities in 30 countries .', 'Our people come from a variety of academic and professional backgrounds including finance , engineering , science , technology and the humanities to make things possible .', 'Goldman Sachs have 20,000 developers all over the world .', 'Goldman Sachs has around 38,300 employees working .', 'The Goldman Sachs Group , Inc. , is an American multinational investment bank and financial services company headquartered in New York City .', 'It offers services in investment management , securities , asset management , prime brokerage , and securities underwriting.The bank is one of the largest investment banking enterprises in the world , and is a primary dealer in the United States Treasury security market and more generally , a prominent market maker .', 'The group also owns Goldman Sachs Bank USA , a direct bank .', 'Goldman Sachs was founded in 1869 and is headquartered at 200 West Street in Lower Manhattan with additional offices in other international financial centers .', 'Goldman Sachs was founded in New York in 1869 by Marcus Goldman .', "In 1882 , Goldman 's son-in-law Samuel Sachs joined the firm .", 'It has total revenue of US $ 36.546 billion and capitalization of US $ 8.466 billion .', 'Richard Gnodde is a COO of company .'] |

<br><br>

### 3. Questions File(General Questions)

```
{

    "name": ["What is the name of organization_name?","With what name organization_name is identified?","How organization_name is recognised?"],

    "domain": ["What is the domain of organization_name?", "In which domain does organization_name works?", 
               "What does organization_name recommends?","what is the area organization_name deals in?",
               "What is the business type of organization_name?","What industry organization_name comes into?",
               "What is the industry type of organization_name?","What industry organization_name deals in?",
               "Which industry does organization_name serve?","Which sector organization_name deals in?",
               "What is organization_name known for?"],

    "founded": ["When was organization_name founded?", "When was organization_name started?", 
                "When organization_name started its journey", "From how long organization_name serving?",
                "What is the foundation year of organization_name","Since when organization_name is serving?",
                "When did organization_name found a site for its headquaters?","What was the birth year of organization_name?",
                "When did organization_name open its first office?","What is organization_name's origin year?"],

    "employee": ["How many employees are there in organization_name?","What is the employee strength of organization_name?",
                 "How many professionals are working in organization_name?","How many employees does organization_name include?",
                 "What is the work force employed by organization_name?","How many employees work for organization_name?"],

    "developer": ["How many developers are there in organization_name?"],

    "state": ["In how many states does organization_name deal?", "What are the number of states in which organization_name spread?",
              "In what locations organization_name operates?","Where organization_name is located?","In how many locations organization_name has its offices?",
              "Where has organization_name opened its ofiices?","What are the different locations of organization_name?"],

    "countries": ["In how many countries does organization_name deal?", "What are the number of countries in which organization_name spread?",
                  "In what locations organization_name operates?","Where organization_name is located?","Where has organization_name opened its ofiices?",
                  "In how many locations organization_name has its offices?","What are the different locations of organization_name?"],


    "reviews": ["How many reviews does organization_name have?"],

    "fein": ["What is fein number of organization_name"],

    "address": ["What is the address of organization_name?", "Where is organization_name located?","Where is organization_name headquartered?"],

    "sic": ["What is sic number of organization_name?"],

    "revenue": ["What is the revenue of organization_name?", "How much is the revenue of organization_name?"],

    "capitalization": ["What is the capitalization of organization_name?", "How much is the capitalization of organization_name?"],

    "clients": ["How many clients does organization_name have?"],

    "margin": ["How much is the margin of organization_name have?"],

    "liability": ["What are the liabilities of organization_name?"],

    "ceo": ["Who is the CEO of organization_name?", "Who is the Chief Executive Officer of organization_name?"],

    "cfo": ["Who is the CFO of organization_name?", "Who is the Chief Financial Officer of organization_name?",
            "Who handles Financial aspects of organization_name?"],

    "cmo": ["Who is the CMO of organization_name?", "Who is the Chief Marketing Officer of organization_name?"],

    "founder": ["Who is the founder of organization_name?", "Who is the owner of organization_name?", 
                "Who owned organization_name?","Who are the founding fathers of organization_name?",
                "Who initiated organization_name?","Who opened organization_name?","Who started organization_name?"],

    "co-founder": ["Who is the co-founder of organization_name?"],

    "products-services": ["What are the services provided by organization_name?", "What does organization_name caters to clients?", 
                          "What is the aim of organization_name?","What are products of organization_name?"]
}
```

<br><br>
### 4. Questions according to business name

```
{
    "name": [
        "What is the name of Goldman Sachs?",
        "With what name Goldman Sachs is identified?",
        "How Goldman Sachs is recognised?"
    ],
    "domain": [
        "What is the domain of Goldman Sachs?",
        "What is orgaization_name?",
        "In which domain does Goldman Sachs works?",
        "What does Goldman Sachs recommends?",
        "what is the area Goldman Sachs deals in?",
        "What is the business type of Goldman Sachs?",
        "What industry Goldman Sachs comes into?",
        "What is the industry type of Goldman Sachs?",
        "What industry Goldman Sachs deals in?",
        "Which industry does Goldman Sachs serve?",
        "Which sector Goldman Sachs deals in?",
        "What is Goldman Sachs known for?"
    ],
    "founded": [
        "When was Goldman Sachs founded?",
        "When was Goldman Sachs started?",
        "When was Goldman Sachs office opened?",
        "When Goldman Sachs started its journey",
        "From how long Goldman Sachs serving?",
        "What is the foundation year of Goldman Sachs",
        "Since when Goldman Sachs is serving?",
        "When did Goldman Sachs found a site for its headquaters?",
        "What was the birth year of Goldman Sachs?",
        "When did Goldman Sachs open its first office?",
        "What is Goldman Sachs's origin year?",
        "Founded in?",
        "When was Goldman Sachs established?"
    ],
    "employee": [
        "How many employees are there in Goldman Sachs?",
        "What is the employee strength of Goldman Sachs?",
        "How many professionals are working in Goldman Sachs?",
        "How many employees does Goldman Sachs include?",
        "What is the work force employed by Goldman Sachs?",
        "How many employees work for Goldman Sachs?"
    ],
    "developer": [
        "How many developers are there in Goldman Sachs?"
    ],
    "state": [
        "In how many states does Goldman Sachs deal?",
        "What are the number of states in which Goldman Sachs spread?",
        "In what locations Goldman Sachs operates?",
        "Where Goldman Sachs is located?",
        "In how many locations Goldman Sachs has its offices?",
        "Where has Goldman Sachs opened its ofiices?",
        "What are the different locations of Goldman Sachs?"
    ],
    "countries": [
        "In how many countries does Goldman Sachs deal?",
        "What are the number of countries in which Goldman Sachs spread?",
        "In what locations Goldman Sachs operates?",
        "Where Goldman Sachs is located?",
        "Where has Goldman Sachs opened its ofiices?",
        "In how many locations Goldman Sachs has its offices?",
        "What are the different locations of Goldman Sachs?"
    ],
    "reviews": [
        "How many reviews does Goldman Sachs have?"
    ],
    "address": [
        "What is the address of Goldman Sachs?",
        "Where is Goldman Sachs located?",
        "Where is Goldman Sachs headquartered?"
    ],
    "revenue": [
        "What is the revenue of Goldman Sachs?",
        "How much is the revenue of Goldman Sachs?"
    ],
    "capitalization": [
        "What is the capitalization of Goldman Sachs?",
        "How much is the capitalization of Goldman Sachs?"
    ],
    "clients": [
        "How many clients does Goldman Sachs have?",
        "In how many countries does organization_have has its client?"
    ],
    "margin": [
        "How much is the margin of Goldman Sachs have?"
    ],
    "liability": [
        "What are the liabilities of Goldman Sachs?"
    ],
    "ceo": [
        "Who is the CEO of Goldman Sachs?",
        "Who is the Chief Executive Officer of Goldman Sachs?"
    ],
    "cfo": [
        "Who is the CFO of Goldman Sachs?",
        "Who is the Chief Financial Officer of Goldman Sachs?",
        "Who handles Financial aspects of Goldman Sachs?"
    ],
    "cmo": [
        "Who is the CMO of Goldman Sachs?",
        "Who is the Chief Marketing Officer of Goldman Sachs?"
    ],
    "coo": [
        "Who is the COO of Goldman Sachs?"
    ],
    "founder": [
        "Who is the founder of Goldman Sachs?",
        "Who is the owner of Goldman Sachs?",
        "Who owned Goldman Sachs?",
        "Who are the founding fathers of Goldman Sachs?",
        "Who initiated Goldman Sachs?",
        "Who opened Goldman Sachs?",
        "Who started Goldman Sachs?"
    ],
    "co-founder": [
        "Who is the co-founder of Goldman Sachs?"
    ],
    "products-services": [
        "What are the services provided by Goldman Sachs?",
        "What does Goldman Sachs caters to clients?",
        "What is the aim of Goldman Sachs?",
        "What are products of Goldman Sachs?",
        "What does Goldman Sachs owns?"
    ]
}
```

<br><br> 

### 5. Final Output by Q&A model

```
{
    "name": [
        "Goldman Sachs"
    ],
    "domain": [
        "investment management",
        "investment bank and financial services",
        "multinational",
        "United States Treasury security market",
        "onshore",
        "investment management , securities , asset management , prime brokerage , and securities underwriting",
        "we turn ideas into reality",
        "investment management , securities"
    ],
    "founded": [
        "1869",
        "2004",
        "ten-year"
    ],
    "employee": [
        "38,300",
        "developers",
        "we turn ideas into reality for our clients"
    ],
    "developer": [
        "20,000"
    ],
    "state": [
        "international financial centers",
        "38,300",
        "200 West Street",
        "30 countries",
        "200 West Street in Lower Manhattan"
    ],
    "countries": [
        "international financial centers",
        "200 West Street",
        "38,300",
        "200 West Street in Lower Manhattan",
        "30",
        "30 countries"
    ],
    "reviews": [
        "20,000"
    ],
    "address": [
        "200 West Street",
        "200 West Street in Lower Manhattan"
    ],
    "revenue": [
        "$ 36.546 billion"
    ],
    "capitalization": [
        "$ 8.466 billion",
        "US $ 8.466 billion"
    ],
    "clients": [
        "38,300"
    ],
    "margin": [
        "It has total revenue of US $ 36.546 billion"
    ],
    "liability": [
        "capitalization of US $ 8.466 billion"
    ],
    "ceo": [
        "Richard Gnodde"
    ],
    "cfo": [
        "Richard Gnodde"
    ],
    "cmo": [
        "Richard Gnodde"
    ],
    "coo": [
        "Richard Gnodde"
    ],
    "founder": [
        "Samuel Sachs",
        "Richard Gnodde",
        "Marcus Goldman"
    ],
    "co-founder": [
        "Richard Gnodde"
    ],
    "products-services": [
        "turn ideas into reality",
        "investment management , securities , asset management , prime brokerage , and securities underwriting"
    ]
}
```


