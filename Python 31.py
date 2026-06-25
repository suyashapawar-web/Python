class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket -- Player: {self.__player}, Score: {self.__score}")
    
    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):             # getter - read private data
        return self.__score

    def set_score(self, new_score):    # setter - update private data safely
            if new_score >= 0:
                 self.__score = new_score
                 print (f"Score updated to {self.__score}")
            else:
                 print("Score cannot be negative")


class Football:
    
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football -- Player: {self.__player}, Score: {self.__score}")
    
    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):             # getter - read private data
        return self._score

    def set_score(self, new_score):    # setter - update private data safely
            if new_score >= 0:
                 self.__score = new_score
                 print (f"Score updated to {self.__score}")
            else:
                 print("Score cannot be negative")

# create objects
c = Cricket("Rohit", 85)
f = Football("Arjun", 2)

# Polymorphism - same method different behaviour
print("===== Sports Scorebord =====")
for s in (c, f):
    s.info()
    s.play()
    print()

# Encapsulation - direct changes does NOT work
print("----- Direct Change Attempt -----")
c.__score = 99
print(f"get_score() still shows: {c.get_score()}")


# Setter - only safe way to update
print("\n ---- Updating scores ----")
c.set_score(100)
f.set_score(3)