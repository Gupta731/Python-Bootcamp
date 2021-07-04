import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    "Fur color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}
color_data = pandas.DataFrame(data_dict)
print(color_data)
color_data.to_csv('squirrel_color_count.csv')
