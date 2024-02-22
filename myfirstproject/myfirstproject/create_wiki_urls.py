import json

# function to construct the wiki URL
def construct_wiki_url(name):
    parts = name.split()
    first_name = parts[0]
    last_name = "_".join(parts[1:])  # join all remaining parts as the last name
    return f"https://www.baseball-reference.com/bullpen/{first_name}_{last_name}"

# iterate through JSON file and construct the wiki URL
def process_mlb_player_data(input_file, output_file):
    # read the input JSON file
    with open(input_file, 'r') as file:
        players = json.load(file)

    # open the output file
    with open(output_file, 'w') as file:
        file.write('[')  # Start of the list

        for i, player in enumerate(players):
            name = player.get('name', '')  # get the player name
            player['wiki_url'] = construct_wiki_url(name)
            player.pop('html_body', None)  #cclean dictionary by removing html_body

            # serialize player dictionary to a JSON string
            player_json = json.dumps(player)
            
            # write the JSON string to the file
            if i > 0:
                file.write(',')
            file.write('\n' + player_json)

        file.write('\n]')

input_file = 'json_data/mlb_data.json'
output_file = 'json_data/mlb_data_with_urls.json'

process_mlb_player_data(input_file, output_file)
