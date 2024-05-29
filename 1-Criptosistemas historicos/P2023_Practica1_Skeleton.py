#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randrange

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:?"



# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed




# ----------------------------------------------------------------------------




def uoc_rotative_encrypt(message, shift):
    """
    EXERCISE 1: Simple substitution cipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    for letter in message:
        position = ABC.find(letter)
        if position + shift <= 40:
            ciphertext = ciphertext + ABC[position + shift]
        else:
            ciphertext = ciphertext + ABC[(position + shift) - 41]

    # --------------------------------

    return ciphertext


def uoc_rotative_decrypt(message, shift):
    """
    EXERCISE 2: Simple substitution decipher
    :message: message to cipher (plaintext)
    :shift: offset or displacement
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    for letter in message:
        position = ABC.find(letter)
        if position - shift >= 0:
            plaintext = plaintext + ABC[position - shift]
        else:
            plaintext = plaintext + ABC[(position - shift) + 41]

    # --------------------------------

    return plaintext



def uoc_grille_genkey(grille_len, num_holes):
    """
    EXERCISE 3: Key generation
    :gruille_len: total grille length in symbols
    :num_holes: Number of holes in the grille
    :return: key as list of 0 and 1
    """

    key = []

    #### IMPLEMENTATION GOES HERE ####
    key = [0]*grille_len
    num_holes_used = 0
    while num_holes_used != num_holes:
        position = randrange(grille_len)
        if key[position] != 1:
            key[position] = 1
            num_holes_used += 1
    # --------------------------------

    return key




def uoc_grille_encrypt(key, plaintext):
    """
    EXERCISE 4: Encrypt a text using the key
    :message: message to grille_encrypt
    :shift: offset or displacement
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    chars_add = 0
    key_position = 0
    while chars_add != len(plaintext):
        if key_position == len(key):
            key_position = 0
        if key[key_position] == 0:
            ciphertext += chr(randrange(33, 159))
        else:
            ciphertext += plaintext[chars_add]
            chars_add += 1
        key_position += 1
    # --------------------------------

    return ciphertext



def uoc_grille_decrypt(key, ciphertext):
    """
    EXERCISE 5: Decrypt a text using the key
    :message: message to grille_decrypt
    :subs_alphabet: substitution alphabet
    :return: ciphered text
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    chars_add = 0
    key_position = 0
    while chars_add != len(ciphertext):
        if key_position == len(key):
            key_position = 0
        if key[key_position] == 1:
            plaintext += ciphertext[chars_add]
        chars_add += 1
        key_position += 1

    # --------------------------------

    return plaintext




def uoc_encrypt(key, plaintext):
    """
    EXERCISE 6: Complete cryptosystem (encrypt)
    :key: grille key
    :plaintext: message to encrypt
    :return: encrypted text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    ciphertext = uoc_grille_encrypt(key, uoc_rotative_encrypt(plaintext, key.count(1)))

    # --------------------------------

    return ciphertext




def uoc_decrypt(key, ciphertext):
    """
    EXERCISE 6: Complete cryptosystem (decrypt)
    :key: grille key
    :ciphertext: message to decrypt
    :return: plaintext
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    plaintext = uoc_rotative_decrypt(uoc_grille_decrypt(key, ciphertext), key.count(1))


    # --------------------------------

    return plaintext





