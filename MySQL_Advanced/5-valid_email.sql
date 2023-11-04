-- Create a trigger that resets the attribute 'valid_email'
-- only when the email has been changed.
CREATE TRIGGER reset_valid_email
    AFTER UPDATE ON users
    FOR EACH ROW
    IF(NEW.email!=OLD.email) THEN
        UPDATE users SET valid_email=DEFAULT
        WHERE email=NEW.email
;
