import json, ast

def json_union(*argv):
    
    final_dictionary = mergeDict(ast.literal_eval(argv[0]), ast.literal_eval(argv[1]))
    
    for i in range(2, len(argv)):
        final_dictionary = mergeDict(final_dictionary, ast.literal_eval(argv[i]))
    
    print(final_dictionary)
    

        
def mergeDict(dict1, dict2):
    
    ''' Merge dictionaries and keep values of common keys in list'''
    dict3 = {}
    print(dict1)
    for key, value in dict1.items():
        if key in dict1 and key in dict2:
            dict3[key] = [values for values in value]
            dict3[key].extend([values for values in dict2[key]])
        else:
            if key in dict1:
                dict3[key] = [values for values in dict1[key]]
            else:
                dict3[key] = [values for values in dict2[key]] 
    for key, value in dict3.items():
        dict3[key] = list(set(value))
    
    return dict3







if __name__ == "__main__":
    
    json_union('{"domain": ["NASDAQ"], "founded": [   "July 14 , 2006"], "employee": [ "228,000"], "state": ["46"],"countries": ["46"]}', '{"domain": [    "NASDAQ"], "founded": ["July 14 , 2006"],"employee": ["228,000"],"state": [    "46"], "countries": ["47"]}', '{"domain": [    "NASDAQ"], "founded": ["July 14 , 2006"],"employee": ["228"],"state": ["44","46"], "countries": ["47"]}')



























##---------------------------- Further Ref --------------------------##
    # print(list(dict1.items()))        
    # context = dict(list(dict1.items()) + list(dict2.items()))
    # print(context)
    # print(**dict1)
    
    # dict3 = collections.defaultdict(dict)
    # print(dict1.items())
    # print(dict2)

    # for key, value in itertools.chain(dict1.items(), dict2.items()):
    #     dict3[key].update(value)
    # dict3 = {n:{*dict1[n],*dict2[n]} for n in dict1}
    # for key, value in dict3.items():
    #     if key in dict1 and key in dict2:
    #         dict3[key] = [value , dict1[key]]
            
    # return dict(dict3)

# Merge dictionaries and add values of common keys in a list
# dict3 = mergeDict(dict1, dict2)
# print('Dictionary 3 :')
# print(dict3)