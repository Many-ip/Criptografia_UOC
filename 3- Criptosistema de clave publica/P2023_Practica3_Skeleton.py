#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

P_INFINITY = (None, None)


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed


# ----------------------------------------------------------------------------


def uoc_ComputePoints(curve):
    """
    EXERCISE 1.1: Count the points on an elliptic curve
    :curve: a list with the curve values [a, b, p]
    :return: number of points on the curve
    """

    num_points = 1

    #### IMPLEMENTATION GOES HERE ####
    a, b, p = curve

    # fuerza bruta para el valor x de 0 a p
    for x in range(p):
        y_sqr = (x ** 3 + a * x + b) % p
        for y in range(p):
            if (y ** 2) % p == y_sqr:
                num_points += 1
    # --------------------------------

    return num_points


def uoc_VerifyNumPoints(curve, n):
    """
    EXERCISE 1.2: Verify group order
    :curve: a list with the curve values [a, b, p]
    :n: number of points
    :return: True if it satisfies the equation or False
    """

    result = False

    #### IMPLEMENTATION GOES HERE ####
    if uoc_ComputePoints(curve) == n:
        result = True

    # --------------------------------

    return result


def uoc_AddPoints(curve, P, Q):
    """
    EXERCISE 2.1: Add two points
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :Q: another point as a pair (x, y)
    :return: P+Q
    """

    # R = P+Q
    suma = None

    #### IMPLEMENTATION GOES HERE ####

    # recurso usado para resolver este apartado:
    #       * https://www.secg.org/sec1-v2.pdf

    a, b, p = curve
    Px, Py = P
    Qx, Qy = Q

    # Si alguno de los puntos es el punto en el infinito, el resultado es el otro punto.
    if P == P_INFINITY:
        return Q
    elif Q == P_INFINITY:
        return P

    # Si los puntos son iguales pero con y opuestas, el resultado es el punto en el infinito.
    elif Px == Qx and Py != Qy:
        return P_INFINITY

    # Si los puntos son iguales pero con y igual a 0, el resultado es el punto en el infinito.
    elif Px == Qx and Py == Qy == 0:
        return P_INFINITY

    # Si los puntos son iguales, se calcula la pendiente de la tangente en el punto.
    elif P == Q:
        m = (3 * Px ** 2 + a) * pow(2 * Py, p - 2, p) % p

    # Se calcula la pendiente de la recta que pasa por los puntos.
    else:
        m = (Qy - Py) * pow(Qx - Px, p - 2, p) % p

    # Se calcula el punto resultante de la suma.
    Rx = (m ** 2 - Px - Qx) % p
    Ry = (m * (Px - Rx) - Py) % p
    suma = Rx, Ry
    # --------------------------------
    return suma


def uoc_SelfProductPoint(curve, n, P):
    """
    EXERCISE 3.1: Multiplication of a scalar by a point
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    # R = nP
    product = None

    #### IMPLEMENTATION GOES HERE ####
    product = P_INFINITY

    # recursos:
    #          https://sefiks.com/2016/03/27/double-and-add-method/
    #          https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication

    # double and add method

    binary_n = bin(n)[2:]  # Representación binaria de n.
    for bit in binary_n:
        product = uoc_AddPoints(curve, product, product)  # Doblado del punto.
        if bit == '1':
            product = uoc_AddPoints(curve, product, P)  # Suma del punto P.

    """""
    #PASA TODO MENOS EL TEST5
    
    # Fuerza Bruta
    
    
    
    product = P_INFINITY
    for i in range(n):
            product = uoc_AddPoints(curve, P, product)
       """""


    # -----------------
    return product


def uoc_IsGroup(curve):
    """
    EXERCISE 3.2: xxx
    :curve: check if the curve is a group
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    result = None

    #### IMPLEMENTATION GOES HERE ####

    result = True
    a, b, p = curve

    # tal como indica en la pagina 2 del enunciado, una curva no puede tener una doble raiz,
    # siendo 4a^3 + 27 b^2 = 0 la condicion de esa doble raiz y la excepcion de que forme parte
    # de un grupo

    equacio = pow(4*pow(a, 3)+27*pow(b, 2),1,p)

    if equacio == 0:
        result = False
    # --------------------------------
    return result


def uoc_OrderPoint(curve, P):
    """
    EXERCISE 3.3: Point order
    :curve: a list with the curve values [a, b, p]
    :n: constant to multiply
    :P: a point as a pair (x, y)
    :return: nP
    """

    point_order = None

    #### IMPLEMENTATION GOES HERE ####
    Q = P
    point_order = 1
    for i in range(uoc_ComputePoints(curve)):
        if Q == P_INFINITY:
            break
        else:
            point_order += 1
            Q = uoc_SelfProductPoint(curve, point_order, P)

    # --------------------------------
    return point_order


def uoc_GenKey(curve, P):
    """
    EXERCISE 4.1: Generate a pair of keys
    :curve: a list with the curve values [a, b, p]
    :P: a point as a pair (x, y)
    :return: a pair of keys (pub, priv)
    """

    key = (None, None)

    #### IMPLEMENTATION GOES HERE ####

    a, b, p = curve

    #cada participante genera un numero aleatorio entre 1 i el numero p
    private = random.randint(1, p)

    # public = private*P
    public = uoc_SelfProductPoint(curve, private, P)

    key = private, public

    # --------------------------------
    return key


def uoc_SharedKey(curve, priv_user1, pub_user2):
    """
    EXERCISE 4.2: Generate a shared secret
    :curve: a list with the curve values [a, b, p]
    :pub_user1: a public key
    :pub_user2: a private key
    :return: shared secret
    """

    shared = None

    #### IMPLEMENTATION GOES HERE ####
    # αPubB = βPubA = αβP = βαP.
    shared = uoc_SelfProductPoint(curve, pub_user2, priv_user1)
    # --------------------------------
    return shared
