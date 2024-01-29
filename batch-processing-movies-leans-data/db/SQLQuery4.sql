/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [id]
      ,[name]
      ,[gender]
      ,[popularity]
      ,[profile_path]
      ,[known_for_department]
  FROM [TheMoviesDB].[dbo].[Persons]

  drop table [Genres]
  drop table FactMovies
  drop table MovieCredits
  drop table MovieDetails
  drop table MovieGenres
  drop table Movies_ProductionCompanies
  drop table ProductionsCompanies
  drop table Persons
  

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




  drop table Genres
  drop table FactMovies
  drop table MovieGenres
  drop table MovieCredits
  drop table [Persons]
  drop table MovieDetails
  drop table ProductionsCompanies
  drop table Movies_ProductionCompanies
