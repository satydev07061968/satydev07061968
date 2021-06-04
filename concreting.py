class CiviLcalc:
    def __init__ (self, item1, item2):
        self.item1 = item1
        self.item2 = item2

    def calkaro(self):
        
        if(self.item1 == 7.5):
            cM = 1
            sN = 4
            sT = 8            
        else:
            if(self.item1 == 15):
                cM = 1
                sN = 2
                sT = 4
            else:
                if(self.item1 == 20):
                    cM = 1
                    sN = 1.5
                    sT = 3
                else:
                    if(self.item1 == 25):
                        cM = 1
                        sN = 1
                        sT = 2
        totalMix = cM + sN + sT
        drYvol = 1.625 * self.item2
        ceMent = drYvol * cM *1440 /(50 * totalMix)
        finE = drYvol * sN / totalMix
        couRs = drYvol * sT / totalMix            
        print("Cement :=", ceMent," Bags", "\nFine Agge :=", finE," Cum" "\nCours Agge :=", couRs," CuM")

calc1 = CiviLcalc((float(input("Enter Concrete Mix as 7.5,15,20,25"))),(float(input("\nEnter Volume concrete"))))
calc1.calkaro()
