print("******************************** WELCOME TO ALDRIN MOBILE STORE*********************************************")
mobiles={"motorla":18000,"oppo":10000,"vivo":34000,"redmi":9999,"oneplus":16100}

your_mobile=input("enter your mobile:")

if your_mobile in mobiles:
    print("your mobile is available")

    book=input("do you want this mobile type yes:")
    if book=="yes":
        brand=input("enter the mobile brand name:")
        full_name=input("enter your full name:")
        phone_num=int(input("enter your mobile number:"))
        quantity=int(input(f"enter the how many {your_mobile} you want:"))

        if your_mobile=="motrola":
            one_motorla=18000
            total=one_motorla*quantity
            print(f"tour mobile bill is{total}")
        if your_mobile=="oppo":
            one_oppo=10000
            total=one_oppo*quantity
            print(f"tour mobile bill is{total}")
        if your_mobile=="vivo":
            one_vivo=34000
            total=one_vivo*quantity
            print(f"tour mobile bill is{total}")
        if your_mobile=="redmi":
            one_redmi=9999
            total=one_redmi*quantity
            print(f"tour mobile bill is{total}")
        if your_mobile=="oneplus":
            one_oneplus=16100
            total=one_oneplus*quantity
            print(f"tour mobile bill is{total}")


        total_amount=mobiles [your_mobile] * quantity
        print(total_amount)

        #gst calculation
        gst_rate=12
        gst_amount=(total_amount*gst_rate)/100
        final_price=(gst_amount)
        print(final_price)
        print(f"hello{full_name} your mobile {your_mobile} is booked your total amount is withgst is {total_amount} then we calculate the gst 12%. then your final price is{final_price}")
        
else:
    print("mobile is not available")

    
     
 


