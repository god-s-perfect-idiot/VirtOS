from subprocess import call
import time
import pyAesCrypt
from editor import *
import getpass

fisys=[]
files=[]
par=1 
k= len(open("filesystem").readlines(  ))
q=0
broken=0
buff= 64*1024
passw="qaz1"
user=""
new=0
pw=""

pyAesCrypt.decryptFile("loginf.enc","loginf",passw,buff)
pwinf=open("loginf")
pwi=pwinf.read()
pwi=pwi.split()
pwinf.close()
pwinf=open("loginf","w")

def boot():
	call(["clear"])
	print("\n\n\n\n\t\t\tVirtOS\n\n\t\t\tBooting up")
	time.sleep(0.2)
	call(["clear"])
	print("\n\n\n\n\t\t\tVirtOS\n\n\t\t\tBooting up.")
	time.sleep(0.2)
	call(["clear"])
	print("\n\n\n\n\t\t\tVirtOS\n\n\t\t\tBooting up..")
	time.sleep(0.2)
	call(["clear"])
	print("\n\n\n\n\t\t\tVirtOS\n\n\t\t\tBooting up...")
	time.sleep(0.2)
	call(["clear"])
	print("\n\n\n\n\t\t\tVirtOS")
	time.sleep(0.2)
	call(["clear"])

def shutdown():
	global pwi,pwinf,passw,buff,q
	call(["clear"])
	print("\n\n\n\n\t\t\tVirtOS\n\n\t\t\tShutting Down")
	time.sleep(0.5)
	call(["clear"])
	fsw=open("filesystem","w")
	for i in range(q):
		for j in range(len(fisys[i])):
			if(j==0):
				fsw.write("fo."+fisys[i][j]+"\n")
			else:
				fsw.write("fi."+fisys[i][j]+"\n")
	fsw.close()	
	pwinfo=pwi[0]+"\n"+pwi[1]
	pwinf.write(pwinfo)
	pwinf.close()
	pyAesCrypt.encryptFile("loginf","loginf.enc",passw,buff)
	pwinf=open("loginf","w")
	pwinf.close()	
	quit()

def login():
	global user,pw,pwi
	user=input("\n\n\n\t\t\tUserName:")
	pw=getpass.getpass("\n\t\t\tPassword:")
	if(user!=pwi[0] or pw!=pwi[1]):
		print("\n\n\t\t\tInvalid login info. Please try again.\n\n\t\t1.Ok\t2.Shutdown")
		lock=input("\nkey:")
		if(lock=="1"):
			call(["clear"])
			login()
		elif(lock=="2"):
			shutdown()
	call(["clear"])

def clock():
	call(["clear"])
	tym=time.ctime()
	print("Clock:\t\tcheck\te-exit\n\n"+tym)
	key=input("\n\nkey:")
	if(key=="e"):
		call(["clear"])
		pass
	else:
		clock()	

def newfile(i):
	call(["clear"])
	print("Files:\t\ta-back\n")
	print(fisys[i][0])
	name=input("\n\nEnter the name of the file:")
	fisys[i].append(name)
	mema=open("mem","a")
	mema.write("/"+name+"\\\n*EOF*\n")
	mema.close()

def taskbar():
	print("\t\t|f-Files||\t||c-Clock||\t\t\t||s-Shutdown||\n\n")
	
def edit(i,j):
	mem=open("mem")
	memr=mem.readline()
	memor=memr
	while(memr!="/"+fisys[i][j]+"\\\n"):
		memr=mem.readline()
		memor+=memr
	sec=""
	memr=mem.readline()
	while(memr!="*EOF*\n"):
		sec+=memr
		memr=mem.readline()
	memor2=memr
	while(memr!=""):
		memr=mem.readline()
		memor2+=memr
	mem.close()
	bufc=open("buffer","w")
	bufc.write(sec)
	bufc.close()
	main()
	buff
	bufc=open("buffer")
	sec=bufc.read()
	bufc.close()
	mem=open("mem","w")
	mem.write(memor+sec+memor2)
	mem.close()
	bufc=open("buffer","w")
	bufc.close()

def empty(i):
	global new,broken
	while(1):
		call(["clear"])	
		print("Files:\t\te-exit\ta-back\tn-new\nempty\t:(\n")
		key=input("\n\nkey:")
		if(key=="e"):
			broken=1	
			break
		elif(key=="n"):
			newfile(i)
			new=1
			break
		elif(key=="a"):
			break
	

def fileview(i):
	global broken
	k=1
	while(1):
		tf=len(fisys[i])
		call(["clear"])		
		print("Files:\t\ts-down\tw-up\te-exit\ta-back\tn-new\ted-edit\n")
		print(fisys[i][0]+":")
		j=1
		l=k+1
		while(j<k):
			print(fisys[i][j])
			j+=1		
		print(">"+fisys[i][k])
		while(l<tf):
			print(fisys[i][l])
			l+=1			
		key=input("\n\nkey:")
		if(key=="w"):
			if(k>1):
				k-=1
		elif(key=="s"):
			if(k<q-1):
				k+=1
		elif(key=="e"):
			broken=1
			break	
		elif(key=="ed"):
			edit(i,k)
		elif(key=="n"):
			newfile(i)
		elif(key=="a"):
			break

def folderview():
	global broken,new
	p=0
	while(1):
		call(["clear"])
		print("Files:\t\ts-down\tw-up\te-exit\tq-enter\tn-new\n\nroot:\n")
		i=0
		t=p+1
		while(i<p):
			print(fisys[i][0])
			i+=1		
		print(">"+fisys[p][0])
		while(t<q):
			print(fisys[t][0])
			t+=1			
		key=input("\n\nkey:")
		if(key=="w"):
			if(p>0):
				p-=1
		elif(key=="s"):
			if(p<q-1):
				p+=1
		elif(key=="e"):
			break	
		elif(key=="q"):
			if(len(fisys[p])>1):
				fileview(p)
			else:
				empty(p)
				if(new==1):
					new=0
					fileview(p)
			if(broken==1):
				broken=0
				break
			call(["clear"])	
		

with open("filesystem") as fs:
	for i in range(k):
		f=fs.readline()
		print(f)
		if(f[:2]=="fi"):
			files.append(f[3:-1])
		if(f[:2]=="fo"):
			if(par==1):
				files.append(f[3:-1])
				par=0
			else:
				fisys.append(files)
				q+=1
				files=[]
				files.append(f[3:-1])
	fisys.append(files)
	q+=1
	boot()
	login()
	while(1):
		taskbar()
		mose = input("\n\nkey:")
		if(mose=="f"):
			folderview()
		elif(mose=="s"):
			shutdown()
		elif(mose=="c"):
			clock()
		call(["clear"])
