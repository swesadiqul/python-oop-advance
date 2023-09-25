class HighSchool:
    def basic_education(self):
        return "Completed high school education."

class Bachelor(HighSchool):
    def undergraduate_studies(self):
        return "Completed Bachelor's degree."

class Master(Bachelor):
    def postgraduate_studies(self):
        return "Completed Master's degree."

class Doctorate(Master):
    def research(self):
        return "Completed Doctorate degree."

student = Doctorate()
print(student.basic_education())         # Output: Completed high school education.
print(student.undergraduate_studies())   # Output: Completed Bachelor's degree.
print(student.postgraduate_studies())    # Output: Completed Master's degree.
print(student.research())               # Output: Completed Doctorate degree.
