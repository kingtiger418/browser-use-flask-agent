from langchain_openai import ChatOpenAI

inference_server_url = "http://localhost:1360/v1"

# Initialize the model
llm = ChatOpenAI(model="unsloth/Meta-Llama-3.1-8B-Instruct",
                 openai_api_key="EMPTY",
                 openai_api_base=inference_server_url,
                 temperature=0.7,
                 max_tokens=8192)
