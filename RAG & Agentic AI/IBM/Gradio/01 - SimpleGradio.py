import gradio as gr

def add_numbers(Num1, Num2):
    return Num1 + Num2
    

def combine_sentence(Sentence1, Sentence2):
    return Sentence1 + Sentence2

# Define the interface
demo = gr.Interface(
    fn=combine_sentence, 
    inputs=[gr.Text(), gr.Text()],
    outputs=gr.Text()
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)