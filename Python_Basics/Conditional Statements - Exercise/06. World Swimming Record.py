records = float(input())
distance = float(input())
time_sek_for_one_m = float(input())
time = distance * time_sek_for_one_m
total_time = (int(distance / 15) * 12.5) + time
if total_time < records:
    print(f'Yes, he succeeded! The new world record is {abs(total_time):.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(total_time - records):.2f} seconds slower.')
