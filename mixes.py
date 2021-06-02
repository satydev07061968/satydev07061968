#Program for calculation of building material
#Cement, Fine Aggregate, Course Aggregate out of Concrete qualnity

def mix_des(mix, qty):
    dryVolumn = 1.54 * qty
    print(f"Dry Volumn of {mix} is {dryVolumn}")
    if(mix == "M7.5"): #Calculation for M75 Mix(1:4:8)
        s75 = 1 + 4 + 8
        cement75 =(dryVolumn * 1 * 1440 /(50* s75))
        sand75 = dryVolumn * 4 * 1450 / s75
        stone75 = dryVolumn * 8 * 1500 / s75
        print(f"Quantlty of Cement is {cement75} Bags")
        print(f"Quantlty of Sand is {sand75} CuM.")
        print(f"Quantlty of Stone aggregate is {stone75} Cum.")           
    else:
        if(mix == "M15"):#  Calculation for M15 Mix(1:2:4)
            s15 = 1 + 2 + 4 
            cement15 =(dryVolumn * 1 * 1440 /(50* s15))
            sand15 = dryVolumn * 2 * 1450 / s15
            stone15 = dryVolumn * 4 * 1500 / s15
            print(f"Quantlty of Cement is {cement15} Bags")
            print(f"Quantlty of Sand is {sand15} CuM.")
            print(f"Quantlty of Stone aggregate is {stone15} Cum.")
        else:
            if(mix == "M20"):#  Calculation for M20 Mix(1:1.5:3)
                s20 = 1 + 1.5 + 3
                cement20 =(dryVolumn * 1 * 1440 /(50* s20))
                sand20 = dryVolumn * 1.5 * 1450 / s20
                stone20 = dryVolumn * 3 * 1500 / s20
                print(f"Quantlty of Cement is {cement20} Bags")
                print(f"Quantlty of Sand is {sand20} CuM.")
                print(f"Quantlty of Stone aggregate is {stone20} Cum.")

            else:
                if(mix == "M25"):#  Calculation for M25 Mix(1:1:2)
                    s25 = 1 + 1 + 2
                    cement25 =(dryVolumn * 1 * 1440 /(50* s25))
                    sand25 = dryVolumn * 1 * 1450 / s25
                    stone25 = dryVolumn * 2 * 1500 / s25
                    print(f"Quantlty of Cement is {cement25} Bags")
                    print(f"Quantlty of Sand is {sand25} CuM.")
                    print(f"Quantlty of Stone aggregate is {stone25} Cum.")
                else:
                    print("Value is not in the List")
        

mix_des((input("Enter The Grade of Mix in M7.5/M15/M20/M25 :")) ,(float((input("quantity :")))))
