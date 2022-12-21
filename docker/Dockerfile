# should start with torch but it uses conda. fuck conda
FROM pytorch/pytorch:latest

#Set the working directory
WORKDIR /usr/src/app

# clone shit
RUN apt-get -y update
# I am gonna get fucked for this. and not in a good way
COPY WeatherRecognition .
COPY tokens.py ./web_weather/
RUN ls

# install dependencies. should install torch separately for caching, but i am lazy
RUN pip3 install -r ./web_weather/requirements.txt

#Expose the required port
WORKDIR /usr/src/app/web_weather
EXPOSE 5000

#Run the command
CMD ["python", "server.py"]
