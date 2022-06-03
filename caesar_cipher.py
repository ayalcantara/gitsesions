def caesarcipher(s, k):
    pivot = []
    firstCase= ( 65 + (pivot[i] - 65 + k) % 26)
    secondCase= ( 97 + (pivot[i] - 97 + k) % 26)
    for char in s:
        pivot.append(ord(char))
    for i in range(n):
        if 65 <= pivot[i] <= 90:
            pivot[i] = firstCase
        elif 97 <= pivot[i] <= 122:
            pivot[i] = secondCase
    return "".join(map(chr, pivot))


