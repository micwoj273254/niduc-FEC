
def binaryToBinaryList(string :str,howLong = 8)->[]:
    list = []
    binary = ""
    i = 0
    for char in string:
        binary += char
        # print(binary)          #debug
        i += 1
        if i == howLong :
            list.append(binary)
            i = 0
            binary = ""

    if i != 0 :
        list.append(binary[::-1].zfill(howLong)[::-1])
    return list

def binaryListToBinary(list :[],stripTrailing0 = 0)->str:
    out = ""
    isOn = 1
    for element in list:
        out += element
        # print(out)          #debug

    if stripTrailing0 == 1:
        out = out.rstrip("0")
        #print("out :",out)
        h = len(out)%8
        while isOn == 1:
            if h != 0:
                out += "0"
                h += 1
                h = len(out) % 8
            else:
                isOn = 0
    return out

def d2StrListTod2intList(stringList :[])->[]:
    out = []
    for element in stringList:
        list = []
        for i in range(len(element)):
            list.append(int(element[i]))
            # print(list)
        out.append(list)
        # print(out)
    return out

def intListToStrList(intList :[])->[]:
    out = []
    for i in intList:
        out.append(str(i))
    return out

if __name__ == "__main__":
    print("binary main")