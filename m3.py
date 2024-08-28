import socket
import mysql.connector
import cv2

class login1:
    def __init__(self) -> None:
        self.name=" "
        self.password=" "
        self.email=" "
        self.number=" "

    def signup(self,c1):
        self.name=input("enter your name :- ")
        print("     ")
        c=0
        while c!=3:
            p=0
            e=0
            ph=0
            self.password=input("enter your passward :- ")
            print("     ")
            self.email=input("enter your email :- ")
            print("     ")
            self.number=input("enter your phone number :- ")
            print("     ")
            l, u, d = 0, 0, 0
            if len(self.password) >= 8:
                for i in self.password:
                # counting lowercase alphabets
                    if (i.islower()):
                        l+=1
                # counting uppercase alphabets
                    if (i.isupper()):
                        u+=1
                # counting digits
                    if (i.isdigit()):
                        d+=1
                    if l>=1 and u>=1 and d>=1 :
                        p=1
            if len(self.number)==10 and self.number.isalnum():
                ph=1
            if  self.email.find("@"):
                e=1
            if p==1 and ph==1 and e==1:
                print("your all details are fine ")       
                print("  ")
                break
            if p!=1:
                print("rewrite your password")
            if ph!=1:
                print("rewrite your phone number") 
            if e!=1:
                print("rewrite your email")               
            c=c+1 
            print(" ")      

        if c!=3:
            cur=c1.cursor()
            s="insert into user_info(name,password,email,p_number) values(%s,%s,%s,%s)"
            v=(self.name,self.password,self.email,self.number)
            cur.execute(s,v)
            print("thanks for signing in into whatsapp chat box")
            print("     ")
            a.sever1(self.name)

    def login(self,c1):
        phone1=input("enter your number :- ")
        print("     ")
        password1=input("enter your password :- ")
        cur=c1.cursor()
        print("     ")
        cur.execute("select p_number from user_info")
        p1=cur.fetchall()
        cur.execute("select password from user_info")
        p2=cur.fetchall()
        cur.execute("select name from user_info")
        p3=cur.fetchall()
        k=0
        for i,j in zip(p1,p2):
            if (i[0]==phone1 and j[0]==password1):
                n1=p3[k]
                n=n1[0]
                a.sever1(n)
            k = k+1    

    def sever1(self,n):
        
        while True:
            print("     ")
            print("     ")
            p=int(input("enter 1 to receive msg \nenter 2 to export your chat \nenter 3 to clear chat \nenter 4 to receive img \nenter 5 to send msg \nenter 6 to send img \nenter 7 to exit : "))
            if p==1:
                self.chat(n)
            elif p==2:
                self.export(n)
            elif p==3:
                self.clear(n)
            elif p==4:
                self.img(n)
            elif p==5:
                self.chat1(n)    
            elif p==6:
                self.image1(n)                
            elif p==7:
                break
            else:
                print("enter valid choice")

    def chat(self,n):
        print("     ")
        print("     ")
        try: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            # print ("Socket successfully created")
        except socket.error as err: 
            # print ("socket creation failed with error ")
            pass
        s.bind(("localhost",9998))
        s.listen(2)
        c,addr=s.accept()
        str1=n
        f=open(str1,"a+")
        c.send(str1.encode("utf-8"))
        fn=c.recv(1024).decode('utf-8')
        while True: 
            data = c.recv(1024).decode('utf-8')
            f.writelines("recv from "+fn+" :- ")
            f.writelines(data)
            f.write("\n")
            if data.lower()=='bye':
                print("recv from "+fn+" :- "+data)
                break
            else:
                print("recv from "+fn+" :- "+data)
                print("     ")
                msg=input("enter msg to "+fn+" :- ")  
                print("     ")
                f.writelines("send to "+fn+" :- ")
                f.writelines(msg)
                f.write("\n")
                if msg.lower()=="bye":
                    c.send(msg.encode('UTF-8'))
                    break
                else:
                    c.send(msg.encode('UTF-8'))
        f.close()
        c.close()

    def export(self,n):
        print("     ")
        str1=n
        f=open(str1,"r")
        data=f.read()
        print(data)
        if data==" ":
            print("sorry you dont have any chat")
            
        f.close()

    def clear(self,n):
        print("     ")
        str1=n
        f=open(str1,"w")
        f.write(" ")
        print("your chat is deleted")
        f.close()

    def img(self,n):
        print("     ")
        print("     ")
        try: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            # print ("Socket successfully created")
        except socket.error as err: 
            # print ("socket creation failed with error ")
            pass
        s.bind(("localhost",9998))
        s.listen(2)
        c,addr=s.accept()
        str1=n
        c.send(str1.encode("utf-8"))
        fn=c.recv(1024).decode('utf-8')
        ifile=open("i1.png",'wb')
        image_c=c.recv(2048)
        while image_c:
            ifile.write(image_c)
            image_c=c.recv(2048)
        ifile.close()
        g="i1.png"
        src=cv2.imread(g)
        window_name = 'image'
        print("image from "+fn+" :- ")
        cv2.imshow(window_name, src)
        cv2.waitKey(0)
        c.close()

    def chat1(self,n):
        print("     ")
        print("     ")
        str1=n
        f=open(str1,"a+")
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(("localhost", 9998))
        fn=c.recv(1024).decode('utf-8')
        c.send(str1.encode("utf-8"))
        message = input("Enter msg to "+fn+" : ")
        while True:
            f.writelines("send to "+fn+" :- ")
            f.writelines(message)
            f.write("\n")
            if message.lower()=="bye":
                c.send(message.encode('utf-8'))
                break
            else:
                c.send(message.encode('utf-8'))
                data = c.recv(1024).decode('utf-8')
                f.writelines("recv from "+fn+" :- ")
                f.writelines(data)
                f.write("\n")  
                if data.lower()=='bye':
                    print("Received from "+fn+" : " + data)
                    break
                else:
                    print("     ")
                    print("Received from "+fn+" : " + data)
                    print("     ")
                    message = input("Enter msg to "+fn+" : ")     
        f.close()

    def image1(self,n):
        print("     ")
        print("     ")
        str1=n
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(("localhost", 9998))
        fn=c.recv(1024).decode('utf-8')
        c.send(str1.encode("utf-8"))
        print("image to "+fn+" :- ")
        pi=input("enter image file name")
        ifile=open(pi,"rb")
        image_c=ifile.read(2048)
        while image_c:
            c.send(image_c)
            image_c=ifile.read(2048)     
        ifile.close()
        c.close()    
    


con = mysql.connector.connect( host="localhost", user="root", password="", database="chatbox") 

print("welcome to the chatbox")
print("     ")
ch=int(input("enter 1 if you new to the chatbox :\nenter 2 if you already use the chatbox :\n"))
a= login1()
if ch==1:
    a.signup(con)
elif ch==2:
    a.login(con)
else:
    print("enter valid  option ")
con.commit()    