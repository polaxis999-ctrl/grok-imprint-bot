# grok_bot.py

# Updated to focus on Detroit and Motown culture.

class GrokBot:
    def __init__(self):
        # Original emphasis on Cincinnati is changed to Detroit
        self.city = 'Detroit'
        self.culture_reference = 'Motown'
        self.prompts = {
            'system': 'Focus on Detroit-based content, including chat about meme coins like "DetroitRise" and "MotownMojo".',
            'user': 'Let’s dive into Detroit culture and the vibes of Motown!'
        }

    def get_prompt(self, prompt_type):
        return self.prompts.get(prompt_type, '')

# Example usage
bot = GrokBot()
print(bot.get_prompt('system'))
print(bot.get_prompt('user'))

# The output will be prompts tailored to Detroit and its vibrant culture.