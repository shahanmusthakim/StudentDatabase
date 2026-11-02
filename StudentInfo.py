class StudentData:
    student_list=[]
    @classmethod
    def add_student(self,student):
        self.student_list.append(student)
    
        

class Student():
    def __init__(self,student_id, name, department):
        self.__student_id=student_id
        self.__name=name
        self.__department=department
        self.__is_enrolled=False
        StudentData.add_student(self)
    
    def get_student_id(self):
        return self.__student_id  
    
    def enroll_student(self):
        if  self.__is_enrolled==False:
            self.__is_enrolled=True
            print("Student enrolled successfully.")  
        else:
            print("Student is Already enrolled.")
             
    def drop_student(self):
            if  self.__is_enrolled==True:
                self.__is_enrolled=False
                print("Student dropped successfully.")  
            else:
                print("Student is Not enrolled.") 
                
    def view_student_info(self):
        
        print(f'Student_id: {self.__student_id}')
        print(f'Name: {self.__name}')
        print(f'Department: {self.__department}')
        if self.__is_enrolled:
            print("Status: Enrolled\n")
        else:
            print("Status: Not Enrolled\n")
        

student1=Student(101, "Shahan", "Software Engineering")
student2=Student(102, "Rahim", "Computer Science")
student3=Student(103, "Karim", "Electrical Engineering")
        
    
    
    
    
while True:
    print("\n------------------------- Student Management System -------------------------\n")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit\n\n")
    option=int(input("\nEnter your option: "))
    if option==1:
        if not StudentData.student_list:
             print("No students found.\n")
        else:
            print("\n------------------STUDENT INFORMATION------------------\n")
            for st in StudentData.student_list:
                st.view_student_info()
            
        
                 
    elif option==2:
        id=int(input("\nEnter the Student ID: "))
        flag=False
        for st in StudentData.student_list:
            if st.get_student_id()==id:
                st.enroll_student()
                flag=True
        if flag==False:
            print("Invalid Student ID")
    elif option==3:
        id=int(input("\nEnter the Student ID: "))
        flag=False
        for st in StudentData.student_list:
            if st.get_student_id()==id:
                st.drop_student()
                flag=True
        if flag==False:
            print("Invalid Student ID")
    elif option==4:
        print("\nProgram Exit.")
        break
    else:
        print("Wrong Choice. Enter any valid option.")