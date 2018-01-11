

cd nmt
python3 -m nmt.nmt \
    --attention=scaled_luong \
    --src=from --tgt=to \
    --vocab_prefix=../tmp/chat_data/vocab  \
    --train_prefix=../tmp/chat_data/train \
    --dev_prefix=../tmp/chat_data/test  \
    --test_prefix=../tmp/chat_data/test \
    --out_dir=../tmp/chat_model \
    --num_train_steps=12000 \
    --steps_per_stats=10 \
    --infer_batch_size=10 \
    --num_layers=2 \
    --num_units=512 \
    --dropout=0.2 \
    --metrics=bleu \
    --encoder_type=bi \
    --num_gpus=0 \
    --beam_width=10 \
    --length_penalty_weight=1.0 \
    --batch_size=16 \
    --optimizer=adam 

 
    
