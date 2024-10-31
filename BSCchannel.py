import komm

def bscchannel(bits, error):
    bsc = komm.BinarySymmetricChannel(error)
    return bsc(bits)
    #error - error probability