from user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []     # will contain objects
        self.users_collection = []      # will contain objects

    @staticmethod
    def find_user_in_collection(username, collection):
        for obj in collection:
            if obj.name == username:
                return obj

    @staticmethod
    def find_movie_by_username(movies_collection, username):
        for movie in movies_collection:
            if movie.owner.name == username:
                return movie

    @staticmethod
    def find_movie_title_in_collection(movie_title, collection):
        for movie in collection:
            if movie.title == movie_title:
                return movie

    def register_user(self, username, age):
        user = User(username, age)
        if self.find_user_in_collection(user.name, self.users_collection):
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{user.name} registered successfully."

    def upload_movie(self, username, movie):
        found_user = self.find_user_in_collection(username, self.users_collection)

        if username != found_user.name:
            raise Exception("This user does not exist!")
        if movie.owner != found_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        found_user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        found_movie = self.find_movie_by_username(self.movies_collection, username)

        if found_movie not in self.movies_collection:
            raise Exception(f"The movie {found_movie.title} is not uploaded!")
        if movie.owner != found_movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for k, v in kwargs.items():
            if k == 'title':
                found_movie.title = v
            elif k == 'year':
                found_movie.year = v
            elif k == 'age_restriction':
                found_movie.age_restriction = v

        return f"{username} successfully edited {found_movie.title} movie."

    @staticmethod
    def compare_two_movies(movie1, movie2):
        if movie1.title == movie2.title:
            return movie1

    def delete_movie(self, username, movie):
        user = self.find_user_in_collection(username, self.users_collection)

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        movie_found_in_user_collection = self.find_movie_title_in_collection(movie.title, user.movies_owned)
        movie_found_in_app = self.find_movie_by_username(self.movies_collection, user.name)

        user.movies_owned.remove(movie_found_in_user_collection)
        self.movies_collection.remove(movie_found_in_app)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        found_user = self.find_user_in_collection(username, self.users_collection)

        if found_user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in found_user.movies_owned:
            raise Exception(f"{found_user.name} already liked the movie {movie.title}!")

        movie.likes += 1
        found_user.movies_liked.append(movie)
        return f"{found_user.name} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        user = self.find_user_in_collection(username, self.users_collection)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        # TODO rework this

        if not self.movies_collection:
            return "No movies found."

        ll = [x.year for x in self.movies_collection]
        for el in ll:
            dd = {}
            if el not in dd:
                dd[el] = 1
            dd[el] += 1

            for i in dd.values():
                if i >= 2:
                    return [x.details() for x in sorted(self.movies_collection, key=lambda x: x.title)]
                return [x.details() for x in sorted(self.movies_collection, key=lambda x: x.year, reverse=True)]

    def __str__(self):
        if not self.users_collection:
            return f"All users: No users."
        result = f"All users: {', '.join([x.name for x in self.users_collection])}\n"
        if not self.movies_collection:
            return f"All movies: No movies."
        result += f"All movies: {', '.join([x.title for x in self.movies_collection])}"

        return result
