"""Markov Text Generator.

Patrick Wang, 2021

Resources:
Jelinek 1985 "Markov Source Modeling of Text Generation"
"""

import nltk
import random

def get_next_word(words,n,corpus,det):


    wordlist=[]
    valuelist=[]
    total_uses=0
    dict_words={}
    vocab_size = len(list(set(corpus)))
    vocabulary = sorted(set(corpus))

    nwords=words[-(n-1):]
    for i in range(len(list(corpus))):
        if corpus[i: i + (n-1)]==nwords:
            if corpus[i + (n-1)] in dict_words:
                dict_words[corpus[i + (n-1)]]=dict_words[corpus[i + (n-1)]]+1
                total_uses=total_uses+1
                pass
            else:
                dict_words[corpus[i + (n-1)]] = 1
                total_uses=total_uses+1
                pass
            pass
        pass

    if total_uses==0:
        return get_next_word(words,n-1,corpus,det)

    for key in dict_words:
        wordlist.append(key)
        valuelist.append(dict_words.get(key))
        pass
    if det:
      return max(dict_words, key=dict_words.get)
    else:
        probs = []
        for val in valuelist:
            probs.append(val / total_uses)
        return random.choices(wordlist, weights=probs,k=1)[0]

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += " "+ele  
    
    # return string  
    return str1 


def finish_sentence(words,n,corpus,det):
    punc=".?!"

    if len(words)==0:
        words.append(random.choice(corpus))

    while words[-1] not in punc and len(words)<15:
        words.append(get_next_word(words,n,corpus,det))
        pass
    print(listToString(words))
    return words






def test_generator():
    """Test Markov text generator."""
    corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
    corpus = nltk.word_tokenize(corpus.lower())

    words = finish_sentence(
       ['my','future','is'],
        4,
        corpus,
        False,
    )
   # assert words == ['she', 'was', 'not', 'in', 'the', 'world', '.']


if __name__ == "__main__":
    test_generator()