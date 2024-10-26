from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simple Financial Data Chatbot Logic
def simple_chatbot(user_query):
    # Responses based on predefined queries
    if user_query == "What is the total revenue for Microsoft in 2023?":
        return "The total revenue for Microsoft in 2023 is $211,915 million."
    elif user_query == "What is the total revenue for Tesla in 2023?":
        return "The total revenue for Tesla in 2023 is $96,773 million."
    elif user_query == "What is the total revenue for Apple in 2023?":
        return "The total revenue for Apple in 2023 is $383,285 million."
    elif user_query == "How has net income changed for Microsoft from 2022 to 2023?":
        return "Microsoft's net income decreased by 15.76% from 2022 to 2023."
    elif user_query == "How has net income changed for Tesla from 2022 to 2023?":
        return "Tesla's net income decreased by 15.94% from 2022 to 2023."
    elif user_query == "How has net income changed for Apple from 2022 to 2023?":
        return "Apple's net income decreased by 5.13% from 2022 to 2023."
    elif user_query == "What is the trend in total assets for Microsoft from 2021 to 2023?":
        return "Microsoft experienced a decrease of 11.44% in total assets from 2021 to 2022 and an additional 8.51% decrease in 2023."
    elif user_query == "What is the trend in total assets for Tesla from 2021 to 2023?":
        return "Tesla's total assets decreased by 22.77% from 2022 to 2023."
    elif user_query == "What is the trend in total assets for Apple from 2021 to 2023?":
        return "Apple's total assets showed negligible growth of 0.05% from 2022 to 2023."
    elif user_query == "What is the cash flow from operating activities for Microsoft in 2023?":
        return "Microsoft's cash flow from operating activities in 2023 is $87,582 million."
    elif user_query == "What is the cash flow from operating activities for Tesla in 2023?":
        return "Tesla's cash flow from operating activities in 2023 is $13,256 million."
    elif user_query == "What is the cash flow from operating activities for Apple in 2023?":
        return "Apple's cash flow from operating activities in 2023 is $110,543 million."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chat requests
@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.form['query']
    response = simple_chatbot(user_query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
