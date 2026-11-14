from django.shortcuts import render

def Churn_Rate_area(request):
    TOTAL_CUSTOMER_LOST = float(request.POST.get('total', '0'))
    INITIAL_CUSTOMERS = float(request.POST.get('initial', '0'))

    area =(TOTAL_CUSTOMER_LOST/INITIAL_CUSTOMERS) * 100 if request.method == 'POST' else 0
    print("TOTAL CUSTOMER LOST =", TOTAL_CUSTOMER_LOST)
    print("INITIAL CUSTOMERS =", INITIAL_CUSTOMERS)
    print("CHURN RATE =", area)

    return render(
        request,
        'myapp/custm.html',
        {'TOTAL_CUSTOMER_LOST': TOTAL_CUSTOMER_LOST, 'INITIAL_CUSTOMERS':  INITIAL_CUSTOMERS, 'area': area }
    )