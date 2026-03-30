import math
import random


def get_locations(file_name):
    loc_list = []
    try:
        f = open(file_name, "r")
        lines = f.readlines()

        for line in lines:
            parts = line.split(",")
            city_name = parts[0].strip()
            city_x = float(parts[1].strip())
            city_y = float(parts[2].strip())

            loc_list.append((city_name, city_x, city_y))

        f.close()
    except FileNotFoundError:
        print("File not found! Please check the name and try again.")
        return []

    return loc_list


def get_distance(c1, c2):
    x_diff = c1[1] - c2[1]
    y_diff = c1[2] - c2[2]

    dist = math.sqrt(x_diff**2 + y_diff**2)
    return dist


def calc_total_dist(route):
    total = 0

    for i in range(len(route) - 1):
        total = total + get_distance(route[i], route[i + 1])

    total = total + get_distance(route[-1], route[0])

    return total


def optimize_route(locations):
    curr_route = locations.copy()
    random.shuffle(curr_route)
    curr_dist = calc_total_dist(curr_route)

    best_route = curr_route.copy()
    best_dist = curr_dist

    temp = 10000.0
    cooling = 0.995

    for i in range(10000):
        new_route = curr_route.copy()

        index1 = random.randint(0, len(new_route) - 1)
        index2 = random.randint(0, len(new_route) - 1)

        new_route[index1], new_route[index2] = new_route[index2], new_route[index1]

        new_dist = calc_total_dist(new_route)

        if new_dist < curr_dist:
            curr_route = new_route
            curr_dist = new_dist

            if new_dist < best_dist:
                best_route = new_route.copy()
                best_dist = new_dist
        else:
            diff = new_dist - curr_dist
            prob = math.exp(-diff / temp)

            if random.random() < prob:
                curr_route = new_route
                curr_dist = new_dist

        temp = temp * cooling

    return best_route, best_dist


if __name__ == "__main__":
    print("Logistics Route Optimizer Tool")
    print("------------------------------")

    fname = input("Enter file name (e.g., locations.txt): ")
    my_locations = get_locations(fname)

    if len(my_locations) > 0:
        print("\nCalculating best route... please wait.")

        start_route = my_locations.copy()
        start_dist = calc_total_dist(start_route)

        final_route, final_dist = optimize_route(my_locations)

        print("\nOptimization Finished.")
        print("Starting random distance: " + str(round(start_dist, 2)))
        print("AI optimized distance: " + str(round(final_dist, 2)))

        print("\nBest Route found:")
        for stop in final_route:
            print(stop[0] + " -> ", end="")

        print(final_route[0][0])
