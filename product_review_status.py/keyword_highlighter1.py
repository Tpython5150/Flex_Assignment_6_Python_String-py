'''
Product Reveiw Analysis 1 Task 1

Keyword Highlighter

Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

python reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

'''
python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "It was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]


 
 # had to add "It was a" before the word Poor. Since it was the beginning of a sentence it wouldnt captailize the whole word.  Also, tried entering it as poor in lowercase and then it worked.
keywords = ['good', 'excellent', 'bad', 'poor', 'average']

def keyword_highlights(reviews):
  
    for review in reviews:
      each_review = review.lower()
      #This part of code should have put the lowercase
    
      for keyword in keywords:
        if keyword in each_review:
          highlighted_review = review.replace(keyword, keyword.upper())
          #This part of code should have out the keywords in uppercase
          print(highlighted_review)
          break
        
keyword_highlights(python_reviews)