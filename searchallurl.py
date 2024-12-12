import requests
import json
import sys
import subprocess
from urllib.parse import urlparse

invalid_extensions = ['.json', '.js', '.fnt', '.ogg', '.css', '.jpg', '.jpeg', '.png', '.svg', 'img', 
                      '.gif', '.exe', '.mp4', '.flv', '.pdf', '.doc', '.ogv', '.webm', '.wmv', '.webp', '.mov', '.mp3']

def get_urls_from_archive(user_input):
    print(f"Sending request to web.archive.org for {user_input}")
    url = f"https://web.archive.org/cdx/search/cdx?url={user_input}/*&output=json&collapse=urlkey"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        archive_urls = set()
        for entry in data:
            extracted_url = entry[2]
            parsed_url = urlparse(extracted_url)
            if not any(parsed_url.path.endswith(ext) for ext in invalid_extensions):
                archive_urls.add(extracted_url)
        return archive_urls
    else:
        print(f"Failed to get data from web.archive.org. Status code.": {response.status_code}")
        return set()


def get_urls_from_gau(user_input):
    print(f"Running the gau tool for {user_input}")
    try:
        gau_switches = []  # you can set gau switches ["--theards","1"]
        gau_output = subprocess.check_output(["gau"] + gau_switches + [user_input], text=True)
        gau_urls = set(gau_output.splitlines())
        final_urls = set()
        for url in gau_urls:
            parsed_url = urlparse(url)
            if not any(parsed_url.path.endswith(ext) for ext in invalid_extensions):
                final_urls.add(url)
        return final_urls
    except subprocess.CalledProcessError as e:
        print(f"Error executing command gau: {e}")
        return set()


def get_user_input_from_stdin():
    input_data = sys.stdin.read().strip().splitlines()
    if not input_data:
        print("Please enter the sites input.")
        sys.exit(1)
    return input_data


def ask_output_choice():
    if len(sys.argv) < 2:
        print("Please specify an input parameter for how to save:")
        print("y: save in separate files for each site")
        print("n: Save in a single file")
        sys.exit(1)
    
    choice = sys.argv[1].strip().lower() 
    if choice not in ['y', 'n']:
        print("The entry is not valid! Use the 'y' or 'n' parameter.")
        sys.exit(1)

    return choice == 'y' 


def main():
    sites = get_user_input_from_stdin()  

 
    separate_files = ask_output_choice()  

    
    for site in sites:
        print(f"\nExtracting URLs from{site} ...")
        archive_urls = get_urls_from_archive(site)
        gau_urls = get_urls_from_gau(site)

    
        all_urls = archive_urls.union(gau_urls)
        print(f"Number of URLs extracted from {site}: {len(all_urls)}")

        
        if separate_files:
            output_file = f"{site}_urls.txt"
        else:
            output_file = "combined_urls.txt"

         
        if all_urls:
            with open(output_file, "a") as combined_file:
                for url in all_urls:
                    combined_file.write(url + "\n")
            print(f"All URLs saved in {output_file}.")
        else:
            print(f"No URL found for {site}.")


if __name__ == "__main__":
    main()
