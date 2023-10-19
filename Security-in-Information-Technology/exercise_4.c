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

    /* Αctivity 4 declaring variables */
    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *signed_message_1 = BN_new();
    BIGNUM *message_1 = BN_new();
    BIGNUM *signed_message_2 = BN_new();
    BIGNUM *message_2 = BN_new();

    /* Assign values n, e, d | The values (n, e, d) are given by the exercise */
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");

    /* Our message | SIGAD US-984XN */
    BN_hex2bn(&message_1, "53494741442055532d393834584e");
    /* Our message with a small change | SIGOD US-984XN */
    BN_hex2bn(&message_2, "5349474f442055532d393834584e");

    /* Encrypt with our given private key and sign the original message */
    BN_mod_exp(signed_message_1, message_1, d, n, ctx);
    /* Encrypt with our given private key and sign the edited message */
    BN_mod_exp(signed_message_2, message_2, d, n, ctx);

    // Print the signs
    printBN("Sign message : ", signed_message_1);
    printBN("Sign message with a small change : ", signed_message_2);

    return 0;
}
