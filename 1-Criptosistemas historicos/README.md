# 1-Criptosistemas historicos

Este proyecto incluye una serie de funciones implementadas en Python para realizar diversos ejercicios relacionados con criptosistemas. El código abarca desde cifrados de sustitución simples hasta el uso de rejillas para encriptación y decriptación de mensajes.

## Estructura del Código

El archivo contiene las siguientes funciones:

1. **uoc_rotative_encrypt(message, shift)**
   - Cifra un mensaje utilizando un cifrado de sustitución simple con un desplazamiento dado.
   - **Parámetros:**
     - `message`: El mensaje en texto claro que se desea cifrar.
     - `shift`: El desplazamiento o desplazamiento para el cifrado.
   - **Retorna:** El texto cifrado.

2. **uoc_rotative_decrypt(message, shift)**
   - Descifra un mensaje cifrado utilizando un cifrado de sustitución simple con un desplazamiento dado.
   - **Parámetros:**
     - `message`: El mensaje cifrado que se desea descifrar.
     - `shift`: El desplazamiento o desplazamiento utilizado para el cifrado.
   - **Retorna:** El texto en claro.

3. **uoc_grille_genkey(grille_len, num_holes)**
   - Genera una clave para una rejilla de cifrado con una longitud y número de agujeros especificados.
   - **Parámetros:**
     - `grille_len`: Longitud total de la rejilla en símbolos.
     - `num_holes`: Número de agujeros en la rejilla.
   - **Retorna:** La clave como una lista de 0 y 1.

4. **uoc_grille_encrypt(key, plaintext)**
   - Cifra un texto utilizando una rejilla de cifrado y una clave dada.
   - **Parámetros:**
     - `key`: La clave de la rejilla.
     - `plaintext`: El mensaje en texto claro que se desea cifrar.
   - **Retorna:** El texto cifrado.

5. **uoc_grille_decrypt(key, ciphertext)**
   - Descifra un texto cifrado utilizando una rejilla de cifrado y una clave dada.
   - **Parámetros:**
     - `key`: La clave de la rejilla.
     - `ciphertext`: El mensaje cifrado que se desea descifrar.
   - **Retorna:** El texto en claro.

6. **uoc_encrypt(key, plaintext)**
   - Cifra un texto utilizando un sistema criptográfico completo que combina el cifrado rotativo y la rejilla de cifrado.
   - **Parámetros:**
     - `key`: La clave de la rejilla.
     - `plaintext`: El mensaje en texto claro que se desea cifrar.
   - **Retorna:** El texto cifrado.

7. **uoc_decrypt(key, ciphertext)**
   - Descifra un texto utilizando un sistema criptográfico completo que combina el cifrado rotativo y la rejilla de cifrado.
   - **Parámetros:**
     - `key`: La clave de la rejilla.
     - `ciphertext`: El mensaje cifrado que se desea descifrar.
   - **Retorna:** El texto en claro.
