# Jobbly - API Endpoint Integrated with LLM (OpenAI)
### Abstract: <br>
Jobbly is an API endpoint named, designed to assist job seekers and career enthusiasts. Integrated with the LLM (Large Language Model) from OpenAI, Jobbly offers a comprehensive set of features to provide valuable job-related information and resources. With Jobbly, users can access various endpoints to receive personalized job recommendations, explore necessary skills for different roles, discover salary ranges, and gain access to curated resources such as books, free online courses, and paid Udemy courses. With its seamless integration of the OpenAI LLM, Jobbly empowers users with the insights they need to make informed career decisions and take the next steps towards their professional success.
### API Link:
https://jobbly-65re.onrender.com <br> (Deployed on Render)
### Routes: <br>
(All these POST Requests can be tested on Postman) <br><br>
/ : This is the default route of the Flask app. It simply returns the message "Welcome to the API!" when you access the root URL<br>
/api : This route handles POST requests. It expects a JSON payload with a "message" field which expects skills of the user and then the response contains a JSON object with a list of recommended jobs.<br>
/jobs/links : The response contains a JSON array with dictionaries that include the job title and the corresponding Indeed job link.<br>
/jobs/skills : The response contains a JSON array with dictionaries that include the job title and a list of necessary skills.<br>
/jobs/salary : The response contains a JSON array with dictionaries that include the job title and the salary range<br>
/resources/books : The response contains a JSON array with dictionaries that include the job title and a list of recommended books.<br>
/resources/freecourses : The response contains a JSON array with dictionaries that include the job title and the YouTube URL.<br>
/resources/paidcourses : The response contains a JSON array with dictionaries that include the job title and the Udemy URL.<br>
