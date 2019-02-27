
import random
# src: https://www.rookieslab.com/posts/how-to-find-multiplicative-inverse-of-a-number-modulo-m-in-python-cpp
def multiplicative_inverse(e, phi):
	for i in range(0, phi):
		if (e*i) % phi == 1:
			return i
	return -1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Check if a number is a prime
def is_prime(num):
    if num == 2: # corner case
        return True
    if num < 2 or num % 2 == 0: 
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

# Read input from console and make sure the number is prime 
def read_prime_input(message):
	loop = True
	num = 0
	while loop: 
		num = int(input(message))
		loop = not is_prime(num)
		if loop:
			print("Not a prime number, try again..")
	return num

# To read about the logic, see: 
# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_understanding_rsa_algorithm.htm
def generate_keypairs(p, q):
    n = p * q

    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    # https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e,phi)

    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt_message(publickey, message_text):
	# Get e and n from publickey
    e, n = publickey

    #For each letter of the message get the Unicode code and follow math from ref in method desc
    encrypt = [(ord(char) ** e) % n for char in message_text]

    #Return the array of bytes
    return encrypt


def decrypt_message(pk, encryptedtext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in encryptedtext]
    #Return the array of bytes as a string
    return "".join(plain)
    


if __name__ == '__main__':
    print ("--------------- RSA Encrypter/ Decrypter --------------- ")
    p = read_prime_input("Enter a prime number:")
    q = read_prime_input("Enter a another (different) prime number:")
    print ("Generating your public and private keypairs...")
    public_key, private_key = generate_keypairs(p, q)
    print ("Your public key is ", public_key ," and your private key is ", private_key)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt_message(private_key, message)
    print ("Encrypted message: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("Decrypted message using with public key: ", public_key ," . . .")
    print (decrypt_message(public_key, encrypted_msg))









