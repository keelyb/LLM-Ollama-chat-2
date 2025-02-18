import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []


def generate_response(model, prompt):
    print("Gradio version:" + gr.__version__)
    conversation_history.append(prompt)

    full_prompt = "\n".join(conversation_history)
    print("conversation history: " + full_prompt)
    

    data = {
        # "model": "mistral",
        "model": f"""{model}""",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None


iface = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Dropdown(
            ["llama2","tinyllama","deepseek-r1","midiman","dnaman"], label="Model", info="The local models you have installed will appear here below."),
        gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
        ],
    outputs="text"
)
# non working
    # inputs=gr.inputs.Textbox(lines=2, placeholder="Enter your prompt here..."),


iface.launch()
