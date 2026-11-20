```sql
-- Create the players table
CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the RLS policy to restrict access to players table
CREATE POLICY player_profile_policy ON players FOR SELECT USING (username = current_user);
```

### Explanation:
1. **players Table**: This table stores information about each player, including their unique identifier (`id`), username, and email.
2. **RLS Policy**: The `player_profile_policy` is created to restrict access to the `players` table. It ensures that only the user whose `username` matches the current user can select from this table.

### Schema Compatibility:
- This migration assumes a PostgreSQL database with Supabase installed.
- The `CREATE POLICY` statement is used to define row-level security policies in PostgreSQL, which are similar to RLS in other databases like SQL Server or Oracle.