import json
from database import initialize_database, store_data


if __name__ == '__main__':
    initialize_database()

    with open("test.json") as f:
        conversation = json.load(f)

    store_data(conversation["conv_name"],
               conversation["conv_id"],
               conversation["user"],
               conversation["messages"],)
