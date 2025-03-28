from Person import Person

class GeneralWorker(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, job: str, salary: int, given_worker_id: int = None):
        super().__init__(name, surname, age, gender)
        self.__job = job
        self.__salary = salary
        self.__role = "General Worker"
        self.__worker_id = self.__random_worker_id(given_worker_id)
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
    
    def __random_worker_id(self, given_worker_id):
        #it generates random worker number within the given range
        if given_worker_id == None:
            from random import randint
            #if it is a new worker added by app, then the default worker id is None, but
            #if different then it is already in the database, that is why we pass the saved worker number
            from Database import Database
            #loading all employees
            data_read = Database.load_employees()
            all_employees = data_read["General Workers"]
            while True:
                #generating the number
                new_generated_id = randint(0, 999)
                if all_employees:
                    for employee in all_employees:
                        # if someone has generated number then it redo the loop
                        if employee.id == new_generated_id:
                            continue
                        #if nobody has generated number then it returns it as new worker id
                    return new_generated_id
                else:
                    return new_generated_id
        else:
            #if worker is already in database then pass his worker number
            return given_worker_id

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

    @property
    def role(self):
        return self.__role
    
    @property
    def id(self):
        return self.__worker_id

    # Overloading
    def __eq__(self, value):
        return self.__salary == value
    
    def __lt__(self, value):
        return self.__salary < value
    
    def __gt__(self, value):
        return self.__salary > value