-- Initiatives table
CREATE TABLE initiatives (
    initiative_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    original_title TEXT NULL,
    description TEXT NULL,
    original_description TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    vector_data JSON NULL,
    upvotes INT NULL,
    downvotes INT NULL,
    initiative_url TEXT
);