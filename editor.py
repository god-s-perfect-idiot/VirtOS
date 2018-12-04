from subprocess import call
from pynput.keyboard import Key, Listener

chars=["'!'","'@'","'#'","'$'","'%'","'^'","'&'","'*'","'('","')'","'q'","'w'","'e'","'r'","'t'","'y'","'u'","'i'","'o'","'p'","'a'","'s'","'d'","'f'","'g'","'h'","'j'","'k'","'l'","'z'","'x'","'c'","'v'","'b'","'n'","'m'","'1'","'2'","'3'","'4'","'5'","'6'","'7'","'8'","'9'","'0'","'Q'","'W'","'E'","'R'","'T'","'Y'","'U'","'I'","'O'","'P'","'A'","'S'","'D'","'F'","'G'","'H'","'J'","'K'","'L'","'Z'","'C'","'V'","'B'","'N'","'M'","'<'","'>'","'?'","','","'.'","'/'","':'","';'","'\''","'\"'","'-'","'_'","'='","'+'"]
char=""
buf=""
esc=0
lef=0
rig=0
bsp=0
fail=0
broken=0
bug=0
ren=0
	
def on_release(key):
		global esc,rig,lef,bsp,char,ren
		k=format(key)
		print(k)
		if key == Key.esc:
			esc=1	
		elif key == Key.right:
			rig=1
		elif key == Key.left:
			lef=1
		elif key == Key.backspace:
			bsp=1
		elif key == Key.space:
			char=" "
		elif key == Key.tab:
			char="\t"
		elif key == Key.enter and bug==1:
			char="\n"
		elif key == Key.ctrl:
			ren=1
		else:
			if(format(key) in chars):		
				char=format(key)[1:-1]
		return False
	

def main():
	global chars,char,buf,esc,lef,rig,bsp,fail,broken,bug,ren	
	call(["clear"])	
	r=open("buffer")
	cont=r.read()
	ptr=0
	skip=0
	while(1):
		with Listener(on_release=on_release) as listener:
			if(buf!=""):
				ptr+=1
				buf=""							
			call(["clear"])				
			k=len(cont)		
			print("\tText Editor:\n\nFile:"+":\n"+cont[:ptr-skip]+"|"+cont[ptr-skip:]+"\n\nESC: save and exit\t CTRL: exit")		
			if(ptr>0) and skip==1:
				ptr-=1		
			skip=0
			listener.join()
			if(bug==0):
				bug=1		
			if(esc==1):
				esc=0
				break
			if(rig==1):
				if(ptr<k-1):
					ptr+=1
				rig=0
			if(lef==1):
				if(ptr>0):
					ptr-=1
				lef=0
			if(bsp==1):
				if(skip<k and ptr-skip>0):
					skip+=1
				bsp=0
			if(char!=""):
				buf+=char
				char=""
			if(ren==1):			
				break
			cont=cont[:ptr-skip]+buf+cont[ptr:]
	call(["clear"])
	if(ren!=1):
		if(cont[-1:]!="\n"):
			cont+="\n"
		w=open("buffer","w")
		w.write(cont)
		r.close()
		w.close()	
	else:
		ren=0
