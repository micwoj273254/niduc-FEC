import binary
import komm
from BSCchannel import bscchannel
from GEchannel import gechannel
from b2b import bytearray_to_bits, bits_to_bytearray
from generator import generate_random_bytes

# Hamming returns list with encoded hamming_code arrays
def HammingFunction(byte_array: bytearray, redundancy:int):
    output = []
    code = komm.HammingCode(redundancy)
    encoder = komm.BlockEncoder(code)
    dimension = pow(2, redundancy) - redundancy - 1
    bits = bytearray_to_bits(byte_array)
    bits = binary.intListToStrList(bits)
    bin = binary.binaryListToBinary(bits)
    list = binary.binaryToBinaryList(bin,dimension)
    list = binary.d2StrListTod2intList(list)
    for i in list:
        output.append(encoder(i))

    return output


if __name__ == "__main__":
    aH = generate_random_bytes(47)
    bH = HammingFunction(aH, 8)
    codeH = komm.HammingCode(8)
    decoderH = komm.BlockDecoder(codeH)
    cH = []

    for i in bH:
        cH.append(bscchannel(i, 0.001))

    dH = []
    ge_errorH = 0
    ge_error_positionH = []

    for i in bH:
        eH, errorH, kH = gechannel(i.tolist(), 0.00, 0.00004, 0.001, 0.09)
        dH.append(eH)
        ge_errorH += errorH
        ge_errorH += kH

    for kH in range(len(dH)):
        for i in range(len(dH[kH])):
            if dH[kH][i] != bH[kH][i]:
                stringH = str(kH) + "; " + str(i)
                ge_error_positionH.append(stringH)

    bsc_errorH = 0
    bsc_error_positionH = []

    for kH in range(len(cH)):
        for i in range(len(cH[kH])):
            if cH[kH][i] != bH[kH][i]:
                bsc_errorH += 1
                stringH = str(kH) + "; " + str(i)
                bsc_error_positionH.append(stringH)

    decoded_cH = []
    decoded_dH = []

    for i in cH:
        decoded_cH.append(decoderH(i))

    for i in dH:
        decoded_dH.append(decoderH(i))

    flatcH = []

    for i in decoded_cH:
        flatcH.extend(i)
    decoded_cH = flatcH

    flatdH = []

    for i in decoded_dH:
        flatdH.extend(i)
    decoded_dH = flatdH

    decoded_list_cH = []
    decoded_cH = binary.intListToStrList(decoded_cH)

    stringH = ""
    listcH = []
    for j in decoded_cH:
        stringH += j
    stringH = stringH.rstrip("0")
    while len(stringH) % 8 != 0:
        stringH += "0"
    for j in stringH:
        listcH.append(int(j))

    decoded_list_cH = listcH
    decoded_byte_cH = bits_to_bytearray(decoded_list_cH)

    decoded_list_dH = []
    decoded_dH = binary.intListToStrList(decoded_dH)

    stringH = ""
    listdH = []
    for j in decoded_dH:
        stringH += j
    stringH = stringH.rstrip("0")
    while len(stringH) % 8 != 0:
        stringH += "0"
    for j in stringH:
        listdH.append(int(j))

    decoded_list_dH = listdH
    decoded_byte_dH = bits_to_bytearray(decoded_list_dH)

    print("generated bytes :", aH)
    print("(byte) decoded Hamming code after bsc :", decoded_byte_cH)
    print("(byte) decoded Hamming code after ge :", decoded_byte_dH)
    print("(bit)Hamming code :", bH)
    print("(bit)Hamming code after bsc :", cH)
    print("(bit) decoded Hamming code after bsc :", decoded_cH)
    print("(bit)Hamming code after ge :", dH)
    print("(bit) decoded Hamming code after ge :", decoded_dH)
    print("number of bsc errors:", bsc_errorH)
    print("(bit)position of bsc errors:", bsc_error_positionH)
    print("number of ge errors:", ge_errorH)
    print("(bit)position of ge errors:", ge_error_positionH)