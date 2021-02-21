def sun_angle(time:str):
  hour, minute = time.split(':')
  if 360 <= int(hour) * 60 + int(minute) <= 1080:
    return (int(hour) - 6) * 15 + 15/60 * int(minute)
  else:
    return "I don't see the sun!"

print(sun_angle('18:01'))