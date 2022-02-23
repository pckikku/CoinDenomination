
count=0

def make_change(denomination_list, amount):
    for i in range(len(denomination_list),0,-1):
        if(denomination_list[i-1]<=amount):
            global count
            count=count+1
            amount=amount-denomination_list[i-1]
            return make_change(denomination_list,amount)
    if (count==0):
        return -1
    else:
        return count


amount= 1
denomination_list = [2,15,10]
denomination_list.sort()
make_change(denomination_list, amount)
