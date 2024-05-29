# 3- Criptosistema de clave publica

## Estructura del Código

El archivo contiene las siguientes funciones:

1. **uoc_ComputePoints(curve)**
   - Cuenta el número de puntos en una curva elíptica.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
   - **Retorna:** Entero, número de puntos en la curva.

2. **uoc_VerifyNumPoints(curve, n)**
   - Verifica si el número de puntos en la curva elíptica coincide con un número dado \(n\).
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
     - `n`: Entero, número de puntos a verificar.
   - **Retorna:** Booleano, True si el número de puntos coincide con \(n\), de lo contrario False.

3. **uoc_AddPoints(curve, P, Q)**
   - Suma dos puntos en la curva elíptica.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
     - `P`: Punto en la curva como par `(x, y)`.
     - `Q`: Otro punto en la curva como par `(x, y)`.
   - **Retorna:** Tupla, punto resultante después de sumar los puntos \(P\) y \(Q\).

4. **uoc_SelfProductPoint(curve, n, P)**
   - Multiplica un escalar \(n\) por un punto \(P\) en la curva elíptica.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
     - `n`: Entero, escalar a multiplicar.
     - `P`: Punto en la curva como par `(x, y)`.
   - **Retorna:** Tupla, punto resultante después de la multiplicación escalar \(nP\).

5. **uoc_IsGroup(curve)**
   - Verifica si la curva elíptica forma un grupo.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
   - **Retorna:** Booleano, True si la curva forma un grupo, de lo contrario False.

6. **uoc_OrderPoint(curve, P)**
   - Calcula el orden de un punto \(P\) en la curva elíptica.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
     - `P`: Punto en la curva como par `(x, y)`.
   - **Retorna:** Entero, orden del punto \(P\).

7. **uoc_GenKey(curve, P)**
   - Genera un par de claves criptográficas (pública y privada) para la criptografía de curva elíptica.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
     - `P`: Punto base en la curva como par `(x, y)`.
   - **Retorna:** Tupla, par de claves `(privada, pública)`.

8. **uoc_SharedKey(curve, priv_user1, pub_user2)**
   - Genera una clave compartida utilizando la clave privada de un usuario y la clave pública de otro usuario.
   - **Parámetros:**
     - `curve`: Lista con los valores de la curva `[a, b, p]`.
     - `priv_user1`: Entero, clave privada del usuario 1.
     - `pub_user2`: Tupla, clave pública del usuario 2 como par `(x, y)`.
   - **Retorna:** Tupla, clave compartida.
