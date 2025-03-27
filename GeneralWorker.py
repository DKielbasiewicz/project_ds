from Person import Person

class GeneralWorker(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, job: str, salary: int):
        super().__init__(name, surname, age, gender)
        self.__job = job
        self.__salary = salary

    def __str__(self):
        return f"{self.name} {self.surname} is a {self.__job} and has {self.__salary} salary"

    def __validate_gender(self, gender):
        if gender.lower() == "f" or gender.lower() == "female":
            return "female"
        if gender.lower() == "m" or gender.lower() == "male":
            return "male"
        # we do not discriminate !!!
        if gender.lower() == "n" or gender.lower() == "none" or gender.lower() == "other":
            return "none"
        raise NameError("Invalid gender: The Person has to be either Male (M) or Female (F) or other (N)")

    @property
    def job(self):
        return self.__job
    
    @job.setter
    def job(self, job):
        self.__job = job

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    # Overloading
    def __eq__(self, value):
        return self.__salary == value
    
    def __lt__(self, value):
        return self.__salary < value
    
    def __gt__(self, value):
        return self.__salary > value