# DRW Coding Test
## Instructions
Run the file as ```python main.py input.txt output.txt```
## Intuition for design choice
I chose to simulate each exchange, as we need to keep the state in order to print the right outputs for C when we add multiple times to a stock of the same price, and then try to delete.

Internally, I implemented it using the simplest data structure possible, the python list. I then had classes for exchanges, which was reused for all 3 exchanges.

On hindsight, there are a lot of places where I can reuse code, though having to rush through this exercise meant I did not have time to refactor my code.
