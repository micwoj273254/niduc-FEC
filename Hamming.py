import binary
import komm

def Hamming(message: str,coding_bits:int):
    code = komm.HammingCode(coding_bits)
    encoder = komm.BlockEncoder(code)
    list_length = pow(2,coding_bits)-coding_bits-1
    list = []
    templist = []
    output = []
    print("przed strToBinary")
    bin = binary.strToBinary(message)
    print("po strToBinary")
    list.append(binary.binaryToBinaryList(bin,list_length))
    print("po włączeniu do listy")
    for element in list:
        templist.append(binary.binaryToBinaryList(element,1))
        print(templist)
    list = templist
    templist.clear()
    print("po liscie 2d")
    for element in list:
        templist.append(binary.strListTointList(element))
    list = templist
    templist.clear()
    print(list)
    for element in list:
        encodedarray = encoder(element)
        print(encodedarray)
        output.append(encodedarray)
        print(output)
    return ''.join(output)















if __name__ == "__main__":
    print("hi")
    print(Hamming("hi",4))