def main(list1,list2):
    list=[]
    i=0
    j=0
    if list1==[]:
        list=list2
    elif list2==[]:
        list=list1
    else:
        try:
            while i <len(list1):
                while j<len(list2):
                    if list1[i]<list2[j]:
                        list.append(list1[i])
                        i+=1
                    elif list1[i]>list2[j]:
                        list.append(list2[j])
                        j+=1
                    else:
                        list.append(list2[j])
                        list.append(list1[i])
                        i+=1
                        j+=1
        except IndexError:
            if i==len(list1):
                for x in range(j,len(list2)):
                    list.append(list2[x])
            else:
                for x in range(i,len(list1)):
                    list.append(list1[x])
    return list



list1 = [0]
list2 = [1, 3, 4]
print(main(list1,list2))