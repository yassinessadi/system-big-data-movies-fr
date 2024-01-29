/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (10000) [Actors_Key]
	  ,[id]
	  ,[cast_id]	
      ,[name]
      ,[gender]
      ,[popularity]
      ,[profile_path]
      ,[known_for_department]
      ,[Effective_Date]
  FROM [TheMoviesDB].[dbo].[Actors]

  SELECT TOP (1000) [id]
      ,[name]
  FROM [TheMoviesDB].[dbo].[Genres]
  --------------------
  --Genre table-------
  --------------------
   Create Table [Genres](
	[id] int PRIMARY KEY,
	[name] varchar(300)
  );
    --------------------
	--[Actors] table----
	--------------------
  Create Table [Actors](
	Actors_Key int PRIMARY KEY IDENTITY(1,1),
	id int,
	cast_id int,
	[name] varchar(300),
	[gender] varchar(100),
	[popularity] Float,
	[profile_path] varchar(300),
	[known_for_department] varchar(100),
	[Effective_Date] varchar(100),
  );
	-------------------------
	--[FactMovies] table-----
	-------------------------
  Create Table [FactMovies](
	   FactMovies_Key int PRIMARY KEY IDENTITY(1,1)
	  ,[id] int
      ,[budget] FLOAT
      ,[popularity] FLOAT
      ,[revenue] FLOAT
      ,[runtime] FLOAT
      ,[vote_average] FLOAT
      ,[vote_count] FLOAT
      ,[Effective_Date] varchar(150)
 );

 	-------------------------
	--[MovieDetails] table-----
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
		  ,[Effective_Date] varchar(150)
	  );


 select * from MovieDetails


  drop table Genres
  drop table FactMovies
  drop table MovieGenres
  drop table MovieCredits
  drop table [Actors]
  drop table MovieDetails
  drop table ProductionsCompanies
  drop table Movies_ProductionCompanies
