# Day 6: Functions, While Loops & Reeborg's World

A no-code lesson day using [Reeborg's World](https://reeborg.ca/), an in-browser Python sandbox where you write code to navigate a robot through hurdles and mazes. The challenge: solve increasingly difficult problems using only sensor checks and movement commands — no hardcoded paths.

## What I learned
- Defining and calling functions to organize and reuse logic
- `while` loops for indefinite repetition (loop until a condition changes)
- Building helper functions from primitives (writing `turn_right()` from three `turn_left()` calls)
- Reading API documentation to discover available sensors (`right_is_clear()`, `front_is_clear()`, `at_goal()`)
- Acting on confirmed information vs. acquiring information through sensor checks
- The right-hand rule for solving simply-connected mazes

## Hurdle 4 solution

Variable-height walls with variable spacing. The key insight: `jump()` shouldn't assume a fixed wall height — it climbs until the wall ends, detected by `right_is_clear()`.

```python
def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
```

## Maze solution

The right-hand rule: always keep the right hand on a wall and the exit will eventually be reached. Three priority-ordered cases per step:

```python
def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

## Reflection

This lesson was the first real debugging experience of the course. The hurdle solution failed because I assumed `front_is_clear()` would tell me when to stop climbing — it doesn't, because nothing in front of the robot doesn't mean the wall is over. The fix came from realizing I needed a different question: "is the wall still beside me?" That's what `right_is_clear()` answers.

The bigger lesson: APIs and libraries always have more capabilities than the tutorial shows. The skill is recognizing what question you need to ask, then going to look for the tool that answers it — not hunting for tools first and hoping one fits.

The maze and hurdle problems share the same structure: a `while not done` loop with sensor-based decisions inside. Recognizing that pattern across both problems was a moment of real understanding — the same shape solves very different-looking problems.