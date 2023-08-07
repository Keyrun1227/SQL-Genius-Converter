from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_text_to_sql_output(input_text):
    url = "https://toolske.com/text2sql/php/generatesql.php"
    # Set up the headers to simulate a user request with Chrome user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    # Form data to send in the POST request
    form_data = {
        "sql-query": input_text,
    }
    try:
        # Send a POST request to the website with the form data
        response = requests.post(url, headers=headers, data=form_data)

        # Parse the JSON response
        json_data = response.json()

        # Check if the response was successful
        if json_data.get("success", False):
            sql_output = json_data.get("sql", "")
            return sql_output.strip()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        output_text = get_text_to_sql_output(input_text)
        return jsonify({'output': output_text})
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)