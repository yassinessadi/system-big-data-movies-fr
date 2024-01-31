use TheMoviesDB

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

-- run the PROCEDURE
Go
DECLARE @Success BIT, @ErrorMessage NVARCHAR(MAX);
EXEC dbo.CheckNullValues @Success OUTPUT, @ErrorMessage OUTPUT;
PRINT 'CheckNullValues Result: ' + CASE WHEN @Success = 1 THEN 'Passed' ELSE 'Failed' END;
IF @ErrorMessage != ''
    PRINT 'Error Message: ' + @ErrorMessage;








-- Drop
DROP PROCEDURE IF EXISTS dbo.CheckNullValues;


-- test on of these column
select * 
from FactProductions
where id =11

update FactProductions
set popularity = 79.865
where id = 11