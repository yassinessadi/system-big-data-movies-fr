drop database TheMoviesDB
create database TheMoviesDB
use TheMoviesDB

drop table Genres
drop table FactProductions
drop table MovieGenres
drop table MovieCredits
drop table [Actors]
drop table MovieDetails
drop table ProductionsCompanies
drop table Movies_ProductionCompanies


---------------------
-- genres table
---------------------
Create Table [Genres](
	[id] int PRIMARY KEY,
	[name] varchar(300)
);

----------------------------------
-- Productions Companies table
----------------------------------
Create Table [ProductionsCompanies](
	[id] int PRIMARY KEY
    ,[logo_path] varchar(300)
    ,[name] varchar(100)
    ,[origin_country] varchar(100)
);



--------------------
--[Actors] table----
--------------------
Create Table [Actors](
	--Actors_Key int PRIMARY KEY IDENTITY(1,1),
	id int PRIMARY KEY,
	cast_id int,
	[name] varchar(300),
	[gender] varchar(100),
	[popularity] Float,
	[profile_path] varchar(300),
	[known_for_department] varchar(100),
	--[Effective_Date] varchar(100),
);


-------------------------
--[FactMovies] table-----
-------------------------
Create Table [FactProductions](
	--FactMovies_Key int PRIMARY KEY IDENTITY(1,1),
	[id] int PRIMARY KEY
    ,[budget] FLOAT
    ,[popularity] FLOAT
    ,[revenue] FLOAT
    ,[runtime] FLOAT
    ,[vote_average] FLOAT
    ,[vote_count] FLOAT
    --,[Effective_Date] varchar(150)
);




----------------------------------------------------relationship----------------------------------------------

Create Table [Movies_ProductionCompanies](
	[movie_id] int
   ,[production_companies_id] int,
   PRIMARY KEY ([movie_id], [production_companies_id]),
   FOREIGN KEY ([movie_id]) REFERENCES [FactProductions](id) ON DELETE CASCADE ON UPDATE CASCADE,
   FOREIGN KEY ([production_companies_id]) REFERENCES [ProductionsCompanies](id) ON DELETE CASCADE ON UPDATE CASCADE
);

-------------------------
--[MovieDetails] table---
-------------------------
Create Table MovieDetails(
	[Movies_Key] int PRIMARY KEY IDENTITY(1,1)
	,[id] int
	,[title] varchar(150)
	,[overview] Text
	,[adult] BIT
	,[homepage] varchar(350)
	,[original_language] varchar(4)
	,[original_title] varchar(150)
	,[imdb_id] varchar(100)
	,[poster_path] varchar(250)
	,[release_date] varchar(150)
	,[status] varchar(100)
	,[tagline] varchar(150)
	,[video] BIT
	--,[Effective_Date] varchar(150)
	FOREIGN KEY ([id]) REFERENCES FactProductions([id]) ON DELETE CASCADE ON UPDATE CASCADE
);


-----------------------------------------
--relation between movie and actor
-----------------------------------------

Create Table [MovieCredits](
	[cast_id] int
    ,[movie_id] int
    ,[character] varchar(300)
    ,[credit_id]varchar(250)
    ,[order] int
	PRIMARY KEY ([movie_id], [cast_id]),
    FOREIGN KEY (movie_id) REFERENCES [FactProductions](id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ([cast_id]) REFERENCES [Actors](id) ON DELETE CASCADE ON UPDATE CASCADE
);

--ON DELETE CASCADE ON UPDATE CASCADE


-----------------------------------------
--relation between movie and genres
-----------------------------------------

Create Table [MovieGenres](
	[movie_id] int,
    [genre_id] int
	PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES [FactProductions](id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES [Genres](id) ON DELETE CASCADE ON UPDATE CASCADE
);


--------------------------------------------------------Query--------------------------------------------



---------------------------------------------------------------------------------------------------------
select * from [ProductionsCompanies]
where id = 294



-----------------
select * from [Actors]
where name = 'Anthony Daniels'

-----------------
select * from FactProductions
where id = 49049

select * from genres
select * from MovieDetails
where id = 1228246

update MovieDetails
set release_date = '2014-11-11'
where id = 1228246

-------------------------
select * from MovieCredits
where cast_id =2 and movie_id =11


select * from MovieGenres
------------------------------------------
select * from [Movies_ProductionCompanies]

select * from [MovieGenres]

select count(*) from [Actors]
where id = 130


-----------------------------------------------------Create Indexes-------------------------------------------------

-- Actors table
CREATE INDEX idx_actor_name ON Actors ([name]);
CREATE INDEX idx_actor_gender ON Actors (gender);

-- FactProductions table
CREATE INDEX idx_fact_budget ON FactProductions (budget);
CREATE INDEX idx_fact_popularity ON FactProductions (popularity);
CREATE INDEX idx_fact_revenue ON FactProductions (revenue);
CREATE INDEX idx_fact_runtime ON FactProductions (runtime);
CREATE INDEX idx_fact_vote_average ON FactProductions (vote_average);
CREATE INDEX idx_fact_vote_count ON FactProductions (vote_count);

-- MovieDetails table
CREATE INDEX idx_movie_title ON MovieDetails (title);
CREATE INDEX idx_movie_language ON MovieDetails (original_language);
CREATE INDEX idx_movie_release_date ON MovieDetails (release_date);

-- MovieCredits table
CREATE INDEX idx_movie_credits_character ON MovieCredits ([character]);
CREATE INDEX idx_movie_credits_order ON MovieCredits ([order]);

-- ProductionsCompanies table
CREATE INDEX idx_production_companies_name ON ProductionsCompanies ([name]);

-- Movies_ProductionCompanies table
CREATE INDEX idx_movies_productioncompanies_movie_id ON Movies_ProductionCompanies (movie_id);
CREATE INDEX idx_movies_production_companies_id ON Movies_ProductionCompanies ([production_companies_id]);


-- MovieGenres table
CREATE INDEX idx_moviegenres_genre_id ON MovieGenres (genre_id);



-- MovieGenres table
-- No additional indexes recommended.

-- Movies_ProductionCompanies table
-- No additional indexes recommended.

-- Note: The primary keys and foreign keys already create indexes implicitly.

---------------------------------------------drop indexes (testing)------------------------------------------------------------


-- Actors table
DROP INDEX idx_actor_name ON Actors;
DROP INDEX idx_actor_gender ON Actors;

-- FactProductions table
DROP INDEX idx_fact_budget ON FactProductions;
DROP INDEX idx_fact_popularity ON FactProductions;
DROP INDEX idx_fact_revenue ON FactProductions;
DROP INDEX idx_fact_runtime ON FactProductions;
DROP INDEX idx_fact_vote_average ON FactProductions;
DROP INDEX idx_fact_vote_count ON FactProductions;

-- MovieDetails table
DROP INDEX idx_movie_title ON MovieDetails;
DROP INDEX idx_movie_language ON MovieDetails;
DROP INDEX idx_movie_release_date ON MovieDetails;

-- MovieCredits table
DROP INDEX idx_movie_credits_character ON MovieCredits;
DROP INDEX idx_movie_credits_order ON MovieCredits;

-- MovieGenres table
DROP INDEX idx_moviegenres_genre_id ON MovieGenres;
-- Movies_ProductionCompanies table
DROP INDEX idx_movies_productioncompanies_movie_id ON Movies_ProductionCompanies;
-- ProductionsCompanies table
DROP INDEX idx_production_companies_name ON ProductionsCompanies;


-- Note: The primary keys and foreign keys already create indexes implicitly, so there's no need to drop them explicitly.




---------------------------------------------------------------



SELECT *
FROM FactProductions AS F
INNER JOIN Movies_ProductionCompanies AS MP ON F.id = MP.movie_id
INNER JOIN ProductionsCompanies AS P ON MP.production_companies_id = P.id
INNER JOIN MovieGenres AS MG ON F.id = MG.movie_id
INNER JOIN Genres AS G ON G.id = MG.genre_id
INNER JOIN MovieDetails AS M ON M.id = F.id
INNER JOIN MovieCredits AS MC ON MC.movie_id = F.id
INNER JOIN Actors AS A ON A.id = MC.cast_id
where F.id =11




---------------------------------------views--------------------------------------------------

go
CREATE VIEW FactProductionsMoviesDetailsView AS
SELECT 
    F.id,
    F.budget,
    F.popularity,
    F.revenue,
    F.runtime,
    F.vote_average,
    M.title,
    M.original_language,
    M.release_date,
    M.status
FROM 
    dbo.FactProductions AS F
INNER JOIN 
    MovieDetails AS M ON F.id = M.id;
