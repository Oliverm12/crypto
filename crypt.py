from Crypto.PublicKey import RSA

key = RSA.generate(1024)

k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')

with open('private.pem','w') as kf:
	kf.write(k.decode())
	kf.close()

with open('public.pem','w') as pf:
	pf.write(p.decode())
	pf.close()

with open('private.pem','r') as fk:
        priv = fk.read()
        fk.close()

with open('public.pem','r') as fp:
        pub = fp.read()
        pf.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)

with open('toto.txt','rb') as file:
	original = file.read()

public_key = key.publickey()
enc_data = public_key.encrypt(original, 32)

print(enc_data)

print()

x = key.decrypt(enc_data)
x = x.decode('utf-8')
print(x)
























