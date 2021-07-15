# import ascii?

english_list = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
rot_13_list = [n, o, p, q, r, s, t, u, v, w, x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m]

user_str = input("Type a secret message for encryption: ")

counter = 0
def encryption():
    counter += 1 % len()