'''
Product Review Analysis 1 Task 2 Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.
python positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


'''
python_reviews = [ "This product is really good. I'm impressed with its quality.",
                  "The performance of this product is excellent. Highly recommended!",
                  "I had a bad experience with this product. It didn't meet my expectations.",
                  "It was a poor quality product. Wouldn't recommend it to anyone.",
                  "The product was average. Nothing extraordinary about it." ]

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def word_count(reviews):
  
  for review in reviews:
    each_review = review.lower()
    positive_count = 0
    negative_count = 0
    
    for word in python_positive_words:
      if word in each_review:
        positive_count += 1
        
    for word in negative_words:
      if word in each_review:
        negative_count += 1
        
    #prints out each review , then give the positve_word count, then the negative_count       
    print(f"Review: {review}")
    print(f"Postive word count: {positive_count}, Negative word count: {negative_count}")

word_count(python_reviews)    