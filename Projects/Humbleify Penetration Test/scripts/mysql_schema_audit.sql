-- mysql_schema_audit.sql
-- Schema-only MySQL audit queries (AUTHORIZED environments only).
-- Safe by default: focuses on schema metadata and aggregate counts.
--
-- Run examples:
--   mysql -u <user> -p -h <host> <db> < scripts/mysql_schema_audit.sql
--
-- Notes:
-- - Do NOT run against systems without explicit permission.
-- - Avoid SELECTing raw sensitive rows; prefer COUNTs and information_schema.

-- 0) Server context
SELECT VERSION() AS mysql_version;

-- 1) List databases (visibility depends on privileges)
SHOW DATABASES;

-- 2) If you know the application DB, switch to it:
-- USE <humbleify_db>;

-- 3) Tables and schema metadata
SHOW TABLES;

-- 4) Identify potentially sensitive columns by name (adjust patterns as needed)
SELECT
  TABLE_NAME,
  COLUMN_NAME,
  DATA_TYPE
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND (
    LOWER(COLUMN_NAME) LIKE '%ssn%' OR
    LOWER(COLUMN_NAME) LIKE '%credit%' OR
    LOWER(COLUMN_NAME) LIKE '%card%' OR
    LOWER(COLUMN_NAME) LIKE '%password%' OR
    LOWER(COLUMN_NAME) LIKE '%salt%'
  )
ORDER BY TABLE_NAME, COLUMN_NAME;

-- 5) Safe volume metrics (no row content)
-- Uncomment/adjust for known table names:
-- SELECT COUNT(*) AS customer_count FROM customers;
-- SELECT COUNT(*) AS employee_count  FROM employees;

-- 6) Privilege review (requires SHOW GRANTS privilege)
-- SHOW GRANTS;
