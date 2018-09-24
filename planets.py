def weight_on_planets():
   # write your code here
    weight = float(input("What do you weigh on earth? "))
    mars = weight * 0.38
    jupiter = weight * 2.34
    planet_weights = {"Mars": mars, "Jupiter": jupiter}
    for planet in planet_weights:
        print("On {} you would weigh {} pounds.".format(planet, planet_weights[planet]))


if __name__ == '__main__':
    weight_on_planets()