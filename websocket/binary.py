import hashlib

from binascii import hexlify

origin = 'あ'
encoded_origin = origin.encode('utf-8')
hash_obj = hashlib.sha256()
hash_obj.update(encoded_origin)
digest = hash_obj.digest()
print(digest)                 # 人間が読めない
print(hexlify(digest))        # 人間が読める