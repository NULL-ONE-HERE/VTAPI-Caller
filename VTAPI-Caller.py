import vt

def check_vt_connection(api_key):
    """Check the VirusTotal API connection"""
    try:
        with vt.Client(api_key) as client:
            print("Connected to VirusTotal API was successful.")
    except vt.APIError as e:
        print("Failed to connect to VirusTotal API. Error:", e)

    client.close()

if __name__ == '__main__':
    api_key = '<API KEY>'
    check_vt_connection(api_key)
