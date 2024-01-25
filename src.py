import requests #import request library
from datetime import datetime, timedelta

def get_github_stats(owner, repo, token):
    # Construct the base URL for the GitHub repository
    base_url = f'https://api.github.com/repos/{owner}/{repo}'

    # Set up headers for making authenticated requests to the GitHub API
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Fetch basic repository information
    repo_info = requests.get(base_url, headers=headers).json()

    # Fetch contributors information
    contributors_url = f'{base_url}/contributors'
    contributors = requests.get(contributors_url, headers=headers).json()

    # Fetch open issues information
    issues_url = f'{base_url}/issues'
    issues = requests.get(issues_url, headers=headers).json()

    # Fetch pull requests information
    prs_url = f'{base_url}/pulls'
    pull_requests = requests.get(prs_url, headers=headers).json()

    # Build a dictionary with relevant statistics
    stats = {
        'repository_name': repo_info['full_name'],
        'created_at': repo_info['created_at'],
        'updated_at': repo_info['updated_at'],
        'watchers_count': repo_info['watchers_count'],
        'forks_count': repo_info['forks_count'],
        'open_issues_count': repo_info['open_issues_count'],
        'contributors_count': len(contributors),
        'issues_count': len(issues),
        'pull_requests_count': len(pull_requests),
    }

    return stats

def main():
    # User input for GitHub repository details
    owner = input("Enter the GitHub repository owner: ")
    repo = input("Enter the GitHub repository name: ")
    token = input("Enter your GitHub personal access token: ")

    try:
        # Fetch GitHub statistics using the provided details
        stats = get_github_stats(owner, repo, token)

        # Display the fetched statistics
        print("\nGitHub Repository Stats:")
        for key, value in stats.items():
            print(f"{key.capitalize()}: {value}")

    except Exception as e:
        # Handle and display any errors that occur during the execution
        print(f"Error: {e}")

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()