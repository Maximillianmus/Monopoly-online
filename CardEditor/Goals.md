# Card Editor specification
A card editor that will be used to implement cards for a monopoly game.

## Ledger

 \* = Not important

 \** = Important
 
 \*** = Critical 
## Functionality goals

- Be able to preview cards before saving to a file, if possible in realtime ** ✓
- Write card text *** ✓
- Be able to use tags in text *
- Be able to use card tags to define properties of a card. ***
- Define tags with numerical value. *** ✓
- Preview gameboard *
- Edit gameboard cards *
- Save to file *** ✓
- Implement card aesthetics that can change color ** ✓
- Implement card pictures *** ✓
- Be able to implement custom card layouts(based on pixels) *** ✓
- Define key color *** ✓
- List of cards already created, cards can be edited and deleted from the list *** 

## Technical goals

### UI
- list with scroll, for cards/gameboard slots ✓
- boxes to write in, both text and numbers ✓
- preview card ✓
- editing buttons: save, load, delete
- file searcher
- Mouse functionality ✓
- Add picture ✓
- Add text ✓
- tag list(maybe show the tag list when card is selected)
- Add tags to card ✓
- Add new tag ✓

### File reading and saving
- Save to XML ✓
- read all XML objects 
- create new XML objects ✓
- Remove XML objects 

### Tags
- give number values to tags ✓
- tag order matters ✓
- use tags to define behaviour (cancelled)


