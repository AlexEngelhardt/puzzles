debug = False

if debug:
    filename = 'test_input'
else:
    filename = 'input'

with open(filename) as f:
    my_time = int(f.readline().strip())
    bus_IDs = f.readline().strip().split(',')
bus_IDs = list(map(int, [d for d in bus_IDs if d.isdigit()]))

print(my_time)
print(bus_IDs)

# "my_time % bus_id" would give the time *backwards* when the last bus departed.
# Subtract that from "bus_id" to get the time forwards. Then modulo it "bus_id" so that you wait 0 mins
# if the bus is there on this exact timestamp (instead of waiting for the next one):
n_minutes_wait = [(bus_id - (my_time % bus_id)) % bus_id for bus_id in bus_IDs]

best_wait_time = min(n_minutes_wait)
best_wait_i = n_minutes_wait.index(best_wait_time)
best_bus_ID = bus_IDs[best_wait_i]

print(f"bus {best_bus_ID}, waiting for {best_wait_time} mins => answer: {best_bus_ID * best_wait_time}")
