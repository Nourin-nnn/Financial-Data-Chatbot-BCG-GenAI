import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Expanded Financial Data for 2021, 2022, and 2023
financial_data = {
    "Microsoft": {
        "revenue": {
            "2021": "$168,088 million",
            "2022": "$198,270 million",
            "2023": "$211,915 million"
        },
        "net_income": {
            "2021": "$61,271 million",
            "2022": "$67,056 million",
            "2023": "$72,361 million"
        },
        "revenue_growth": {
            "2021-2022": "17.94%",
            "2022-2023": "-6.44%"
        },
        "net_income_growth": {
            "2021-2022": "9.45%",
            "2022-2023": "7.92%"
        },
        "total_assets": {
            "2021": "$333,779 million",
            "2022": "$364,840 million",
            "2023": "$411,976 million"
        },
        "total_liabilities": {
            "2021": "$183,007 million",
            "2022": "$192,562 million",
            "2023": "$205,753 million"
        },
        "cash_flow": {
            "2021": "$76,683 million",
            "2022": "$89,035 million",
            "2023": "$87,582 million"
        },
        "cash_flow_growth": {
            "2021-2022": "16.12%",
            "2022-2023": "-1.66%"
        }
    },
    "Tesla": {
        "revenue": {
            "2021": "$53,823 million",
            "2022": "$81,462 million",
            "2023": "$96,773 million"
        },
        "net_income": {
            "2021": "$5,519 million",
            "2022": "$17,717 million",
            "2023": "$14,974 million"
        },
        "revenue_growth": {
            "2021-2022": "51.35%",
            "2022-2023": "15.82%"
        },
        "net_income_growth": {
            "2021-2022": "221.11%",
            "2022-2023": "-15.94%"
        },
        "total_assets": {
            "2021": "$62,131 million",
            "2022": "$82,517 million",
            "2023": "$106,618 million"
        },
        "total_liabilities": {
            "2021": "$29,250 million",
            "2022": "$40,357 million",
            "2023": "$43,009 million"
        },
        "cash_flow": {
            "2021": "$11,497 million",
            "2022": "$14,912 million",
            "2023": "$13,256 million"
        },
        "cash_flow_growth": {
            "2021-2022": "29.67%",
            "2022-2023": "-11.07%"
        }
    },
    "Apple": {
        "revenue": {
            "2021": "$365,817 million",
            "2022": "$394,328 million",
            "2023": "$383,285 million"
        },
        "net_income": {
            "2021": "$94,680 million",
            "2022": "$94,374 million",
            "2023": "$96,995 million"
        },
        "revenue_growth": {
            "2021-2022": "7.79%",
            "2022-2023": "-2.88%"
        },
        "net_income_growth": {
            "2021-2022": "-0.32%",
            "2022-2023": "2.89%"
        },
        "total_assets": {
            "2021": "$351,002 million",
            "2022": "$352,755 million",
            "2023": "$352,583 million"
        },
        "total_liabilities": {
            "2021": "$287,912 million",
            "2022": "$289,735 million",
            "2023": "$290,437 million"
        },
        "cash_flow": {
            "2021": "$104,038 million",
            "2022": "$123,456 million",
            "2023": "$110,543 million"
        },
        "cash_flow_growth": {
            "2021-2022": "18.67%",
            "2022-2023": "-10.50%"
        }
    }
}

def simple_chatbot(user_query):
    for company, data in financial_data.items():
        if company in user_query:
            
            # Revenue Queries
            if "revenue" in user_query:
                if "growth" in user_query:
                    if "2021 to 2022" in user_query:
                        return f"{company}'s revenue growth from 2021 to 2022 was {data['revenue_growth']['2021-2022']}."
                    elif "2022 to 2023" in user_query:
                        return f"{company}'s revenue growth from 2022 to 2023 was {data['revenue_growth']['2022-2023']}."
                else:
                    for year, amount in data["revenue"].items():
                        if year in user_query:
                            return f"The total revenue for {company} in {year} is {amount}."

            # Net Income Queries
            if "net income" in user_query:
                if "growth" in user_query:
                    if "2021 to 2022" in user_query:
                        return f"{company}'s net income growth from 2021 to 2022 was {data['net_income_growth']['2021-2022']}."
                    elif "2022 to 2023" in user_query:
                        return f"{company}'s net income growth from 2022 to 2023 was {data['net_income_growth']['2022-2023']}."
                else:
                    for year, amount in data["net_income"].items():
                        if year in user_query:
                            return f"The net income for {company} in {year} is {amount}."

            # Total Assets Queries
            if "total assets" in user_query:
                for year, amount in data["total_assets"].items():
                    if year in user_query:
                        return f"The total assets for {company} in {year} is {amount}."

            # Total Liabilities Queries
            if "total liabilities" in user_query:
                for year, amount in data["total_liabilities"].items():
                    if year in user_query:
                        return f"The total liabilities for {company} in {year} is {amount}."

            # Cash Flow from Operating Activities Queries
            if "cash flow from operating activities" in user_query:
                if "growth" in user_query:
                    if "2021 to 2022" in user_query:
                        return f"{company}'s cash flow growth from 2021 to 2022 was {data['cash_flow_growth']['2021-2022']}."
                    elif "2022 to 2023" in user_query:
                        return f"{company}'s cash flow growth from 2022 to 2023 was {data['cash_flow_growth']['2022-2023']}."
                else:
                    for year, amount in data["cash_flow"].items():
                        if year in user_query:
                            return f"The cash flow from operating activities for {company} in {year} is {amount}."

    # Default response if the query isn't recognized
    return "Sorry, I can only provide information on predefined queries for Microsoft, Tesla, and Apple from 2021 to 2023."

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
    host = os.getenv('FLASK_HOST', '127.0.0.1')  # Default to localhost
    port = int(os.getenv('FLASK_PORT', 5000))     # Default to port 5000
    app.run(host=host, port=port, debug=True)
