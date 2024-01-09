class School():
    def __init__(self, name, level, numberOfstudents):
        self.name = name
        self.level = level
        self.numberOfstudents = numberOfstudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number_of_students(self):
        return self.numberOfstudents

    def set_number_of_students(self, new_number):
        self.numberOfstudents = new_number

class PrimarySchool(School):
    def __init__(self, name, pickupPolicy, numberOfstudents):
        super().__init__(name, 'primary', numberOfstudents)
        self.pickupPolicy = pickupPolicy

    def get_pickup_policy(self):
        return self.pickupPolicy

    def __repr__(self):
        parent_repr = super().__repr__()
        return f"{parent_repr} The pickup policy is {self.pickupPolicy}"

class Highschool(School):
  def __init__(self, name, sportsTeams, numberOfstudents):
    super().__init__(name, 'high', numberOfstudents)
    self.sportsTeams = sportsTeams

  def get_sports_teams(self):
    return self.sportsTeams

  def __repr__(self):
    parent_repr = super().__repr__()
    return f"{parent_repr} This is the sports team {self.sportsTeams}"




a = School("school", "high", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_number_of_students(200)
print(a.get_number_of_students())


b = PrimarySchool("school", 300, "Pickup Allowed")
print(b.get_pickup_policy())
print(b)



c = Highschool("school", 500, ["Tennis", "Basketball"])
print(c.get_sports_teams())
print(c)