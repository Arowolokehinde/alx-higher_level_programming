This repository contains Bash scripts and Python code for performing various network-related tasks. Below is a summary of the scripts available in this repository along with their descriptions and usage instructions.

Scripts Overview
get_body_size.sh

Description: Bash script that takes in a URL as an argument, sends a request to that URL using cURL, and displays the size of the body of the response in bytes.
Usage: ./get_body_size.sh URL
get_response_body.sh

Description: Bash script that takes in a URL as an argument, sends a GET request to the URL using cURL, and displays the body of the response.
Usage: ./get_response_body.sh URL
send_delete_request.sh

Description: Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
Usage: ./send_delete_request.sh URL
get_accepted_methods.sh

Description: Bash script that takes in a URL as an argument and displays all HTTP methods the server will accept.
Usage: ./get_accepted_methods.sh URL
get_response_with_header.sh

Description: Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. It also sends a header variable X-School-User-Id with the value 98.
Usage: ./get_response_with_header.sh URL
send_post_request.sh

Description: Bash script that takes in a URL as an argument, sends a POST request to the passed URL, and displays the body of the response. It sends two variables email with the value test@gmail.com and subject with the value I will always be here for PLD.
Usage: ./send_post_request.sh URL

