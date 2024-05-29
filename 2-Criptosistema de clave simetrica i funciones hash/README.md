# 2-Criptosistema de clave simetrica y funciones hash

## Estructura del Código

El archivo contiene las siguientes funciones:

1. **ByteHex_to_ByteBin(hex)**
   - Convierte un valor hexadecimal a su representación binaria.
   - **Parámetros:**
     - `hex`: Valor en hexadecimal.
   - **Retorna:** Cadena binaria.

2. **add_value(array, polynomial)**
   - Añade un valor basado en el polinomio a un array mediante desplazamientos y operaciones bit a bit.
   - **Parámetros:**
     - `array`: Lista de enteros.
     - `polynomial`: Lista de enteros que representa un polinomio.
   - **Retorna:** Array modificado.

3. **uoc_lfsr_sequence(polynomial, initial_state, output_bits)**
   - Genera la secuencia de salida de un LFSR con un estado inicial y un polinomio de conexión dados.
   - **Parámetros:**
     - `polynomial`: Lista de enteros con los coeficientes del polinomio de conexión.
     - `initial_state`: Lista de enteros con el estado inicial del LFSR.
     - `output_bits`: Entero, número de bits de la secuencia de salida.
   - **Retorna:** Lista de bits de salida.

4. **uoc_ext_a5_pseudo_random_gen(params_pol_0, params_pol_1, params_pol_2, clocking_bits, output_bits)**
   - Implementa el generador pseudoaleatorio extendido A5/1.
   - **Parámetros:**
     - `params_pol_0`: Lista de dos elementos que describe el primer LFSR.
     - `params_pol_1`: Lista de dos elementos que describe el segundo LFSR.
     - `params_pol_2`: Lista de dos elementos que describe el tercer LFSR.
     - `clocking_bits`: Lista de tres elementos con los bits de reloj de cada LFSR.
     - `output_bits`: Entero, número de bits de la secuencia de salida.
   - **Retorna:** Lista de bits pseudoaleatorios.

5. **uoc_a5_cipher(initial_state_0, initial_state_1, initial_state_2, message, mode)**
   - Implementa el cifrado/descifrado con el generador pseudoaleatorio A5.
   - **Parámetros:**
     - `initial_state_0`: Lista, estado inicial del primer LFSR.
     - `initial_state_1`: Lista, estado inicial del segundo LFSR.
     - `initial_state_2`: Lista, estado inicial del tercer LFSR.
     - `message`: Cadena, texto plano a cifrar o texto cifrado a descifrar.
     - `mode`: `MODE_CIPHER` o `MODE_DECIPHER`, si se desea cifrar o descifrar.
   - **Retorna:** Cadena, texto cifrado o descifrado.

6. **uoc_aes(message, key)**
   - Implementa el cifrado AES de un bloque utilizando una clave de 256 bits.
   - **Parámetros:**
     - `message`: Cadena de 1s y 0s con la representación binaria del mensaje, de 128 caracteres de largo.
     - `key`: Cadena de 1s y 0s con la representación binaria de la clave, de 256 caracteres de largo.
   - **Retorna:** Cadena de 1s y 0s con la representación binaria del mensaje cifrado, de 128 caracteres de largo.

7. **uoc_g(message)**
   - Implementa la función `g`.
   - **Parámetros:**
     - `message`: Cadena de 1s y 0s con la representación binaria del mensaje, de 128 caracteres de largo.
   - **Retorna:** Cadena de 1s y 0s, de 256 caracteres de largo.

8. **uoc_naive_padding(message, block_len)**
   - Implementa un esquema de padding ingenuo. Se añaden tantos 0s al final del mensaje hasta alcanzar la longitud de bloque deseada.
   - **Parámetros:**
     - `message`: Cadena con el mensaje.
     - `block_len`: Entero, longitud del bloque.
   - **Retorna:** Cadena de 1s y 0s con el mensaje padded.

9. **uoc_mmo_hash(message)**
   - Implementa la función hash.
   - **Parámetros:**
     - `message`: Cadena de caracteres con el mensaje.
   - **Retorna:** Cadena de 1s y 0s con el hash del mensaje.

10. **uoc_collision(prefix)**
    - Genera colisiones para `uoc_mmo_hash`, con mensajes que tienen un prefijo dado.
    - **Parámetros:**
      - `prefix`: Cadena, prefijo para los mensajes.
    - **Retorna:** Tupla de dos elementos, con las dos cadenas que comienzan con el prefijo y tienen el mismo hash.
