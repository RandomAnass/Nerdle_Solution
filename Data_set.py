def FindExp(Pattern, Element, Exp):
    #recursively add elements to the expression trying all possible values
    #when all elements are added, compute the result and save it
    #if it is valid
    if (isinstance(Pattern[Element],str)):
        #+ indicates all 4 operators in turn
        if (Pattern[Element]=="+"):
            for Operator in ["+", "-", "*", "/"]:
                FindExp(Pattern, Element+1, Exp+Operator)
        else:
            #= indicates end of expression and need to calculate result
            try:
                Result = eval(Exp)
                #eliminate negative, too big, non-integer, zero, and leading zero results
                if (Result >=0 and Result < 10**Pattern[Element+1] and int(Result) == Result and len(str(int(Result)))==Pattern[Element+1]):
                    OutputFile.write (Exp+"="+format(int(Result),"0"+str(Pattern[Element+1]))+"\n")
            except ZeroDivisionError:
                return
    else:
        #numbers indicate the digits in a numeric field
        for i in range(10**Pattern[Element]):
            NewNum = format(i, "0"+str(Pattern[Element])).lstrip("0")
            if (len(NewNum)==Pattern[Element]):
                    FindExp(Pattern, Element+1, Exp+NewNum)
def nerdle():
    PatternList = [
        #numbers indicate the digits in the field, + indicates all the operators,
        #and = indicates where the result goes with the next number indicating
        #how many digits the result has
        [2,"+",2,"=",2],
        [3,"+",2,"=",1],
        [2,"+",3,"=",1],
        [2,"+",1,"=",3],
        [3,"+",1,"=",2],
        [1,"+",3,"=",2],
        [1,"+",2,"=",3],
        [4,"+",1,"=",1],
        [1,"+",4,"=",1],
        [2,"+",1,"+",1,"=",1],
        [1,"+",2,"+",1,"=",1],
        [1,"+",1,"+",2,"=",1],
        [1,"+",1,"+",1,"=",2]
        ]

    for Pattern in PatternList:
        print ("Starting ", Pattern)
        FindExp(Pattern, 0, "")        



OutputFile = open("expressions.txt", "w")

nerdle()

OutputFile.close()