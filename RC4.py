'''
>	@author Juan Manuel Nava Rosales
>	@date 26/septiembre/2022
>	@brief RC4 Cipher Algorithm - Cryptography - Practice 2
>	@version 1.0 
'''
from tkinter import messagebox, Tk, StringVar, Label, Entry, Button

# Key-scheduling algorithm
def KSA( key ):
	j, S = 0, list( range(256) )
	for i in  range(256):
		j = ( j + S[i] + key[i%len(key)] ) % 256
		S[i], S[j] = S[j], S[i]
	return S

# Pseudo-random generation algorithm (PRGA)
def PRGA( S, K ):
	i, j, k = 0, 0, 0

	while( k < len(K) ):
		i = ( i + 1 ) % 256
		j = ( j + S[i] ) % 256
		S[i], S[j] = S[j], S[i]
		t = ( S[i] + S[j] ) % 256
		K[k] = S[t]
		k = k + 1

# Implementando el algoritmo RC4 - XOR
def RC4( key, plainText ):
	if key and plainText:
		S = KSA( key )
		# len(KeyStream) = len(plainText)
		keyStream = list(range(len(plainText)))
		PRGA( S, keyStream )

		R, j = [], 0
		for i in plainText:# XOR
			R.append( i ^ keyStream[j] )
			j = j + 1
		messagebox.showinfo(message=bytes(keyStream).hex().upper(), title="KeyStream")
		return bytes(R)
	return bytes(0) # Exception Tkinter

# Funcion Principal del PROGRAMA
def main():
	#______ MAIN PROGRAM GRAPHIC______
	root = Tk()
	root.title("RC4 P2 - 419048901")
	root.eval('tk::PlaceWindow . center')
	root.config(bd = 50)
	x = StringVar()  # Key
	y = StringVar()  # PlaintText
	ct = StringVar() # CipherText
	
	Label(root, text = "Key").pack()
	Entry(root, justify = "center", width=30, textvariable = x).pack()
	Label(root, text = "Text").pack()
	Entry(root, justify = "center", width=30, textvariable = y).pack()
	Label(root, text = "CipherText").pack()
	Entry(root, justify = "center", width=30, textvariable = ct, state="disabled").pack()
	Label(root, text = "").pack()  # Separator
	
	Button(root,text="Encrypt",command=lambda:ct.set( RC4(bytes(x.get(),'utf-8'),bytes(y.get(),'utf-8')).hex().upper())).pack(side="bottom")

	root.resizable(width = False, height = False)
	root.mainloop()


if __name__ == "__main__":
	main()