''''''
'''
Service   :
---------------
     1. Receive the validated data from Controller
     2. Implement business logic as per give requirement
        If required interact with database for more data (dao layer call)
     4. Call dao layer(Pass the data) for data persistence
     5. Get response from DAO and send it to controller

'''
from _22_2_DB_String._1_CREATE_strs._3_dao import save_to_db

# Business logic
def get_length(str_val):
    print("-- SERVICE LAYER :: ----")
    data = str_val.split(",")
    c_data = data[0:-1]
    user_id = data[-1]
    print("--SERVICE Layer :: ", c_data, user_id)
    words = {}
    for word in c_data:
        le = 0
        for char in word:
            le += 1
        word = word.upper()
        words[word] = le
    print("--SERVICE Layer :: Words length : ", words)
    f_words = list(words.keys())
    f_words.sort()
    word_len = len(words.keys())
    print("--SERVICE Layer :: Final data : ", user_id, f_words, word_len)
    res = save_to_db(user_id, f_words, word_len)
    if res:
        return user_id, words
    else:
        return "Something happened!!"
