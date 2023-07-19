def AskForMissingModules():
        return input("the script you try to run needs some missing modules to operates correctly\nmodules are : rsa\ndo you want the script to install the missing modules ? [Y\\N] :")[0].lower()
def install_rsa():
    try:
        import rsa
    except:
        try:
            import pip
            accept = AskForMissingModules()
            print("pip imported successfully")
            if accept == "y":
                if hasattr(pip, "main"):
                    pip.main(["install", "rsa"])
                else:
                    pip._internal.main(["install", "rsa"])
                import rsa

                print("missing modules are installed successfully!")
            elif accept == "n":
                print("Exit the program!")
                exit(-5)
            else:
                install_rsa()
        except:
            print("pip did not work!", file=sys.stderr)
            exit(-21)


import os
import argparse
import sys
install_rsa()
import rsa
import hashlib






class signer:
    
    
    def Sign(self, FilePath, PrivateKeyFilePath, OutputFilePath,DigestMode):
        File = None
        PrivateKey = None
        try:
            File = open(FilePath, "rb")
        except FileNotFoundError:
            print(FilePath + " is invalid file!", file=sys.stderr)
            exit(-1)
        except:
            print("Exception occured!", file=sys.stderr)
            exit(-2)

        try:
            PrivateKeyFile = open(PrivateKeyFilePath, "rb")
            PrivateKey = rsa.PrivateKey.load_pkcs1(PrivateKeyFile.read())
            PrivateKeyFile.close()

        except FileNotFoundError:
            print(PrivateKeyFilePath + " is invalid file!", file=sys.stderr)
            exit(-3)

        except:
            print("Exception occured!", file=sys.stderr)
            exit(-4)

        try:
            signature = rsa.sign(File, PrivateKey, DigestMode)
            OutputFile = open(OutputFilePath, "wb")
            OutputFile.write(signature.hex().encode('utf-8'))
            OutputFile.close()
        except ValueError:
            print("Invalid hash method: "+DigestMode, file=sys.stderr)
            exit(-50)
        except:
            print("Exception occured!", file=sys.stderr)
            exit(-5)

    def Verify(self, FilePath, SignatureFilePath, PublicKeyFilePath):
        File = None
        PublicKey = None
        Signature = None
        try:
            File = open(FilePath, "rb")
        except FileNotFoundError:
            print(FilePath + " is invalid file!", file=sys.stderr)
            exit(-6)

        except:
            print("Exception occured!", file=sys.stderr)
            exit(-7)

        try:
            PublicKeyFile = open(PublicKeyFilePath, "rb")
            PublicKey = rsa.PublicKey.load_pkcs1(PublicKeyFile.read())
            PublicKeyFile.close()

        except FileNotFoundError:
            print(PublicKeyFilePath + " is invalid file!", file=sys.stderr)
            exit(-8)

        except:
            print("Exception occured!", file=sys.stderr)
            exit(-9)

        try:
            SignatureFile = open(SignatureFilePath, "rb")
            Signature = bytes.fromhex(str(SignatureFile.read(),'utf-8'))
            SignatureFile.close()

        except FileNotFoundError:
            print(SignatureFilePath + " is invalid file!", file=sys.stderr)
            exit(-10)

        except:
            print("Exception occured!", file=sys.stderr)
            exit(-11)

        try:
            Verification = rsa.verify(File, Signature, PublicKey)
            print("Signature is Valid!")
        except:
            print("Signature is Invalid!", file=sys.stderr)
            exit(-12)
        finally:
            File.close()

    def GenerateKeys(self, KeyPairID, DirPath, KeySize):
        Publickey, Privatekey = None, None
        
        try :
            Publickey,Privatekey= rsa.newkeys(KeySize)

        except:
            print("Invalid key size", file=sys.stderr)
            exit(-13)

        try:
            KeyPairDir = os.path.join(DirPath, KeyPairID)
            if not os.path.exists(KeyPairDir):
                os.makedirs(KeyPairDir)
            PublickeyFilePath = str(
                os.path.join(KeyPairDir, "rsa" + str(KeySize) + ".pub")
            )
            PrivatekeyFilePath = str(
                os.path.join(KeyPairDir, "rsa" + str(KeySize) + ".pri")
            )
            PublickeyFile = open(PublickeyFilePath, "wb")
            PrivatekeyFile = open(PrivatekeyFilePath, "wb")
            PublickeyFile.write(Publickey.save_pkcs1())
            PrivatekeyFile.write(Privatekey.save_pkcs1())
            PublickeyFile.close()
            PrivatekeyFile.close()
            print("key pair generated successfully, they are stored at : ", KeyPairDir)
        except:
            print("Exception occured!", file=sys.stderr)
            exit(-14)


if __name__ == "__main__":
    class app:
        
        def SetArgs(self):
            parser = argparse.ArgumentParser(description="sign files using RSA.")
            signgroup = parser.add_argument_group("Signing Options")
            verifygroup = parser.add_argument_group("Verification Options")
            generategroup = parser.add_argument_group("Generation Options")
            signgroup.add_argument(
                "-s",
                "--sign",
                help="sign a file, not allowed with -v  --verify \\ -p  --pub_key\\-f  --signature_file \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )

            signgroup.add_argument(
                "-o",
                "--output",
                help="specify where to store the output, not allowed with -v  --verify \\ -p  --pub_key \\ -f  --signature_file \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )

            signgroup.add_argument(
                "-r",
                "--priv_key",
                help="specify private key to sign a file, not allowed with -v  --verify \\ -p  --pub_key \\ -f  --signature_file \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )

            signgroup.add_argument(
                "-m",
                "--digest_mode",
                help="specify a digest mode to use for sign or verify, available Modes are: MD5 - SHA-1 - SHA-224 - SHA-256 - SHA-384 - SHA-512 - SHA3-256 - SHA3-384 - SHA3-512 \n, not allowed with -v  --verify \\ -p  --pub_key \\ -f  --signature_file \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )
        

            verifygroup.add_argument(
                "-v",
                "--verify",
                help="verify a file, not allowed with -s  --sign \\ -p  --priv_key \\ -o  --output \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )

            verifygroup.add_argument(
                "-p",
                "--pub_key",
                help="specify public key to verify a signature, not allowed with -s  --sign \\ -p  --priv_key \\ -o  --output \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )

            verifygroup.add_argument(
                "-f",
                "--signature_file",
                help="specify a signature to complete verification, not allowed with -s  --sign \\ -p  --priv_key \\ -o  --output \\ -S  --key_size \\ -g  --generate_key \\ -d  --dir",
            )

            generategroup.add_argument(
                "-S",
                "--key_size",
                help="tell what the generated key size is, not allowed with -s  --sign \\ -p  --priv_key \\ -o  --output \\ -v  --verify \\ -p  --pub_key \\ -f  --signature_file",
                type=int,
            )

            generategroup.add_argument(
                "-g",
                "--generate_key",
                help="generate rsa key pair, not allowed with -s  --sign \\ -p  --priv_key \\ -o  --output \\ -v  --verify \\ -p  --pub_key \\ -f  --signature_file",
            )

            generategroup.add_argument(
                "-d",
                "--dir",
                help="specify a directory to save the key pair, not allowed with -s  --sign \\ -p  --priv_key \\ -o  --output \\ -v  --verify \\ -p  --pub_key \\ -f  --signature_file",
            )

        
            self.args = parser.parse_args()

            SignGroupOptions = {"sign", "output", "priv_key","digest_mode"}
            VerifyGroupOptions = {"verify", "signature_file", "pub_key"}
            GenerateGroupOptions = {"generate_key", "key_size", "dir"}

            actual_args = {arg for arg in vars(self.args) if getattr(self.args, arg)}
            if not (
                actual_args.issubset(VerifyGroupOptions)
                or actual_args.issubset(SignGroupOptions)
                or actual_args.issubset(GenerateGroupOptions)
            ):
                print("Options from different groups are mutually exclusive.", file=sys.stderr)
                exit(-20)


        def __init__(self):
                
            s = signer()
            self.SetArgs()
           
            
            if self.args.sign:
                FilePath = self.args.sign
                PrivateKeyFilePath = self.args.priv_key
                OutputSignFilePath = self.args.output
                DigestMode = self.args.digest_mode
            

                if PrivateKeyFilePath == None:
                    print("please specify a private key file path, to sign " + FilePath + " !", file=sys.stderr)
                    exit(-16)
                if OutputSignFilePath == None:
                    OutputSignFilePath = FilePath + ".sig"
                if DigestMode == None:
                    DigestMode = "SHA-256"
                print(DigestMode)
                s.Sign(FilePath, PrivateKeyFilePath, OutputSignFilePath,DigestMode)

            if self.args.verify:
                FilePath = self.args.verify
                PublicKeyFilePath = self.args.pub_key
                SignatureFilePath = self.args.signature_file

            
                if SignatureFilePath == None:
                    print("please specify a Signature file path, to verify it!", file=sys.stderr)
                    exit(-17)

                if PublicKeyFilePath == None:
                    print(
                        "please specify a Public key file path, to verify file : "
                        + FilePath
                        + " and signature : "
                        + SignatureFilePath
                        + "!", file=sys.stderr
                    )
                    exit(-18)

                s.Verify(FilePath, SignatureFilePath, PublicKeyFilePath)

            if self.args.generate_key:
                KeyPairID = self.args.generate_key
                DirPath = self.args.dir
                KeySize = self.args.key_size


                if DirPath == None:
                    DirPath = "."

                s.GenerateKeys(KeyPairID, DirPath, KeySize)

    app()
