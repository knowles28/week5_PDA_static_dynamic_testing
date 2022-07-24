### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False

# ERROR line 21 - card.value should be followed by '== 1:'
# ERROR line 23 - no colon after else

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  
# ERROR line 29 - 'def' not 'dif'
# ERROR line 29 - no comma between arguments 'card1' and 'card2'
# ERROR line 31 - 'card' is undefined, likely meant to be 'card1'
# ERROR lines 30-33 - not indented




def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total


# ERROR line 44 - total is undefined, should be = 0
# ERROR line 47 - return have been over-indented
# ERROR line 47 - total should be inside the string. The string should be formatted with f"....{total}"
  
```

