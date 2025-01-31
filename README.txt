# RSA Encryption and Digital Signature System

## Overview

This project implements an **RSA-based encryption, decryption, and digital signature system** in Python. It enables secure communication between two parties by encrypting messages, decrypting received messages, signing messages, and verifying digital signatures. The RSA algorithm ensures secure data transmission through public and private key cryptography.

## Features

- **Key Generation**: Generates prime numbers `P` and `Q`, computes `N`, `phi(N)`, and generates public (`e`) and private (`d`) keys.
- **Message Encryption**: Uses modular exponentiation for encrypting messages with RSA.
- **Message Decryption**: Decrypts received ciphertext to obtain the original message.
- **Digital Signature**: Signs messages using the sender's private key.
- **Signature Verification**: Verifies the authenticity of the received message using the sender’s public key.
- **Square and Multiply Algorithm**: Used for efficient modular exponentiation in encryption and decryption.
- **Signature without Hashing**: The signature is generated directly from the message without applying a hash function.

## How It Works

1. **Key Pair Generation**:

   - The sender and receiver generate their own RSA key pairs (`N`, `e`, `d`).
   - Public keys (`N`, `e`) are exchanged, while private keys (`d`) are kept secret.

2. **Encryption Process**:

   - The sender converts the message into an integer.
   - The message integer is encrypted using the receiver’s public key (`e`, `N`).
   - The encrypted message is sent to the receiver.

3. **Decryption Process**:

   - The receiver decrypts the message using their private key (`d`).
   - The integer is converted back into text to obtain the original message.

4. **Digital Signature Process**:

   - The sender signs the message by encrypting it with their private key (`d`).
   - The signed message (signature) is sent to the receiver.

5. **Signature Verification**:

   - The receiver decrypts the signature using the sender’s public key (`e`).
   - The decrypted signature is compared with the expected message.
   - If they match, the signature is valid.

## Setup and Usage

### 1. Clone the Repository

```sh
   git clone https://github.com/Hariharan-2411/RSA_Algorithm.git
   cd RSA_Algorithm
```

### 2. Install Dependencies

Ensure you have Python installed and install **SymPy** (used for prime checking):

```sh
   pip install sympy
```

### 3. Run the Program

Execute the Python script to encrypt, decrypt, sign, and verify messages:

```sh
   python rsa_encryption.py
```

### 4. Example Interaction

#### Message Encryption & Decryption:

```
Enter a message to be encrypted: Hello
Encryption of original message: [1369094137, 1466292742, 1444999541]
Decryption of encrypted message: [Message chunks]
Message after decryption: Hello
```

#### Digital Signature & Verification:

```
Enter message to be signed: SecureMessage
Signature: [Signature values]
Partner sign: SecureMessage
Valid Signature
```

## Code Explanation

### Functions:

- `gcd(a, b)`: Computes the greatest common divisor.
- `extended_euclidean_algorithm(a, b)`: Computes modular inverse.
- `modular_exponentiation(a, b, c)`: Performs modular exponentiation using the Square and Multiply method.
- `generation_of_P_and_Q()`: Generates prime numbers.
- `check_for_not_twin_prime(P, Q)`: Ensures `P` and `Q` are not twin primes.
- `generation_of_N(P, Q)`: Computes `N = P * Q`.
- `generation_of_phi(P, Q)`: Computes Euler’s totient function `phi(N)`.
- `generation_of_public_key(phi)`: Generates public key `e`.
- `generation_of_private_key(phi, e)`: Generates private key `d`.
- `conversion_of_message_into_integer_value(message)`: Converts message to an integer.
- `convert_integer_back_to_string(p1)`: Converts integer back to text.
- `encryption(o, e, N)`: Encrypts message using the Square and Multiply function.
- `decryption(p, d, N)`: Decrypts message using the Square and Multiply function.
- `valid(z1, A)`: Verifies signature (without hashing).

## Configuration

- The script is pre-configured with **partner's public keys (`N, e`) and your private key (`d`)**. Modify these values as needed for actual encryption between parties.
- To test with real values, generate new RSA keys and replace them in the script.

## Contributing

Feel free to contribute by submitting pull requests, reporting issues, or improving documentation.

## License

This project is open-source under the **MIT License**.

## Author

Developed by Hariharan Duraisingh
