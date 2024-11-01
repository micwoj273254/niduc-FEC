from reedsolo import RSCodec, ReedSolomonError

from BSCchannel import bscchannel
from GEchannel import gechannel
from b2b import bytearray_to_bits, bits_to_bytearray
from generator import generate_random_bytes


# Generate random bytes
a = bytearray("hello world", "utf-8")
print("Original data:", a)

# Create an RSCodec instance with 4 error correction symbols
rsc = RSCodec(16)

# Encode the data
b = rsc.encode(a)
print("Encoded data:", b)

# Convert the encoded data to bits
c = bytearray_to_bits(b)
print("Encoded data in bits:", c)

# Simulate transmission through channels
d = bscchannel(c, 0.03)
print("BSC channel data:", d)
bsc_errors = 0
for i in range(len(c)):
    if c[i] != d[i]:
        bsc_errors += 1
print("Number of errors in BSC channel:", bsc_errors)
print("BSC BER:", bsc_errors/len(c))


e = gechannel(c, 0.0009, 0.00004, 0.003631513, 0.99999)
print("Gilbert-Elliott channel data:", e)
ge_errors = 0
for i in range(len(c)):
    if c[i] != e[i]:
        ge_errors += 1
print("Number of errors in Gilbert-Elliott channel:", ge_errors)
print("Gilbert-Elliott BER:", ge_errors/len(c))


# Convert the bits back to bytearrays
f = bits_to_bytearray(d)
print("Data after BSC channel:", f)

g = bits_to_bytearray(e)
print("Data after GE channel:", g)

# Decode the data
try:
    decoded_z = rsc.decode(f)
    print("Decoded data from BSC channel:", decoded_z)
except ReedSolomonError as z:
    print("Decoding error from BSC channel:", z)

try:
    decoded_y = rsc.decode(f)
    print("Decoded data from GE channel:", decoded_y)
except ReedSolomonError as z:
    print("Decoding error from GE channel:", z)