class multipleFunctions():
#OddEven:
    def OddEven():
            lv_num = int(input("Enter a number:"))
            if((lv_num%2)==0):
                print(lv_num, "is Even Number")
            else:
                print(lv_num, "is Odd number")
    
    
    
    
#BMI Index check
    def bmi():
            bmi = int(input("Enter the BMI Index:"))
            if(bmi<18.5):
                print("Underweight")
                message="underweight"
            elif(bmi<24.9):
                print("Normal")
                message="Normal"
            elif(bmi<29.9):
                print("Overweight")
                message="Overweight"
            else:
                print("Very Overweight")    
                message="Very Overweight"
                return message
#AI Categories:
    def Subfields():
            print("AI Categories:")
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")  
            message = "Happy Hope AI Learning"
            return message
#elegibility of marriage for male and female
    def Elegible():
            lv_gen = input("Your Gender:").upper()
            lv_age = int(input("Your Age:"))
            if ((lv_gen=='MALE') and (lv_age>21)):
                  message = "ELIGIBLE"
            elif ((lv_gen=='FEMALE') and (lv_age>18)): 
                  message = "ELIGIBLE"
            else:
                  message = "NOT ELIGIBLE"
                
            return message

#    calculate the percentage of your 10th mark
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        
        total = sub1+sub2+sub3+sub4+sub5
        percent = (total / 500) * 100
        
        print("Subject1= ",sub1)
        print("Subject2= ",sub2)
        print("Subject3= ",sub3)
        print("Subject4= ",sub4)
        print("Subject5= ",sub5)
        print("Total : ",total)

        message = f"Percentage : {percent:.2f}%"
        return message

#print area and perimeter of triangle     
    def triangle():
        print("Enter Values to Calculate Area of Triangle")
        height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        
        area_triangle = (height*Breadth)/2
        
        print("Enter Values to Calculate Perimeter of Triangle")
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))        
        Breadth = ' '
        Breadth = int(input("Breadth:"))
        
        peri_triangle = height1+height2+Breadth
        
        print("Output for the Area of Triangle")
        print("Height:",height)
        print("Breadth:",Breadth)
        print("Area of Triangle:",area_triangle)
        print("Output for the Perimeter of Triangle")
        print("Height1:",height1)
        print("Height2:",height2)
        print("Breadth:",Breadth)
        print("Perimeter of Triangle:",peri_triangle)

        message = f"Area of Triangle: {area_triangle}\nPerimeter of Triangle: {peri_triangle}"
        
        return message
    
            