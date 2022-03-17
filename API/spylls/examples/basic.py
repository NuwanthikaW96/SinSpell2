import pathlib
path = pathlib.Path(__file__).parent  / 'si_LK'

from spylls.hunspell import Dictionary

dictionary = Dictionary.from_files(str(path))

def detector_fun(word):
    print(word)
    file_content = word
   
    # # characters = [".",",","%","!","@","&"]
    # test_string = ''.join(i for i in file_content)


    word_list1 = file_content.split(" ")
    word_list=[]
    for i in word_list1:
        if i[-1]==".":
            word_list.append(i[:-1])
            word_list.append(i[-1])
        else:
            word_list.append(i)
    print(word_list)
    incorrect_word_list = []
    correct_word_list = []
    

    for word in word_list:
        if dictionary.lookup(word):
            print("correct")
            correct_word_list.append(word)
        else: 
            # print("Incorrect")   
            # marked = "\u0332".join(word+ " ")
            # result = result.replace(word,marked)
            incorrect_word_list.append(word)
            # print(incorrect_word_list)
    
    return incorrect_word_list,correct_word_list,word_list
   