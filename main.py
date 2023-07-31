import random


def generate_random_numbers(count):
    random_numbers = [random.randint(1, 100) for _ in range(count)]
    return random_numbers


def main():
    try:
        num = int(input("Enter the number of random numbers to generate: "))
        if num <= 0:
            print("Please enter a positive number.")
        else:
            random_numbers = generate_random_numbers(num)
            print(f"Random numbers: {random_numbers}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
