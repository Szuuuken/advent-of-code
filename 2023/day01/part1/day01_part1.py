from typing import List

def main():
    file = open('day01_real_input.txt', 'r')
    lines = file.readlines()
    file.close()

    numbers: List(int) = []
    sum = 0

    for line in lines:
        first_number = ""
        last_number = ""

        for char in line:
            if char.isdigit() and first_number == "" : first_number = char
            if char.isdigit() and first_number != "" : last_number = char


        number = int(first_number + last_number)
        numbers.append(number)
        sum += number

    print(numbers)
    print(sum)

if __name__ == "__main__":
    main()