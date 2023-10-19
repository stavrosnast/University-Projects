# SECURITY IN INFORMATION TECHNOLOGY (LABORATORY)

This document pertains to a laboratory exercise in the field of Information Security and provides a practical introduction to concepts such as cryptography, digital signatures, and more.

## Table of Contents

1. **Introduction**
2. **Tools Used for the Exercise**
3. **Activity 1: Creating a Private Key**
4. **Activity 2: Message Encryption**
5. **Activity 3: Message Decryption**
6. **Activity 4: Message Signing**
7. **Activity 5A: Signature Verification**
8. **Activity 5B: Signature Verification**
9. **Activity 6: Non-Automatic X.509 Certificate Verification**
10. **Conclusion**
11. **References**

## Introduction

This document serves as a report for a laboratory exercise in the field of Information Security. The primary focus of this exercise is to introduce students to concepts like cryptography and digital signatures, specifically delving into the RSA cryptographic algorithm using the 'bn' library.

## Tools Used for the Exercise

The following tools were used in the development of this exercise:

1. Visual Studio Code v1.55.0
2. SEEDUbuntu-16.04-32bit
3. Virtual Box Version 6.1.18 r142142 (Qt5.6.2)
4. Windows Education 10 20H2 64bit (19042.967)

## Activity 1: Creating a Private Key

In this activity, a private key is generated using the RSA cryptographic algorithm following the mathematical formula: `e * d mod (p-1) * (q-1) = 1`. The steps for calculating the private key are outlined, and the code is available in the provided source file.

## Activity 2: Message Encryption

This activity involves the encryption of a message. It includes the conversion of the message into a hexadecimal string and calculating the mod_exp of the message for encryption. The provided code demonstrates these steps.

## Activity 3: Message Decryption

In this activity, the decryption of a message is performed. It involves the calculation of mod_exp for the ciphertext to retrieve the original message. The code also shows the conversion of the decrypted message into an ASCII string.

## Activity 4: Message Signing

Activity 4 involves signing a message using a private key. The document describes the mathematical formula for creating a signature and the code for generating the signatures. It also highlights how even a slight change in the original message significantly affects the signature.

## Activity 5A: Signature Verification

In this activity, the verification of a signature is demonstrated. It involves comparing the calculated message with the original message. Any changes in the signature result in an invalid verification, which is exemplified in the provided code.

## Activity 5B: Signature Verification

Activity 5B provides an additional demonstration of signature verification, emphasizing the importance of maintaining the integrity of the signature and the message.

## Activity 6: Non-Automatic X.509 Certificate Verification

The last activity is about non-automatic verification of an X.509 certificate. The code extracts the modulus 'n' and 'e' values from a certificate and computes the hash of the certificate body. The result is then used to verify the signature. The document provides detailed steps and commands for these tasks.

## Conclusion

The document concludes the laboratory exercise, summarizing the key takeaways and the importance of understanding information security concepts.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of this license.
