from flask import Flask , render_template , request
import datetime
from datetime import datetime
import numpy as np
import pandas as pd
import pickle

app =Flask(__name__ , template_folder="templates")
model = pickle.load(open("model/flight-fare-prediction.pkl", 'rb'))
X_train = pd.read_csv("data/cleaned_data/X_train.csv")

@app.route("/home/" , methods=["GET" , "POST"])
def home():
    kwargs = {}
    if request.method == "POST":
        source = request.form["Source"]
        destination = request.form["Destination"]
        airline = request.form["Airline"]
        date_of_journey = request.form["Date_of_Journey"]
        departure_time = request.form["dep_time"]
        total_stops = request.form["Total Stops"]

        date_of_journey = datetime.strptime(date_of_journey , "%Y-%m-%d")
        journey_day = date_of_journey.day
        journey_month = date_of_journey.month
        journey_weekday = date_of_journey.weekday()
        season = date_of_journey.month %12 // 3 + 1
        journey_season = season
        dep_hour = int(departure_time.split(":")[0])
        dep_min = int(departure_time.split(":")[1])

        #------Source--------#
        if source == "Delhi":
            Source = 3377
        elif source == "Kolkata":
            Source = 2159
        elif source == "Banglore":
            Source = 1589
        elif source == "Mumbai":
            Source = 529
        elif source == "Chennai":
            Source = 287
        #------Destination--------#
        if destination == "Cochin":
            Destination = 3377
        elif destination == "Banglore":
            Destination = 2159
        elif destination == "Delhi":
            Destination = 935
        elif destination == "New Delhi":
            Destination = 654
        elif destination == "Hyderabad":
            Destination = 529
        elif destination == "Kolkata":
            Destination = 287
        #------Airline--------#
        if airline == "Jet Airways":
            Airline = 2866
        elif airline == "IndiGo":
            Airline = 1530
        elif airline == "Air India":
            Airline = 1294
        elif airline == "Multiple carriers":
            Airline = 880
        elif airline == "SpiceJet":
            Airline = 629
        elif airline == "Vistara":
            Airline = 355
        elif airline == "Air Asia":
            Airline = 238
        elif airline == "GoAir":
            Airline = 136
        elif airline == "Multiple carriers Premium economy":
            Airline = 10
        elif airline == "Vistara Premium economy":
            Airline = 2
        elif airline == "Trujet":
            Airline = 1

        #-----Total Stops----#
        if total_stops == "non-stop":
            Total_Stops = 1
        elif total_stops == "1 stop":
            Total_Stops = 2
        elif total_stops == "2 stops":
            Total_Stops = 3
        elif total_stops == "3 stops":
            Total_Stops = 4
        elif total_stops == "4 stops":
            Total_Stops = 5

        #-----Month------#
        if journey_month == 3:
            Month_March = 1
            Month_May = 0
            Month_June = 0
        elif journey_month == 4:
            Month_March = 0
            Month_May = 0
            Month_June = 0
        elif journey_month == 5:
            Month_March = 0
            Month_May = 1
            Month_June = 0
        elif journey_month == 6:
            Month_March = 0
            Month_May = 0
            Month_June = 1
        
        #-----Season------#
        if journey_season == 2:
            Season_Summer = 0
        elif journey_season == 3:
            Season_Summer = 1

        #-----Day--------#
        Day_Sin = round(np.sin(journey_day * (2 * np.pi / 10)) , 2)
        Day_Cos = round(np.cos(journey_day * (2 * np.pi / 10)) , 2)
        
        #-----Weekday--------#
        Weekday_Sin = round(np.sin(journey_weekday * (2 * np.pi / 7)) , 2)
        Weekday_Cos = round(np.cos(journey_weekday * (2 * np.pi / 7)) , 2)
        
        #-----Departure Hour--------#
        Dep_Hour_Sin = round(np.sin(dep_hour * (2 * np.pi / 24)) , 2)
        Dep_Hour_Cos = round(np.cos(dep_hour * (2 * np.pi / 24)) , 2)
        
        #-----Departure Minute--------#
        Dep_Min_Sin = round(np.sin(dep_min * (2 * np.pi / 12)) , 2)
        Dep_Min_Cos = round(np.cos(dep_min * (2 * np.pi / 12)) , 2)
        
        prediction = model.predict([[Airline , Source , Destination , Total_Stops,
                                    Month_June , Month_March , Month_May,
                                    Season_Summer , Dep_Hour_Sin , Dep_Hour_Cos,
                                    Dep_Min_Sin, Dep_Min_Cos , Day_Sin , Day_Cos , 
                                    Weekday_Sin , Weekday_Cos]])
        price = round(prediction[0][1])
        duration = round(prediction[0][0])
        hour = duration // 60
        minute = duration - (hour * 60)
        
        duration_time = datetime.strptime(str(hour) + ":" + str(minute) , "%H:%M")
        departure_time = datetime.strptime(departure_time , "%H:%M")
        origin_time = datetime.strptime("00:00", "%H:%M")
        arrival_time = (departure_time -  origin_time + duration_time).time()

        kwargs = {
            "price":price,
            "hour":hour,
            "minute":minute,
            "arrival_time":arrival_time,
        }
    return render_template("template.html" , **kwargs)    

if __name__=="__main__":
    app.run(debug=True)