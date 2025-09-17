AA = ["AS", "AC","SS","SC"]

PN  = input("enter your genotype: ").upper()
LN = input("enter your genotype: ").upper()

if PN in AA and LN in AA:
    print("Lover's are not compatible")
else:
    print("Lover's are compatible")

