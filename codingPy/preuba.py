import hashlib
import string
def sha256(palabra):
    hash = palabra.encode()
    resultado = hashlib.sha256(hash)
    return resultado.hexdigest()



def sha256decode(word):
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                for l in string.ascii_lowercase:
                    for m in string.ascii_lowercase:
                        if sha256('{}{}{}{}{}'.format(i,j,k,l,m)) == word:
                            print('{}{}{}{}{}'.format(i,j,k,l,m))
                        else:
                            pass
                    
                    

sha256decode('23661ebec0d785b2f26aae81a86c556db678fb85bdb9ea2622297472ebaaa43d')