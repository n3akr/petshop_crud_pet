import requests
import json
import sys
import random

# Test data
url = "http://petstore.swagger.io/v2/pet"
headers = {'Content-Type': "application/json"}
pet_id = random.randint(1,999)

# Payload for create pet
data = {
    "id": pet_id,
    "category": {
        "id": 1,
        "name": "cats"
    },
    "name": "Boil",
    "photoUrls": [
        "http://image.test/" + str(pet_id) + ".jpg"
    ],
    "tags": [
        {
            "id": 1,
            "name": "tag1"
        }
    ],
    "status": "available"
}

# Payload for update
new_data = {
    "id": pet_id,
    "category": {
        "id": 1,
        "name": "cats"
    },
    "name": "Boil",
    "photoUrls": [
        "http://image.test/" + str(pet_id*2) + ".jpg"
    ],
    "tags": [
        {
            "id": 2,
            "name": "tag2"
        }
    ],
    "status": "sold"
}


# Create pet
def test_create_pet():
    """Create pet test: """
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        assert response.status_code == 200, "Status code is {}".format(response.status_code)
        assert response.json() == data
    # Handling exceptions
    except requests.exceptions.HTTPError as errh:
        print ("HTTP error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Connection error:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout error", errt)
    except requests.exceptions.RequestException as err:
        print ("Other error", err)


# Find pet
def test_get_pet():
    """Find pet test: """
    try:
        response = requests.get(url + str(pet_id), headers=headers)
        response.raise_for_status()
        assert response.status_code == 200, "Status code is {}".format(response.status_code)
        assert response.json() == data
    # Handling exceptions
    except requests.exceptions.HTTPError as errh:
        print ("HTTP error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Connection error:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout error", errt)
    except requests.exceptions.RequestException as err:
        print ("Other error", err)


# Update pet
def test_update_pet():
    """Update pet test: """
    try:
        response = requests.put(url, data=json.dumps(new_data), headers=headers)
        response.raise_for_status()
        assert response.status_code == 200, "Status code is {}".format(response.status_code)
        assert json.loads(response.content) == new_data
    # Handling exceptions
    except requests.exceptions.HTTPError as errh:
        print ("HTTP error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Connection error:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout error", errt)
    except requests.exceptions.RequestException as err:
        print ("Other error", err)

# Delete pet
def test_delete_pet():
    """Delete pet test: """
    try:
        response = requests.delete(url + str(pet_id), headers=headers)
        response.raise_for_status()
        assert response.status_code == 200, "Status code is {}".format(response.status_code)
        assert json.loads(response.content) == new_data
    # Handling exceptions
    except requests.exceptions.HTTPError as errh:
        print ("HTTP error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Connection error:", errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout error", errt)
    except requests.exceptions.RequestException as err:
        print ("Other error", err)


methods = [test_create_pet(), test_get_pet(), test_update_pet(), test_delete_pet()]


def main():
    for m in methods:
        m()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exit")
        sys.exit(0)




