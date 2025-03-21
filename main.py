"""
General structure of the UniTrack application
"""

class UniTrack:
  def __init__(self):
    pass

class UniTrackApp:
  def __init__(self):
    self.__uniTrack = UniTrack()

  def help(self):
    print("List of commands:")
    print("[1] - Add course")

  def add_course(self, name, ec):
    name = input("Enter name of the course: ")
    ec = input("Number of credits: ")
    pass

  def run(self):
    while True:
      self.help()
      print("\n")
      command = input("Enter command: ")
      if command == "1":
        self.help()
      else:
        print("Invalid command")