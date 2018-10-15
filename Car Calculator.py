#Ask User to input car price
carPrice=float(input("Enter Car Price:"))

#Ask User to input years or number of months(26 months or 36 month))
months=input("Enter months(24 or 36?):")
months24="24"
months36="36"

#Add condition statements so that user can only use 24 or 36 months
if months==months24:
    downPayment= float(carPrice) * float(0.10)
    initialBalance=(float(carPrice)-float(downPayment)) + ((float(carPrice)-float(downPayment)) * float(0.06) * (int(months)/12))
    monthlyPayment= float(initialBalance)/int(months)
    endingBalance=initialBalance-monthlyPayment
    #Display Headers
    print("%5s"%("Months"),"%10s"%("Year"),"%20s"%("Starting Balance"),"%20s"%("Installments"),"%20s"%("Ending Balance"),"%30s"%("Remaining Installments"))
    #Print table
    monthsCounter=1
    years=1
    endingBalance=initialBalance-monthlyPayment
    remainingInstallments=int(months)-1
    for months in range(1,int(months)+1):
        print("%5s"%months,"%10s"%(years),"%20s"%(initialBalance),"%20s"%(monthlyPayment),"%20s"%(endingBalance),"%30s"%(remainingInstallments))
        months=months+1
        if months<=12:
            years=1
        elif months<=24:
            years=2
        elif months<=36:
            years=3
        initialBalance=initialBalance-monthlyPayment
        endingBalance=endingBalance-monthlyPayment
        remainingInstallments=int(remainingInstallments)-1
elif months==months36:
    downPayment= float(carPrice) * float(0.10)
    initialBalance=(float(carPrice)-float(downPayment)) + ((float(carPrice)-float(downPayment)) * float(0.06) * (int(months)/12))
    monthlyPayment= float(initialBalance)/int(months)
    endingBalance=initialBalance-monthlyPayment
    #Display Headers
    print("%5s"%("Months"),"%10s"%("Year"),"%20s"%("Starting Balance"),"%20s"%("Installments"),"%20s"%("Ending Balance"),"%30s"%("Remaining Installments"))
    #Print table
    monthsCounter=1
    years=1
    endingBalance=initialBalance-monthlyPayment
    remainingInstallments=int(months)-1
    for months in range(1,int(months)+1):
        print("%5s"%months,"%10s"%(years),"%20s"%(initialBalance),"%20s"%(monthlyPayment),"%20s"%(endingBalance),"%30s"%(remainingInstallments))
        months=months+1
        if months<=12:
            years=1
        elif months<=24:
            years=2
        elif months<=36:
            years=3
        initialBalance=initialBalance-monthlyPayment
        endingBalance=endingBalance-monthlyPayment
        remainingInstallments=int(remainingInstallments)-1
else:
    print("Error:")
    print("Please enter 24 or 36 months.")




