import hashlib

#returns the SHA1 hash of the given file
def hash_file(filename):
    hash = hashlib.sha1()

    #open file to read in binary mode
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            #read 1024 bytes at a time
            chunk = file.read(1024)
            hash.update(chunk)

    return hash.hexdigest()


print(hash_file("filehash.py"))