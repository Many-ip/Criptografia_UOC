#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

MODE_CIPHER = 0
MODE_DECIPHER = 1


# --- IMPLEMENTATION GOES HERE ---------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
def ByteHex_to_ByteBin(hex):
    return ''.join(f'{byte:08b}' for byte in hex)
def add_value(array,polinomio):
    #Desplazamiento derecha
    value = None
    bit = None
    for i in range(len(array)):
        if value is not None:
            value.append(array[i] & polinomio[i])
        else:
            value = [array[i] & polinomio[i]]
    for i in value:
        if bit is not None:
            bit ^= i
        else:
            bit = i
    del array[-1]
    array.insert(0, bit)

    return array
# --------------------------------------------------------------------------


def uoc_lfsr_sequence(polynomial, initial_state, output_bits):
    """
    Returns the output sequence of output_bits bits of an LFSR with a given initial state and connection polynomial.

    :param polynomial: list of integers, with the coefficients of the connection polynomial that define the LFSR.
    :param initial_state: list of integers with the initial state of the LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: a list of output_bits bits
    """
    result = None

    # --- IMPLEMENTATION GOES HERE ---
    state = initial_state[::-1]
    polynomial = polynomial[::-1]
    result = []
    for i in range(output_bits):

        #Variable para aplicar el xor de bits

        xor_bit = None

        #El bucle recorre el valor del polinomio, en caso de tener el valor 1, se busca la posicion
        # hayada para operar con el xor. Finalmente hace una traslacion del valor, agregando en
        # la posicion 0 el resultado del xor y eliminado el ultimo elemento del array

        for index in range(len(polynomial)):
            if polynomial[index]:
                if xor_bit is None:
                    xor_bit = state[index]
                else:
                    xor_bit ^= state[index]
        result.append(state[-1])
        state.insert(0, xor_bit)
        del state[-1]

    # --------------------------------

    return result


def uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, output_bits):
    """
    Implements extended A5's pseudorandom generator.
    :param params_pol_0: two-element list describing the first LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_1: two-element list describing the second LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param params_pol_2: two-element list describing the third LFSR: the first element contains a list with the
    coefficients of the connection polynomial, the second element contains a list with the initial state of the LFSR.
    :param clocking_bits: three-element list, with the clocking bits of each LFSR
    :param output_bits: integer, number of bits of the output sequence
    :return: list of output_bits elements with the pseudo random sequence
    """

    sequence = []

    # --- IMPLEMENTATION GOES HERE ---

    # Se inicializa los lfsr del estado inicial
    lfsr0 = uoc_lfsr_sequence(params_pol_0[0], params_pol_0[1], len(params_pol_0[1]))[::-1]
    lfsr1 = uoc_lfsr_sequence(params_pol_1[0], params_pol_1[1], len(params_pol_1[1]))[::-1]
    lfsr2 = uoc_lfsr_sequence(params_pol_2[0], params_pol_2[1], len(params_pol_2[1]))[::-1]

    #Secuencia de bits que nos permitiran obtener el siguiente en la rotacion
    bits_lfsr0 = uoc_lfsr_sequence(params_pol_0[0], params_pol_0[1], len(params_pol_0[1])+output_bits)
    bits_lfsr1 = uoc_lfsr_sequence(params_pol_1[0], params_pol_1[1], len(params_pol_1[1]) + output_bits)
    bits_lfsr2 = uoc_lfsr_sequence(params_pol_2[0], params_pol_2[1], len(params_pol_2[1]) + output_bits)

    #indica que posicion actual de la secuencia para ir agregando los nuevos bits
    n0 = len(params_pol_0[0])
    n1 = len(params_pol_1[0])
    n2 = len(params_pol_2[0])

    # estas variables guarda los polinomios al reves, dado que nos pasan por parametro el array al revés
    p0 = params_pol_0[0][::-1]
    p1 = params_pol_1[0][::-1]
    p2 = params_pol_2[0][::-1]

    for i in range(output_bits):
        #La secuencia es el xor de los ultimos valores de los lfsr
        sequence.append(lfsr0[-1] ^ lfsr1[-1] ^ lfsr2[-1])

        # se guardan la posición del vector donde hace referencia al bit mayoria
        cb0 = clocking_bits[0]
        cb1 = clocking_bits[1]
        cb2 = clocking_bits[2]

        #Guardamos el valor del bit que contiene en la posicion del bit mayoria
        c0 = lfsr0[cb0]
        c1 = lfsr1[cb1]
        c2 = lfsr2[cb2]

        #comprobación para saber que pol tiene que rotar teniendo en cuenta si su bit forma parte de la mayoria
        if c0 == c1 == c2:
            del lfsr0[-1]
            lfsr0.insert(0, bits_lfsr0[n0])
            n0 += 1

            del lfsr1[-1]
            lfsr1.insert(0, bits_lfsr1[n1])
            n1 += 1

            del lfsr2[-1]
            lfsr2.insert(0, bits_lfsr2[n2])
            n2 += 1
        elif c0 == c1 != c2:
            del lfsr0[-1]
            lfsr0.insert(0, bits_lfsr0[n0])
            n0 += 1

            del lfsr1[-1]
            lfsr1.insert(0, bits_lfsr1[n1])
            n1 += 1
        elif c0 == c2 != c1:
            del lfsr0[-1]
            lfsr0.insert(0, bits_lfsr0[n0])
            n0 += 1

            del lfsr2[-1]
            lfsr2.insert(0, bits_lfsr2[n2])
            n2 += 1
        else:
            del lfsr1[-1]
            lfsr1.insert(0, bits_lfsr1[n1])
            n1 += 1

            del lfsr2[-1]
            lfsr2.insert(0, bits_lfsr2[n2])
            n2 += 1
        # --------------------------------

    return sequence


def uoc_a5_cipher(initial_state_0, initial_state_1, initial_state_2, message, mode):
    """
    Implements ciphering/deciphering with the A5 pseudo random generator.

    :param initial_state_0: list, initial state of the first LFSR
    :param initial_state_1: list, initial state of the second LFSR
    :param initial_state_2: list, initial state of the third LFSR
    :param message: string, plaintext to cipher (mode=MODE_CIPHER) or ciphertext to decipher (mode=MODE_DECIPHER)
    :param mode: MODE_CIPHER or MODE_DECIPHER, whether to cipher or decipher
    :return: string, ciphertext (mode=MODE_CIPHER) or plaintext (mode=MODE_DECIPHER)
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---
    #Se pasa el texto en binario
    if mode==MODE_CIPHER:
        bin_text = ''.join(format(ord(i), '08b') for i in message)
    else:
        bin_text = message

    #se agrega el polinomio de cada uno
    pol0 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pol1 = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pol2 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    #Indicamos donde se encuentra el bit que permite saber si son mayoria para su desplazamiento
    clocking_bits = [8, 10, 10]
    params_pol_0 = [pol0, initial_state_0]
    params_pol_1 = [pol1, initial_state_1]
    params_pol_2 = [pol2, initial_state_2]
    # s guarda la secuencia de A5/1
    s = uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, len(bin_text))

    for i in range(len(s)):
        output += str(int(s[i]) ^ int(bin_text[i]))
    if mode == MODE_DECIPHER:
        text = ""
        byte = ""
        for i in output:
            byte += i
            if len(byte) == 8:
                decimal = int(byte, 2)
                char = chr(decimal)
                text += char
                byte = ""
        output = text
    # --------------------------------

    return output


def uoc_aes(message, key):
    """
    Implements 1 block AES enciphering using a 256-bit key.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :param key: string of 1 and 0s with the binary representation of the key, 256 char. long
    :return: string of 1 and 0s with the binary representation of the ciphered message, 128 char. long
    """

    cipher_text = ""

    # --- IMPLEMENTATION GOES HERE ---
    message = bytes.fromhex(hex(int(message, 2))[2:])
    key = bytes.fromhex(hex(int(key, 2))[2:])
    cipher = AES.new(key, AES.MODE_ECB)

    # encrypt the message
    ciphertext_bytes = cipher.encrypt(message)

    # convert the ciphertext to binary string
    cipher_text = ''.join(format(byte, '08b') for byte in ciphertext_bytes)

    # --------------------------------

    return cipher_text


def uoc_g(message):
    """
    Implements the g function.

    :param message: string of 1 and 0s with the binary representation of the messsage, 128 char. long
    :return: string of 1 and 0s, 256 char. long
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---
    output += message*2
    # --------------------------------

    return output


def uoc_naive_padding(message, block_len):
    """
    Implements a naive padding scheme. As many 0 are appended at the end of the message
    until the desired block length is reached.

    :param message: string with the message
    :param block_len: integer, block length
    :return: string of 1 and 0s with the padded message
    """

    output = ""

    # --- IMPLEMENTATION GOES HERE ---
    output = ''.join(format(ord(i), '08b') for i in message)
    if (len(message)*8) % block_len != 0:
        while len(output) % block_len != 0:
            output += "0"
    test=len(output) % 128 == 0
    print("Es el output multiple de 128?",test )
    # --------------------------------

    return output


def uoc_mmo_hash(message):
    """
    Implements the hash function.

    :param message: a char. string with the message
    :return: string of 1 and 0s with the hash of the message
    """

    h_i = ""

    # --- IMPLEMENTATION GOES HERE ---
    block_len = 128
    h_i = bytes.fromhex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    padding = uoc_naive_padding(message, block_len)
    #generamos bloques de bits
    blocks_bits = []
    string_block = ""
    for bit in padding:
        string_block += bit
        if len(string_block) == block_len:
            blocks_bits.append(string_block)
            string_block = ""
    print("Numero de interaciones:", len(blocks_bits))
    i=0
    for bloc in blocks_bits:
        g = uoc_g(ByteHex_to_ByteBin(h_i))
        i+=1
        print("iteracion:",i)
        cipher_aes = uoc_aes(bloc, g)

        h_i = bin(int(ByteHex_to_ByteBin(h_i), 2) ^ int(cipher_aes, 2))[2:]
        h_i = bytes.fromhex(hex(int(h_i, 2))[2:])

    h_i = ByteHex_to_ByteBin(h_i)

    # --------------------------------
    return h_i
def uoc_collision(prefix):
    """
    Generates collisions for uoc_mmo_hash, with messages having a given prefix.

    :param prefix: string, prefix for the messages
    :return: 2-element tuple, with the two strings that start with prefix and have the same hash.
    """

    collision = ("", "")

    # --- IMPLEMENTATION GOES HERE ---
    #variables para las dos parametros que se pasaran por el hash
    new_word1 = ""
    new_word2 = ""
    # Hay que tener en cuenta que para generar la colision hay que hacer que el padding llene de 0 los bloques finales.

    # Primer caso, en caso, el prefijo no es multiple de 128 bits, en este caso se puede usar el propio prefijo como uno
    # de los elementos de la colisión, entonces el otro elemento de colisión és el binario del texto después del padding
    if len(prefix)*8 % 128 !=0:
        new_word1 = prefix+"HOLA"
        new_bin = uoc_naive_padding(new_word1, 128)
        byte = ""
        for i in new_bin:
            byte += i
            if len(byte) == 8:
                decimal = int(byte, 2)
                char = chr(decimal)
                new_word2 += char
                byte = ""
    #Segundo caso, de colision es en caso que sea el prefijo multiplo de 128 bits, por lo que se podria hacer dos cosas:
    #    * Eliminar el ultimo caracter del prefijo y hacer su padding como en el anterior caso (se descarta porque no se conserva el prefijo)
    #    * Agregar cualquier entre 1 a 15 letras (en caso de hacerlo en string) o agregar 1 a 127 bits (en caso de hacerlo en binario)
    # Ambas situaciones fuerzan a realizar lo que se ha realizado en el if, tener una información no multiple de 128 bits y obtener su padding
    else:
        new_word1 = prefix+"Colision"
        new_bin = uoc_naive_padding(new_word1, 128)
        byte = ""
        for i in new_bin:
            byte += i
            if len(byte) == 8:
                decimal = int(byte, 2)
                char = chr(decimal)
                new_word2 += char
                byte = ""
    collision = new_word1, new_word2
    print(collision)
    # --------------------------------

    return collision
