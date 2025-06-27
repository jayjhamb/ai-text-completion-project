# ai-text-completion-project
Capstone Project

 Python-based command-line application that uses OpenAI's GPT-3.5 model to generate text completions based on user prompts.

## Setup

1. Clone the repository
git clone https://github.com/yourusername/ai-text-completion-project.git
cd ai-text-completion-project

2. Install dependencies
pip install openai

3. Set your API key  
Store your OpenAI API key as an environment variable:
export OPENAI_API_KEY=your-api-key-here

## How to Run

Run the script from your terminal:
python text_completion_app.py

You will be prompted to:
- Enter a custom prompt
- Set temperature (controls creativity)
- Set max tokens (controls response length)

## Example Prompts

- Explain recursion like I’m five.
- Write a haiku about the ocean.
- Once upon a time, there was a robot who...
- Summarize the causes of World War I.

## Files

- `text_completion_app.py`: Main application script
- `project_report.pdf`: Project summary and evaluation
- `README.md`: This file

## Observations

- Temperature values closer to 1.0 produce more creative, random responses.
- Lower temperature values produce more focused and predictable responses.
- Always review outputs for accuracy, especially when used for factual tasks.
