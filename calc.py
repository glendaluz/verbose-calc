#!/usr/bin/python3

import sys

class OperationNotSupported(Exception):
        pass

def print_words(words_list):
    """Return a string with words separated by space"""
    final_string = ""
    index = 0
    size_array = len(words_list)
    last_word_index = size_array -1 #Index of the last word
    for word in words_list:
        if index == last_word_index:
            final_string = final_string + word #Should not have space
        else:
            final_string = final_string + word + " "
        index = index + 1
    return final_string

def main():
    #words = ["Sugar","nao","come","coco"]
    #print(print_words(words))

    #print(sys.argv[0])
    #print(len(sys.argv))
    #print(str(sys.argv))

    #print(print_words(sys.argv))

    try:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op =="mais":
            print(a+b)
        elif op == "vezes":
            print(a*b)
        elif op == "menos":
            print(a-b)
        elif op == "dividido":
            print(a/b)
        else:
            raise OperationNotSupported
            
    except ZeroDivisionError:
        print("Seu burro nao pode dividir por zero")
    except ValueError:
        print("Invalid number, please enter integers")
    except OperationNotSupported:
        print("Operation not supported! (+ - / *)")



if __name__ == "__main__":
    main()
