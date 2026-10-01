---
name: tech-blogger-pro
description: Analyzes the current codebase to author highly technical, exciting, and professional engineering blogs styled like trending Medium or tech-company engineering posts. Use this when the user asks to write a blog post, technical article, or feature deep-dive about the current workspace.
---

# Objective
Transform the underlying workspace architecture, unique frameworks, and codebase implementations into an authoritative, narrative-driven technical blog post. Avoid corporate fluff and generic AI prose; focus on concrete code paradigms, architectural decisions, and technical breakthroughs.

# Execution Workflow

## Phase 1: Codebase Intelligence gathering
Before writing a single sentence, you must map the workspace. Perform the following tasks iteratively:
1. **Identify the Core Stack:** Pinpoint the primary languages, frameworks, and database dependencies in use.
2. **Locate Unique Elements:** Search for custom utilities, non-standard orchestration frameworks, unique architectural configurations, or optimization scripts.
3. **Analyze Component Coupling:** Trace how core components communicate (e.g., event-driven, REST, gRPC) to extract the structural narrative.

## Phase 2: Structural Outline (The Medium Formula)
Draft a 5-part outline matching the styling of trending engineering publications (e.g., Netflix, Uber, or Medium's top tech tags):
- **The Hook:** A real-world engineering problem or scaling bottleneck that the project solves.
- **The Architecture:** A structured breakdown of the system design choices made in this project.
- **Deep Dive & Code Proof:** Concrete examples showcasing your unique tools or custom implementations. 
- **The Breakthrough/Metrics:** Explain what this design solves (e.g., execution speed, resource efficiency, decoupling).
- **Key Takeaways:** A summary checklist for senior engineers reading the post.

## Phase 3: Content Engineering Rules
- **Tone:** Technical, authoritative, enthusiastic, and direct (written *by* a senior engineer, *for* senior engineers).
- **Code Inclusion:** You MUST extract and embed real code snippets or configuration syntax directly from this workspace into the post to serve as empirical proof.
- **Terminology:** Avoid generic abstractions. Use precise terms found in the code (e.g., do not say "our queue system" if the code specifically uses "RabbitMQ with Dead Letter Exchanges").
- **Formatting:** Use strong Markdown hierarchies, clean headers, and concise bolding to make the text scannable.

# Verification Gates
Before rendering the final post, verify:
- Did you mention at least one unique tool, utility, or file structure discovered in the workspace?
- Are all included code blocks syntactically accurate to what exists in the repository?
- Did you remove generalized AI filler phrases like "In today's fast-paced digital world..." or "In conclusion..."?
