#!/usr/bin/env python3
import json
import boto3
import requests

# Initialize the Bedrock Runtime client
bedrock_runtime = boto3.client('bedrock-runtime')

def chat_with_document(document, user_query):
    instructions = (
    "I will provide you with a document, followed by a question about its content. "
    "Your task is to analyze the document, extract relevant information, and provide "
    "a comprehensive answer to the question. Please follow these detailed instructions:"

    "\n\n1. Identifying Relevant Quotes:"
    "\n   - Carefully read through the entire document."
    "\n   - Identify sections of the text that are directly relevant to answering the question."
    "\n   - Select quotes that provide key information, context, or support for the answer."
    "\n   - Quotes should be concise and to the point, typically no more than 2-3 sentences each."
    "\n   - Choose a diverse range of quotes if multiple aspects of the question need to be addressed."
    "\n   - Aim to select between 2 to 5 quotes, depending on the complexity of the question."

    "\n\n2. Presenting the Quotes:"
    "\n   - List the selected quotes under the heading 'Relevant quotes:'"
    "\n   - Number each quote sequentially, starting from [1]."
    "\n   - Present each quote exactly as it appears in the original text, enclosed in quotation marks."
    "\n   - If no relevant quotes can be found, write 'No relevant quotes' instead."
    "\n   - Example format:"
    "\n     Relevant quotes:"
    "\n     [1] \"This is the first relevant quote from the document.\""
    "\n     [2] \"This is the second relevant quote from the document.\""

    "\n\n3. Formulating the Answer:"
    "\n   - Begin your answer with the heading 'Answer:' on a new line after the quotes."
    "\n   - Provide a clear, concise, and accurate answer to the question based on the information in the document."
    "\n   - Ensure your answer is comprehensive and addresses all aspects of the question."
    "\n   - Use information from the quotes to support your answer, but do not repeat them verbatim."
    "\n   - Maintain a logical flow and structure in your response."
    "\n   - Use clear and simple language, avoiding jargon unless it's necessary and explained."

    "\n\n4. Referencing Quotes in the Answer:"
    "\n   - Do not explicitly mention or introduce quotes in your answer (e.g., avoid phrases like 'According to quote [1]')."
    "\n   - Instead, add the bracketed number of the relevant quote at the end of each sentence or point that uses information from that quote."
    "\n   - If a sentence or point is supported by multiple quotes, include all relevant quote numbers."
    "\n   - Example: 'The company's revenue grew by 15% last year. [1] This growth was primarily driven by increased sales in the Asian market. [2][3]'"

    "\n\n5. Handling Uncertainty or Lack of Information:"
    "\n   - If the document does not contain enough information to fully answer the question, clearly state this in your answer."
    "\n   - Provide any partial information that is available, and explain what additional information would be needed to give a complete answer."
    "\n   - If there are multiple possible interpretations of the question or the document's content, explain this and provide answers for each interpretation if possible."

    "\n\n6. Maintaining Objectivity:"
    "\n   - Stick to the facts presented in the document. Do not include personal opinions or external information not found in the text."
    "\n   - If the document presents biased or controversial information, note this objectively in your answer without endorsing or refuting the claims."

    "\n\n7. Formatting and Style:"
    "\n   - Use clear paragraph breaks to separate different points or aspects of your answer."
    "\n   - Employ bullet points or numbered lists if it helps to organize information more clearly."
    "\n   - Ensure proper grammar, punctuation, and spelling throughout your response."
    "\n   - Maintain a professional and neutral tone throughout your answer."

    "\n\n8. Length and Depth:"
    "\n   - Provide an answer that is sufficiently detailed to address the question comprehensively."
    "\n   - However, avoid unnecessary verbosity. Aim for clarity and conciseness."
    "\n   - The length of your answer should be proportional to the complexity of the question and the amount of relevant information in the document."

    "\n\n9. Dealing with Complex or Multi-part Questions:"
    "\n   - For questions with multiple parts, address each part separately and clearly."
    "\n   - Use subheadings or numbered points to break down your answer if necessary."
    "\n   - Ensure that you've addressed all aspects of the question in your response."

    "\n\n10. Concluding the Answer:"
    "\n    - If appropriate, provide a brief conclusion that summarizes the key points of your answer."
    "\n    - If the question asks for recommendations or future implications, include these based strictly on the information provided in the document."

    "\n\nRemember, your goal is to provide a clear, accurate, and well-supported answer based solely on the content of the given document. "
    "Adhere to these instructions carefully to ensure a high-quality response that effectively addresses the user's query."
    )

    document_content =  f"Here is the document:  <document> {document} </document>"

    messages_API_body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": instructions,
                    "cache_control": {
                        "type": "ephemeral"
                    }
                },
                {
                    "type": "text",
                    "text": document_content,
                    "cache_control": {
                        "type": "ephemeral"
                    }
                },
                {
                    "type": "text",
                    "text": user_query
                },
            ]
        }
    ]
    }

    response = bedrock_runtime.invoke_model(
        body=json.dumps(messages_API_body),
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        accept="application/json",
        contentType="application/json"
    )
    response_body = json.loads(response.get("body").read())
    return response_body

def fetch_blog_content(url):
    """Fetch content from a URL"""
    response = requests.get(url)
    return response.text

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Chat with a document using Amazon Bedrock')
    parser.add_argument('--url', type=str, help='URL to fetch document content from')
    parser.add_argument('--file', type=str, help='Path to a file containing document content')
    parser.add_argument('--query', type=str, required=True, help='Question to ask about the document')
    
    args = parser.parse_args()
    
    # Get document content
    if args.url:
        document = fetch_blog_content(args.url)
    elif args.file:
        with open(args.file, 'r') as f:
            document = f.read()
    else:
        # Default example
        document = fetch_blog_content("https://aws.amazon.com/blogs/machine-learning/enhance-conversational-ai-with-advanced-routing-techniques-with-amazon-bedrock/")
    
    # Chat with the document
    response_body = chat_with_document(document, args.query)
    print(json.dumps(response_body, indent=2))

if __name__ == "__main__":
    main()