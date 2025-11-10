import sys
#checks if correct number of arguments a
if len(sys.argy)==3:
        script_name - sys,argv[0]
        name = sys.argv[1]
        rollno=sys.argv[2]
        print("user provided input vlaues:")
else:
   script_name=sys.argv[0]
   name="chitra"
   rollno = "086"
   print("no input given - using default values:")
print("script name:",script_name)
print("stuednt name:",name)
print("roll number:",rollno)
 
