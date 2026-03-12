
"""

Ivan D. Linares

Text Processing and Word Frequency Analysis

Original article:
    hhttps://www.guinnessworldrecords.com/news/2025/10/inside-a-canadian-professors-43-year-old-dungeons-and-dragons-campaign

Title: Inside a Canadian professor's 43-year-old Dungeons & Dragons campaign
By:Ben Hollingum
wordcount:~1200
"""

import operator

# Function to fetch data
def fetch_text(raw_url):
  """Fetch text from a URL with local caching support.
  
  Downloads text from the given URL and caches it locally using SHA1 hashing
  of the URL as the filename. On subsequent calls with the same URL, returns
  the cached version without re-downloading.
  
  Args:
      raw_url (str): The URL to fetch text from.
  
  Returns:
      str: The text content from the URL, or an empty string if the fetch fails.
  """
  import requests
  from pathlib import Path
  import hashlib

  CACHE_DIR = Path("cs_110_content/text_cache")
  CACHE_DIR.mkdir(parents=True, exist_ok=True)

  def _url_to_filename(url):
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    return CACHE_DIR / f"{url_hash}.txt"

  cache_path = _url_to_filename(raw_url)

  SUCCESS_MSG = "✅ Text fetched."
  FAILURE_MSG = "❌ Failed to fetch text."
  try:
    if not cache_path.exists():
      response = requests.get(raw_url, timeout=10)
      response.raise_for_status()
      text_data = response.text
      cache_path.write_text(text_data, encoding="utf-8")
    print(SUCCESS_MSG)
    return cache_path.read_text(encoding="utf-8")

  except Exception as e:
    print(FAILURE_MSG)
    print(f"Error: {e}")
    return ""


# Fetch the text
DnDtext = """ On 25 April 1982, two teenage boys in the small town of Borden, Saskatchewan, Canada began playing the relatively new fantasy role-playing game Dungeons & Dragons. Within the fantasy world being developed, a young warrior and adventurer by the name of Titanius Baldwinov set out from the burned ruins of his village in Greyhawk, looking for revenge. On his travels, he would fight beasts in the foothills of the Drachensgrab Mountains, hunt for hidden treasure in caves, and do what he could to survive in the violent and dangerous land.
Titanius's fate was guided by Jeff Golding – who was playing the young fighter – and Robert Wardhaugh – who was in the role of Dungeon Master (or DM). The graph paper maps, character sheets, dice, and printed adventure modules and rule books (from TSR - the company that developed Dungeons & Dragons) were laid out wherever the two boys could find a place to play.
The game they played was a lot of fun, and they decided to keep going with the campaign. Over the next few months, more players joined Robert's game. Titanius met the thief Conan Blackrazor, the wizard Elrond Miltonov and the cleric Arak. These adventurers joined forces as the "Party of the Pendant", and their players became devotees of what they called simply "The Game".
Today, 43 years later and more than 2,000 km away, Robert Wardhaugh's D&D campaign is still going strong. The Dungeon Master, who is today also a history professor at the University of Western Ontario, is the proud holder of the GWR title for the longest running D&D campaign (homebrew).
He estimates that around 500 player characters have passed through the ranks of the Party of the Pendant over the last four decades, which corresponds to over four centuries of in-game time. Characters have come and gone, empires have risen and fallen, magical items – taken from cursed tombs or dragon's hoards – have been handed down through generations of player characters. Despite all the changes in Robert's life and those of his many players, The Game – as they still call it – has endured, never going more than a couple weeks without a session, and typically doing two or three sessions a week.
So how has Robert kept The Game going for so long, and what makes it so special?
1. Spectacle

It's hard to overstate Robert's dedication to the Dungeon Master's art. The entire basement of his house – which he picked because it met The Game's needs as well as his family's – is dedicated to Dungeons & Dragons. In addition to the large room where sessions are held, there is also a model-painting workshop and storage rooms that contain every setting a storyteller might need.
This includes huge modular town sets, each representing a different historical period or culture; terrain for everywhere from barren deserts to snow covered mountains; and grand set-pieces such as ancient ruined temples, gladiatorial amphitheatres or castles.
Robert estimates that he has around 30,000 hand-painted miniature figures, allowing him to set up encounters with everything from a horde of puny kobolds to a towering multi-headed dragon.

2. Pacing


Robert's priority is keeping his players interested and engaged. As Dungeons & Dragons is a turn-based game, that means he emphasizes speed and action, moving from one player to the next as quickly as possible. When he started out, he was using the (1st and 2nd edition) rules laid out in Advanced Dungeons & Dragons but he quickly found that traditional rule-set slowed things down too much.
Taking the advice of AD&D's introduction (written by the game's co-creator Gary Gygax), Robert started modifying the rules to suit his own game. He dropped things that slowed down combat, created his own systems for levelling characters and – as the scope of his campaign grew – started adding new character classes, new enemies and new gameplay mechanics. These changes (which have been made in parallel with the shifting rules of D&D's official releases) are the reason for the qualifier "homebrew" in the record title (a term used to describe DM-specific rule changes).
3. Flexibility

After Robert left Borden to go to university in Saskatoon in 1985, the original Party of the Pendant grew to include a rotating cast of players. Not everyone attends every session – at the moment there are around 60 active players involved in The Game, but generally sessions only involve five to eight players at a time.
Robert has developed a number of ways to keep his players engaged, even if they can't play for an extended period. Each session, a party report is written by one of the players, that is then sent out the others. A massive website has been developed containing decades of information and material. Players are often flying into London, Ontario (the present home of The Game) for gaming trips. Players are now able to participate online from anywhere in the world.

If players have to step away from The Game for an extended period, Robert will keep track of their characters, quizzing players on what their character has been doing while they were away from the action. Characters can train or study to improve their skills or teach things to their in-game children. Long-standing players now have family trees extending over fifteen generations.

4. Player Freedom

Because Robert has been running The Game continuously for more than four decades, he knows the setting inside and out (being a history professor helps develop the world and its many cultures). Adventures take place in a world that is based on real-life historical Earth, but one that has been altered into a fantasy setting that includes orcs and dragons. Characters that travelled to England, for example, would find themselves in the land of Arthurian legend, while Viking Sagas or Roman mythology might dominate elsewhere.

His familiarity with this fictional world means that he doesn't generally have to do much – if any – specific prep for sessions. Robert prefers to react to whatever his players decide to do as the events he describes unfold, and he abhors the dark art of "railroading" (pushing players towards specific actions and outcomes that fit with a DM's planned narrative).

5. Longevity

The simple fact that The Game has been going on for so long gives it a depth and breadth that no other campaign can match. Robert has decades (or centuries, in-game) of lore and history to draw on, a massive cast of established characters, countries and factions with their own agendas and alignments. A demon lord banished a century ago (or a decade in real time), for example, might be summoned back and unleashed once again on the material plane, testing old alliances and bringing a new generation of heroes out into the world.

Robert plans to keep going with his campaign for as long as he is able. The grand overarching narrative of his setting – the growing threat from a mysterious entity that his players know only as "The Arriver" – still has plenty of life in it (he's been building this conflict up since the early 1990s), and his players' decisions constantly push the game in novel directions that inspire new storylines.
"""

# assign the inline text to the variable used throughout the script
pride_prejudice_text = DnDtext

# Statistics about the data
def print_text_stats(text):
  """Print basic statistics about text content.
  
  Calculates and prints the total number of characters, lines, and words
  in the provided text.
  
  Args:
      text (str): The text to analyze.
  
  Returns:
      None
  """
  num_chars = len(text)

  lines = text.splitlines()
  num_lines = len(lines)

  num_words = 0
  for line in lines:
    words_in_line = line.split()
    num_words_in_line = len(words_in_line)
    num_words += num_words_in_line

  print(f"Number of characters: {num_chars}")
  print(f"Number of lines: {num_lines}")
  print(f"Number of words: {num_words}")

# Function to get word counts
def get_word_counts(text):
  """Count frequency of each word in text.
  
  Converts all words to lowercase and counts their occurrences throughout
  the text. Returns a dictionary mapping each unique word to its count.
  
  Args:
      text (str): The text to analyze.
  
  Returns:
      dict: Dictionary with words as keys and their frequency counts as values.
  """
  word_counts = {}
  lines = text.splitlines()
  for line in lines:
    words = line.split()
    for word in words:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
  return word_counts

# the print_top_10_frequent_words will call the above get_word_counts() and print only the top 10 frequent words.
def print_top_10_frequent_words(text):
    """Print the 10 most frequently occurring words in text.
    
    Calculates word frequencies and displays the top 10 words sorted by
    occurrence count in descending order.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        None
    """
    word_counts = get_word_counts(text)
    sorted_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_10_words = list(sorted_word_counts.items())[:10]  # Get the top 10 words and counts
    for word, count in top_10_words:
        print(f"{word}: {count}")


# this is a test print
print_text_stats(pride_prejudice_text)

# get the word counts
word_counts = get_word_counts(pride_prejudice_text)
print(word_counts)

# print the top 10 frequent words
print_top_10_frequent_words(pride_prejudice_text)

"""

Using spaCy for advanced text processing

"""

import spacy

nlp = spacy.load('en_core_web_sm')

def word_tokenization_normalization(text):
    """Tokenize and normalize text using spaCy.

    This function lowercases the input, processes it with the global
    spaCy `nlp` pipeline, filters out newline tokens, stop words,
    punctuation, numeric-like tokens, and tokens shorter than three
    characters, then returns the lemmatized form of each remaining
    token.

    Parameters:
    - text (str): Raw input text to be tokenized and normalized.

    Returns:
    - list[str]: A list of normalized, lemmatized tokens.

    Notes:
    - Requires a spaCy language model to be loaded into the global
      variable `nlp` (for example, `en_core_web_sm`).
    - For very large texts this may be CPU- and memory-intensive.
    """

    text = text.lower() # lowercase
    doc = nlp(text)     # loading text into model

    words_normalized = []
    for word in doc:
        if word.text != '\n' \
        and not word.is_stop \
        and not word.is_punct \
        and not word.like_num \
        and len(word.text.strip()) > 2:
            word_lemmatized = str(word.lemma_)
            words_normalized.append(word_lemmatized)

    return words_normalized


def word_count(word_list):
    """Count frequency of each word in a word list.
    
    Converts all words to lowercase and counts their occurrences in the
    provided list. Returns a dictionary mapping each unique word to its count.
    
    Args:
        word_list (list): List of words to count.
    
    Returns:
        dict: Dictionary with words as keys and their frequency counts as values.
    """
    word_counts = {}
    for word in word_list:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
    return word_counts


def print_top_15_frequent_words(word_counts):
    """Print the 15 most frequently occurring words from a word count dictionary.
    
    Sorts the word count dictionary by frequency in descending order and
    displays the top 15 words with their occurrence counts.
    
    Args:
        word_counts (dict): Dictionary mapping words to their frequency counts.
    
    Returns:
        None
    """
    sorted_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_15_words = list(sorted_word_counts.items())[:15]  # Get the top 15 words and counts
    for word, count in top_15_words:
        print(f"{word}: {count}")


doc_tokenized = word_tokenization_normalization(pride_prejudice_text)

print(doc_tokenized)

new_counts = word_count(doc_tokenized)
print(new_counts)

print_top_15_frequent_words(new_counts)

from collections import Counter

def print_top_verbs_simple(text, n=10):
    """Print the top `n` verb lemmas using a concise Counter-based approach."""
    doc = nlp(text)
    verbs = [t.lemma_.lower() for t in doc if t.pos_ == "VERB" and not t.is_punct and not t.is_space]
    for verb, count in Counter(verbs).most_common(n):
        print(f"{verb}: {count}")


# run the simpler verb analysis
print_top_verbs_simple(pride_prejudice_text, 10)

"""
analysis 

1. 
The top 15 words in the text that was analyzed reflect the core themes and elements of the article well.
Words such as "player", "game", and "character" all incompass core aspects of the D&D game and overarching 
narrative of Robert's campaign. The word "robert" is the third most frequent word, which is fitting given
the article focuses on him and his dedication to the game. The word "go" was a little surprising to see amongst the
other words because the other words are so specific to the content of the article.

2. 
the words on the list displays a lot of words that are specific to those who have played Dungeons & Dragons with words
such as session, campaign, set. from the words on the list you can also see a sense of storytelling and adventure,
with words such as world, develop, and play. 


3. 
the verbs that aremost common give us an insight to the actions that usually take place in Robert's D&D campaign, with words such as play, find, take, etc.
there are other verbs that give us a hint to what Robert does as the DM(host of the game) such as keep, develop, find. All verbs that could
be associated with making a word or adding things to the story/game.

"""