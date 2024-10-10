-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

-- 1. Insert data into table
CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);


INSERT INTO articles(title, content, createdAt)
VALUES('hello', 'worlds', '2000-01-01')


INSERT INTO articles(title, content, createdAt)
VALUES
  ('hello2', 'worlds2', '2000-01-01'),
  ('hello3', 'worlds3', '2000-01-01'),
  ('hello4', 'worlds4', '2000-01-01')


INSERT INTO articles(title, content, createdAt)
VALUES('hello', 'worlds', DATE())


-- 2. Update data in table
UPDATE articles
SET title = 'updated title'
WHERE id = 1;


UPDATE articles
SET title = 'updated title', content='update content'
WHERE id = 2;


-- 3. Delete data from table
DELETE FROM articles
WHERE id = 1;


DELETE FROM articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);