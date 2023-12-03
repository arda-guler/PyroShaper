import math
import tkinter as tk
import time
import matplotlib.pyplot as plt

from mesh import *

def generate_tubular_grain(msh):
    for c in msh.cells:
        if (msh.Nx/2)**2 >= (c.x - msh.Nx/2)**2 + (c.y - msh.Ny/2)**2 >= (msh.Nx*0.3)**2:
            c.fuel = 100

def ignite_tubular_grain(msh):
    for c in msh.cells:
        if c.fuel > 0:
            c.active = True
            if c.get_burn_rate(msh) > 0 and (msh.Nx*0.45)**2 >= (c.x - msh.Nx/2)**2 + (c.y - msh.Ny/2)**2:
                c.active = True
            else:
                c.active = False

def generate_cocentric_grain(msh):
    for c in msh.cells:
        if (msh.Nx*0.5)**2 > (c.x - msh.Nx/2)**2 + (c.y - msh.Ny/2)**2:
            c.fuel = 100
            if (msh.Nx*0.3)**2 >= (c.x - msh.Nx/2)**2 + (c.y - msh.Ny/2)**2 >= (msh.Nx*0.2)**2:
                c.fuel = 0

def ignite_tubular_grain(msh):
    for c in msh.cells:
        if c.fuel > 0:
            c.active = True
            if c.get_burn_rate(msh) > 0 and (msh.Nx*0.45)**2 >= (c.x - msh.Nx/2)**2 + (c.y - msh.Ny/2)**2:
                c.active = True
            else:
                c.active = False

def simulate(msh, dt):
    root = tk.Tk()
    root.title("Solid ")
    cvas = tk.Canvas(root, width=900, height=590, bg="black")
    cvas.grid(row=0, column=0, rowspan=15, columnspan=5)

    thrusts = []
    times = []
    fuels = []

    running = True
    time = 0
    cycle = 0
    while running:
        # PHYSICS
        for c in msh.cells:
            c.update(msh, dt)

        fuel = 0
        thrust = 0
        for c in msh.cells:
            fuel += c.fuel
            thrust += c.get_burn_rate(msh)

        if fuel == 0:
            running = False

        times.append(time)
        thrusts.append(thrust)
        fuels.append(fuel)

        # GRAPHICS
        for c in msh.cells:
            if c.fuel > 0:
                if not c.active:
                    fill_color = "gray"
                #elif c.get_burn_rate(msh) > 0:
                else:
                    fill_color = "red"

                cvas.create_oval(c.x*3-2 + 200, c.y*3-2 + 150, c.x*3+2 + 200, c.y*3+2 + 150, fill=fill_color)
                
        cvas.create_text(250, 50, text="Time: "+str(time), fill="red")
        cvas.create_text(250, 70, text="Fuel: "+str(fuel), fill="red")
        cvas.create_text(250, 90, text="Thrust: "+str(thrust), fill="red")

        root.update()
        cvas.delete("all")
        # time.sleep(dt)
        cycle += 1
        time = cycle * dt

    root.destroy()

    plt.plot(times, thrusts)
    plt.title("Thrust Profile")
    plt.xlabel("Time")
    plt.ylabel("Thrust")
    plt.grid()
    plt.show()
    
    plt.plot(times, fuels)
    plt.title("Fuel Mass Profile")
    plt.xlabel("Time")
    plt.ylabel("Fuel")
    plt.grid()
    plt.show()
