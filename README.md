# Simple Signer
Simple Signer is a Python script that provides functionality for signing files using RSA encryption, verifying signatures, and generating RSA key pairs.<br>

# Scope
the script is a simple implementation for file signature idea using rsa.<br>
this script is suitable for any size files, and any type files.<br>

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
Simple Signer provides three primary operations: sign, verify, and key generation.



# Sign a File
To sign a file, use the following command:

```bash
python3 signer.py -s <file-path> -r <private-key-path> -o <output-file-path> -m <digest-mode>
```

file-path : Path to the file you want to sign.<br>
private-key-path : Path to the private key file used for signing.<br>
output-file-path : Path to store the signed output, default to (filename.ext.sig).<br>
digest-mode : used hash function in the signature process [SHA-1 / MD5 / ....], default to (SHA-256). <br>

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

# Example
consider you had ```/home/user/Documents/part1.dd``` file, with a size of 3GB<br>
to sign it first you need to generate a key pair using :
```bash
python3 signer.py -g test_keys -d /home/user/Documents -S 2048
```
then go to 
```/home/user/Documents/test_keys``` directory.<br>
keep the private key (rsa2048.pri) on your computer, and share (rsa2048.pub) freely.<br>


<br>
now you can sign 
```part1.dd```
using : 

```bash
python3 signer.py -s /home/user/Documents/part1.dd -r /home/user/Documents/test_keys/rsa2048.pri -m MD5
```

now you will find  ```/home/user/Documents/part1.dd.sig``` file


<br>
now you can send part1.dd and part1.dd.sig to another computer, on the other computer, to verify the sig use :

```bash
python3 signer.py -v /home/user2/SharedFiles/part1.dd -p /home/user2/SharedFiles/rsa2048.pub -f /home/user/SharedFiles/part1.dd.sig 
```

if everything is okay and the signature is good (file and signature do not change, and you used the correct public key), you will see a message telling you "Signature is Valid!"<br>
otherwise, it will display "Signature is Invalid!"

