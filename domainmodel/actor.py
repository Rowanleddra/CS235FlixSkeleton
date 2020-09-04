from typing import List, Any


class Actor:

    def __init__(self, actor_full_name: str, colleagues=None):

        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        if colleagues is None:
            self.colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):

        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):

        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):

        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague.__actor_full_name not in self.colleagues:
            self.colleagues.append(colleague.__actor_full_name)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.__actor_full_name in self.colleagues:
            return True
        else:
            return False


actor1 = Actor("Angelina Jolie")
actor2 = Actor("Brad Pitt")
actor1.add_actor_colleague(actor2)
print(actor1.check_if_this_actor_worked_with(actor2))