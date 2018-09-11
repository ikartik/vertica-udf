
# Execute these SQLs as admin user to register your UDF on Vertica.

CREATE OR REPLACE LIBRARY pylib AS '/path/to/your/roundoff.py' LANGUAGE 'Python';

CREATE OR REPLACE FUNCTION roundoff AS LANGUAGE 'Python' NAME 'roundoff_factory' LIBRARY pylib fenced;

