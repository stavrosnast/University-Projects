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
    BIGNUM *sign_message = BN_new();
    BIGNUM *sign_message1 = BN_new();
    BIGNUM *message = BN_new();
    BIGNUM *message1 = BN_new();

    /* Assign values n, e, d, S | The values are given by the exercise */
    BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");
    BN_hex2bn(&e, "010001");

    BN_hex2bn(&sign_message, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F");
    BN_mod_exp(message, sign_message, e, n, ctx);

    BN_hex2bn(&sign_message1, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6803F");
    BN_mod_exp(message1, sign_message1, e, n, ctx);

    printBN("Sign message : ", message);
    //python -c 'print("4C61756E63682061206D697373696C652E".decode("hex"))'
    printBN("Sign message : ", message1);
    //python -c 'print("91471927C80DF1E42C154FB4638CE8BC726D3D66C83A4EB6B7BE0203B41AC294".decode("hex"))'

    return 0;
}
