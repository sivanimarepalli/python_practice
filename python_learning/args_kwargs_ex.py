def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')}{kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

shipping_label("Dr.","SPongebob","Squarepants","III", street="ABC STREET",city="UNKNOWN_CITY",state="NOBODY_KNOWS",zip=32541,apt="apt apt",pobox=123)