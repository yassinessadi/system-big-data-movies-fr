use TheMoviesDB


-- Stored Procedure for Relationship
Go
CREATE PROCEDURE dbo.CheckForeignKeys
    @Success BIT OUTPUT,
    @ErrorMessage NVARCHAR(MAX) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    SET @Success = 1;
    SET @ErrorMessage = '';

    -- Check foreign key relationships
    IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE CONSTRAINT_TYPE = 'FOREIGN KEY' AND TABLE_SCHEMA = 'TheMoviesDB')
    BEGIN
        SET @Success = 0;
        SET @ErrorMessage = 'One or more foreign key relationships do not exist.';
        RETURN;
    END
END;

-- Stored Procedure for Null Values:
Go
CREATE PROCEDURE dbo.CheckNullValues
    @Success BIT OUTPUT,
    @ErrorMessage NVARCHAR(MAX) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    SET @Success = 1;
    SET @ErrorMessage = '';

    -- Check null values in specific columns
    IF EXISTS (
        SELECT 1
        FROM FactProductions
        WHERE popularity IS NULL OR budget IS NULL
    )
    BEGIN
        SET @Success = 0;
        SET @ErrorMessage = 'One or more columns in FactProductions have NULL values.';
        RETURN;
    END
END;



-- Stored Procedure for Table Existence:
Go
CREATE PROCEDURE dbo.CheckTableExistence
    @Success BIT OUTPUT,
    @ErrorMessage NVARCHAR(MAX) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    SET @Success = 1;
    SET @ErrorMessage = '';

    -- Check if tables exist
    IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'TheMoviesDB')
    BEGIN
        SET @Success = 0;
        SET @ErrorMessage = 'One or more tables do not exist.';
        RETURN;
    END
END;

-- Execution Script:
Go
DECLARE @Success BIT, @ErrorMessage NVARCHAR(MAX);
EXEC dbo.CheckForeignKeys @Success OUTPUT, @ErrorMessage OUTPUT;
PRINT 'CheckForeignKeys Result: ' + CASE WHEN @Success = 1 THEN 'Passed' ELSE 'Failed' END;
IF @ErrorMessage != ''
    PRINT 'Error Message: ' + @ErrorMessage;

Go
DECLARE @Success BIT, @ErrorMessage NVARCHAR(MAX);
EXEC dbo.CheckNullValues @Success OUTPUT, @ErrorMessage OUTPUT;
PRINT 'CheckNullValues Result: ' + CASE WHEN @Success = 1 THEN 'Passed' ELSE 'Failed' END;
IF @ErrorMessage != ''
    PRINT 'Error Message: ' + @ErrorMessage;

Go
DECLARE @Success BIT, @ErrorMessage NVARCHAR(MAX);
EXEC dbo.CheckTableExistence @Success OUTPUT, @ErrorMessage OUTPUT;
PRINT 'CheckTableExistence Result: ' + CASE WHEN @Success = 1 THEN 'Passed' ELSE 'Failed' END;
IF @ErrorMessage != ''
    PRINT 'Error Message: ' + @ErrorMessage;



-- Drop
DROP PROCEDURE IF EXISTS dbo.CheckTableExistence;
DROP PROCEDURE IF EXISTS dbo.CheckNullValues;
DROP PROCEDURE IF EXISTS dbo.CheckForeignKeys;
