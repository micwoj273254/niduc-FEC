import binary
import komm
from BSCchannel import bscchannel


# Hamming returns list with encoded hamming_code arrays
def Hamming(message: str,coding_bits:int):
    code = komm.HammingCode(coding_bits)
    encoder = komm.BlockEncoder(code)
    list_length = pow(2,coding_bits)-coding_bits-1
    list = []
    templist = []
    output = []
    bin = binary.strToBinary(message)
    for element in binary.binaryToBinaryList(bin,list_length):
        list.append(element)
    for element in list:
        list1 = binary.binaryToBinaryList(element,1)
        templist.append(list1)
    list = templist
    list = binary.d2StrListTod2intList(list)
    for element in list:
        output.append(encoder(element))
    return output


if __name__ == "__main__":
    string = "My name is Blank I live in a quiet neighbourhood"
    binstring = binary.strToBinary(string)
    binlist = binary.binaryToBinaryList(binstring,1)
    for i in range(len(binlist)):
        binlist[i] = int(binlist[i])
    a = Hamming(string,8)
    code = komm.HammingCode(8)
    leng = code.dimension
    decoder = komm.BlockDecoder(code)
    b = a
    c = []
    err_number = 0
    err_position_list = []
    for element in a:
        c.append(bscchannel(element,0.001))

    a = c
    k = 0
    for i in a:
        for j in range(len(i)):
            if i[j] != b[k][j] :
                err_number += 1
                err_position_list.append(j)
        k += 1
    c = decoder(a)
    err_number_after_decoding = 0
    err_position_list_after_decoding = []
    for i in range(len(binlist)%leng):
        binlist.append(0)
    for i in range(len(c)):
        if c[i] != binlist[i]:
            err_number_after_decoding += 1
            err_position_list_after_decoding.append(i)
    print(err_number,err_position_list)
    print(err_number_after_decoding, err_position_list_after_decoding)
    print(b)
    print(a)
    print(c)

