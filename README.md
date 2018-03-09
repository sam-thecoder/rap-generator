# rap-generator
Machine Learning Example Code on Learning to Rap

First model of a LSTM trained on some rap text corpus to generate rap like text. 
Generated the text character by character.

To run it use

```
python generate.py "Start text" diversity (int) total_len_chars (int)

python generate.py "thinking out loud" 0.3 400
```

Note since this is not sequence to sequence it expects a sentence of 50 char length so I pad it with spaces at the start if it's too short or clip it at 50 if it's too long. Will work on a sequence to sequence model next.

The diversity (from 0.1 to 1.5 or even higher) works on making it more sporadic found the sweet spot is between 0.2 to 0.5

total_len_chars determines the total len of characters generated.
