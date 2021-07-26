# Encryption
key = input("Enter the key : ")
key = key.lower().replace(" ", "")
Alphabets = [0 for i in range(26)]
Matrix = [[0 for i in range(5)]for i in range(5)]
r, c = 0, 0
for i in key:
    if Alphabets[ord(i)-97] == 0:
        Alphabets[ord(i)-97] = 1
        Matrix[r][c] = i
        if c == 4:
            r = r+1
            c = 0
        else:
            c = c+1

for i in range(26):
    if Alphabets[i] == 0:
        Alphabets[i] = 1
        if i == 9:
            continue
        Matrix[r][c] = chr(i+97)
        if c == 4:
            r = r+1
            c = 0
        else:
            c = c+1

plaintext = input("Enter the plain text(only lowercase) : ")
plaintext = plaintext.lower().replace(" ", "").replace('j', 'i')
if len(plaintext) % 2 != 0:
    plaintext += "x"
ciphertext = ""
i = 0
while i < len(plaintext):
    r1, c1, r2, c2 = -1, -1, -1, -1
    for row in range(5):
        for col in range(5):
            if Matrix[row][col] == plaintext[i]:
                r1, c1 = row, col
            elif Matrix[row][col] == plaintext[i+1]:
                r2, c2 = row, col
    if r1 == r2:
        c1 = (c1+1) % 5
        c2 = (c2+1) % 5
    elif c1 == c2:
        r1 = (r1+1) % 5
        r2 = (r2+1) % 5
    else:
        temp = c1
        c1 = c2
        c2 = temp
    ciphertext += Matrix[r1][c1]
    ciphertext += Matrix[r2][c2]
    i = i+2

print("Ciphertext : ", ciphertext)

# Decryption
ciphertext = input("Enter the cipher text(only lowercase) : ")
ciphertext = ciphertext.lower().replace(" ", "")

plaintext = ""
i = 0
while i < len(ciphertext):
    r1, c1, r2, c2 = -1, -1, -1, -1
    for row in range(5):
        for col in range(5):
            if Matrix[row][col] == ciphertext[i]:
                r1, c1 = row, col
            elif Matrix[row][col] == ciphertext[i+1]:
                r2, c2 = row, col
    if r1 == r2:
        c1 = (c1-1) % 5
        c2 = (c2-1) % 5
    elif c1 == c2:
        r1 = (r1-1) % 5
        r2 = (r2-1) % 5
    else:
        temp = c1
        c1 = c2
        c2 = temp
    plaintext += Matrix[r1][c1]
    plaintext += Matrix[r2][c2]
    i = i+2

print("Plaintext : ", plaintext)
