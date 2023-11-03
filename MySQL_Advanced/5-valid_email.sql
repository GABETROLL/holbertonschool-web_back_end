-- Create a trigger that resets the attribute 'valid_email'
-- only when the email has been changed.
CREATE TRIGGER IF NOT EXISTS reset_valid_email
    AFTER INSERT ON users
    