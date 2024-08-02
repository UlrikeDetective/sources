# Sentiment Analysis - description see below

install.packages("sentimentr")

library(sentimentr)

# Sample text data

text_data <- c(
  "I love using R for data analysis!",
  "The latest updates are very impressive.",
  "Sometimes, the learning curve can be steep.",
  "Leipzig, London, Lisabon",
  "San Francisco, San Diego, Santa Barbara.",
  "Welcome to California. Let's go surfing."
)

# Perform sentiment analysis
sentiment_scores <- sentiment(text_data)

# View the results
print(sentiment_scores)

# What is Sentiment Analysis?
#   Sentiment analysis is a natural language processing (NLP) technique used to determine the 
# sentiment or emotional tone behind a series of words. It is commonly used to understand opinions, 
# attitudes, and emotions expressed in textual data. Sentiment analysis typically categorizes text into 
# positive, negative, or neutral sentiments, though more complex models can detect a range of emotions or 
# specific sentiments.
# 
# Interpreting the Output
# In the given code snippet, the sentiment function is applied to a list of textual data to perform 
# sentiment analysis. Here's a breakdown of the output:
# 
# r
# Copy code
# element_id sentence_id word_count sentiment
#         <int>       <int>      <int>     <num>
# 1:          1           1          7 0.2834734
# 2:          2           1          6 0.5511352
# 3:          3           1          7 0.2078805
# 4:          4           1          3 0.0000000
# 5:          5           1          6 0.0000000
# 6:          6           1          3 0.2886751
# 7:          6           2          3 0.0000000
# Each row of the output provides information about the sentiment analysis of a sentence from the input 
# text data. Here's what each column represents:
#   
#   element_id: This is the identifier for each piece of text in the original input. Each unique piece 
# of text (e.g., each entry in text_data) is assigned a unique element_id.
# sentence_id: This is the identifier for each sentence within an element. Since some elements may 
# contain multiple sentences, this helps differentiate between them.
# word_count: The number of words in the sentence.
# sentiment: This is the sentiment score assigned to the sentence. Typically, sentiment scores range 
# from -1 to 1, where:
#   Positive values indicate positive sentiment.
# Negative values indicate negative sentiment.
# Values close to 0 indicate neutral sentiment.
# Detailed Analysis of the Output
# Let's look at the specific results:
# 
# Row 1:
# 
# element_id = 1: Corresponds to "I love using R for data analysis!"
# sentence_id = 1: First and only sentence.
# word_count = 7: There are 7 words in this sentence.
# sentiment = 0.2834734: Indicates a positive sentiment.
# Row 2:
# 
# element_id = 2: Corresponds to "The latest updates are very impressive."
# sentence_id = 1: First and only sentence.
# word_count = 6: There are 6 words in this sentence.
# sentiment = 0.5511352: Indicates a positive sentiment.
# Row 3:
# 
# element_id = 3: Corresponds to "Sometimes, the learning curve can be steep."
# sentence_id = 1: First and only sentence.
# word_count = 7: There are 7 words in this sentence.
# sentiment = 0.2078805: Indicates a slightly positive sentiment, acknowledging the difficulty but 
# not in a strongly negative manner.
# Row 4:
# 
# element_id = 4: Corresponds to "Leipzig, London, Lisabon"
# sentence_id = 1: First and only sentence.
# word_count = 3: There are 3 words in this sentence.
# sentiment = 0.0000000: Indicates a neutral sentiment (probably because it’s just a list of city names).
# Row 5:
# 
# element_id = 5: Corresponds to "San Francisco, San Diego, Santa Barbara."
# sentence_id = 1: First and only sentence.
# word_count = 6: There are 6 words in this sentence.
# sentiment = 0.0000000: Indicates a neutral sentiment (again, likely due to being just a list of 
# city names).
# Rows 6 and 7:
# 
# element_id = 6: Corresponds to "Welcome to California. Let's go surfing."
# sentence_id = 1: "Welcome to California."
# word_count = 3: There are 3 words in this sentence.
# sentiment = 0.2886751: Indicates a positive sentiment.
# sentence_id = 2: "Let's go surfing."
# word_count = 3: There are 3 words in this sentence.
# sentiment = 0.0000000: Indicates a neutral sentiment.
# Conclusion
# Sentiment analysis helps in understanding the overall tone of textual data. In this output, positive 
# and neutral sentiments are identified in different sentences. Neutral scores for lists of city names 
# make sense since they don't convey any particular sentiment. Positive scores for phrases like "I love 
# using R for data analysis!" show how the sentiment analysis captures positive feelings effectively.
