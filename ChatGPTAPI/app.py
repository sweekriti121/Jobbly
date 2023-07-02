from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load the environment variables from the .env file
load_dotenv()

# Set up OpenAI API credentials
api_key = os.getenv("API_KEY")
openai.api_key = api_key

# Define the default route to return the index.html file
@app.route("/")
def index():
    return "Welcome to the API!"

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")

    # Send the message to OpenAI's API and receive the response
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"
    
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100,
        n=6,  # Generate 6 job titles
        stop=None,  # Let the model generate the job titles without a specific stop token
        temperature=0.7  # Controls the randomness of the output. Lower values make it more focused, higher values make it more random.
    )

    # Extract the generated job titles from the response
    job_titles = completion.choices[0].text.strip().split("\n")

    # Create a JSON response
    response = {
        "job_titles": job_titles
    }

    # Return the JSON response
    return jsonify(response)

@app.route("/jobs/links", methods=["POST"])
def get_job_links():
    # Get the message from the POST request
    message = request.json.get("message")
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"
    
    # Send the message to OpenAI's API and receive the response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100,
        n=6
    )

    # Extract the generated text from the response
    generated_text = completion.choices[0].text.strip()

    # Split the generated text into individual job titles
    job_titles = generated_text.split("\n")

    # Create a list to store job title, link, necessary skills, and additional skills
    job_data = []

    # Retrieve necessary and additional skills for each job title
    for title in job_titles:
        url_job_title = "+".join(title.split())
        indeed_url = f"https://in.indeed.com/jobs?q={url_job_title}"
        # Create a dictionary to store job data
        job_dict = {
            "job_title": title,
            "job_link": indeed_url,
        }

        # Add job data to the list
        job_data.append(job_dict)

    return jsonify(job_data)

@app.route("/jobs/skills", methods=["POST"])
def get_job_skills():
    # Get the message from the POST request
    message = request.json.get("message")
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"
    
    # Send the message to OpenAI's API and receive the response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100,
        n=6
    )

    # Extract the generated text from the response
    generated_text = completion.choices[0].text.strip()

    # Split the generated text into individual job titles
    job_titles = generated_text.split("\n")

    # Create a list to store job title, link, necessary skills, and additional skills
    job_data = []

    # Retrieve necessary and additional skills for each job title
    for title in job_titles:
        # Formulate prompt to retrieve necessary and additional skills
        skills_prompt = f"What are the necessary and additional skills required for a {title}?"

        # Send the prompt to OpenAI's API and receive the response
        skills_completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=skills_prompt,
            max_tokens=100,
            n=1
        )
        # Extract the generated text from the response
        skills_text = skills_completion.choices[0].text.strip()
        # Split the generated text into necessary and additional skills
        skills_list = skills_text.split("Necessary Skills:")
        necessary_skills = skills_list[1].strip().split("\n") if len(skills_list) > 1 else []
        # Remove empty lines from the necessary skills list
        necessary_skills = [skill for skill in necessary_skills if skill]
        # Create a dictionary to store job data
        job_dict = {
            "job_title": title,
            "necessary_skills": necessary_skills,
        }

        # Add job data to the list
        job_data.append(job_dict)
    return jsonify(job_data)

@app.route("/jobs/salary", methods=["POST"])
def get_job_salary():
    # Get the message from the POST request
    message = request.json.get("message")
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"
    
    # Send the message to OpenAI's API and receive the response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100,
        n=6
    )

    # Extract the generated text from the response
    generated_text = completion.choices[0].text.strip()

    # Split the generated text into individual job titles
    job_titles = generated_text.split("\n")

    # Create a list to store job title, link, necessary skills, and additional skills
    job_data = []

    # Retrieve necessary and additional skills for each job title
    for title in job_titles:
        # Formulate prompt to retrieve necessary and additional skills
        salary_prompt = f"Give upper limit and lower limit of salary required for a {title}?Give in this format - lowerlimitval - upperlimitval"

        # Send the prompt to OpenAI's API and receive the response
        salary_completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=salary_prompt,
            max_tokens=100,
            n=1
        )
        # Extract the generated text from the response
        salary_text = salary_completion.choices[0].text.strip()
        # Create a dictionary to store job data
        job_dict = {
            "job_title": title,
            "salary_range": salary_text,
        }

        # Add job data to the list
        job_data.append(job_dict)
    return jsonify(job_data)

@app.route("/resources/books", methods=["POST"])
def get_resource_books():
    # Get the message from the POST request
    message = request.json.get("message")
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"

    # Send the message to OpenAI's API and receive the response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100,
        n=6
    )

    # Extract the generated text from the response
    generated_text = completion.choices[0].text.strip()
    
    # Split the generated text into individual job titles
    job_titles = generated_text.split("\n")
    
    # Create a list to store job title, link, necessary skills, and additional skills
    job_data = []

    # Retrieve necessary and additional skills for each job title
    for title in job_titles:
        # Formulate prompt to retrieve necessary and additional skills
        resourcebook_prompt = f"Give 5 best books required for a {title}?"

        # Send the prompt to OpenAI's API and receive the response
        resourcebook_completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=resourcebook_prompt,
            max_tokens=100,
            n=1
        )

        # Extract the generated text from the response
        resourcebook_text = resourcebook_completion.choices[0].text.strip()
        
        # Split the generated text into individual book titles
        book_titles = resourcebook_text.split("\n")
        
        # Create a dictionary to store job data
        resource_dict = {
            "job_title": title,
            "resource_books": book_titles,
        }

        # Add job data to the list
        job_data.append(resource_dict)

    return jsonify(job_data)

@app.route("/resources/freecourses", methods=["POST"])
def get_resources_free():
    # Get the message from the POST request
    message = request.json.get("message")
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"

    # Send the message to OpenAI's API and receive the response
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100,
        n=6
    )

    # Extract the generated text from the response
    generated_text = completion.choices[0].text.strip()

    # Split the generated text into individual job titles
    job_titles = generated_text.split("\n")

    # Create a list to store job title, courses, necessary skills, and additional skills
    job_data = []

    # Retrieve courses for each job title
    for title in job_titles:
        # Formulate YouTube search URL for the job title
        url_job_title = "+".join(title.split())
        youtube_url = f"https://www.youtube.com/results?search_query=playlists+for+{url_job_title}"

        # Create a dictionary to store job data
        resource_dict = {
            "job_title": title,
            "youtube_url": youtube_url,
        }

        # Add job data to the list
        job_data.append(resource_dict)

    return jsonify(job_data)

@app.route("/resources/paidcourses", methods=["POST"])
def get_resources_paid():
    # Get the message from the POST request
    message = request.json.get("message")
    augmented_message = f"{message} - recommend 6 jobs for these skills without any description only the job titles and each in a new line"
    # Send the message to OpenAI's API and receive the response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=augmented_message,
        max_tokens=100
    )

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    # Split the generated text into individual job titles
    job_titles = generated_text.split("\n")

    # Create a list to store job title and link pairs
    udemy_links = []

    # Convert each job title to a valid URL format and create the corresponding job link
    for title in job_titles:
        url_job_title = "+".join(title.split())
        udemy_url = f"https://www.udemy.com/courses/search/?q={url_job_title}"
        udemy_links.append({"job_title": title, "udemy_link": udemy_url})

    return jsonify(udemy_links)

if __name__ == "__main__":
    app.run(debug=True)