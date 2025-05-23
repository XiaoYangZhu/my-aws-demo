from flask import Flask, request, session
from strands import Agent

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Initialize or restore agent conversation history from session
    if "messages" not in session:
        session["messages"] = []

    # Create agent with session state
    agent = Agent(messages=session["messages"])

    # Process message
    result = agent(user_message)

    # Update session with new messages
    session["messages"] = agent.messages

    # Return the agent's final message
    return {"response": result.message}