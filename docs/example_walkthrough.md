# Example Walkthrough: Stack-Guided Reasoning

## Input Prompt
"Solve a structured reasoning task"

### Initial Subtasks
1. Understand the problem
2. Identify constraints
3. Solve main problem
4. Verify final answer

---

## Step-by-Step Execution

### Step 1
- **Pop:** Understand the problem
- **Action:** LLM processes task
- **Stack Size:** 3

---

### Step 2
- **Pop:** Identify constraints
- **Action:** LLM processes task
- **Stack Size:** 2

---

### Step 3
- **Pop:** Solve main problem
- **Action:** LLM generates subtasks:
  - Break down Solve main problem
  - Execute Solve main problem
- **Push:** New subtasks
- **Stack Size:** 3

---

### Step 4
- **Pop:** Break down Solve main problem
- **Action:** LLM processes task
- **Stack Size:** 2

---

### Step 5
- **Pop:** Execute Solve main problem
- **Action:** LLM processes task
- **Stack Size:** 1

---

### Step 6
- **Pop:** Verify final answer
- **Action:** LLM processes task
- **Stack Size:** 0

---

## Visualization Interpretation

- Early increase in stack height reflects task decomposition.
- Gradual decrease reflects reasoning convergence.
- The final stack height of zero indicates task completion.

---

## Key Takeaway
The stack structure provides an explicit, interpretable control mechanism for
LLM reasoning, similar to a call stack in traditional programs.

