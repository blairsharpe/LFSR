def xor(state, inputs, length):
    """Computes XOR digital logic

    Parameters:

        :param str state  : Current state of the register
        :param list inputs: Position to tap inputs from register
    Returns:

        :return output: Output of the XOR gate digital logic
        :rtype int :
    """

    # Obtain bits to feed into Xor gate given index value
    input_a = int(state[inputs[0]])
    input_b = int(state[inputs[1]])

    result = (input_a & ~input_b) | (~input_a & input_b)

    return result << length


if __name__ == "__main__":

    current_state = "010"
    index_inputs = [0, 2]

    xor_output = xor(current_state, index_inputs, len(current_state)-1)
    shift = int(current_state, 2) >> 1
    result = xor_output | shift

    print(bin(result))


