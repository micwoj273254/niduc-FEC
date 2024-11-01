import random

def gechannel(bits, p_good_to_bad, p_bad_to_good, p_error_good, p_error_bad):
    """
    Simulate a Gilbert-Elliott channel and count dependent and independent errors.

    :param bits: A list of bits (0s and 1s) to be transmitted through the channel.
    :param p_good_to_bad: Probability of transitioning from the Good state to the Bad state.
    :param p_bad_to_good: Probability of transitioning from the Bad state to the Good state.
    :param p_error_good: Probability of error in the Good state.
    :param p_error_bad: Probability of error in the Bad state.
    :return: A tuple containing the transmitted bits, number of independent errors, and number of dependent errors.
    """
    state = 'Good'  # Start in the Good state
    transmitted_bits = []
    independent_errors = 0
    burst_errors = 0

    for bit in bits:
        if state == 'Good':
            # Determine if an error occurs in the Good state
            error_occurred = random.random() < p_error_good
            if error_occurred:
                independent_errors += 1
            # Determine if a state transition occurs
            if random.random() < p_good_to_bad:
                state = 'Bad'
        else:  # state == 'Bad'
            # Determine if an error occurs in the Bad state
            error_occurred = random.random() < p_error_bad
            if error_occurred:
                burst_errors += 1
            # Determine if a state transition occurs
            if random.random() < p_bad_to_good:
                state = 'Good'

        # Flip the bit if an error occurred
        transmitted_bits.append(bit ^ error_occurred)

    return transmitted_bits, independent_errors, burst_errors
