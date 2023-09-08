# Plugins4All
Bringing chatgpt plugins to all local LLMs

## GPT4All-snoozy 13b - Weather Plugin Demo
![](assets/weather-plugin-demo.gif)

## Installation
You can easily install and use Plugins4All by pip installing the package:
```
pip install plugins4all
```

## Usage
```python
from plugins4all.plugins4all import generate_instructions, get_plugin_response

# get instructions for a plugin - this can be easily inserted into a prompt
instructions = generate_instructions("https://example-plugin.com/.well-known/ai-plugin.json")

# example output of the llm
llm_output = 'some llm output ... example_function_call({"query":"some query"})'

# extract and run plugin operations
plugin_response = get_plugin_response(llm_output)

# you can then feed the output back into the llm along with the original prompt to get the final output
```
