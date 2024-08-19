Pranav and Prithvi are back from last year, and this time they're on an adventure to find the secret lost treasure in an ancient Japanese ruin. They realise that the secret to where the treasure lies is hidden in a coded message - one that is represented by some strange symbols. They discover these haikus, corresponding to the structure of the lines (translated to English, of course):

`@ & -` <br>
*Variable breathes life,* <br>
*Value whispers in its ear,* <br>
*New dawn for the name.*

`+ & -` <br>
*Value joins the dance,* <br>
*Increasing as shadows grow,* <br>
*Addition's soft grace.*

`* & -` <br>
*Strength of numbers blend,* <br>
*Variable's power grows,* <br>
*Multiplication.*

`/ & -` <br>
*Splitting parts with care,* <br>
*Division by quiet force,* <br>
*Fair share to the whole.*

`# -` <br>
*Echo of the name,* <br>
*Whispers truth from within code,* <br>
*Value in the light.*

`!` <br>
*End of tales unfolds,* <br>
*A sudden halt to the quest,* <br>
*Silence speaks in code.*

Pranav and Prithvi have deciphered these to mean that the coded message is written in some esoteric language, and the syntax is given by the symbols before the haikus. The ampersand represents the name of some variable, and the hyphen represents some numerical value.

For example: <br>
`@ x 3` means "Set x to 3" <br>
`+ x 4` means "Add 4 to x" <br>
`* x 8` means "Multiply x by 8" <br>
`/ x 2` means "Divide x by 2" <br>
`- x 5` means "Subtract 5 from x" <br>
`# x` means "Print x" (print statements print on new lines and **not** on the same line) <br>
`!` means "Stop decoding here" (ignore all further statements) <br>
and reveals the coded message $23$.

Given a message that is $n$ lines long, can you figure out the secret code?

### Input Format
- The first line of the input contains an integer $n$, denoting the number of lines.
- The next $n$ lines of the input each contain the encoded message.

### Output Format
Your output should contain the decoded message. If there is no decoded message, type in 'no output'.