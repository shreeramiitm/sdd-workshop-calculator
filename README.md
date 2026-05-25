# Simple Calculator: Vibe Coding vs. Spec Driven Development

This repository contains the completion of the "Future of Software Development with LLM" workshop assignment. The project is a simple web-based calculator built with a Python Flask backend and a vanilla HTML/CSS/JS frontend. 

The primary goal of this repository is to compare two distinct AI-assisted software development workflows across two separate branches: **Vibe Coding** and **Spec Driven Development (SDD)**.

## Branch Overview

* **`main`**: Contains the project overview, comparison, and conclusions.
* **`vibe_coded_submission`**: Contains the calculator built using an unstructured, unassisted "vibe coding" approach.
* **`sdd_submission`**: Contains the calculator built using a structured Spec Driven Development approach utilizing the `openspec` CLI.

## Conclusion & Comparison

Both methodologies offer unique approaches to building software with AI tools. Here is a high-level comparison based on this project's workflow:

| Feature | Vibe Coding (`vibe_coded_submission`) | Spec Driven Development (`sdd_submission`) |
| :--- | :--- | :--- |
| **Planning Phase** | None. Code is written directly. | High. Requires drafting a clear `spec.md`. |
| **Tooling** | Standard IDE + manual coding. | `openspec` CLI + IDE AI Agent integration. |
| **Documentation** | Code is the only documentation. | Generates architectural specs, proposals, and tasks. |
| **Speed to First Code** | Instant. | Delayed (requires setup and spec writing). |
| **Scalability** | Low. Prone to messy architecture as it grows. | High. Specs keep the AI and architecture aligned. |

**Final Verdict:** Vibe coding is excellent for rapid prototyping, quick scripts, or hacking together a simple frontend where structure matters less than seeing immediate visual results. However, Spec Driven Development (SDD) is the superior choice for production applications. By forcing the developer to define the architecture and rules beforehand, SDD ensures the AI agent writes predictable, structured, and well-documented code that is much easier to scale and maintain.
