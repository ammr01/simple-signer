# Simple Signer
Simple Signer is a Python script that provides functionality for signing files using RSA encryption, verifying signatures, and generating RSA key pairs.<br>

# Scope
the script is a simple implementation for file signature idea using rsa.<br>
this script is not suitable for large files, or very small file.<br>
to use a reliable, and lightweight script use Hash-Based-Signer, not this script.<br>
look for Hash-Based-Signer in my account.

# Prerequisites
The following dependencies are required to run Simple Signer:

rsa: Python module for RSA encryption and decryption.
If the required dependencies are missing, the script will prompt you to install them.
to install rsa module manually:

```bash
pip install rsa
```

# Installation
To install Simple Signer and its dependencies, follow these steps:

Clone the Simple Signer repository from GitHub:

```bash
git clone https://github.com/ammr01/simple-signer.git
```

# Usage
Simple Signer provides three main operations: sign, verify, and key generation.



# Sign a File
To sign a file, use the following command:

```bash
python3 signer.py -s <file-path> -r <private-key-path> -o <output-file-path>
```

file-path : Path to the file you want to sign.<br>
private-key-path : Path to the private key file used for signing.<br>
output-file-path : Path to store the signed output.<br>

# Verify a Signature
To verify a signature, use the following command:

```bash
python3 signer.py -v <file-path> -f <signature-file-path> -p <public-key-path>
```

file-path : Path to the file you want to verify.<br>
signature-file-path : Path to the signature file.<br>
public-key-path : Path to the public key file used for verification.<br>


# Generate RSA Key Pair
To generate an RSA key pair, use the following command:

```bash
python3 signer.py -g <key-pair-id> -d <output-directory> -S <key-size>
```


key-pair-id : Identifier for the generated key pair.<br>
output-directory : Directory to store the generated key pair.<br>
key-size : Size of the generated key in bits (e.g., 2048).<br>

Note: Optional arguments can be omitted if not required.

