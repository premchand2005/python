sub1 = int(input("Enter the first sunject :"))
sub2 = int(input("Enter the second sunject :"))
sub3 = int(input("Enter the third sunject :"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail. beacause you have obtained below 33 marks in any one subject or more")
    
    
elif (sub1+sub2+sub3)/3 <40:
    print("you are fail.because total percentage less than 40")
else:
    print("congratulation you can be passed!")
 