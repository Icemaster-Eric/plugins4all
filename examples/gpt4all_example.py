from gpt4all import GPT4All
from plugins import generate_instructions, get_plugin_response


if __name__ == "__main__":
    model = GPT4All(model_name="GPT4All-13B-snoozy.ggmlv3.q4_1.bin")

    while True:
        prompt = input("Prompt: ")

        output1 = ""

        for token in model.generate(
            f"""### System:
{generate_instructions('https://chatgpt-plugins.replit.app/openapi/weather-plugin')}

### Human:
{prompt}

### Assistant:""", max_tokens=256, temp=0, streaming=True):
            print(token, end="", flush=True)
            output1 += token

        print("\n")

        output2 = ""

        for token in model.generate(
            f"""### System:
{get_plugin_response(output1)}

### Human:
{prompt}

### Assistant:""", max_tokens=128, temp=0, streaming=True):
            print(token, end="", flush=True)
            output2 += token

        print("\n")
