def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)

    if g != 1:
        raise ValueError("No inverse")

    return x % m

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if extended_gcd(e, phi)[0] == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

p = 13
q = 11

public_key, private_key = generate_keys(p, q)

message = 3

cipher = encrypt(message, public_key)
plain = decrypt(cipher, private_key)

print("Public Key:", public_key)
print("Private Key:", private_key)
print("Message:", message)
print("Encrypted:", cipher)
print("Decrypted:", plain)
