import click
import requests
import gzip
import json
from  fuzzywuzzy import process
import os
my_key = '1bcb08db89ac563aa5175e82001c0b1d'
output_file_path='outputfile.txt'


def load_names():
    
    '''file_path = 'city.list.json.gz'
    output_file_path = 'outputfile.txt'
    names=[]
    with gzip.open(file_path, 'rb') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            decoded_line = line.decode('utf-8')
            output_file.write(decoded_line)
    print(f"Data from {file_path} has been decoded and written to {output_file_path}")'''
    

    file_path = 'outputfile.txt'
    if os.path.exists(output_file_path):
       with open(file_path, 'r', encoding='utf-8') as file:
          data = json.load(file)
          names = [entry['name'] for entry in data]

       return names
    else:
        download_names()
        return load_names()
def download_names():
    file_path = 'city.list.json.gz'
    url = 'https://bulk.openweathermap.org/sample/city.list.json.gz'

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

        with gzip.open(file_path, 'rb') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                decoded_line = line.decode('utf-8')
                output_file.write(decoded_line)

        print(f"Data downloaded and decoded, written to {output_file_path}")
    else:
        print(f"Failed to download data. Error code: {response.status_code}")


'''def closest_location(input_location,names):
    match, score=process.extractOne(input_location,names)
    return match if score>=80 else none
closest_location()'''

'''def check_location_format(location ):
    
    return isinstance(location or a, tuple) and len(location or a ) == 2 and all(isinstance(s, str) for s in location )'''





@click.command()
@click.option('-L','--location',help="use double quotes if the location has 2 or more words")
@click.option('--list-locations',is_flag=True,help="list of all avilable options")
def weather(location,list_locations):
    

    if list_locations:
       
        names = load_names()
        for name in names:
            print(name)
        return


    if not location:
        click.echo("please provide a valid location")
        return
    names=load_names()
    '''words = location.split()
    if len(words) >= 2 and not (location.startswith('"') and location.endswith('"')):
        click.echo("Please provide the location in double quotes (e.g., \"New York\")")
        return'''
    
    

    a=None
    '''check_location_format(location)'''
    
    
    if location.lower() not in map(str.lower, names):
        '''click.echo("Not a valid location")'''
         
        def closest_location(location,names):
        
        
           match, score=process.extractOne(location,names)
           return match if score>=80 else none
        a=closest_location(location,names)
        
        '''print(f"please enter {a} instead of {location}")'''
        '''return'''
    url = f"http://api.openweathermap.org/data/2.5/weather?q={a  if a is not None else location}&appid={my_key}"

    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        display_weather_report(weather_data)
    else:
        click.echo(f"Failed to fetch data. Error code: {response.status_code}")
    '''def closest_location(location,names):
        
        
        match, score=process.extractOne(location,names)
        return match if score>=80 else none
   closest_location(location,names)'''
def display_weather_report(weather_data):
    
    click.echo(f"city: {weather_data['name']}")
    click.echo(f"sky: {weather_data['weather'][0]['description']}")
    click.echo(f"wind speed: {weather_data['wind']['speed']} m/s")
    click.echo(f"humidity: {weather_data['main']['humidity']} gm/m³")
    click.echo(f"Temperature: {round(weather_data['main']['temp']-273)}˚celsius ")
weather()
