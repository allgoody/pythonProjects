# Objects are created , used and discarded
# method - moment of creation - constructor
# method - moment of destruction - destructor

class PartyAnimal:
    x = 0

    def __init__(self):
        print('im constracted')

    def party(self):
        self.x +=1
        print('so far',self.x)

    def __del__(self):
        print('im deconstracted', self.x)

an = PartyAnimal()
an.party()
an.party()
# an = 42
# print('an contains', an)