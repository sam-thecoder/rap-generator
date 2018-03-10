# rap-generator
Machine Learning Example Code on Learning to Rap

First model of a LSTM trained on some rap text corpus to generate rap like text. 
Generated the text character by character.

To run it use

```
python generate.py "start text" diversity (int) total_len_chars (int)

python generate.py "thinking out loud" 0.3 400
```

example generated output

```
i'm the say "go drank a bitch in the car off the world it and i know the willer money
the world i got the carter than you the can but i was fack and the bottle to the beat bitch ass when 
i got this bitch i'm the sail the rapper man
and i ain't never see my niggas that you say she wind i ain't the still my showes and shotters and sh
ow you all my shower still corver
i was the bough a bitch
i'm th
```

The input text should be in lowercase only.

Note since this is not sequence to sequence it expects a sentence of 50 char length so I pad it with spaces at the start if it's too short or clip it at 50 if it's too long.

The diversity (from 0.1 to 1.5 or even higher) works on making it more sporadic found the sweet spot is between 0.2 to 0.5

total_len_chars determines the total len of characters generated.
