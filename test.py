from BSCchannel import bscchannel
from GEchannel import gechannel
from generator import generate_bits

x = generate_bits(10)
print(x)
print(bscchannel(x,0.1))
print(gechannel(x,0.1,0.1,0.1,0.1))