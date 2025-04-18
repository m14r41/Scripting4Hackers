import datetime
import csv
import os
import time
from colorama import Fore, Style, init
import requests

# Initialize colorama for colored output
init(autoreset=True)

# Jenkins connection details
JENKINS_URL = ""
AUTH = ('user', 'token')  # Replace with Jenkins username and API token

# Log file path
LOG_FILE = "script_log.txt"

# Function to log messages to a file
def log(message):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")
    print(message)  # Print the message to the console as well

# Function to get the crumb for CSRF protection
def get_crumb():
    crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    response = requests.get(crumb_url, auth=AUTH)
    if response.status_code == 200:
        return response.json()['crumb']
    else:
        log(f"{Fore.RED}Failed to get CSRF crumb: {response.status_code}{Fore.RESET}")
        return None

# Function to extract the Job Name from Jenkins job details
def get_job_name(job_url):
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
        log(f"{Fore.RED}Failed to fetch job details from {job_url}: {response.status_code}{Fore.RESET}")
        return "Unknown Job Name"

# Function to process a job and extract detailed build information from a specific date range
def process_job(job_url, start_date, end_date):
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

        for build in job_data.get('builds', []):
            build_url = build['url']
            build_data = requests.get(f"{build_url}api/json", auth=AUTH, headers=headers).json()
            timestamp = build_data.get('timestamp', 0)
            build_date = datetime.datetime.fromtimestamp(timestamp / 1000)

            # Process builds within the specified date range
            if build_date < start_date or build_date > end_date:
                continue

            duration = build_data.get('duration', 0)
            minutes = duration / 60000
            if minutes < 0.1:
                minutes = 0

            build_number = build_data.get('number', 'Unknown')
            build_status = build_data.get('result', 'Unknown')

            build_details.append({
                'build_number': build_number,
                'status': build_status,
                'duration_minutes': int(minutes),
                'build_date': build_date.strftime('%Y-%m-%d %H:%M:%S')
            })

            minute_values.append(int(minutes))
            total_minutes += int(minutes)

        build_range_start = build_details[0]['build_number'] if build_details else "Unknown"
        build_range_end = build_details[-1]['build_number'] if build_details else "Unknown"

        job_name = get_job_name(job_url)
        return total_minutes, minute_values, build_details, f"{build_range_start} to {build_range_end}", job_name

    except requests.exceptions.RequestException as e:
        log(f"{Fore.RED}Error fetching job details: {e}{Fore.RESET}")
        return 0, [], [], "", ""  # Return 0 minutes if an error occurs

# Function to list folders recursively and process jobs
def list_folders(folder_url, start_date, end_date, level=0, results=None, filtered_results=None):
    crumb = get_crumb()
    if not crumb:
        return

    headers = {'Jenkins-Crumb': crumb}
    try:
        folder_url = f"{folder_url}/api/json"
        response = requests.get(folder_url, auth=AUTH, headers=headers)
        response.raise_for_status()
        folder_data = response.json()

        # Extract the full folder URL (this is now the full folder URL, not just an API endpoint)
        full_folder_url = folder_url.replace("/api/json", "")
        indent = "  " * level

        # Log folder name with full URL and the > symbol
        log(f"{indent}{Fore.RED}> {full_folder_url}{Fore.RESET}")

        for index, item in enumerate(folder_data.get('jobs', [])):
            job_url = item['url']
            log(f"{indent}  {Fore.CYAN} [{index + 1}] - {job_url}{Fore.RESET}")  # Subfolders and jobs printed with -

            total_minutes, minute_values, build_details, build_range, job_name = process_job(job_url, start_date, end_date)
            total_entries = len(minute_values)
            extracted_minutes_str = ' + '.join([str(min_val) for min_val in minute_values])

            log(f"{indent}  {Fore.WHITE} Job Name     :{Style.BRIGHT} {job_name}{Fore.RESET}")
            log(f"{indent}  {Fore.WHITE} Build Range  :{Style.BRIGHT} {build_range} ({total_entries} entries){Fore.RESET}")
            log(f"{indent}  {Fore.WHITE} Build Minutes:{Style.BRIGHT} {extracted_minutes_str} {Fore.RESET}")
            log(f"{indent}  {Fore.WHITE} Total Minutes:{Style.BRIGHT} {total_minutes} minutes{Fore.RESET}")
            log(f"{indent}  {Fore.WHITE} Time in Hours:{Style.BRIGHT} {total_minutes / 60:.2f} hours{Fore.RESET}")

            results.append({
                'job_url': job_url,
                'job_name': job_name,
                'build_range': build_range,
                'total_entries': total_entries,
                'extracted_minutes': extracted_minutes_str,
                'total_minutes': total_minutes,
                'time_in_hours': total_minutes / 60
            })

            # Filtered results: Include only jobs with non-empty "Extracted Minutes"
            if extracted_minutes_str.strip():
                filtered_results.append({
                    'job_url': job_url,
                    'job_name': job_name,
                    'build_range': build_range,
                    'total_entries': total_entries,
                    'extracted_minutes': extracted_minutes_str,
                    'total_minutes': total_minutes,
                    'time_in_hours': total_minutes / 60
                })

        # Recursively process any subfolders
        for subfolder in folder_data.get('jobs', []):
            if 'url' in subfolder:
                subfolder_url = subfolder['url']
                subfolder_response = requests.get(f"{subfolder_url}/api/json", auth=AUTH, headers=headers).json()
                if 'jobs' in subfolder_response:
                    list_folders(subfolder_url, start_date, end_date, level + 1, results, filtered_results)

    except requests.exceptions.RequestException as e:
        log(f"{Fore.RED}Error fetching folder details: {e}{Fore.RESET}")

def save_to_csv(results, folder_name, filename="builds.csv"):
    csv_filename = f"{folder_name}/{filename}"
    os.makedirs(folder_name, exist_ok=True)
    with open(csv_filename, 'w', newline='') as file:
        fieldnames = ['job_url', 'job_name', 'build_range', 'total_entries', 'extracted_minutes', 'total_minutes', 'time_in_hours']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    log(f"{Fore.GREEN}CSV file saved as {csv_filename}{Fore.RESET}")

def save_to_html(results, folder_name):
    html_filename = f"{folder_name}/builds.html"
    os.makedirs(folder_name, exist_ok=True)
    with open(html_filename, 'w') as file:
        file.write("<html><body><h1>Build Information</h1><table border='1'>")
        file.write("<tr><th>Job URL</th><th>Job Name</th><th>Build Range</th><th>Total Entries</th><th>Extracted Minutes</th><th>Total Minutes</th><th>Time in Hours</th></tr>")
        for result in results:
            file.write(f"<tr><td>{result['job_url']}</td><td>{result['job_name']}</td><td>{result['build_range']}</td><td>{result['total_entries']}</td><td>{result['extracted_minutes']}</td><td>{result['total_minutes']}</td><td>{result['time_in_hours']:.2f}</td></tr>")
        file.write("</table></body></html>")
    log(f"{Fore.GREEN}HTML file saved as {html_filename}{Fore.RESET}")

def main():
    log("Script started.")
    
    start_date_str = input(f"{Fore.CYAN}Enter the start date (YYYY-MM-DD) or leave blank for default (14 days ago): {Fore.RESET}")
    if start_date_str.strip() == "":
        start_date = datetime.datetime.now() - datetime.timedelta(days=14)  # Default to 14 days ago
    else:
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        except ValueError:
            log(f"{Fore.RED}Invalid start date format. Please use YYYY-MM-DD.{Fore.RESET}")
            return

    end_date_str = input(f"{Fore.CYAN}Enter the end date (YYYY-MM-DD) or leave blank for today: {Fore.RESET}")
    if end_date_str.strip() == "":
        end_date = datetime.datetime.now()
    else:
        try:
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            log(f"{Fore.RED}Invalid end date format. Please use YYYY-MM-DD.{Fore.RESET}")
            return

    # Prompt for root folder with a default value
    root_folder_input = input(f"{Fore.CYAN}Enter the root folder (leave blank for default 'testing2'): {Fore.RESET}")
    root_folder = f"{JENKINS_URL}/job/{root_folder_input.strip() if root_folder_input.strip() else 'testing2'}"
    
    results = []
    filtered_results = []
    list_folders(root_folder, start_date, end_date, results=results, filtered_results=filtered_results)

    folder_name = f"{start_date.strftime('%Y-%m-%d')}_to_{end_date.strftime('%Y-%m-%d')}_builds"
    
    # Save the 3 CSVs
    save_to_csv(results, folder_name)  # All data
    save_to_csv(filtered_results, folder_name, filename="filtered_builds.csv")  # Filtered data with non-empty "Extracted Minutes"
    
    save_to_html(results, folder_name)

    log(f"{Fore.GREEN}Report generation complete!{Fore.RESET}")

if __name__ == "__main__":
    main()
