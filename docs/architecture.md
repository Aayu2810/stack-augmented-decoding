# Stack-Augmented Decoding Framework – Architecture

## Overview
This project introduces a lightweight, stack-augmented framework that assists
Large Language Model (LLM) reasoning without modifying the model’s internal
decoder or attention mechanisms.

The framework operates externally by managing structured subtasks using a
Last-In-First-Out (LIFO) stack.

---

## System Components

1. **Prompt Parser**
   - Decomposes an input prompt into structured subtasks.

2. **Task Stack**
   - Stores pending subtasks.
   - Supports push, pop, peek, and size operations.

3. **LLM Interface (Mock)**
   - Simulates LLM task processing.
   - May generate additional subtasks.

4. **Stack Controller**
   - Orchestrates task execution.
   - Maintains stack history and execution logs.

5. **Visualizer**
   - Plots stack height over time to show reasoning depth.

---

## Execution Flow


