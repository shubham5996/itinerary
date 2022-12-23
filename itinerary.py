import datetime
import streamlit as st
import random


class Activity:
    def __init__(self, name, date_start, date_end, time_start, time_end, duration, desc, price):
        self.name = name;
        self.date_start = date_start;
        self.date_end = date_end
        self.time_start = time_start
        self.time_end = time_end
        self.desc = desc 
        self.price = price
        self.duration = duration

museum = Activity("Dholbaha Museum", (1, 1), (12, 31), (9, 0), (18, 0), 3, "DholbahaMuseum", "Free")
temple = Activity("Radha Krishna Temple", (1, 1), (12, 31), (9, 0), (12, 0), 2, "Pilgrimage", "Free")
boating = Activity("Boating", (5, 1), (10, 31), (16, 0), (18, 0), 2, "Boating Masti", "Rs 150/person")
nursery = Activity("Nursery", (1, 1), (12, 31), (9, 0), (18, 0), 3, "Get some plants!", "Free")
safari = Activity("Jungle Safari", (1, 1), (12, 31), (9, 0), (12, 0), 2, "Exoplore caves!", "Rs 450/person")
treks = Activity("Trekking", (1, 1), (12, 31), (9, 0), (15, 0), 2, "Trekking Masti", "Free")
waterfall = Activity("Waterfall", (1, 1), (12, 31), (9, 0), (18, 0), 2, "Waterfall dekho", "Free")
mangoes = Activity("Nani Bagh", (3, 1), (8, 31), (9, 0), (18, 0), 3, "Mango masti", "Free")
fair = Activity("Holi Mela", (2, 1), (4, 30), (9, 0), (18, 0), 5, "Janaudi Village", "Free")
bonfire = Activity("Bonfire", (10, 1), (2, 28), (21, 0), (3, 0), 2, "Bonfire", "Free")

activities = [museum, temple, boating, nursery, safari, treks, fair, waterfall, mangoes, bonfire]
# times user can input - 7 am to 11 pm, diff of 1 hour
start = "7:00"
end = "23:00"
allowedtimes = []
start = now = datetime.datetime.strptime(start, "%H:%M")
end = datetime.datetime.strptime(end, "%H:%M")
while now != end:
    allowedtimes.append(str(now.strftime("%H:%M")))
    now += datetime.timedelta(hours=1)
allowedtimes.append(end.strftime("%H:%M"))




st.title("Itinerary Generator")
with st.form("itinierary"):
    date_in = st.date_input("Which day are you arriving at Hoshiarpur?")
    time_in = st.selectbox("When are you arriving?", allowedtimes)

    date_out = st.date_input("Which day are you leaving Hoshiarpur?")
    time_out = st.selectbox("When are you leaving?", allowedtimes)
    submitted = st.form_submit_button()
    if submitted:
        time_in = datetime.datetime.strptime(time_in, "%H:%M")
        time_out = datetime.datetime.strptime(time_out, "%H:%M")
        ranges = {}
        start = datetime.datetime(day = date_in.day, month=date_in.month, year = date_in.year, hour=time_in.hour, second=0)
        end = datetime.datetime(day = date_out.day, month= date_out.month, year =date_in.year, hour=time_out.hour, second=0)
        now = start
        while now != end:
            ranges[now] = None
            now += datetime.timedelta(hours=1)

        filteredactivites = []
        for activity in activities:
            date_first = datetime.date(day=activity.date_start[1], month=activity.date_start[0], year=date_in.year)
            date_last = datetime.date(day=activity.date_end[1], month=activity.date_end[0], year=date_in.year + 1 if activity.name == "Bonfire" else date_in.year)
            if  date_first <= date_in <= date_last:
                filteredactivites.append(activity)
        # for key, val in ranges.items():
        #     if key.hour in range(0, 8):
        #         ranges[key] = "SLEEP"
        for key, val in ranges.items():
            if key.hour in (20, 21):
                ranges[key] = "Dinner"
        l1 = [safari, treks]
        if datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in + datetime.timedelta(days=1)).day, hour=9, minute=0) in ranges.keys():
            c1 = random.choice(l1)
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in  + datetime.timedelta(days=1)).day, hour=9, minute=0)] = c1
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in  + datetime.timedelta(days=1)).day, hour=10, minute=0)] = c1
            l1.remove(c1)
        if datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=9, minute=0) in ranges.keys():
            c1 = random.choice(l1)
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=9, minute=0)] = c1
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=10, minute=0)] = c1

        l2 = [boating, museum]
        if datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in + datetime.timedelta(days=1)).day, hour=12, minute=0) in ranges.keys():
            c2 = random.choice(l2)
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in  + datetime.timedelta(days=1)).day, hour=12, minute=0)] = c2
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in  + datetime.timedelta(days=1)).day, hour=13, minute=0)] = c2
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=(date_in  + datetime.timedelta(days=1)).day, hour=14, minute=0)] = c2
            l2.remove(c2)
        if datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=12, minute=0) in ranges.keys():
            c2 = random.choice(l2)
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=12, minute=0)] = c2
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=13, minute=0)] = c2
            ranges[datetime.datetime(year=date_in.year, month=date_in.month, day=date_in.day, hour=14, minute=0)] = c2
        
        b = False 

        for activity in filteredactivites:
            if activity.name == "Bonfire":
                b = True
        if b:
            for key, val in ranges.items():
                if key.hour == 22 or key.hour == 23:
                    ranges[key] = bonfire
        m = False
        for activity in filteredactivites:
            if activity.name == "Nani Bagh":
                m = True
        if m:
            for key, val in ranges.items():
                if key.hour in (16, 17, 18):
                    if key.day == date_in.day:
                        ranges[key] = mangoes
                    else:
                        ranges[key] = temple
            
        else:
            l3 =  [temple, nursery]
            c3 = random.choice(l3)
            for key, val in ranges.items():
                if key.hour in (16, 17, 18):
                    if key.day == date_in.day:
                        ranges[key] = l3[0]
                    else:
                        ranges[key] = l3[1]
        for key, val in ranges.items():
            if key.hour == 8:
                ranges[key] = "Breakfast"
        new = {}
        for key, val in ranges.items():
            if val != None:
                new[key] = val
        ranges = new
        formattime = "%M %d, %Y %H:%M"
        for key, val in ranges.items():
            if type(val) == Activity:
                st.write(key, val.name)
            else:
                st.write(key, val)



            





            
  
