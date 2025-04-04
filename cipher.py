"""
Name: Megan Kim
Student Number: 251431752
Western Username: mkim945
Date Created: April 4, 2025
Description: This file implements Caesar and Vigenère cipher encryption and
decryption functions. It handles input/output file operations and applies the
specified cipher transformations to encrypt or decrypt text.
"""

import os

def encrypt_caesar(input_file, output_file, key):
    """
    Encrypts the contents of the input_file using the Caesar Cipher and writes the result to output_file.

    Parameters:
        input_file (str): The path to the plaintext input file.
        output_file (str): The path to the ciphertext output file.
        key (int): The shift amount (positive or negative).

    Returns:
        int: The number of characters processed.

    Raises:
        TypeError: If key is not an integer.
        FileNotFoundError: If input_file does not exist.
        FileExistsError: If output_file already exists.
    """
    if not isinstance(key, int):
        raise TypeError("The given key value is the wrong type!")
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    if os.path.isfile(output_file):
        raise FileExistsError(f"The output file {output_file} already exists.")

    count = 0
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            new_line = ""
            for char in line:
                count += 1
                if char.isalpha():
                    # Convert to uppercase and shift within A-Z
                    shifted = (ord(char.upper()) - ord('A') + key) % 26
                    new_char = chr(ord('A') + shifted)
                    new_line += new_char
                else:
                    new_line += char
            fout.write(new_line)
    return count

def decrypt_caesar(input_file, output_file, key):
    """
    Decrypts the contents of the input_file using the Caesar Cipher and writes the result to output_file.

    Parameters:
        input_file (str): The path to the ciphertext input file.
        output_file (str): The path to the plaintext output file.
        key (int): The original shift used for encryption (positive or negative).

    Returns:
        int: The number of characters processed.

    Raises:
        TypeError: If key is not an integer.
        FileNotFoundError: If input_file does not exist.
        FileExistsError: If output_file already exists.
    """
    return encrypt_caesar(input_file, output_file, -key)

def encrypt_vigenere(input_file, output_file, key):
    """
    Encrypts the input_file using the Vigenère Cipher and writes to output_file.

    Parameters:
        input_file (str): The name of the input plaintext file.
        output_file (str): The name of the encrypted output file.
        key (str): The keyword used for encryption (letters only).

    Returns:
        int: Number of characters processed (including non-alphabetic).

    Raises:
        TypeError: If key is not a string.
        FileNotFoundError: If input_file does not exist.
        FileExistsError: If output_file already exists.
    """
    if not isinstance(key, str):
        raise TypeError("The given key value is the wrong type!")
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    if os.path.isfile(output_file):
        raise FileExistsError(f"The output file {output_file} already exists.")

    key = key.upper()
    key_index = 0
    count = 0
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            new_line = ""
            for char in line:
                count += 1
                if char.isalpha():
                    shift = ord(key[key_index % len(key)]) - ord('A')
                    shifted = (ord(char.upper()) - ord('A') + shift) % 26
                    new_char = chr(ord('A') + shifted)
                    new_line += new_char
                    key_index += 1  # Advance key only for alphabetic characters
                else:
                    new_line += char
            fout.write(new_line)
    return count

def decrypt_vigenere(input_file, output_file, key):
    """
    Decrypts the input_file using the Vigenère Cipher and writes to output_file.

    Parameters:
        input_file (str): The name of the encrypted input file.
        output_file (str): The name of the decrypted output file.
        key (str): The keyword used for encryption (letters only).

    Returns:
        int: Number of characters processed (including non-alphabetic).

    Raises:
        TypeError: If key is not a string.
        FileNotFoundError: If input_file does not exist.
        FileExistsError: If output_file already exists.
    """
    if not isinstance(key, str):
        raise TypeError("The given key value is the wrong type!")
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"The input file {input_file} does not exist.")
    if os.path.isfile(output_file):
        raise FileExistsError(f"The output file {output_file} already exists.")

    key = key.upper()
    key_index = 0
    count = 0
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            new_line = ""
            for char in line:
                count += 1
                if char.isalpha():
                    shift = ord(key[key_index % len(key)]) - ord('A')
                    shifted = (ord(char.upper()) - ord('A') - shift) % 26
                    new_char = chr(ord('A') + shifted)
                    new_line += new_char
                    key_index += 1
                else:
                    new_line += char
            fout.write(new_line)
    return count
