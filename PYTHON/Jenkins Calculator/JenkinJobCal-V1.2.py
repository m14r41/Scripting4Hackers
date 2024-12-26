import datetime
import csv
import os
import time
from colorama import Fore, Style, init
import requests

# Initialize colorama for colored output
init(autoreset=True)

# Jenkins connection details
JENKINS_URL = "url"
AUTH = ('username', 'token')  # Replace with Jenkins username and API token

# Function to get the crumb for CSRF protection
def get_crumb():
    crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    response = requests.get(crumb_url, auth=AUTH)
    if response.status_code == 200:
        return response.json()['crumb']
    else:
        print(f"{Fore.RED}Failed to get CSRF crumb: {response.status_code}{Fore.RESET}")
        return None

# Function to extract the Job Name from Jenkins job details
def get_job_name(job_url):
    # Fetch the job details using the Jenkins API
    crumb = get_crumb()
    if not crumb:
        return "Unknown Job Name"

    headers = {'Jenkins-Crumb': crumb}
    job_url = f"{job_url}/api/json"
    response = requests.get(job_url, auth=AUTH, headers=headers)
    if response.status_code == 200:
        job_data = response.json()
        return job_data.get('name', 'Unknown Job Name')
    else:
        print(f"{Fore.RED}Failed to fetch job details from {job_url}: {response.status_code}{Fore.RESET}")
        return "Unknown Job Name"

# Function to process a job and extract detailed build information from a specific start date
def process_job(job_url, start_date):
    crumb = get_crumb()
    if not crumb:
        return 0, [], [], "", ""  # No crumb, return 0 minutes, and empty lists

    headers = {'Jenkins-Crumb': crumb}
    try:
        job_url = f"{job_url}/api/json"
        response = requests.get(job_url, auth=AUTH, headers=headers)
        response.raise_for_status()
        job_data = response.json()

        total_minutes = 0
        minute_values = []  # To store individual build durations
        build_details = []  # To store detailed build info

        # Process each build in the job
        for build in job_data.get('builds', []):
            build_url = build['url']
            build_data = requests.get(f"{build_url}api/json", auth=AUTH, headers=headers).json()
            timestamp = build_data.get('timestamp', 0)  # Timestamp of the build
            build_date = datetime.datetime.fromtimestamp(timestamp / 1000)  # Convert to datetime object
            if build_date < start_date:  # Skip builds before the start date
                continue

            duration = build_data.get('duration', 0)  # Duration in milliseconds
            minutes = duration / 60000  # Convert milliseconds to minutes

            # Ensure even very small durations (like < 1 minute) are included
            if minutes < 0.1:
                minutes = 0  # Treat very small durations as 0 minutes

            build_number = build_data.get('number', 'Unknown')  # Build number
            build_status = build_data.get('result', 'Unknown')  # Build status (SUCCESS, FAILURE, etc.)

            # Append detailed information about the build
            build_details.append({
                'build_number': build_number,
                'status': build_status,
                'duration_minutes': int(minutes),  # Convert to integer
                'build_date': build_date.strftime('%Y-%m-%d %H:%M:%S')  # Save build date as string
            })

            # Append the integer duration for the minute values
            minute_values.append(int(minutes))  # Store as integer

            # Accumulate total time (as integer)
            total_minutes += int(minutes)

        # Generate build range (first and last build number)
        if len(build_details) > 0:
            build_range_start = build_details[0]['build_number']
            build_range_end = build_details[-1]['build_number']
        else:
            build_range_start = build_range_end = "Unknown"

        job_name = get_job_name(job_url)  # Fetch the actual job name dynamically

        return total_minutes, minute_values, build_details, f"{build_range_start} to {build_range_end}", job_name

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching job details: {e}{Fore.RESET}")
        return 0, [], [], "", ""  # Return 0 minutes if an error occurs

# Function to list folders recursively and process jobs
def list_folders(folder_url, start_date, level=0, results=None):
    crumb = get_crumb()
    if not crumb:
        return

    headers = {'Jenkins-Crumb': crumb}
    try:
        folder_url = f"{folder_url}/api/json"
        response = requests.get(folder_url, auth=AUTH, headers=headers)
        response.raise_for_status()
        folder_data = response.json()

        for index, item in enumerate(folder_data.get('jobs', [])):
            job_url = item['url']
            indent = "  " * level  # Indentation based on the folder depth
            print(f"{indent}{Fore.CYAN}[{index + 1}] - {job_url}{Fore.RESET}")

            # Process and display job information
            total_minutes, minute_values, build_details, build_range, job_name = process_job(job_url, start_date)
            total_entries = len(minute_values)

            # Sum the extracted minutes for Total Duration
            extracted_minutes_str = ' + '.join([str(min_val) for min_val in minute_values])

            # Display formatted job information with improved readability
            print(f"{indent}  {Fore.WHITE}Job Name   : {Style.BRIGHT} {job_name}{Fore.RESET}")
            print(f"{indent}  {Fore.WHITE}Build Range: {Style.BRIGHT} {build_range} ({total_entries} entries){Fore.RESET}")
            print(f"{indent}  {Fore.WHITE}Extracted Minute Values: {Style.BRIGHT} {extracted_minutes_str}{Fore.RESET}")
            print(f"{indent}  {Fore.WHITE}Total Sum of Minutes   : {Style.BRIGHT} {total_minutes} minutes{Fore.RESET}")
            print(f"{indent}  {Fore.WHITE}Time in Hours: {Style.BRIGHT} {total_minutes / 60:.2f} hours{Fore.RESET}")
            print(f"{indent}  {Fore.WHITE}Total Entries: {Style.BRIGHT} {total_entries}{Fore.RESET}")

            # Save the job details to results
            results.append({
                'job_url': job_url,
                'job_name': job_name,
                'build_range': build_range,
                'extracted_minutes': extracted_minutes_str,
                'total_minutes': total_minutes,
                'time_in_hours': total_minutes / 60,
                'total_entries': total_entries
            })

        # Check for subfolders (if they have 'jobs')
        for subfolder in folder_data.get('jobs', []):
            if 'url' in subfolder:
                subfolder_url = subfolder['url']
                # Check for subfolders (if they contain jobs)
                subfolder_response = requests.get(f"{subfolder_url}/api/json", auth=AUTH, headers=headers).json()
                if 'jobs' in subfolder_response:  # If it contains jobs, it's a subfolder
                    print(f"{indent}{Fore.RED}> {subfolder_url}")
                    list_folders(subfolder_url, start_date, level + 1, results)

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching folder details: {e}{Fore.RESET}")

def save_to_csv(results, folder_name):
    csv_filename = f"{folder_name}/builds.csv"
    os.makedirs(folder_name, exist_ok=True)
    with open(csv_filename, 'w', newline='') as file:
        fieldnames = ['job_url', 'job_name', 'build_range', 'extracted_minutes', 'total_minutes', 'time_in_hours', 'total_entries']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    print(f"{Fore.GREEN}CSV file saved as {csv_filename}{Fore.RESET}")

def save_to_html(results, folder_name):
    html_filename = f"{folder_name}/builds.html"
    os.makedirs(folder_name, exist_ok=True)
    with open(html_filename, 'w') as file:
        file.write("<html><body><h1>Build Information</h1><table border='1'>")
        file.write("<tr><th>Job URL</th><th>Job Name</th><th>Build Range</th><th>Extracted Minutes</th><th>Total Minutes</th><th>Time in Hours</th><th>Total Entries</th></tr>")
        for result in results:
            file.write(f"<tr><td>{result['job_url']}</td><td>{result['job_name']}</td><td>{result['build_range']}</td><td>{result['extracted_minutes']}</td><td>{result['total_minutes']}</td><td>{result['time_in_hours']:.2f}</td><td>{result['total_entries']}</td></tr>")
        file.write("</table></body></html>")
    print(f"{Fore.GREEN}HTML file saved as {html_filename}{Fore.RESET}")

def main():
    # Ask the user for the start date
    start_date_str = input(f"{Fore.CYAN}Enter the start date (YYYY-MM-DD): {Fore.RESET}")
    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    except ValueError:
        print(f"{Fore.RED}Invalid date format. Please use YYYY-MM-DD.{Fore.RESET}")
        return

    # Define root folder
    root_folder = f"{JENKINS_URL}/job/testing2"

    print(f"\n{Fore.CYAN}Fetching data from {start_date_str} to today...{Fore.RESET}")
    
    start_time = time.time()  # Start time for report duration
    results = []
    list_folders(root_folder, start_date, results=results)

    # Get the report duration (time taken for the script to run)
    end_time = time.time()
    report_duration = f"{end_time - start_time:.2f} seconds"

    # Save results to CSV and HTML with the new columns
    folder_name = start_date_str
    save_to_csv(results, folder_name)
    save_to_html(results, folder_name)

    print(f"\n{Fore.CYAN}Report generated in {report_duration}{Fore.RESET}")

if __name__ == "__main__":
    main()
