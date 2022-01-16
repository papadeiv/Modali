import random
import csv
from Scraper import Reddit, Facebook

class DatasetBuilder:

	def __init__(self):
		self.reddit_scraper = Reddit()
		self.facebook_scraper = Facebook()

	def build(self):
		# self.reddit_scraper.scrape()
		self.facebook_scraper.scrape()

	def shuffle():
		# Generate randomly sampled index arrays for the two .csv datasets
		shuffled_reddit_idx = random.sample(range(1, self.reddit_scraper.cardinality), self.reddit_scraper.cardinality)
		shuffled_facebook_idx = random.sample(range(1, self.facebook_scraper.cardinality), self.facebook_scraper.cardinality)

		# Generate json with random samples
		reddit_counter = 0
		facebook_counter = 0
		for idx in range(1, self.reddit_scraper.cardinality + self.facebook_scraper.cardinality):
			if random.random() > 0.5:
				if reddit_counter < self.reddit_scraper.cardinality:
					# Append row from reddit.csv
					reddit_counter += 1
			else:
				if facebook_counter < self.facebook_scraper.cardinality:
					# Append row from facebook.csv
					facebook_counter += 1

				else:
					# Append row from reddit.csv
					reddit_counter += 1

		# Delete the csv files
