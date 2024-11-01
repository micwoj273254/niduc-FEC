def bytearray_to_bits(byte_array):
    """
    Convert a bytearray into an array of bits.

    :param byte_array: The bytearray to convert.
    :return: A list of bits.
    """
    bits = []
    for byte in byte_array:
        # Convert each byte to its binary representation and remove the '0b' prefix
        # Fill leading zeros to ensure each byte is represented by 8 bits
        bits.extend([int(bit) for bit in f'{byte:08b}'])
    return bits


def bits_to_bytearray(bits):
    """
    Convert an array of bits into a bytearray.

    :param bits: A list of bits.
    :return: A bytearray representing the bits.
    """
    if len(bits) % 8 != 0:
        raise ValueError("The number of bits must be a multiple of 8.")

    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        # Take a chunk of 8 bits
        byte_bits = bits[i:i+8]
        # Convert the list of bits to a string, then to an integer, and finally to a byte
        byte = int(''.join(str(bit) for bit in byte_bits), 2)
        byte_array.append(byte)

    return byte_array
