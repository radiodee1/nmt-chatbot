Links:
--------
some interesting sites for finding corpus data.


* https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html
* http://files.pushshift.io/reddit/

Early Notes:
-------
I am trying to prepare a corpus that has elements of auto-encoder data in it. To that end the input 'to' and 'from' files have been sprinkled with identical data on every nth location. This n is currently 64. The batch size is currently 32.

These models have all been trained with different inputs over time. That is to say I may have started out with one corpus for 25,000 global steps, and then switched to a totally different corpus for the next 25,000 global steps. Similarly I've changed the hyper parameters during these corpus switches. My results may not be re-producible.

I decided that I wanted to do a full training iteration of auto-encoding. I removed the 'train.from' file from the 'data' folder and replaced it with a link to the 'train.to' file in that same folder. I ran the training script for 1,000 global steps - just long enough to save one checkpoint.

I immediately replaced the train.from file with its original contents and trained until another checkpoint was saved. I don't know if this helped my overall training or not. I am concerned that when I start and stop training the model does not pick up where it left off in the 'train' files, but rather always restarts at the 0th element in the 'train' files.

Later:
------
I have put together 'train.from' and 'train.to' files that contain 4 million sentence pairs. I have focused on an architecture that has 600 units (for the vector size), 2 LSTM layers and a vocabulary size of about 20000 words. I've also separated the training files into 16 smaller equally sized files. This helps me ensure I train with all of my sentences.

Training the first epoch I have found some interesting patterns. The model is meant to be a chat-bot that's supposed to answer questions somewhat intelligently. In fact it's more of a 'yes' bot. This is because it doesn't answer most questions, but is constantly on the alert for one that can be answered with a yes or no. Then, under these conditions, it answers 'yes'. It is actually interesting how complex the question sentence can be. 

The model, I believe, can be trained further. It will be interesting to see if the 'yes-bot' behavior remains after further training, or if some other pattern takes over. 

The model definitely doesn't answer all the time, and this I find to be disappointing. The resulting model might be described as a 'shy-bot' because it doesn't always even answer. To the other extreme we might describe a 'rude-bot' that answers all the time but not always appropriately. We might define a spectrum between 'shy' and 'rude'. Right now my chat-bot is definitely on the 'shy' side. I'm hoping further training will help this.

