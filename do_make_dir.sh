git clone https://github.com/tensorflow/nmt/

wget http://www.cs.cornell.edu/~cristian/data/cornell_movie_dialogs_corpus.zip
mv cornell_movie_dialogs_corpus.zip raw/.

mkdir raw


pip3 install tqdm colorama regex


#mkdir tmp/chat_model tmp/chat_data tmp/chat_new

if [ -f raw/RC_2015-01.bz2 ] ; then
    echo "found RC"
    cd raw/
    
    if [ -f RC_2015-01 ] ; then
    
        echo "already unzipped"
        mv RC_2015-01 ..
        
    else
        if [ -f ../RC_2015-01 ] ; then
            echo "already moved"
            
        else
            echo "unzip may take some time..."
            bunzip2 -kv RC_2015-01.bz2
            mv RC_2015-01 ..    
        fi
  
    
    fi
    cd ../
else
    
    echo "nothing for RC_2015-01"
fi

if [ -f raw/cornell_movie_dialogs_corpus.zip ] ; then
    if [ -d raw/cornell\ movie-dialogs\ corpus ] ; then
        echo "unzipped"
    else
        cd raw
        unzip cornell_movie_dialogs_corpus.zip
        cp cornell\ movie-dialogs\ corpus/movie_lines.txt ..
        cd ..

    fi
fi
