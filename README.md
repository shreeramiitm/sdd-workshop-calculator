# Spec Driven Development (SDD) Implementation

![image](https://github.com/user/repo/assets/...)<img width="1280" height="633" alt="Screenshot 2026-05-25 at 8 33 03 PM" src="https://github.com/user-attachments/assets/6c961667-542e-457d-b905-108a99a5d876" />


This branch contains the simple calculator built utilizing **Spec Driven Development (SDD)** with the `openspec` CLI and an integrated AI IDE agent.

## What is Spec Driven Development?
SDD is a methodology where the developer writes a strict, plain-text specification (usually in Markdown) defining the application's architecture, rules, and features *before* any code is written. An AI agent then reads this specification to autonomously scaffold and generate the required codebase.

## The OpenSpec CLI
This project utilized **OpenSpec** (by Fission-AI), a lightweight CLI tool that manages the SDD lifecycle. It creates an isolated environment (`openspec/` folder) to track proposals, architectural designs, task checklists, and final specifications.

## Workflow Used
1.  **Initialization:** Ran `npm install -g @fission-ai/openspec` and `openspec init` to configure the workspace for the Antigravity IDE agent.
2.  **Proposal & Spec Generation:** Used the `/opsx:propose` slash command to instruct the AI agent to draft the initial calculator requirements.
3.  **Documentation Artifacts:** The agent autonomously populated the `openspec/changes/` directory with `proposal.md`, `design.md`, `tasks.md`, and the final `spec.md`.
4.  **Automated Implementation:** Instructed the agent to read the `spec.md` and generate the backend (`app.py`) and frontend (`index.html`) code.
5.  **Verification:** Tested the generated code against the initial spec requirements.

## Advantages
* **Predictable Output:** Because the AI follows strict rules, it doesn't hallucinate random file structures or unwanted dependencies.
* **Self-Documenting:** The process automatically generates high-quality design documents and task lists alongside the code.
* **Highly Scalable:** When adding new features, the AI references the existing `spec.md`, ensuring new code aligns perfectly with the established architecture.

## Disadvantages
* **Slower Setup:** Requires installing Node.js packages, initializing the CLI, and restarting the IDE.
* **Learning Curve:** Requires learning new workflows, slash commands, and how to write effective specification documents.
* **Overkill for Micro-Projects:** Drafting 4 different markdown documents just to build a 50-line calculator can feel unnecessarily tedious.
