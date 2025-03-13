import dis


def example_for_loop():
    for i in range(3):
        print(i)


dis.dis(example_for_loop)
