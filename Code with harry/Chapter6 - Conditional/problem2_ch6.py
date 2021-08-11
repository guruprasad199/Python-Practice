# write a program to check the student is pass or fail it requres 40% marks to pass and at least 33% marks in each subject the subject is 3 

sub1 = int(input("Enter the 1st subject marks : "))
sub2 = int(input("Enter the 2nd subject marks : "))
sub3 = int(input("Enter the 3rd subject marks : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("oops you are failed due to less marks in any of subject")
elif(sub1+sub2+sub3) / 3 < 40:
    print("you are failed percentage low")
else:
    print("Congratulation!! You are passed")
