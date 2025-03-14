Cellular Automata Simulation – Python Project
Author: Marlon

This project explores Elementary Cellular Automata (ECA) through two Python implementations: a batch renderer for multiple rule-based simulations and a Tkinter-based interactive GUI. The goal is to visualize how simple rules evolve over time and observe how initial conditions and parameters (like width or steps) influence emergent patterns.
# What Are Cellular Automata?

Cellular automata are simple models of computation consisting of:

    A one-dimensional array of cells (binary states: 0 or 1)
    Rules (numbered 0–255) that determine how each cell updates based on its left, center, and right neighbors
    An initial state, often a single 1 in a field of 0s

These automata can display chaotic, repetitive, or computationally rich behaviors — even Turing completeness (e.g., Rule 110).
# Overview of Implementations
# cell10rules.py – Batch Generator

This script:

    Defines a rule engine for any 3-cell neighborhood using an 8-bit binary rule number
    Initializes an array with a single 1 in the center
    Evolves it over n steps
    Generates .png images using matplotlib
    Supports parallel processing for speed

# Customizable Parameters:

    rule_number – pick from 0–255 (10 included by default)
    width – number of cells per row (e.g., 800)
    steps – number of generations (e.g., 300)

# Example Output:

    Rule30.png → chaotic pseudo-random pattern
    Rule110.png → complex, computation-like growth
    Rule110_wide.png → wider pattern shows more global behavior
    Rule110_steps500.png → extended generations

# cellular.py – Interactive GUI (Tkinter)

This app provides:

    A visual interface to enter a rule, width, and number of steps
    A Play/Pause mechanism to watch the simulation evolve live
    A Reset button to reconfigure inputs
    Auto-scrolling canvas for large vertical growth

# GUI Controls:
Control	Description
Rule	Integer from 0–255 (e.g., 110)
Width	Number of cells in one row
Steps	Total number of generations
Play / Pause	Animates step-by-step growth
Reset	Re-initializes with new inputs
# Great for:

    Exploring behavior of a single rule interactively
    Understanding step-by-step visual transitions
    Experimenting with visual space (width) and duration (steps)

# Experimental Results

You’ll find several output .png files in this repo, representing the impact of different settings:
File	Description
Rule30.png	Chaotic randomness pattern (rule 30)
Rule110.png	Complex pattern growth (rule 110)
Rule110_wide.png	Wider width to show more structure globally
Rule110_steps500.png	More steps = deeper evolution view

These demonstrate:

    Emergence from simple rules
    How small rule changes lead to drastically different behaviors
    The effect of width (horizontal resolution) and steps (vertical depth)
  # Theory Background

Each rule number (0–255) represents a binary-encoded truth table for the 8 possible 3-bit neighborhood combinations:

    E.g., Rule 110 = 01101110 (binary)
    This maps: "111" -> 0, "110" -> 1, ..., "000" -> 0

These are part of Wolfram’s classification of behavior:

    Class 1: settles to a uniform state
    Class 2: periodic, stable patterns
    Class 3: chaotic, pseudo-random
    Class 4: complex, localized structures

By Marlon (2025)
