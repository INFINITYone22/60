import threading
import time
import requests

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded {filename} successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")

def main():
    urls = [
        ("https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif", "file1.gif"),
        ("https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif", "file2.gif"),
        ("https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif", "file3.gif")
    ]

    threads = []
    for url, filename in urls:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
