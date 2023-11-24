def print_fibonacci(length):
    if length == 0:
        print("[]")
        return
    
    first = 0
    second = 1
    result = [first]

    if length == 1:
        print(result)
        return

    result.append(second)

    length -= 2

    while length > 0:
        temp = second
        second = first + second
        first = temp

        result.append(second)

        length -= 1

    print(result)
