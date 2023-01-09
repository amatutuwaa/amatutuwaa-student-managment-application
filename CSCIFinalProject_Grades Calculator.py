
class GradeCalculator:
    pass 
class Course:

    def __init__ (self, name, code, assignment_types):
        """ initializing the Course aspect of the grade calculator;
            takes the name of the course in question and the course code.
        """
        self.name = name 
        self.code = code
        self.assignment_types = assignment_types

    # Calculating the final weighted grade
    def calculate_final_grade (self):
        
        weighted_averages = []
        for assignment_type in self.assignment_types:
            weighted_averages.append(assignment_type.weighted_average())
        
        total_weighted_averages = sum (weighted_averages)
        final_weighted_grade = total_weighted_averages * 100
        # print (weighted_averages)
        return final_weighted_grade

class Assignment:

    def __init__ (self, name, score):
        """ initializing the Assignment aspect of the grade calculator;
            takes in the name of the assignment and the score received on that assignment.
        """

        self.name = name
        if type(score) == str:
            score = score.split ("/")
            score = float (score[0])/float(score[1])

        self.score = score 

class AssignmentType:

    def __init__ (self, name,  quantity, weight, assignments):
        """ initializing the Assignment Type aspect of the grade calculator; 
            takes in the quantity of assignments per each assignment type;
            takes in the weighting per each assignment type.
        """
        self.name = name
        self.quantity = quantity
        self.weighting = weight
        self.assignments = assignments

    # Calculating the Average

    def get_average (self):
        assignment_scores = self.assignments
        assignment_score_list = [a.score for a in assignment_scores]
        total_sum = sum (assignment_score_list)
        total_sum = float (total_sum)
        average = total_sum/ len(assignment_score_list)
        # print (assignment_score_list)
        return average

    def weighted_average (self): 
        average = self.get_average()
        weighted_average = average * self.weighting/100
        return weighted_average

class Calculator:

    # def __init__ (self,course):
    #     """ initializing the Calculator aspect of the grade calculator;
    #     takes in the assignment scores and returns the final weigted grade.
    #     """
    #     self.course = course

    @staticmethod
    def input_course ():
        name = input ("Enter the course name: ")
        code = input ("Enter the course code: ")
        course = Course (name, code, [])
        assignment_types_names = input ("Enter the various assignment types.(Seperate with commas): ")
        weighting = input ("Enter the various weightings per each assignment type in the same order as the assignment type. (Seperate with commas | Input integers only | Do not add percentage symbol): ")
     
     
        weighting_list = weighting.split (",")
        weighting_list = [float(x) for x in weighting_list]
        
        total = sum(weighting_list)

        while total != 100:
            print ("Unfortunately, your list of weightings do not add up to 100 | Try Again!")
            weighting = input ("Enter the various weightings per each assignment type in the same order as the assignment type. (Seperate with commas | Input integers only | Do not add percentage symbol): ")
            weighting_list = weighting.split (",")
            weighting_list = [float(x) for x in weighting_list]
            total = sum(weighting_list)

        quantity = input ("Enter the quantity of assignments per each assignment type in the order of the assignment type. (Seperate with commas | Input integers only: ")
        assignment_types_names_list = assignment_types_names.split(",")
        quantity_list = quantity.split(",")
        quantity_list = [float(x) for x in quantity_list]


        for x in range (len(assignment_types_names_list)):
            a = AssignmentType (assignment_types_names_list[x], quantity_list[x], weighting_list[x], [])
            course.assignment_types.append(a)

        for x in range (len(course.assignment_types)):
            assignment_score = input ("Enter the grades received in fractions (score/total) for " + assignment_types_names_list[x] + ". (Seperate with commas): ")
            assignment_score_list = assignment_score.split (",")

            for i in range (len(assignment_score_list)):
                score = Assignment (course.assignment_types[x].name + str (i), assignment_score_list[i])
                course.assignment_types[x].assignments.append(score)
        return course
    @staticmethod
    def main ():
        
        print (" ")
        print (" ")
        print ("Welcome to the Grade Calculator portion of the Student Management App. In this part of the Application you will input your course name and code, the different assignment types in the course and their weightings, the number of assignments per each assignment type and the grades you have made so far under each assignment type. The application will then apply this data and return to you your weighted final grade. Note: The returned results are as accurate as the data you input, meaning, to ensure you'll be receiving an accurate final grade double check your data and make sure you input everything in the exact way the prompt asks. Also, if the semester is not over the returned 'final' grade only considers the assignments done so far, meaning, your final grade can either increase or decrease at the end of the semester depending on how well you do on the remaining assignments.")
        print (" ")
        print (" ")
        courses = []
        course = Calculator.input_course()
        courses.append(course)
        done = False
        while not done:
            print ("Option 1: Add a new Course")
            print ("Option 2: Calculate Final Grades")

            option = input (" Choose an Option (1 or 2). | Or type \"done\" to exit: ")
            if option == str (1):
                course =  Calculator.input_course()
                courses.append(course)

            if option == str (2):
                for course in courses:
                    final_weighted_grade = course.calculate_final_grade()
                    print (" ")

                    print (" Your final grade for " + course.name + "(" + course.code + ") is " + str (final_weighted_grade))
            
            if option == "done":
                done = True 
        
        
        


    
    
     







if __name__ == "__main__":
    Calculator.main()