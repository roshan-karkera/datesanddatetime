import datetime
import pytz

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Sydney",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific /Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}

print("Please choose a time zone (or 0 to quit):")
for place in sorted(available_zones):
    print("\t{}. {}".format(place, available_zones))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice],world_time.strftime('%A %x %X %z'),world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%a %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%a %x %X')))
        print()
