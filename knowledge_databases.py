from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rate):
	article_object = Knowledge(
		name = name,
		topic = topic,
		rate = rate)
	session.add(article_object)
	session.commit()
add_article("Nathan", "music", 8)




def query_all_articles():
	articles = session.query(
      Knowledge).all()
	return articles


print(query_all_articles())

def query_article_by_topic(name):
	ARTICLES = session.query(
       Knowledge).filter_by(
       name="Nathan_Goshen").first()
	return ARTICLES


print(query_article_by_topic("Nathan_Goshen"))


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
