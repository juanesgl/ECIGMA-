from sys import stdin

def jolly_jumper(n, numbers):
    if n < 2:
        return True


    differences = [0] * (n-1)

    for i in range(n-1):
        dif = abs(numbers[i] - numbers[i+1])
        if 1 <= dif < n:
            differences[dif - 1] = 1


    for i in range(n-1):
        if differences[i] == 0:
            return False

    return True

def main():
    input = stdin.read().strip()
    lines = input.splitlines()

    for line in lines:
        if not line:
            continue

        numbers = line.split()


        numbers = [int(num) for num in numbers]

        n = numbers[0]
        sequence = numbers[1:]

        if jolly_jumper(n, sequence):
            print("Jolly")
        else:
            print("Not jolly")

main()