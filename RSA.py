def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
def toitient(a, b):
    return (a-1)*(b-1)
    
def rsa(a, b):
    n = a * b
    phi_n = toitient(a, b)
    
    for i in range(2, phi_n):   #calculate e
        if gcd(i, phi_n) == 1:
            e = i
            break
    
    for j in range(2, phi_n):  #calculate d
        if (j*e) % phi_n == 1:
            d = j
            break
            
    return n, d, e

def isPrime(no):
    for i in range(2, no//2):
        if no%i == 0:
            return 0
    return 1
    
def encryption(plain_text, e, n):
    return pow(plain_text, e) % n
    
def decryption(cipher_text, d, n):
    return pow(cipher_text, d) % n
    
    
def main():
    print("Enter 2 prime no.s to create keys: ")
    a, b = [int(i) for i in input().split()]
    
    if not isPrime(a) or  not isPrime(b):
        print("Numbers are not prime")
        exit()
        
    n, d, e = rsa(a, b)
    
    print("Public key: ", e, n)
    print("Private key: ", d, n)
    
    print("Enter plain text length: ")
    plain_text = int(input())
    
    cipher_text = encryption(plain_text, e, n)
    decrypt = decryption(cipher_text, d, n)
    
    print("Encryption :", cipher_text) 
    print("Decryption :", decrypt)

main()
