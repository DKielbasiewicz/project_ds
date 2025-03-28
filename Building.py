class Building:
    def __init__(self, name: str, address: str, short_name: str, courses: list, workers: list):
        self.name = name # name of the building
        self._address = address # address of the building
        self.short_name = short_name # short name of the building eg. Comenius = com :)
        self.__courses = courses # list of course objects
        self.__workers = workers # list of general worker objects

    def __str__(self):
        return f"Name: {self.name}, Address: {self._address}, Short name: {self.short_name}, Courses: {self.__courses}, Workers: {self.__workers}"
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def workers(self):
        return self.__workers
    
    @workers.setter
    def workers(self, workers):
        self.__workers = workers

    @property
    def courses(self):
        return self.__courses
    
    @courses.setter
    def courses(self, courses):
        self.__courses = courses

    @property
    def short_name(self):
        return self.__short_name
    
    @short_name.setter
    def short_name(self, short_name):
        self.__short_name = short_name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name