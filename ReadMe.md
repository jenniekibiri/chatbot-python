# Making a chat bot🤖🤖🤖🤖

## natural language processing
This is the field that focus on the interaction between human language and computers 
# How questions are processed 
1. converted the entire text to uppercase or lowercase.
2. tokenization
  converts the normal text strings into list of tokens .words
3. Removing Noise
this includes spaces,punctuation etc
4. removing stop words.
stop words are questions not necessary for processing 
5. stemming 
process of reducing the inflected word to their base words 
eg an word with ing it converted to the original word
lemmatization
ensures that the base word after stemming make sense
7. bag of words model:
transforms the word into a meaning array 
bag of words is a representation of the text that describes the  occurrence of words within a document
# The first steps includes opening and reading the files
install the nltk -natural language processing tool kit is first installed.
# punkt sentence tokenizer

used for tokenizing the text into  list of sentences 
converts the words into lists of sentences
# Wordnet
lexical database for english language  its where nltk finds the meaning of the words
sent_tokenize used to convert to list of sentences
word_tokenize converts into list of words 
# Preprocessing.
Stemms the token and looks up the words in the wordnet and stores it the a variable.
Defination of the functions tokenizing and for removing the punctuations from the user entered data.

# Set greetings
responds to the user and  does a short introduction about what the chat bot is for and how to leave the chat
# Vectorizer
* uses sklearn ifidvectorizer. 
* converts the words into vector.
* cosinesilarity check similarity between the user query and our database.
* Defination of the response function that gives the user response based on the question.
* The function append the user tokens and vectorizes the words and compares the user questions and the databases for a match.
* Flatten converts either to row matrix or column matrix.
* if no match then it will give a message no info found.
* Each match is given an id.
* set flag to true.
* The function turns the flag to false if the user ends the session by ``bye``.

Did I mention we need to create a .txt file and store the data where our bot will get the answers from?.
Nope🤗🤗🤗 I didnt.
* so get data from wikipedia and paste it in the ``.txt`` file and the bot by use of nltk  will process the data and give us the answers...
* How cool.. clone the repo and have some fun.

         🔥🔥🔥🎆🎆🎆🎆🎆  

