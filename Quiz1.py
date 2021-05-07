##1.soru
##------------------------------------------------
deger= int(input("Bir sayi giriniz!"))

if deger%2==0:
    
    print("sayi cifttir.")
else:
    print("sayi tektir.")
    
##2.soru
##------------------------------------------------
x=0
while x < 5:
    x=x+1
    deger=int(input("5 adet sayi giriniz!"))
    for i in range(2,deger):
        if deger%i==0:
            print(" {} sayi asal degildir".format(deger))
            
            break
            
        else:
            print(" {} sayi asaldir.".format(deger))
            break
            
##3.soru
##-----------------------------------------------------------
def TemizVeri():
    ilk_string ="Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"

    ilk_string=ilk_string.replace("5",'')
    ilk_string=ilk_string.replace("4","")

    ikinci_string=ikinci_string.replace("9","")
    ikinci_string=ikinci_string.replace("4","")

    ucuncu_string=ucuncu_string.replace("3","")
    ucuncu_string=ucuncu_string.replace("5","")
    ucuncu_string=ucuncu_string.replace("1","")
 
    ilk_string=ilk_string.capitalize()
    ikinci_string=ikinci_string.capitalize()
    ucuncu_string=ucuncu_string.capitalize()

    x = "-"
    Birlesmis_deger=ilk_string+x+ikinci_string+x+ucuncu_string
 
    return Birlesmis_deger
        
TemizVeri()   
