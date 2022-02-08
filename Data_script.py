from multiprocessing import Pool, Manager, cpu_count
from functools import partial
import re
import pickle

## This script was made possible , with the help of user:2823719 Booboo on stackoverflow
# https://stackoverflow.com/questions/71017273/multiprocessing-of-for-nested-loops/71021661#71021661


def process_value(data_set_N, i_1):
    print(i_1)
    for i_2 in list(range(10))+list("+-*/")+["=="]:
        for i_3 in list(range(10))+list("+-*/")+["=="]:
            for i_4 in list(range(10))+list("+-*/")+["=="]:
                for i_5 in list(range(10))+list("+-*/")+["=="]:
                    for i_6 in list(range(10))+list("+-*/")+["=="]:
                        for i_7 in list(range(10))+list("+-*/")+["=="]:
                            for i_8 in list(range(10)):
                                try:
                                    value = str(i_1)+str(i_2)+str(i_3)+str(i_4)+str(i_5)+str(i_6)+str(i_7)+str(i_8)
                                    if '//' in value:
                                        continue
                                    valuev = re.sub(r'\b0+(?!\b)', '', value)
                                    evaluation = eval(valuev)
                                    if type(evaluation) == type(True) and evaluation:
                                        data_set_N.append(value)
                                except:
                                    continue

if __name__ == '__main__':
    with Manager() as manager:
        data_set_N = manager.list()
        # The iterable is the i_1 list:
        i_1_list = list(range(10))+list("+-")
        POOL_SIZE = min(cpu_count(), len(i_1_list))
        pool = Pool(POOL_SIZE)
        pool.map(partial(process_value, data_set_N), i_1_list)
        pool.close()
        pool.join()
        data_set_N=list(data_set_N)
        #print(len(data_set_N))
        data_set_N2 = [equa.replace("==", "=") for equa in data_set_N]
        filename_N = 'Nerdle_data'
        outfile_N = open(filename_N,'wb')
        pickle.dump(data_set_N2,outfile_N)
        outfile_N.close()