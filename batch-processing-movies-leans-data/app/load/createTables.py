# from sqlalchemy import Column, Integer, Float, BigInteger, String, Text, Boolean, ForeignKey,DateTime
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# # FactMovies contains measure values about movies for BI purposes.
# class FactMovies(Base):
#     __tablename__ = "FactMovies"
    
#     id = Column(Integer, primary_key=True)
#     budget = Column(Float)
#     popularity = Column(Float)
#     revenue = Column(Float)
#     runtime = Column(Float)
#     vote_average = Column(Float)
#     vote_count = Column(BigInteger)

#     def __repr__(self) -> str:
#         return f"FactMovies(id={self.id!r}, budget={self.budget!r}, popularity={self.popularity!r}, revenue={self.revenue!r}, runtime={self.runtime!r}, vote_average={self.vote_average!r}, vote_count={self.vote_count!r})"

# # MovieDetails contains info about the movie.
# class MovieDetails(Base):
#     __tablename__ = "MovieDetails"
    
#     id = Column(Integer, primary_key=True)
#     title = Column(String(250))
#     overview = Column(Text)
#     adult = Column(Boolean)
#     homepage = Column(String(200))
#     original_language = Column(String(3))
#     original_title = Column(String(200))
#     imdb_id = Column(String(100))
#     poster_path = Column(String(200))
#     release_date = Column(String(100))
#     status = Column(String(30))
#     tagline = Column(String(250))
#     video = Column(Boolean)

#     def __repr__(self) -> str:
#         return f"MovieDetails(id={self.id!r}, title={self.title!r})"

# # Genres (['action','drama' ...]) Table
# class Genres(Base):
#     __tablename__ = "Genres"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))

#     def __repr__(self) -> str:
#         return f"Genres(id={self.id!r}, name={self.name!r})"

# # MovieGenres (relation between movie table and genre table) Table
# class MovieGenres(Base):
#     __tablename__ = "MovieGenres"
#     genre_id = Column(Integer, primary_key=True)
#     movie_id = Column(Integer, primary_key=True)

#     def __repr__(self) -> str:
#         return f"MovieGenres(movie_id={self.movie_id!r}, genre_id={self.genre_id!r})"

# # Productions Companies (company info) tables
# class ProductionsCompanies(Base):
#     __tablename__ = "ProductionsCompanies"
#     id = Column(Integer, primary_key=True)
#     logo_path = Column(String(500))
#     name = Column(String(200))
#     origin_country = Column(String(3))

#     def __repr__(self) -> str:
#         return f"ProductionsCompanies(id={self.id!r}, name={self.name!r}"

# # Movies_ProductionCompanies (relation between movie table and ProductionCompanies table) Table
# class Movies_ProductionCompanies(Base):
#     __tablename__ = "Movies_ProductionCompanies"
#     movie_id = Column(Integer, primary_key=True)
#     production_companies_id = Column(Integer, primary_key=True)

#     def __repr__(self) -> str:
#         return f"Movies_ProductionCompanies(movie_id={self.movie_id!r}, production_companies_id={self.production_companies_id!r})"

# # Actors (Actors info) tables
# class Actors(Base):
#     __tablename__ = "Actors"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))
#     gender = Column(Integer)
#     popularity = Column(Float)
#     profile_path = Column(String(255))
#     known_for_department = Column(String(255))
#     Effective_Date = Column(DateTime)

#     def __repr__(self) -> str:
#         return f"Person(id={self.id!r}, name={self.name!r}, gender={self.gender!r}, popularity={self.popularity!r}, popularity={self.known_for_department!r}"

# # Movie Credits (Actors info [the role played in the movie]) relation between movie and Person tables
# class MovieCredits(Base):
#     __tablename__ = "MovieCredits"
    
#     cast_id = Column(Integer, primary_key=True)
#     movie_id = Column(Integer, primary_key=True)
#     credit_id = Column(String(255))
#     character = Column(Integer)
#     order = Column(Integer)

#     def __repr__(self) -> str:
#         return f"MovieCredits(cast_id={self.cast_id!r}, movie_id={self.movie_id!r}, character={self.character!r}, credit_id={self.credit_id!r},  order={self.order!r})"
