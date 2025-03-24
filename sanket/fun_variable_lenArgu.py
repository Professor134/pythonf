def Print_args(*args):
    for arg in args:
        print(arg)

def Print_keyword(**kargs):
    for key in kargs.items():
        print(f"{key}")
Print_args(1,2,3,"hello")
Print_keyword(name="raghav",age="28",city="newysork")
Print_args(4,"aws",65)
Print_keyword(frut="aple",coloer="reeeeeed")
