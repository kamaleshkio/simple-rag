from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def get_llm_chain(api_key, model_name = "mistralai/mistral-7b-instruct"):
    llm = ChatOpenAI(
        openai_api_key = api_key,
        openai_api_base = "https://openrouter.ai/api/v1",
        model_name = model_name,
        temperature = 0.8,
    )


    prompt = ChatPromptTemplate("""
    use the following context to answer the question.
    <context>
    {context}                            
    </context>
    Question: {input}
    """
    )

    return create_stuff_documents_chain(llm, prompt)
