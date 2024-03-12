import json

def write_json(filename, data):
    """JSON形式のデータを指定したファイルに書き込む関数"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def read_json(filename):
    """指定したJSONファイルからデータを読み込む関数"""
    with open(filename, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data

def clear_json_file(file_path):
    # ファイルを空文字列で上書きする
    with open(file_path, 'w') as f:
        f.write('')


# 書き込むデータ
data_to_write = {'key1': 'value1', 'key2': 'value2'}

# JSONファイルにデータを書き込む
write_json('data.json', data_to_write)

# JSONファイルからデータを読み込む
loaded_data = read_json('data.json')
print("Loaded data:", loaded_data)

# JSONファイルの内容を削除する
clear_json_file('data.json')
print("Content deleted.")
