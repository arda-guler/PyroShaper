# PyroShaper
Solid rocket propellant grain burn profile approximator.

It uses a simple cartesian 2D mesh of fuel "particles" to simulate the burning of a solid rocket fuel grain. Solid fuels' thrust is dependent on the surface area that undergoes combustion, and this simulation simply uses that fact.

Either increase the mesh size a lot and burn your CPU (burn, lol) or take the results with a grain of salt (haha, "grain", get it? :D). 

All properties and dimensions are unitless. This is not a program to design the fuel grain. This is a program to pick the grain shape for the desired burn profile.

### Example: Simple Tubular Grain

Towards the end of the burn, there are some inaccuracies between the "ideal" real case and the simulation due to the imperfect burn surface propagation of the simulated grain. (I used an insufficient mesh.)

![tubular_grain](https://github.com/arda-guler/PyroShaper/assets/80536083/c5090741-3043-43cb-b915-4cae6b031cf2)

![tubular_thrust](https://github.com/arda-guler/PyroShaper/assets/80536083/f72f298c-fab3-43c7-8df0-1fc6e12b0eff)

![tubular_mass](https://github.com/arda-guler/PyroShaper/assets/80536083/a889a972-bbc6-445e-b942-8714af6cd1d2)

### Example: Cocentric Grain

Towards the end of the burn, there are some inaccuracies between the "ideal" real case and the simulation due to the imperfect burn surface propagation of the simulated grain. (I used an insufficient mesh.)

![cocentric_grain](https://github.com/arda-guler/PyroShaper/assets/80536083/3317f412-dd90-47a4-8abc-23d0c00dbbec)

![cocentric_thrust](https://github.com/arda-guler/PyroShaper/assets/80536083/e342712d-bf08-4bf7-9c35-cc07b8cf3c54)

![cocentric_mass](https://github.com/arda-guler/PyroShaper/assets/80536083/9f8cf34a-947a-40b9-94e1-e4023f2ea6a0)
