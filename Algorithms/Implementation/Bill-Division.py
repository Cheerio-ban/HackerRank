def bonAppetit(bill, k, b):
    actual = sum(bill)
    if k >= 0:
        charged = actual - bill[k]
    else:
        charged = actual
    anna = charged // 2
    if anna == b:
        print("Bon Appetit")
    else:
        print(bill[k] // 2)
    
