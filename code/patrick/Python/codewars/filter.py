def filter_list(lists):
    output = []
    for x in lists:
        if isinstance(x, str) != True:
            try:
                x = str(x)
                val = x.isdigit()
                if val == True:
                    output.append(int(x))
            except:
                pass
        else:
            pass
    return output

print(filter_list([1,2,'aasf','1','123',123]))