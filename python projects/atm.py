print("****** NAME--->HEMACHMADRAN R ******")
print("****** COLLAGE---->GLOBAL INSTITUE OF ENGINEERING AND TECHNOLOGY******")
print("****** BATCH-74 ******")
print("****** MOBILE NO--->6374944765********")
print("****** LOCATION-MALVISHARAM ******")
print("****** DISTRICT-RANIPET*******)
print("********** WELCOME TO CITY UNION BANK OF INDIA **********")
def language():
             language=input("enter your language: ")

             if language=="english":

                 print(f"your selected language is {language}")
             elif language=="tamil":  

                 print(f"your selected language is {language}")
             else:

                 print("invalid answer")
language()
def main():
    p=int(input("enter your 4digit : "))
    m=30000
    if p==1234:

             print("1-savings")
             print("2-current") 
             ac=input("enter your account type: ")   

             if ac=="1":

                 print("1-withdraw")
                 print("2-balance enquiry")
                 print("3-fast cash") 

                 c=int(input("please enter your transaction: "))

                 if (c==1):

                    w=int(input("enter withdraw amount: "))
                    if m>w :

                        print("------Loading------")
                        print("=------Please wait some moment-----")
                        print("please take your case")

                    else:
                        print("insuffiency amount")    
            
                
             elif(c==2):
                 print("your avaliable balance:",m)    

             elif(c==3):
                print("1--->6000")  
                print("2--->12000")
                print("3--->16000")
                print("4--->23000")
                print("5--->26000")
                print("6--->29000")
                 
                f=int(input("Enter fast cash option: "))

                if(f==1 and m>6000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 6000")

                elif(f==2 and m>12000):

                    print("------Loading------")
                    print("------wait for some moment")
                    print (f"Take your cash 12000")

                elif(f==3 and m>16000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 16000")
 
                elif(f==4 and m>23000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 23000")

                elif(f==5 and m>26000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 26000")

                elif(f==6 and m>29000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 29000")
             if ac=="2":
                print("1-withdraw")
                print("2-balance enquiry")
                print("3-fast cash") 
                c=int(input("please enter your transaction: "))


                w=int(input("enter withdraw amount: "))
                if m>w:

                    print("------Loadind------")
                    print("------Please wait some moment------")
                    print(" Please take yor case")

                else:
                    print("invalid amount")

             elif(c==2):
                 print("your avaliable balance:",m)    

             elif(c==3):
                print("1--->6000")  
                print("2--->12000")
                print("3--->16000")
                print("4--->23000")
                print("5--->26000")
                print("6--->29000")

                f=int(input("Enter fast cash option: "))

                if(f==1 and m>6000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 6000")

                elif(f==2 and m>12000):

                    print("------Loading------")
                    print("------wait for some moment")
                    print (f"Take your cash 12000")

                elif(f==3 and m>16000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 16000")

                elif(f==4 and m>23000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 23000")

                elif(f==5 and m>26000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 26000")

                elif(f==6 and m>29000):

                    print("------Loading------")
                    print("------wait for some moment------")
                    print (f"Take your cash 29000")   
                else:
                    print("INVALID INPUT")   


                    print("THANK YOU FOR USING CITY UNION ATM")                
                               
main() 
            
        
