from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from time import sleep
f=True
#while f:
lis1=[]
b1=int(input("num:"))
htmll=urlopen("https://coinmarketcap.com/")
bss=BeautifulSoup(htmll.read(),"lxml")
findd=bss.find_all("div",{"class":"sc-a093f09c-0 gPTgRa"})
for d in range(0,b1):
#print(find[i])
        
        #print(findd[d].get_text())
        pricee=findd[d].get_text().replace("$", "").replace(" ", "").replace("\n","").replace(",","")
        price_noo=float(pricee)
        lis1.append(price_noo)
print(lis1)


lis=[]
f=0.0
b=int(input("num:"))
if(b<20):
        print("please input more than 20")
html=urlopen("https://coinranking.com")
bs=BeautifulSoup(html.read(),"lxml")
find=bs.find_all("div",{"class":"valuta"})
for i in range(0,b,2):
#print(find[i])
#print(find[i].get_text())
        price=find[i].get_text().replace('$', '').replace(' ', '').replace('\n','').replace(',','')
        price_no=float(price)
        lis.append(price_no)

#print(lis[0])
if(lis[0]>lis1[0]):
        print("BTC in https://coinmarketcap.com/ is lower than than BTC in https://coinranking.com")
elif(lis1[0]>lis[0]):
        print("BTC in (https://coinranking.com) is lower than than BTC in (https://coinmarketcap.com/)")
if(lis1[1]>lis[1]):
        print("ETH in (https://coinranking.com) is lower than than ETH in (https://coinmarketcap.com/)")
elif(lis[1]>lis1[1]):
        print("ETH in https://coinmarketcap.com/ is lower than than ETH in https://coinranking.com")
if(lis1[2]>lis[2]):
        print("TETHER in (https://coinranking.com) is lower than than TETHER in (https://coinmarketcap.com/)")
elif(lis[2]>lis1[2]):
        print("TETHER in https://coinmarketcap.com/ is lower than than TETHER in https://coinranking.com")
if(lis[3]>lis1[3]):
        print("BNB in https://coinmarketcap.com/ is lower than than BNB in https://coinranking.com")
elif(lis1[3]>lis[3]):
        print("BNB in (https://coinranking.com) is lower than than BNB in (https://coinmarketcap.com/)")
if(lis[4]>lis1[4]):
        print("SOL in https://coinmarketcap.com/ is lower than than SOL in https://coinranking.com")
elif(lis1[4]>lis[4]):
        print("SOL in (https://coinranking.com) is lower than than SOL in (https://coinmarketcap.com/)")
if(lis[5]>lis1[5]):
        print("stETH in https://coinmarketcap.com/ is lower than than stETH in https://coinranking.com")
elif(lis1[5]>lis[5]):
        print("stETH in (https://coinranking.com) is lower than than stETH in (https://coinmarketcap.com/)")
if(lis[6]>lis1[6]):
        print("USDC in https://coinmarketcap.com/ is lower than than USDC in https://coinranking.com")
elif(lis1[6]>lis[6]):
        print("USDC in (https://coinranking.com) is lower than than USDC in (https://coinmarketcap.com/)")
if(lis[7]>lis1[7]):
        print("XRP in https://coinmarketcap.com/ is lower than than XRP in https://coinranking.com")
elif(lis1[7]>lis[7]):
        print("XRP in (https://coinranking.com) is lower than than XRP in (https://coinmarketcap.com/)")
if(lis[8]>lis1[8]):
        print("DOGE in https://coinmarketcap.com/ is lower than than DOGE in https://coinranking.com")
elif(lis1[8]>lis[8]):
        print("DOGE in (https://coinranking.com) is lower than than DOGE in (https://coinmarketcap.com/)")
if(lis[9]>lis1[9]):
        print("TON in https://coinmarketcap.com/ is lower than than TON in https://coinranking.com")
elif(lis1[9]>lis[9]):
        print("TON in (https://coinranking.com) is lower than than TON in (https://coinmarketcap.com/)")


        

        

#lis.append(price_no)
#print(lis)

        
