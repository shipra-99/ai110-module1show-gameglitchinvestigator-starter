# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I ran the game, the interface loaded correctly but the gameplay had issues. The hints were incorrect—for example, when I guessed a number higher than the secret number, the game told me to go “higher” instead of “lower.”

I also noticed inconsistent behavior with the secret number, which suggested the value or type might be changing during gameplay. Additionally, the instructions always said to guess between 1 and 100 even when the difficulty range was different.

---

## 2. How did you use AI as a teammate?

During this project, I used GitHub Copilot in VS Code to analyze the buggy logic in the game. Using Copilot Chat with the `#file:app.py` context, I asked it to explain the `check_guess()` function. Copilot correctly identified that the hint messages were reversed—when the guess was higher than the secret number, the game incorrectly told the player to go higher.

However, Copilot mainly focused on the hint text and did not fully address the issue where the secret number sometimes became a string. After testing the game multiple times and reviewing the code, I realized this type conversion caused inconsistent comparisons. This showed me that Copilot can help explain code quickly, but its suggestions still need to be verified through testing.


---

## 3. Debugging and testing your fixes

To check if a bug was fixed, I ran the game multiple times in Streamlit and made different guesses. I used the Developer Debug Info panel to compare my guesses with the secret number and verify if the hints were correct.

I tested by guessing numbers higher and lower than the secret number to see if the hints matched the expected behavior. From these tests, I confirmed that the hint logic was incorrect because it told the player to move in the wrong direction. GitHub Copilot helped me understand the comparison logic in the `check_guess()` function, which helped identify the issue.


---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the entire script every time a user interacts with the app, such as clicking a button or entering a guess. Because of this, variables can reset unless they are stored in `st.session_state`. Session state keeps values like the secret number, score, and attempts from resetting.

In simple terms, Streamlit works like refreshing the program each time you interact with it, and session state helps keep important game data saved between those refreshes.


---

## 5. Looking ahead: your developer habits

One habit I want to keep using is AI tools like GitHub Copilot to understand code faster. It helped explain functions and identify possible bugs. However, this project showed that AI suggestions should always be tested and verified. I learned that developers should not rely completely on AI-generated code. Testing and reviewing the code is still very important.
