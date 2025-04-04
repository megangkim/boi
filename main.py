"""
Name: Megan Kim
Student Number: 251431752
Western Username: mkim945
Date Created: April 4, 2025
Description: This file handles user interaction for Encrypt-o-Matic.
It provides a menu for encryption, decryption, and frequency analysis
and calls cipher functions from cipher.py.
"""

from cipher import *

def frequency_analysis(ciphertext):
    """
    Analyzes letter frequencies in the ciphertext.

    Parameters:
        ciphertext (str): The entire ciphered string.

    Returns:
        dict: Keys are uppercase letters A-Z, values are counts.
    """
    freq = {}
    for char in ciphertext.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

def print_frequency_graph(frequency_dict):
    """
    Prints a bar chart of letter frequencies using *'s.

    Parameters:
        frequency_dict (dict): Letter frequency dictionary.
    """
    total = sum(frequency_dict.values())
    for letter in map(chr, range(65, 91)):  # A to Z
        count = frequency_dict.get(letter, 0)
        percentage = round((count / total) * 100) if total > 0 else 0
        print(f"{letter}: {'*' * percentage}")

def print_menu():
    """
    Prints the main menu and gets valid user input (1 to 4).

    Returns:
        int: User-selected menu option.
    """
    while True:
        print("\nEncryption options:")
        print("1) Caesar Cipher")
        print("2) Vigenere Cipher")
        print("3) Frequency Analysis")
        print("4) Exit")
        try:
            option = int(input("Input menu option (1 to 4): ").strip())
            if 1 <= option <= 4:
                return option
            else:
                print("Invalid input!")
        except ValueError:
            print("Invalid input!")

def main():
    """
    Main user interface loop for the Encrypt-o-Matic tool.
    Handles user input and exceptions, and calls appropriate functions.
    """
    while True:
        option = print_menu()

        if option == 1:  # Caesar
            mode = input("Are you encrypting or decrypting (e/d)? ").strip().lower()
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()
            key = int(input("Enter the key (integer): ").strip())
            try:
                if mode == 'e':
                    count = encrypt_caesar(input_file, output_file, key)
                elif mode == 'd':
                    count = decrypt_caesar(input_file, output_file, key)
                else:
                    print("Invalid mode selected.")
                    continue
                print(f"Number of characters processed: {count}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == 2:  # Vigenere
            mode = input("Are you encrypting or decrypting (e/d)? ").strip().lower()
            input_file = input("Enter the input file name: ").strip()
            output_file = input("Enter the output file name: ").strip()
            key = input("Enter the key (a string): ").strip()
            try:
                if mode == 'e':
                    count = encrypt_vigenere(input_file, output_file, key)
                elif mode == 'd':
                    count = decrypt_vigenere(input_file, output_file, key)
                else:
                    print("Invalid mode selected.")
                    continue
                print(f"Number of characters processed: {count}")
            except Exception as e:
                print(f"Error: {e}")

        elif option == 3:  # Frequency Analysis
            filename = input("Enter the cipher text file name: ").strip()
            try:
                with open(filename, "r") as file:
                    text = file.read()
                freq_dict = frequency_analysis(text)
                print_frequency_graph(freq_dict)
            except Exception as e:
                print(f"Error: {e}")

        elif option == 4:  # Exit
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
