


def my_fun(normal,  *args, **kwrgs):
    print(normal)
    for item in args:
        print(item)
    print("hellow it is a code")
    for key, value in kwrgs.items():
        print(f"{key} is a {value}")

all = ("rahul", "nitin", "ajay", "Guru", "mahesh", "the programmer")
normal = "this is a normal"
kwrgs = {"one":1, "two":2, "three":3}
my_fun(normal, *all, **kwrgs)


