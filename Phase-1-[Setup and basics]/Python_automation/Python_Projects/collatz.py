def collatz(number):
    if number % 2 == 0:
        result = number //2
    else:
        result = (3*number + 1)
    return result


def main():
    num = int(input("enter number: "))
    while(num!=1):
        num = collatz(num)

main()
