import csv

# 変数の準備
data = [
    ['名前', '年齢', '職業'],
    ['太郎', 30, 'エンジニア'],
    ['花子', 25, 'デザイナー'],
    ['次郎', 35, 'マネージャー']
]

# 変数をCSVファイルに書き込む関数
def write_to_csv(filename, data):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# CSVファイルから変数を読み込む関数
def read_from_csv(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data

# 変数をテキスト化してCSVファイルに書き込む
write_to_csv('data.csv', data)

# CSVファイルから変数を読み込む
loaded_data = read_from_csv('data.csv')
print("Loaded Data:")
for row in loaded_data:
    print(row)

# CSVファイルの中身を削除する
open('data.csv', 'w').close()
print("CSV file content deleted.")