# NODE => N_of_data_entry; 500000
NODE = int(round(5))
N_unit_test = 3
N_start = int(round(0))   #  24525860/2, 24520000
N = N_start + N_unit_test

def index_list(list1,sorted_list):
    #print len(list1), len(sorted_list)
    index = []
    for i in range(len(sorted_list)) :
        ind = list1.index(sorted_list[i])
        index.append(ind)
    return index

def count_frequency( list1, item1 ) :
    s = 0
    for i in range(len(list1)) :
        if item1 == list1[i] :
            s += 1
    return s

def pharmacy_counting():
    data_c_dn_fn_ln = []
    cost_data = []
    idx = []
    data_input = open('./input/itcont.txt','r')
    for i in range(NODE) :  # 24525860
        line = data_input.readline()
        lins_sp = line.split(',')
        if ( len(lins_sp[4]) == 2 ) :
            data_c_dn_fn_ln.append(line)
            cost_data.append(lins_sp[4])
        
    data_input.close()
    print data_c_dn_fn_ln[0:1] 
    print cost_data[0:1]

    
    
pharmacy_counting()
    
