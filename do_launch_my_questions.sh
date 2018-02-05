
cat my_questions.txt
echo
echo "========"
cd nmt
python3 ../inference.py < ../my_questions.txt
#python3 -m nmt.inference
