#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 128

void printBN(char *msg, BIGNUM *a)
{
    /* Use BN_bn2hex(a) for hex string | Use BN_bn2dec(a) for decimal string */
    char *number_str = BN_bn2hex(a);
    printf("%s %s\n", msg, number_str);
    OPENSSL_free(number_str);
}

int main()
{
    BN_CTX *ctx = BN_CTX_new();
    
    /* Αctivity 5b declaring variables */
    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *sign_message = BN_new();
    BIGNUM *message = BN_new();

    /* Assign values n, e| The values are given by the exercise */
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");

    BN_hex2bn(&sign_message, "DB3F7CDB93483FC1E70E4EACA650E3C6505A3E5F49EA6EDF3E95E9A7C6C7A320");

    // calculate Sign message = encryption with my private key M= S^e mod n 
    BN_mod_exp(message, sign_message, e, n, ctx); 

    // Print the decrypted message
    printBN("message = ", message);
    //python -c 'print("506C65617365207472616E73666572206D652024323030302E416C6963652E".decode("hex"))'
    
    return 0;
}