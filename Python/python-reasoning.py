"""Example of using a reasoning model (e.g. o1, o3-mini) via the LLM Gateway.

Reasoning models think through problems step-by-step before responding.
They use a 'reasoning' parameter instead of temperature, and do not support:
temperature, top_p, presence_penalty, frequency_penalty, or logprobs.
Make sure your .env MODEL value is set to a reasoning-capable model.
"""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables (API key, base URL, model name) from the .env file.
if not load_dotenv(".env"):
    print("Unable to load .env file.", file=sys.stderr)
    sys.exit(1)

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

# A constraint-satisfaction problem (course scheduling) gives the reasoning
# model something worth thinking about: prerequisites, time conflicts, credit
# bounds, and a breadth requirement all have to hold simultaneously.
scheduling_problem = """\
Help a University of Michigan CS junior pick a valid Fall 2025 schedule.

AVAILABLE COURSES (name, credits, meeting times, prerequisites):
  1. EECS 376 — Theory of Computation (4 cr) — MWF 10:00-11:00am — prereq: EECS 281
  2. EECS 370 — Computer Organization (4 cr) — MWF 1:00-2:00pm + lab Th 3:00-5:00pm — prereq: EECS 281
  3. EECS 482 — Operating Systems (4 cr) — TuTh 12:00-1:30pm — prereq: EECS 281 AND EECS 370
  4. EECS 484 — Databases (4 cr) — TuTh 9:00-10:30am — prereq: EECS 281
  5. EECS 485 — Web Systems (4 cr) — MW 3:00-4:30pm — prereq: EECS 281
  6. MATH 425 — Probability (3 cr) — MWF 11:00am-12:00pm — prereq: MATH 215
  7. ENGLISH 325 — Art of the Essay (3 cr) — TuTh 10:00-11:30am — no prereq
  8. STATS 250 — Intro Statistics (4 cr) — MWF 9:00-10:00am + lab Th 4:00-5:00pm — no prereq
  9. PHIL 340 — Minds and Machines (3 cr) — MW 2:30-4:00pm — no prereq
 10. MUSIC 346 — History of Rock (3 cr) — TuTh 1:00-2:30pm — no prereq

STUDENT CONSTRAINTS:
  - Already completed: EECS 281, MATH 215.
  - Has NOT completed EECS 370.
  - Works at the ITS help desk every Mon/Wed/Fri from 8:00-10:00am (unavailable).
  - Plays in the Michigan Marching Band: Tue/Thu 3:30-6:00pm (unavailable).
  - Must enroll in EECS 376 this term (graduation requirement).
  - Needs exactly 4 courses totaling 14-16 credits.
  - Needs at least one non-CS, non-Math course for intellectual breadth.
  - No two classes (or labs) may overlap in time.

Return:
  (a) the 4 courses you recommend,
  (b) the total credit count,
  (c) a step-by-step justification showing how each constraint was checked,
  (d) which courses you ruled out and why.
"""

# Send a request using the Responses API.
# reasoning.effort controls how much internal thinking the model does.
# Options: "low" (fast), "medium" (balanced), "high" (most thorough).
response = client.responses.create(
    model=os.environ['REASONING_MODEL'],
    instructions="You are a helpful academic advisor. Always say GO BLUE! at the end of your response.",
    input=scheduling_problem,
    reasoning={"effort": "high"},
)

# Print the text content of the response.
print(response.output_text)
