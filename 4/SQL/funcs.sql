CREATE OR REPLACE FUNCTION reverse(INPUT int)
    RETURNS int
    LANGUAGE plpgsql
    IMMUTABLE STRICT
    AS $$
DECLARE
    RESULT text = '';
    i INT;
BEGIN
    FOR i IN 1..LENGTH(INPUT::text)
    LOOP
        RESULT = substr(INPUT::text, i, 1) || RESULT;
    END LOOP;
    RETURN RESULT::int;
END
$$;