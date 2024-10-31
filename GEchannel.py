import random

def gechannel(bits, pgb, pbg, eg, eb):
    state = 1
    output =[]

    for bit in bits:
        if state == 1:
            if random.random() < pgb:
                state = 0
            if random.random() < eg:
                bit = (bit + 1) % 2
        else:
            if random.random() < pbg:
                state = 1
            if random.random() < eb:
                bit = (bit + 1) % 2
        output.append(bit)

    return output
    #pgb - Probability of transitioning from the good state to the bad state
    #pbg - Probability of transitioning from the bad state to the good state
    #eg - Probability of no error occurring when in the good state
    #eb - Probability of no error occurring when in the bad state