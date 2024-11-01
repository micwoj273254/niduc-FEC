import random

def gechannel(bits, p_good_to_bad, p_bad_to_good, p_error_good, p_error_bad):
    """
    Simulate a Gilbert-Elliott channel.

    :param bits: A list of bits (0s and 1s) to be transmitted through the channel.
    :param p_good_to_bad: Probability of transitioning from the Good state to the Bad state.
    :param p_bad_to_good: Probability of transitioning from the Bad state to the Good state.
    :param p_error_good: Probability of error in the Good state.
    :param p_error_bad: Probability of error in the Bad state.
    :return: A list of bits after transmission through the channel.
    """
    state = 'Good'  # Start in the Good state
    transmitted_bits = []

    for bit in bits:
        if state == 'Good':
            # Determine if an error occurs in the Good state
            error_occurred = random.random() < p_error_good
            # Determine if a state transition occurs
            if random.random() < p_good_to_bad:
                state = 'Bad'
        else:  # state == 'Bad'
            # Determine if an error occurs in the Bad state
            error_occurred = random.random() < p_error_bad
            # Determine if a state transition occurs
            if random.random() < p_bad_to_good:
                state = 'Good'

        # Flip the bit if an error occurred
        transmitted_bits.append(bit ^ error_occurred)

    return transmitted_bits

# Example usage:
original_bits = [0, 1, 0, 1, 1, 0, 0, 1]
p_good_to_bad = 0.1
p_bad_to_good = 0.3
p_error_good = 0.1
p_error_bad = 0.1

# Set a seed for reproducibility
random.seed(42)

transmitted_bits = gechannel(original_bits, p_good_to_bad, p_bad_to_good, p_error_good, p_error_bad)
print("Original bits:   ", original_bits)
print("Transmitted bits:", transmitted_bits)
