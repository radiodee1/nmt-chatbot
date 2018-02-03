

cd nmt
python3 -m nmt.nmt \
    --attention=scaled_luong \
    --src=from --tgt=to \
    --vocab_prefix=../data/vocab  \
    --train_prefix=../data/train \
    --dev_prefix=../data/test  \
    --test_prefix=../data/test \
    --out_dir=../model \
    --num_train_steps=48000 \
    --steps_per_stats=100 \
    --infer_batch_size=32 \
    --num_layers=2 \
    --num_units=300 \
    --dropout=0.2 \
    --metrics=bleu \
    --encoder_type=bi \
    --beam_width=10 \
    --length_penalty_weight=1.0 \
    --batch_size=256 \
    --optimizer=adam \
    --learning_rate=0.001 \
    --override_loaded_hparams=True
#    --num_gpus=0 \
 
    
