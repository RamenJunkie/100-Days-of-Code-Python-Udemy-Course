import moment_house

calendar = []

calendar += moment_house.get_moment_house()

for each in calendar:
    print(f"{each.date} - {each.artist} - {each.venue}")