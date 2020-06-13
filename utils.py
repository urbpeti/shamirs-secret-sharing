from os import urandom
from random import randint
from math import log

def convert_bytes_to_int(bytes):
  integer = 0
  for b in bytes:
    integer = (integer << 8) + b
  return integer

def convert_int_to_bytes(integer):
  b = b''
  while integer > 0:
    b += bytes([integer % 256])
    integer = integer // 256
  return b[::-1]


def evaluate_polynom(polynom, x, P):
  acc = 0
  for i in range(len(polynom)):
    acc += polynom[i] * pow(x, i, P)
    acc = acc % P
  
  return acc

def generate_shards(secret, n, threshold, P=2 ** 521 - 1):
  polynom = [secret]
  for i in range(threshold - 1):
    polynom.append(randint(1, P - 1))

  shards = []
  for x in range(1, 1 + n):
    shards.append((x, hex(evaluate_polynom(polynom, x, P))))

  return shards

def retrieve_secret_int(shards, P=2 ** 521 - 1):
  acc = 0
  for i in range(len(shards)):
    xi = shards[i][0]
    lagrange = 1
    for j in range(len(shards)):
      if j != i:
        lagrange *= -shards[j][0]
        lagrange *= pow((xi - shards[j][0]), P - 2, P)
        lagrange = lagrange % P
    acc += int(shards[i][1], 16) * int(lagrange)
    acc = acc % P
  return acc