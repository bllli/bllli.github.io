---
title: 签名及验证签名 rsa with sha1
date created: 2024-11-22 14:52
date modified: 2024-11-22 15:26
tags:
  - Area/RD/python
  - Area/RD/加密
slug: sign-and-verify-rsa-with-sha1
---

最初目的是验证参数签名。

由于因为 sign 太长，超出了微信 URL Link 的自定义参数长度限制。最终没有采用此算法


- sha1 的目的是降低明文长度


```python
"""
RSA with SHA1 签名和验证
"""

import hashlib
import random
import string
from typing import cast

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def sha1(data: bytes) -> bytes:
    return hashlib.sha1(data).digest()


def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
        backend=default_backend(),
    )

    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return private_pem, public_pem


hash_algorithm = hashes.SHA1()


def sign_rsa(private_key: bytes, data: bytes):
    # 加载私钥
    pk = cast(rsa.RSAPrivateKey, serialization.load_pem_private_key(private_key, None))

    # 对数据进行签名
    signature = pk.sign(data, padding.PKCS1v15(), hash_algorithm)

    return signature


def verify_rsa(public_key: bytes, data: bytes, signature: bytes):
    pk = cast(rsa.RSAPublicKey, serialization.load_pem_public_key(public_key))
    try:
        pk.verify(signature, data, padding.PKCS1v15(), hash_algorithm)
        return True
    except Exception:
        return False


def _test_rsa_sign_verify():
    private_key, public_key = generate_rsa_keys()
    print("private_key", private_key)
    print("public_key", public_key)

    for _ in range(10):
        word_len = random.randint(10, 100)
        word = "".join(random.choices(string.ascii_letters + string.digits, k=word_len))
        word_sha1 = sha1(word.encode())

        signature = sign_rsa(private_key, word_sha1)
        signature_hex = signature.hex()
        raw_signature = bytes.fromhex(signature_hex)
        print("signature", len(signature_hex), signature_hex)
        assert verify_rsa(public_key, word_sha1, raw_signature)
        assert not verify_rsa(public_key, word_sha1 + b"1", raw_signature)
    print("pass")


if __name__ == "__main__":
    _test_rsa_sign_verify()

```