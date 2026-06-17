---
category: knowledge
tags:
  - python
platform: n/a
status: done
created: 2026-06-17
aliases:
  - 1. [Deep Thought](https://cs50.harvard.edu/python/2022/psets/1/deep/#deep-thought)
---

# 1. [Deep Thought](https://cs50.harvard.edu/python/2022/psets/1/deep/#deep-thought)

> “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
> “You’re really not going to like it,” observed Deep Thought.
> “Tell us!”
> “All right,” said Deep Thought. “The Answer to the Great Question…”
> “Yes…!”
> “Of Life, the Universe and Everything…” said Deep Thought.
> “Yes…!”
> “Is…” said Deep Thought, and paused.
> “Yes…!”
> “Is…”
> “Yes…!!!…?”
> “Forty-two,” said Deep Thought, with infinite majesty and calm.”
>
> — _The Hitchhiker’s Guide to the Galaxy_, Douglas Adams

In `deep.py`, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting `Yes` if the user inputs `42` or (case-insensitively) `forty-two` or `forty two`. Otherwise output `No`.

```python
def main():
    answer=str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
    
    if answer.lower()=="42" or answer.lower()=="forty-two" or answer.lower()=="forty two":
        print("Yes")
    else:
        print("No")
        
if __name__=="__main__":
    main()
```

# # 2. [Home Federal Savings Bank](https://cs50.harvard.edu/python/2022/psets/1/bank/#home-federal-savings-bank)
In [season 7, episode 24](https://en.wikipedia.org/wiki/The_Invitations) of [Seinfeld](https://en.wikipedia.org/wiki/Seinfeld), [Kramer](https://en.wikipedia.org/wiki/Cosmo_Kramer) visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output `$0`. If the greeting starts with an “h” (but not “hello”), output `$20`. Otherwise, output `$100`. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
```python
def main():
    greet=str(input("Greeting: ")).strip().lower()
    if greet.startswith("hello"):
        print("0$")
    elif greet.startswith("h"):
        print("20$")
    else:
        print("100$")

if __name__=="__main__":
    main()
```
