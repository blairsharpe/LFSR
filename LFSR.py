def Xor(state, inputs):
    """Computes XOR digital logic

    Parameters:

        :param str state  : Current state of the register
        :param list inputs: Position to tap inputs from register
    Returns:

        :return output: Output of the XOR gate digital logic
    """

    # Obtain bits to feed into Xor gate given index value
    input_A = int(state[inputs[0]])
    input_B = int(state[inputs[1]])

    output = (input_A & ~input_B) | (~input_A & input_B)

    return output


if __name__ == "__main__":

    current_state = "011"
    index_inputs = [1, 2]

    current_state = Xor(current_state, index_inputs)

    print(current_state)
