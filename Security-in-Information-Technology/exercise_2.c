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

    /* Αctivity 2 declaring variables */
    BIGNUM *p = BN_new();
    BIGNUM *q = BN_new();
    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *name_surname = BN_new();
    BIGNUM *encrypted_message = BN_new();
    BIGNUM *check_name_surname = BN_new();

    /* Assign values to p, q, e, d. | The values (p, q, d) are given from the exercise and the d (private key) is calcuated in ask1.c */
    BN_hex2bn(&p, "953AAB9B3F23ED593FBDC690CA10E703");
    BN_hex2bn(&q, "C34EFC7C4C2369164E953553CDF94945");
    BN_hex2bn(&e, "0D88C3");
    BN_hex2bn(&d, "63F67E805D8DEB0B4182C57C3DC24F3C1350CF182E8ABF85FD24062A3BC7F2EB");

    /* Convert our string to hex */
    BN_hex2bn(&name_surname, "53746176726f73204e6173746f756c6973");

    /* Calculate n = p * q */
    BN_mul(n, p, q, ctx);

    /* Encryption | C = M ^ e mod n  | encrypted_message = name_surname ˆ e mod n */
    BN_mod_exp(encrypted_message, name_surname, e, n, ctx);

    /* Decrypt | M = C ^ d mod n | check_name_surname =  encrypted_message ^ d mod n */
    BN_mod_exp(check_name_surname, encrypted_message, d, n, ctx);

    /* Print my name in HEX the encrupted and the ecrypted message */
    printBN("name_surname : ", name_surname);
    printBN("encrypted_message : ", encrypted_message);
    printBN("check_name_surname : ", check_name_surname);
    /* Use python -c 'print("53746176726F73204E6173746F756C6973".decode("hex"))' for  HEX to ASCII */

    return 0;
}