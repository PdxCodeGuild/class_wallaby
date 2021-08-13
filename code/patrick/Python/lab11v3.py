#Bubble sort 
lst_1 = [5,4,3,2,1]
def bubble_sort(lst):
    sorted = True
    while sorted:
        sorted = False
        for i in range(len(lst_1)-1):
            if lst_1[i] > lst_1[i+1]:
                lst_1[i], lst_1[i+1] = lst_1[i+1], lst_1[i] 
                sorted = True
    return lst_1
  
print(bubble_sort(lst_1))
           
            

        