Links:
--------
some interesting sites for finding corpus data.


* https://datasets.maluuba.com/NewsQA/dl
* https://archive.org/download/2015_reddit_comments_corpus/reddit_data/2015/
* http://files.pushshift.io/reddit/

Notes:
-------
I am trying to prepare a corpus that has elements of auto-encoder data in it. To that end the input 'to' and 'from' files have been sprinkled with identical data on every nth location. This n is currently 64. The batch size is currently 32.

These models have all been trained with different inputs over time. That is to say I may have started out with one corpus for 25,000 global steps, and then switched to a totally different corpus for the next 25,000 global steps. Similarly I've changed the hyper parameters during these corpus switches. My results may not be re-producable.

I decided that I wanted to do a full training iteration of auto-encoding. I removed the 'train.from' file from the 'data' folder and replaced it with a link to the 'train.to' file in that same folder. I ran the training script for 1,000 global steps - just long enough to save one checkpoint.

I immediately replaced the train.from file with its original contents and trained until another checkpoint was saved. I don't know if this helped my overall training or not.


