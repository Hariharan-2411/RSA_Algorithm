import random 
from sympy import isprime

print()

#GCD_calculation
def gcd(b,a):
    d = a
    t = b
    while (t!=0):
        w = d % t
        d = t
        t = w
    return d

#Extended_euclidean
def extended_euclidean_algorithm(a, b):
    x, y = 1, 0
    d = a
    r, s = 0, 1
    t = b
    while (t > 0):
        q = d // t  
        u = x - q * r
        v = y - q * s
        w = d - q * t
        x, y, d = r, s, t
        r, s, t = u, v, w
    return x

#power_function
def modular_exponentiation(a, b, c):
    r = 1  
    a = a % c      
    while (b > 0):
        if (b % 2) == 1:
            r = (r * a) % c
        b = b // 2
        a = (a * a) % c  
    return r

#Generation of P and Q
def generation_of_P_and_Q():
    while True:
        a = random.getrandbits(16)
        if (a >= (2**15)) and (a <= ((2**16) -1)):
            return a
        
#Check the generated p and q are not twin prime numbers, both P and Q are prime numbers and are not equal
def check_for_not_twin_prime(P, Q):
    while True:
        if (P == ( Q + 2) or Q == (P + 2) or P == Q or isprime(P) != True or isprime(Q) != True):
            P = generation_of_P_and_Q()
            Q = generation_of_P_and_Q()
        else:
            print ("Value of P: ",P)
            print ("Value of Q: ",Q)
            return P,Q

#Generation of N
def generation_of_N(P,Q):
    N = P * Q 
    return N

#Generation of phi(N)
def generation_of_phi(P, Q):
    phi = (P - 1) * (Q - 1)
    return phi

#Generation of public key (e)
def generation_of_public_key(phi):
    while True:
        e = random.randint(2, phi - 1)
        if (e > phi):
            if gcd(e, phi) == 1 :
                return e
        else:
            if gcd(phi, e) == 1 :
                return e
    
#Generation of private key (d)
def generation_of_private_key(phi, e):
    d = extended_euclidean_algorithm(e, phi)
    if (d < 0):
        d = d %  phi
    return d
        
#Conversion_of_message_into_integer_value
def conversion_of_message_into_integer_value(message):
    o = []
    x = []
    u = []
    for i in range(0, len(message), 3):

        split1 = message[i:i+3]
        u.append(split1)
        hexa1 = split1.encode()
        hexa2 = '0x' + hexa1.hex()
        x.append(hexa2)

        hexa = hexa1.hex()
        int_conversion = int(hexa,16)
        o.append(int_conversion)
    return x, o, u

#Square_multiple_function
def square_and_multiple_function(r, s, t):
    g = 1
    h = 1

    binary = bin(s)[2:]
    c = len(binary)

    if (binary[-1] == '1'):
        h = r%t

    for i in range(2,c+1,1):
        count = 2**(i-1)
        if (binary[-i] == '1'):
            f = modular_exponentiation(r,count,t)
            g = (f*g) % t
            
    if(h > 0):
        return (h*g)%t
    else:
        return g%t

#Encryption
def encryption(o, e, N):
    p = []
    for integer in o:
        ci = square_and_multiple_function(integer, e, N)
        p.append(ci)  
    return p

#Decryption   
def decryption(p, d, N):
    p1 = []
    for integer1 in p:
        pl = square_and_multiple_function(integer1, d, N)
        p1.append(pl)
    return p1  
    
#Converting_integer_back_to_string
def convert_integer_back_to_string(p1):
    t = []
    for i in range(0,len(p1)):
        p1[i] = hex(p1[i])[2:]
        byte1 = bytes.fromhex(p1[i])
        decode1 = byte1.decode()
        t.append(decode1)

    z = ''.join(t)
    return t,z
    
#validiation
def valid(z1,A):
    if(z1 == A):
        print("\nValid Signature")
    else:
        print("\nInvalid Signature")

#Main_function
def main():
    P = generation_of_P_and_Q()
    Q = generation_of_P_and_Q()
    P,Q = check_for_not_twin_prime(P, Q)

    N = generation_of_N(P, Q)
    print ("Value of N: ", N)

    phi = generation_of_phi(P, Q)
    print("Value of phi(N): ", phi)

    e = generation_of_public_key(phi)
    print ("Value of public key: ", e)
    
    d = generation_of_private_key(phi, e)
    print ("Value of private key: ", d ,"\n")
    N = 1847044079  #partnes's N
    e = 666168589   #partner's E(public key)
    d = 523139501   #Your Private Key
    N1 = 1888532381 #Your N
    e1 = 1643391521 #Your E

    message = input(str("Enter a message to be encrypted: " ))
    x, o, u = conversion_of_message_into_integer_value(message)
    print ("Chunks of original message: ", u)
    print ("Hexa decimal Value for original message : ", x)
    print ("Integer Value: ", o)

    p = encryption(o, e , N)
    print ("Encryption of original message: ", p)
    
    #Encrypted Text received from partner
    p = [1369094137, 1466292742, 1444999541, 1789448043, 1104726336] #Encrypted Text received from partner
    p1 = decryption(p ,d ,N1)
    print ("\nDecryption of encrypted message: ", p1)

    t,z = convert_integer_back_to_string(p1)
    print ("Chunks after decryption: ", t)
    print ("Message after decryption: ", z ,"\n")

    #signature
    A = input(str("Enter message to be signed: "))
    x1, o1, u1 = conversion_of_message_into_integer_value(A)
    print ("chunks of signed message: ", u1)
    print ("Hexa decimal Value for original message: ", x1)
    print ("Integer Value : ", o1)
    B = encryption(o1,d,N1)
    print ("Signature: ", B)

    #verification and signed text received from partner
    B = [1068410606, 1413494148, 771461894, 256148725, 197010186, 1831816208, 171177290] #signature received from partner
    C = decryption(B,e,N)
    print ("\nDecrypted signature: ", C)
    t1,z1 = convert_integer_back_to_string(C)
    print ("Partner sign: ",z1)

    #is_valid
    original_message = "Joshua Reneeth Rajaa" #Name of the signer
    D = valid(z1,original_message)

if __name__ == "__main__":
    main()