# Inheritancance is used to take on the properties of an exisiting class
# The inherited class is known as Base Class while the class who inherits is known as derived class
class User:
  def sign_in(self):
    print("Logged In")
class Wizard(User):
  def __init__(self,name,power):
    self.name=name
    self.power=power
  def attack(self):
    print(f"Attacking with the power of {self.power}")
class Archar(Wizard):
  def __init__(self,name,num_arrows):
    self.name=name
    self.num_arrows=num_arrows
  def attack(self):
    print(f'Player Name is {self.name}')
    print(f"Attacking with left arrows {self.num_arrows}")

 
wizard1=Archar("Talha",100)
wizard1.attack()