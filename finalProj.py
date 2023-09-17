import argparse
import pathlib
parser = argparse.ArgumentParser(
                    prog = 'finalProj.py',
                    description = 'This tool split any file to pieces',
                    epilog = 'Thanks for using this piece of code')



parser.add_argument('-f', '--file',required=True,help="Any path to filename") 
parser.add_argument('-m', '--mode',required=True,help="Tool mode : 0 - cutting , 1 - collection") 
parser.add_argument('-p', '--pieces',required=True,help="Split the file into pieces of ?") 

args = parser.parse_args() #returns list of all args 

if not args.pieces.isdigit():
	print("pieces isn't a number")
	exit()

if not (args.mode == '0' or args.mode == '1'):
	print("Mode is invalid")
	exit()

try:
	f_type=pathlib.Path(args.file).suffix
	f = open(args.file,'rb')
	byte = f.read()
	arr = bytearray(byte)
	f.close()
    	# arr is full of bytes
	st=""
	for i in arr:
		st+=str(i)
	h1=hash(st)
	if (args.mode == '0') :#cutting mode
		x=args.pieces
		c=len(arr)//int(x)
		for i in range(int(x)):#חתיכת הקובץ 
			piece=open("00"+str(i+1)+f_type,'wb')
			piece.write(arr[:c])
			piece.close()
			arr=arr[c::]
		if len(arr)!=0 :
			piece=open("00"+str(int(x)+1)+f_type,'wb')
			piece.write(bytes(arr))
			piece.close()
		
		print("the split is done!!!")
	else :#     collecion mode 
		x=input("how many pieces you have ? ")
		final=open('final'+f_type,'wb')
		for i in range(int(x)):#חיבור של החתיכות 
			piece=open("00"+str(i+1)+f_type,'rb')
			final.write(piece.read())
			piece.close()
		final=open('final'+f_type,'rb')
		byte = final.read()
		arr = bytearray(byte)
		final.close()
		st=""
		for i in arr:
			st+=str(i)
		h2=hash(st)
		print("h1 is h2 ? ",(h1 == h2) )#check hash.....בדיקת "האש" אחרי חיבור החתיכות
		print("well done my friends")
except FileNotFoundError as e:
    print(e)
    
    
    
    
