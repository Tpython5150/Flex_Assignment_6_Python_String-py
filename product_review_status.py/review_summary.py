'''

Review Summary 

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.
review = ["The performance of this product is excellent. Highly recommended!"]

'''

review = ["The performance of this product is excellent. Highly recommended!"]
asterisks = "..."

def create_summary(review):
    if len(review) <= 30:
      return review
    else:
        summary = review[:30].rsplit(' ', 1)
        summary.append(asterisks)
        summary = " ".join(summary)
        #summary = review[:30]output The preformance of this produc need to >rsplit(seperator, maxsplit)
        return(summary)
for review in review:
  summary = create_summary(review)
  print(summary)
    
