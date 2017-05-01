#!/usr/bin/env python

import json, sys, re

sys.path.append('./')

import ManipulateTweets as manip

internet_slang_dict = manip.readFileandReturnADict("internet_slang.csv", "rb", '|', 0, 1, True,None)


contractions_dict = manip.readFileandReturnADict("Contractions.csv", "rU", ',', 0, 1, True)



for line in sys.stdin:
    try:
        # Load Tweets
        parsed_json_tweets = json.loads(line)
        # Extract tweet text
        tweet_text = parsed_json_tweets['text'].lstrip().strip()
        length = 0
        for x in tweet_text:
            length += 1
        if length > 1:
            # Convert multiple white spaces to a single white space
            tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Replace all the internet slang words
            tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', internet_slang_dict, True).lstrip().strip()
            # Replace all word contractions
            tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', contractions_dict, True).lstrip().strip()
            # Replace all emoticons
            tweet_text = manip.replaceEmoticons(str(tweet_text), ' ', False).lstrip().strip()
            # Convert multiple white spaces to a single white space
            tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Remove double quotes
            tweet_text = re.sub(r"\"", r"", tweet_text)
            print '%s' % (tweet_text)
    except ValueError:
        continue
