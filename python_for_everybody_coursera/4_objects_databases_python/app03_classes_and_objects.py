# 

class PartyAnimal:
    x = 0

    def party(self):
        self.x += 1
        print('So far',self.x)

an = PartyAnimal()

# i = 0

# # while True:
# #     an.party()
# #     i +=1
# #     if i == 10:
# #         break

print(type(an))
print(dir(an))