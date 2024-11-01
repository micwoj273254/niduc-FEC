import komm
def strToBinary(string :str)->str:
    list = []

    for char in string:
        list.append(bin(ord(char))[2:].zfill(8))

    return ''.join(list)


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

def binaryToListWithPrefix0b(string :str)->[]:
    list  = binaryToBinaryList(string)
    out = []
    i = 0
    for element in list:
        out.append("0b"+element)
    return out


def binaryToStr(string :str)->str:
    list = binaryToBinaryList(string)
    out = []
    for element in list:
        out.append(chr(sum(int(c) * (2 ** i) for i, c in enumerate(element[::-1]))))
    return ''.join(out)

def d2StrListTod2IntList(stringList :[])->[]:
    out = []
    for element in stringList:
        list = []
        for i in range(len(element)):
            list.append(int(element[i]))
            #print(list)
        out.append(list)
        #print(out)
    return out

def d2IntListTod2StrList(stringList :[])->[]:
    out = []
    for element in stringList:
        list = []
        for i in range(len(element)):
            list.append(str(element[i]))
            #print(list)
        out.append(list)
        #print(out)
    return out

if __name__ == "__main__":
    hammingCode4 = komm.HammingCode(4)
    hamming4Encoder = komm.BlockEncoder(hammingCode4)
    bsc = komm.BinarySymmetricChannel(0.01)

    word = input("input :")
    binary = strToBinary(word)

    print("after str_to_binary :",binary)

    binlist11 = binaryToBinaryList(binary,11)

    print("after binary_to_binary_list :", binlist11)
    print("after binary_to_list_with_prefix_0b :", binaryToListWithPrefix0b(binary))

    d2strBinList = []

    for element in binlist11:
        d2strBinList.append(binaryToBinaryList(element, 1))

    print("List with strList length 11 in it :",d2strBinList)

    d2BinList = d2StrListTod2IntList(d2strBinList)

    print("List with intList length 11 in it :",d2BinList)

    hammEncList = []

    for element in d2BinList:
        hammEncList.append(hamming4Encoder(element))


    print("encoded by Hamming code", hammEncList)

    hammEncListBSC = []

    for element in hammEncList:
        hammEncListBSC.append(bsc(element))

    print("bit flipped by BSC channel", hammEncListBSC)

    d2decodedHammIntList = []

    hamm4decoder = komm.BlockDecoder(hammingCode4)

    for elements in hammEncListBSC:
        d2decodedHammIntList.append(hamm4decoder(elements))

    print("Before encoding :", d2strBinList)
    print("List decoded", d2decodedHammIntList)

    d2decodedHammStrList = d2IntListTod2StrList(d2decodedHammIntList)

    print("list back to str :", d2decodedHammStrList)

    decodedHammStrList = []
    for element in d2decodedHammStrList:
        decodedHammStrList.append(binaryListToBinary(element))

    print("list back to 1d :", decodedHammStrList)

    decodedHammStr = binaryListToBinary(decodedHammStrList,1)

    print("list to str :", decodedHammStr)
    print("bin str to str :", binaryToStr(decodedHammStr))