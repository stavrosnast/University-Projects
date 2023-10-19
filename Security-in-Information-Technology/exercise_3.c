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

    /* Αctivity 3 declaring variables */
    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *crypted_message = BN_new();
    BIGNUM *decrypted_message = BN_new();

    /* Assign values n, e, d | The values (n, e, d) are given by the exercise */
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");

    /* Our encrypted message | The value is given by the exercise */
    BN_hex2bn(&crypted_message, "B3AF0A70793BB53492B5311AED5EA843D94661924C97A446E9DD75846DF860DF");

    // Decrypt
    BN_mod_exp(decrypted_message, crypted_message, d, n, ctx);

    // Print the decrypted message
    printBN("Decrypted message : ", decrypted_message);
    // Use python -c 'print("494345205365637572697479206C616220323032302D3231".decode("hex"))' to see the actual message in a readable format

    return 0;
}