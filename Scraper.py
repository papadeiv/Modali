import csv

#################################################################################################
#################################################################################################
##                                                                                             ##
##                               Implementing a class for a Reddit                             ##
##                                     scraper using praw                                      ##
##                                                                                             ##
#################################################################################################
#################################################################################################

import praw

class Reddit():

  def __init__(self):

    self.source = [['Universitaly', 'flair:"Ingegneria" OR flair:"Magistrale"', 750],
                   ['italy', 'flair:"Discussione" OR flair:"Notizie" OR flair:"Economia & Politica" OR flair:"No Flair" OR flair:"OffTopic"', 500],
                   ['Italia', 'flair:"Diciamocelo" OR flair:"Politica" OR flair:"Notizie"', 250],
                   ['ITAGLIA', 'flair:"ITAGLIANITÀ!!!" OR flair:"Barbari civilizzati" OR flair:"CERCHIONANISMO" OR flair:"Giovine virgulto!" OR flair:"ITAGLIA CAPVT MVNDI" OR flair:"Barbari da civilizzare" OR flair:"Cartellino ROSSO!"', 500]]

    self.reddit = praw.Reddit(client_id = 'p0qRwExdj0hl_I5WCPhyRg',
                  client_secret = 'CdRVMfPGBhjCKZdAixEEr5hXXrVdLg',
                  # username = '', unnecessary as it is a read-only app
                  # password = '', as per above
                  user_agent = 'reddit-UniSTEM-scraper')

    self.cardinality = 0

  def scrape(self):
    for subreddit in self.source:
      threads = self.reddit.subreddit(subreddit[0]).search(subreddit[1], sort='hot', limit=subreddit[2])

      fields = ["Text", "Sentiment"]
      dataset = './' + subreddit[0] + '.csv'

      with open(dataset, 'w+', newline='') as csvf:
        writer = csv.writer(csvf, delimiter=",")
        writer.writerow(fields)
        
        sub_idx = 0
        for submission in threads:
          if not submission.stickied:
            submission.comments.replace_more(limit=0)
            sub_idx += 1
            print('Subreddit: r/{}\n> Thread n.{} ({}): {}'.format(subreddit[0], sub_idx, submission.link_flair_text, submission.title))
            print(50*'-')

            for comment in submission.comments.list():
              print('  Parent ID = {}\n  Comment ID = {}\n  "{}"\n'.format(comment.parent(), comment.id, comment.body))
              entry_list = [str(comment.body), 0]
              writer.writerow(entry_list)
              self.cardinality += 1
              

            print(50*'-')
            print('\n\n')

#################################################################################################
#################################################################################################
##                                                                                             ##
##                             Implementing a class for a Facebook                             ##
##                                scraper using facebook-scraper                               ##
##                                                                                             ##
#################################################################################################
#################################################################################################

from facebook_scraper import get_posts

class Facebook():

  def __init__(self):

    self.source = [[None, '1650533981900983', 'IngegeriadelSuicidio'],
                   ['liberonews', None, 'Libero']]
    
    self.cardinality = 0

  def scrape(self):

    for page in self.source:
      fields = ["Text", "Sentiment"]
      dataset = './' + page[2] + '.csv'
      with open(dataset, 'w+', newline='') as csvf:
        writer = csv.writer(csvf, delimiter=",")
        writer.writerow(fields)

        for post in get_posts(account=page[0], group=page[1], pages=10, cookies="from_browser", options={"comments": True}):
          
          for comment in list(post['comments_full']):
            print(comment.get('comment_text'))
            entry_list = [str(comment.get('comment_text')), 0]
            writer.writerow(entry_list)
            self.cardinality += 1
            
            for reply in list(comment['replies']):
              print(reply.get('comment_text'))
              entry_list = [str(comment.get('comment_text')), 0]
              writer.writerow(entry_list)
              self.cardinality += 1



    