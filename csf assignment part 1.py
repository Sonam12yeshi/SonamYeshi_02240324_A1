def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(start, end):
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, unit):
    if unit.lower() == "feet":
        return value * 0.3048  
    elif unit.lower() == "meter":
        return value / 0.3048  
    else:
        return None

def count_consonants(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char.isalpha() and char not in vowels)

def is_palindrome(string):
    cleaned = "".join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]

def find_min_max(numbers):
    return min(numbers), max(numbers)

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return len(file.read().split())
    except FileNotFoundError:
        return "File not found."

def main():
    while True:
        print("\nMenu:")
        print("1. Sum of prime numbers in a range")
        print("2. Length unit converter (Feet, Meter)")
        print("3. Consonant counter")
        print("4. Palindrome checker")
        print("5. Find Min and Max number in a list")
        print("6. Word counter in a text file")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            start = int(input("Enter start range: "))
            end = int(input("Enter end range: "))
            print("Sum of prime numbers:", sum_primes(start, end))
        
        elif choice == "2":
            value = float(input("Enter value: "))
            unit = input("Enter unit (Feet/Meter): ")
            converted = length_converter(value, unit)
            if converted is not None:
                print(f"Converted value: {converted:.2f}")
            else:
                print("Invalid unit. Please enter Feet or Meter.")
        
        elif choice == "3":
            string = input("Enter a string: ")
            print("Number of consonants:", count_consonants(string))
        
        elif choice == "4":
            string = input("Enter a string: ")
            if is_palindrome(string):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")
        
        elif choice == "5":
            numbers = list(map(int, input("Enter numbers separated by space: ").split()))
            min_num, max_num = find_min_max(numbers)
            print(f"Minimum number: {min_num}, Maximum number: {max_num}")
        
        elif choice == "6":
            filename = input("Enter the filename: ")
            print("Word count:", count_words_in_file(filename))
        
        elif choice == "7":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            
if __name__ == "__main__":
    main()
