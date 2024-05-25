from json import loads
from datetime import datetime
from requests import get


# paste in your personal URL or read it from a token file
try:
    with open("token", "r") as tokenfile:
        token = tokenfile.read()
except:
    print("You need to have your token in a file called 'token' or hardcode it into the script")
    exit

emftalks = loads(get("https://www.emfcamp.org/favourites.json?token="+token).text)

# or if you've downloaded your file, point to it here and comment out the lines above
#emftalks = json.loads(open("emftalks.json", 'r').read())

# this function converts the venue names into mermaid tags to give a bit of colour to the chart
def venuemap(venue):
    if venue == "Stage A":
        mermaidtag = "crit, "
    elif venue == "Stage B":
        mermaidtag = "active, "
    elif venue == "Stage C":
        mermaidtag = ""
    else:
        mermaidtag = "done, "
    return mermaidtag

# I want to get the raw JSON into an ordered dictionary for plotting
scheduledict = {}

for index in range(len(emftalks)):
    start_date = datetime.strptime(emftalks[index]["start_date"], "%Y-%m-%d %H:%M:%S")
    duration = datetime.strptime(emftalks[index]["end_date"], "%Y-%m-%d %H:%M:%S") - start_date
    scheduledict[start_date] = {"title": emftalks[index]["title"].split(":")[0], # colons mess up mermaid, plus the titles are too long to render nicely
                                "venue": emftalks[index]["venue"],
                                "speaker": emftalks[index]["speaker"],
                                "description": emftalks[index]["description"],
                                "duration": f"{duration.seconds/60:.0f}", # convert seconds into minutes
                                "day": start_date.strftime("%A"), # we use the day to divide up the sections
                                "daytime": start_date.strftime("%a %d, %H:%M")}


with open("readme.md", "w") as fname:
    fname.write("# EMF Camp Schedule Viewer\nOnce you have got your link to your favourite talks/workshops from [EMF 2024 Line-up](https://www.emfcamp.org/schedule/2024), clone/fork this repo, modify the code, and run it to generate your personal gantt chart. Github uses [Mermaid.js](http://mermaid.js.org/syntax/gantt.html) to render the code block, so you can visualise the output by committing the repo back to github.\n\n")
    fname.write("```mermaid\ngantt\n    title Your EMF Camp Schedule\n    dateFormat YYYY-MM-DD HH:mm\n    axisFormat %a %H:%M\n") # mermaid preamble
    sections = [] # we give each day its own section
    for key in sorted(scheduledict):
        if scheduledict[key]["day"] not in sections:
            fname.write("    section "+scheduledict[key]["day"]+"\n")
            sections.append(scheduledict[key]["day"]) # make sure we don't keep adding in the section line every time
        # generate the mermaid string for each event
        # indentation, title, optional venue colour/tag, start time, duration
        fname.write("      "+scheduledict[key]["title"]+"  :"+venuemap(scheduledict[key]["venue"])+key.strftime("%Y-%m-%d %H:%M")+", "+scheduledict[key]["duration"]+"m\n")
    fname.write("```")

# magic date for the start of 2024 EMF Camp
previouskey = datetime(2024, 5, 31, 10, 0)
previousvenue = "Stage A"
# print out a more informative schedule for you
for key in sorted(scheduledict):
    if scheduledict[key]["venue"] != previousvenue:
        print("You need to walk to",scheduledict[key]["venue"])
    else:
        print("Stay where you are.")
    print("\n")
    print(scheduledict[key]["title"])
    print("by",scheduledict[key]["speaker"])
    print(scheduledict[key]["venue"],"on",scheduledict[key]["daytime"],"for",scheduledict[key]["duration"],"mins")
    print(scheduledict[key]["description"])
    previouskey = key
    previousvenue = scheduledict[key]["venue"]