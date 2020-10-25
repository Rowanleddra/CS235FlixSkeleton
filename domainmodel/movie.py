##from domainmodel.genre import Genre
##from domainmodel.actor import Actor
##from domainmodel.director import Director
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


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):

        return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):

        return self.__director_full_name < other.__director_full_name

    def __hash__(self):

        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        return self.__genre_name == other.__genre_name

    def __lt__(self, other):

        return self.__genre_name < other.__genre_name

    def __hash__(self):

        return hash(self.__genre_name)


class Movie:
    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year < 1900 or release_year is None or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

        self.description = None
        self.director = None
        self.actors = []
        self.genres = []
        self.runtime_minutes = None

    @property
    def title(self) -> str:
        return self.__title

    def set_description(self, descript):
        self.description = descript

    def get_description(self):
        return self.description

    def set_director(self, drectr):
        self.director = drectr

    def get_director(self):
        return self.director

    def set_actor(self, actrs):
        self.actors = actrs

    def get_actors(self):
        return self.actors

    def set_genres(self, gnr):
        self.genres += gnr

    def get_genres(self):
        return self.genres

    def runtime_min(self, runtime):
        if runtime < 0 or  runtime is not int:
            myerror = ValueError("ValueError exception thrown")
            raise myerror
        else:
            self.runtime_minutes = runtime

    def get_runtime_minutes(self):
        return self.runtime_min

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if self.__title == other.__title is True:
            return self.__release_year == other.__release_year
        else:
            return False

    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        else:
            return self.__title < other.__title

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def add_actor(self, actr):
        if actr not in self.actors:
            self.actors.append(actr)

    def remove_actor(self, actr):
        if actr in self.actors:
            self.actors.remove(actr)

    def add_genre(self, gnr):
        if gnr not in self.genres:
            self.genres.append(gnr)

    def remove_genre(self, gnr):
        if gnr in self.genres:
            self.genres.remove(gnr)


