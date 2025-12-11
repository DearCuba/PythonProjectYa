hour = int(input())
minute = int(input())
delivery_time = int(input())

clock_hour = (hour + (minute + delivery_time) // 60) % 24
clock_minute = (minute + delivery_time) % 60

print(f"{(clock_hour):02}"f":{clock_minute:02}")
#print(f'{clock_hour // 10}{clock_hour % 10}:{clock_minute // 10}{clock_minute % 10}')


