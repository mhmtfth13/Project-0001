import hashlib
import os

metin = "Mehmet"
salt = os.urandom(1000)
hash_object = hashlib.md5(salt + metin.encode())
hash_degeri = hash_object.hexdigest()
saltsiz_hash_degeri = hashlib.md5(metin.encode())


print(f"Saltsiz MD5 Degeri: {saltsiz_hash_degeri.hexdigest()}")
print(f"Salt: {salt.hex()}")
print(f"Salt'li hash degeri: {hash_degeri}")
