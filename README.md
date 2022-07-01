# Daily challenge for T1-W8 Friday 1 July 2022

Your challenge for today is this: write a function that accepts a single string as its input, and converts that string to horse-latin, returning the converted string. You may not have heard of horse-latin before: it is very simple.

- for each word in the string, if the word ends with a vowel, add the letters "nay" to the end of the word. For instance: "time" becomes "timenay" and "cargo" becomes "cargonay".
- on the other hand, if the word ends in a consonant, you should instead add "hay" to it. So, "box" becomes "boxhay" and "hour" becomes "hourhay"

So an example of using this function would look like:

`translation = horse_latin_translator("In one hour it will be time to load the box into the cargo bay")`


and the value assigned to translation here would be:

`"Inhay onenay hourhay ithay willhay benay timenay tonay loadhay thenay boxhay intonay thenay cargonay bayhay"`


Don't worry about punctuation - just assume the string will not contain any punctuation characters. You may find the following two builtin python functions helpful:
https://www.w3schools.com/python/ref_string_split.asp
https://www.w3schools.com/python/ref_string_join.asp