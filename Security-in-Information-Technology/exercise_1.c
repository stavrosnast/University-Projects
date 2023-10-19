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
    /* Αctivity 1 declaring variables */
    BN_CTX *ctx = BN_CTX_new();
    BIGNUM *p = BN_new();
    BIGNUM *p1 = BN_new();
    BIGNUM *q = BN_new();
    BIGNUM *q1 = BN_new();
    BIGNUM *one = BN_new();
    BIGNUM *phi_N = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *modulus = BN_new();

    // Assign a vluew from a hex string to p
    BN_hex2bn(&p, "953AAB9B3F23ED593FBDC690CA10E703");
    // Assign a vluew from a hex string to q
    BN_hex2bn(&q, "C34EFC7C4C2369164E953553CDF94945");
    // Assign "1" to the variable one
    BN_hex2bn(&one, "1");
    // Assign the value "0D88C3" to e
    BN_hex2bn(&e, "0D88C3");

    // Calcualte p-1 and q-1
    BN_sub(p1, p, one);
    BN_sub(q1, q, one);

    // Calculate p*q
    BN_mul(modulus, p, q, ctx);

    // Calculate (p-1)*(q-1)
    BN_mul(phi_N, p1, q1, ctx);

    // Calculate d(inverse of e e^-1)
    BN_mod_inverse(d, e, phi_N, ctx);

    // Print  our  private key
    printBN("Private Key : ", d);

    return 0;
}