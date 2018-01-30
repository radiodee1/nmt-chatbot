

cd nmt
python3 -m nmt.nmt \
    --attention=scaled_luong \
    --src=from --tgt=to \
    --vocab_prefix=../glove/glove.vocab  \
    --embed_prefix=../glove/glove.embed \
    --train_prefix=../data/train \
    --dev_prefix=../data/test  \
    --test_prefix=../data/test \
    --out_dir=../model_glove \
    --num_train_steps=12000 \
    --steps_per_stats=10 \
    --infer_batch_size=10 \
    --num_layers=2 \
    --num_units=300 \
    --dropout=0.2 \
    --metrics=bleu \
    --encoder_type=bi \
    --beam_width=10 \
    --length_penalty_weight=1.0 \
    --batch_size=16 \
    --optimizer=adam \
#    --override_loaded_hparams=True
#    --num_gpus=0 \


