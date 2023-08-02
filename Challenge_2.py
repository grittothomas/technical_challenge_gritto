import requests
import json

def get_instance_metadata():
    metadata_url = "http://169.254.169.254/latest/meta-data/"
    
    try:
        response = requests.get(metadata_url)
        response.raise_for_status()
        metadata = response.text.splitlines()
        return metadata
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_instance_metadata_json():
    metadata = get_instance_metadata()
    if metadata:
        metadata_dict = {}
        for item in metadata:
            item_url = f"http://169.254.169.254/latest/meta-data/{item}"
            try:
                response = requests.get(item_url)
                response.raise_for_status()
                metadata_dict[item] = response.text
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                metadata_dict[item] = None
        return json.dumps(metadata_dict, indent=4)
    else:
        return None

def get_specific_metadata_key(key):
    metadata_url = f"http://169.254.169.254/latest/meta-data/{key}"
    
    try:
        response = requests.get(metadata_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    instance_metadata = get_instance_metadata_json()
    if instance_metadata:
        print("Instance Metadata:")
        print(instance_metadata)
        
        specific_key = "instance-id"
        specific_value = get_specific_metadata_key(specific_key)
        if specific_value:
            print(f"\nValue of '{specific_key}': {specific_value}")
