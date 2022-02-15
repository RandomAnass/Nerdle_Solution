
from multiprocessing import Pool, Manager, cpu_count
from functools import partial
import re
import pickle


def process_value(files, i_1):
    print(i_1)
    file_i_1 = open(files[i_1], "a")
    for i_2 in list("*")+['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print(i_1,i_2)
        for i_3 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '==']:
            for i_4 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '==']:
                for i_5 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '==']:
                    for i_6 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '==']:
                        for i_7 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '==']:
                            for i_8 in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                try:
                                    value = i_1+i_2+i_3+i_4+i_5+i_6+i_7+i_8
                                    if '//' in value:
                                        continue
                                    valuev = re.sub(r'\b0+(?!\b)', '', value)
                                    evaluation = eval(valuev)
                                    if type(evaluation) == type(True) and evaluation:
                                        file_i_1.write(value+",")
                                except:
                                    continue

#double equal is not accepted 

if __name__ == '__main__':
    with Manager() as manager:
        files = manager.dict()
        # The iterable is the i_1 list:
        i_1_list = [ '2', '3', '4', '5', '6', '7', '8', '9'] #'1' 9 reached but not finished
        for i__1 in i_1_list :
            files[i__1]= i__1+".txt"
        POOL_SIZE = min(cpu_count(), len(i_1_list))
        pool = Pool(POOL_SIZE)
        pool.map(partial(process_value, files), i_1_list)
        for i_1 in i_1_list:
            file_i_1 = open(files[i_1], "a")
            file_i_1.close()
        pool.close()
        pool.join()
        print("remove double ==,'1' 9 reached but not finished")

#