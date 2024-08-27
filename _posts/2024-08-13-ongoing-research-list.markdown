---
layout: post
title:  "An ongoing list of ongoing questions"
date:   2024-08-13 00:19
categories: general
---

Research ideas:
- Using interpretability + steering to debias AI-generated results
	- Does superposition + interference encode / explain systematic bias in AI? Play with the toy models of superposition
- How sample-efficient are SAEs?
- Keeping SAEs online (as the data distribution changes); how complete are SAEs?
- What is the right way to manipulate features, especially within feature families or between layers?
- Can we train SAEs with enforced hierarchies (i.e. to prevent feature obscuring a la Makelov)?
- Semantic leakage = superposition? Is there a mechanistic explanation?
- Using AI to simulate multi-agent negotiations and explore the sample space of nuclear de-escalation solutions. Or, express it symbolically --> brute force (similar to algo. search, also simulated social science)
- A systematic survey of inductive biases and when they are/aren't historically helpful (Bitter Lesson -esque). Are people too inclined to the neat and attractive proposition of understanding the brain via AI & vice versa?
- Does MuP come naturally out of LLM mathematics (i.e. eigenvalues of the Fisher matrix)?
- What are the citation patterns of LLMs vs human experts? Is there a way to formalize the "reasoning jumps" that are actually happening?
- “Stupid back off” for LLM agents; is (a lot) of attempts all you need?

Questions I don't know the answer to, but probably have been solved:
- Does the number of layers in a model set a limit on the "depth" of hierarchical reasoning or association that it can perform? Is there some signal in comparing the residual connections vs. the attention/MLP outputs?
- Can you do interpretability on an RL system's representations?
- When have governments nationalized companies with transformative economic potential, and what has the public response been?
- Do we have evolutionary evidence of the Platonic representation hypothesis in humans?
- Is the answer to AI just a re-discovery of the brain? or are tech bros hyper fixated on features (ex. Gabor filters) that happen to coincide? *update on convo w/ Neil*
- Is it possible to do RAG for diffusion models? I.e., few-shot prompting for image generation?
- Is it possible to keep KV caches online (example: if you want to insert a needle in a haystack? efficient propagation of changes? could be related to teaching models to update knowledge)
	- teach the new thing --> think about what could be related (recursively) --> pre-train on self-reflection (?)

Product wish-list:
- A Chrome browser/web app that allows parents to have their kids use ChatGPT, but only educationally (i.e. filters the prompt)
- To be able to highlight any text and immediately ask an AI about it in context (PDF viewer)
- An interactive AI journal -- almost like a drop-in therapist, or at least a built-in voice that pushes back on your ideas & encourages you to expand & is generally comforting
	- Q: is the value of a therapist the human connection, or can you get the benefits from enhanced journaling + sticking to intervention plans/exposure therapy/etc.?
- A small, in-line model that makes you more efficient. Fast feedback loop?
	- I could probably build this myself w/ synthetic examples (to practice training a model?)