

cd data

BIGTRAINFROM=big_train.from
BIGTRAINTO=big_train.to

TRAIN=train


if [ $# -eq 1 ] ; then
    echo "pointing to " $1

    #exit()

    if [ -f $BIGTRAINFROM ] && [ -f $BIGTRAINTO ] ; then
        rm $TRAIN.from $TRAIN.to
        ln -s $TRAIN.$1.from $TRAIN.from
        ln -s $TRAIN.$1.to $TRAIN.to
    else
        mv $TRAIN.from $BIGTRAINFROM
        mv $TRAIN.to $BIGTRAINTO
        rm $TRAIN.from $TRAIN.to
        ln -s $TRAIN.$1.from $TRAIN.from
        ln -s $TRAIN.$1.to $TRAIN.to
    fi

else
    echo "changing link to large initial file! "

    if [ -f $BIGTRAINFROM ] && [ -f $BIGTRAINTO ] ; then
        rm $TRAIN.from $TRAIN.to
        ln -s $BIGTRAINFROM $TRAIN.from
        ln -s $BIGTRAINTO $TRAIN.to
    else
        mv $TRAIN.from $BIGTRAINFROM
        mv $TRAIN.to $BIGTRAINTO

    fi
    ls -hal

fi