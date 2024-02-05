#!/usr/bin/python3
def multiple_returns(sentence):
    ten_leng = len(sentence)
    if ten_leng == 0:
        new_tuple = ten_leng, None
        return new_tuple
    else:
        new_tuple = ten_leng, sentence[0]
        return new_tuple
