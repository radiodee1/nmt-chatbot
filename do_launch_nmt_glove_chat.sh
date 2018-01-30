
# this doesn't work as vocab prefix is missing

cd nmt
python3 -m nmt.nmt \
    --attention=scaled_luong \
    --src=from --tgt=to \
    --src_embed_file=../glove/glove.embed.from \
    --tgt_embed_file=../glove/glove.embed.to \
    --train_prefix=../data/train \
    --dev_prefix=../data/test  \
    --test_prefix=../data/test \
    --out_dir=../model_glove \
    --share_vocab=True \
    --num_train_steps=12000 \
    --steps_per_stats=10 \
    --infer_batch_size=100 \
    --num_layers=2 \
    --num_units=300 \
    --dropout=0.2 \
    --metrics=bleu \
    --encoder_type=bi \
    --beam_width=10 \
    --length_penalty_weight=1.0 \
    --batch_size=16 \
    --optimizer=adam \
    --junk \
    --vocab_prefix=../glove/glove.vocab  \
    --override_loaded_hparams=True
#    --num_gpus=0 \
#    --vocab_prefix=../glove/glove.vocab  \

