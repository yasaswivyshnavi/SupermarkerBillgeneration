from datetime import datetime
print("\t******************************|t")
Name=input("Enter Custmor Name : ")


lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 110/kg
Paneer  Rs 150/kg
Maggi   RS 100/each packet
Boost   Rs 150/each
Colgate Rs 100/each
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]


#rates per items
items={"Rice":20,
       "Sugar":30,
       "Salt":20,
       "Oil":110,
       "Panner":150,
       "Maggi":100,
       "Boost":150,
       "Colgate":100
       }
option=int(input("for list of items 'press 1' :"))
if option==1:
    print(lists)
for i in range(1,len(items)):
    inp=int(input("If you want Buy 'press 1' for Exit 'press 2' :"))
    if inp==2:
        break
    if inp==1:
        item=input("Enter your item: ")
        quantity=int(input("Enter your quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry,you enter item is not available")
    else:
        print("you entered wrong number")
    inp=input("Can I bill for your item Yes/No :")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","KMPS Mart",25*"=")
            print(25*" ","Repalle") 
            print("Name:",Name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ","Items",6*" ","Quantity",3*" ","Price")
            for i in range(len(pricelist)):
                print(i,10*" ",ilist[i],8*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:","Rs",totalprice)
            print("GST amount",50*" ","Rs",gst)
            print(75*"-")
            print(50*" ","FinalAmount:","Rs",finalamount)
            print(75*"-")
            print(25*" ","Thanks for visiting")
            print(75*"-")
                