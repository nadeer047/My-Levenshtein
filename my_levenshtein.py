def my_levenshtein(param_1, param_2):
    index = 0
    if len(param_1) == len(param_2):
        for fuck in range(len(param_1)):
            if param_1[fuck] != param_2[fuck]:
                index = index + 1
    else: 
          index = index - 1
    return index
