def fibonacci(n, return_sequence=False):
    """
    Compute the n-th Fibonacci number or the sequence up to n.

    Args:
        n (int): The index of the Fibonacci number to compute.
        return_sequence (bool): If True, returns the sequence up to n. Defaults to False.

    Returns:
        int or list: The n-th Fibonacci number or the sequence up to n.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return [0] if return_sequence else 0
    elif n == 1:
        return [0, 1] if return_sequence else 1
    else:
        sequence = [0, 1]
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
            if return_sequence:
                sequence.append(b)
        return sequence if return_sequence else b


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Compute the n-th Fibonacci number or the sequence up to n.')
    parser.add_argument('n', type=int, help='The index of the Fibonacci number to compute.')
    parser.add_argument('--sequence', action='store_true', help='Return the sequence up to n.')
    args = parser.parse_args()

    try:
        result = fibonacci(args.n, args.sequence)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()