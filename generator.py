import os

def generate_random_bytes(size):
    """
    Generate a byte array of random bytes.

    :param size: The number of random bytes to generate.
    :return: A byte array containing the random bytes.
    """
    random_bytes = os.urandom(size)
    return bytearray(random_bytes)