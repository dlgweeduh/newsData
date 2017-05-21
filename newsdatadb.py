# Database code for the DB Forum, full solution!

import psycopg2, bleach

DBNAME = "news"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select title, name from articles join authors on article.author = authors.id;")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):
  """select * from authors;"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()

