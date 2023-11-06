-- Create a trigger that resets the attribute 'valid_email'
-- only when the email has been changed.
CREATE TRIGGER reset_valid_email
    BEFORE UPDATE ON users
    FOR EACH ROW
    SET NEW.valid_email = IF(
        OLD.email!=NEW.email,
        0,
        IF(
            OLD.valid_email!=NEW.valid_email,
            NEW.valid_email,
            OLD.valid_email
        )
    )
;
