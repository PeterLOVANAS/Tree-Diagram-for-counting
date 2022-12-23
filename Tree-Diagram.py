import itertools
import math
import numpy as np
#for i in itertools.permutations("ABCD"):
#    print(i)

class Tree_Diagram:
    def __init__(self , text):
        self.text = text


    def Exponential(self , k = int):
        anslst = []
        fortup = []
        text = self.text

        lsta =  list(text)
        lst =  list(map(list , text)) # Pick each individual alphabet in text and make it to list like ["a"] and later they put the output of the map() into another list


        #lsta = ["a" , "b", "c", "d"]
        #lst = [["a"] , ["b"] , ["c"] , ["d"]]
        storage = lst.copy()
        stor2 = []
        #for i in lsta:
        for n in range(k-1):
            #length = len(storage)
            for g in storage:
                for h in lsta:
                    g.append(h)
                    stor2.append(g.copy())
                    g.pop(-1)
            storage = stor2.copy()
            stor2.clear()

        for l in storage.copy():
            anslst.append(tuple(l))

        return anslst
            #storage.clear()

    def Permutations(self , k = int):
        anslst = []

        text = self.text

        if "," in text:
            lsta = text.split(",")
            lsta2 = text.split(",")
            lst = []
            for i in text.split(","):
                lst.append([i])

        elif "," not in text:
            lsta =  list(text)
            lsta2 = list(text)
            lst = list(map(list , text)) # Pick each individual alphabet in text and make it to list like ["a"] and later they put the output of the map() into another list

        storage = lst.copy()
        stor2 = []
        #for i in lsta:
        if k <= len(lsta2):
            pass
        elif k > len(lsta2):
            return "k should smaller or equal to length of string"

        for n in range(k-1):

            for g in storage:
                if "," in text:
                    lsta2 = text.split(",")
                elif "," not in text:
                    lsta2 = list(text)

                for f in g:
                    lsta.remove(f)
                for h in lsta:
                    g.append(h)
                    stor2.append(g.copy())
                    g.pop(-1)
                lsta = lsta2
            storage = stor2.copy()
            stor2.clear()

        for l in storage.copy():
            anslst.append(tuple(l))

        return anslst

    def Combination(self , k = int):
        ansset = set()
        tuplst = self.Permutations(k)
        ans = list(map(frozenset , tuplst))
        for i in ans:
            ansset.add(i)
        ans1 = list(map(tuple , ansset))
        return ans1

    def Rearrange_Count(self , slst = list):
        text = self.text
        lsttex = text.split(",")
        s1 = set()
        ck1 = self.Permutations(k = len(lsttex))
        if all(isinstance(x , tuple) for x in slst) == True :
            pass
        elif all(isinstance(x , tuple) for x in slst) == False:
            return "Every element in list should be tuples"

        for x2 in slst:
            for x3 in x2:
                if x3 in lsttex:
                    pass
                elif x3 not in lsttex:
                    return "Every element should be in the text"

        for j in slst:
            for j1 in j:
                lsttex.remove(j1)

        for i1 in ck1:
            ans2 = []
            for l in slst:
                lst = []
                for k in l:
                    a = i1.index(k)
                    lst.append(a)
                f = frozenset(lst)
                ans2.append(f.copy())
                lst.clear()
            for x in lsttex:
                ans2.append(i1.index(x))

            ans3 = tuple(ans2)

            s1.add(ans3)

        return len(s1)









    def P(self , n = int ,k = int):
        if k <= n:
            return math.factorial(n) / math.factorial(n-k)
        else:
            return None

    def C(self , n = int , k = int):
        if k <= n:
            return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
        else:
            return None

    def show(self , showlst = list):
        for i in showlst:
            print(i)

    def CountShow(self , ele = str , num = int,  lst = list):
        ans = []
        if all(isinstance(x , tuple) for x in lst) == True:
            pass
        elif all(isinstance(x , tuple) for x in lst) == False:
            return None
        for i in lst:
            if i.count(ele) == num:
                ans.append(i)
            elif i.count(ele) != num:
                pass
        return ans

    def Cyclic_Permutation(self , start = str):
        anslst = []
        Permulin = self.Permutations(k = len(self.text))
        if start in self.text:
            pass
        elif start not in self.text:
            return "Start value must be in the permutation"
        for k in Permulin:
            Mapdict = dict(zip(Permulin[0] , k))
            n = start
            lst = []
            lst.append(n)
            #Check = list(Permulin[0])
            while True:
                mapval = Mapdict[n]
                if mapval in lst:
                    break
                elif mapval not in lst:
                    lst.append(mapval)
                n = mapval
            if len(lst) == len(Permulin[0]):
                anslst.append(tuple(lst))
            elif len(lst) != len(Permulin[0]):
                pass
            lst.clear()

        return anslst

    def Repetition_text(self):
        lst = []
        new_lst = []
        if "," in self.text:

            for i in self.text.split(","):
                lst.append(i)

        elif "," not in self.text:
            raise Exception("You need to put comma between each object")

        for ele in set(lst):
            counting = lst.count(ele)
            for i in range(1, counting + 1):
                new_ele = ele + "_" + f"{i}"
                new_lst.append(new_ele)

        ans_str = ""
        for items in new_lst:
            if new_lst.index(items) != len(new_lst) -1:
                ans_str = ans_str + items + ","
            elif new_lst.index(items) == len(new_lst) -1:
                ans_str = ans_str + items


        return ans_str

    def Permutations_Repetition(self , k = int):
        # rep = ["Maximus" , "Minima", "A"]
        # case => A_1

        copy_text = self.text
        self.text = self.Repetition_text()

        permulist = self.Permutations(k)
        repilst = []
        for case in permulist:
            caselst = []

            for i in case:

                index = i.index("_") # Don't use _ in character for self.text (User's input)
                new_ele = i[:index]
                caselst.append(new_ele)
            repilst.append(tuple(caselst))

        repiset = set(repilst)
        self.text = copy_text

        return list(repiset)


