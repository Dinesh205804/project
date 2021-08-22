from tkinter import *

root = Tk()
root.title("Information")
root.geometry("1700x800")
bg = PhotoImage(file="image\solarbig3.png")

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = Frame(root)
frame.pack(side=LEFT, anchor="nw")

heading = Label(frame, text='''Solar System''', fg="black", bg="grey", width="500", height="1", font="10")
heading.pack(side=TOP)

e = Label(root, text='''The Solar System is the Sun and all the objects that orbit around it. The Sun is orbited by
                planets, asteroids, comets and other things. The Solar System is about 4.6 billion years old. ... 
                Most of this matter gathered in the center, and the rest flattened into an orbiting disk that became 
                the Solar System.''', fg="black", bg="grey", width="500", height="1", font="10")

e.pack(side=BOTTOM)


def Sun_temp():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Temperature")
    c = Label(top, text='''Temperature''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface temperature: 5,778 K Trending''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Sun_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 1.989 × 10^30 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Sun_Age():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Age")
    c = Label(top, text='''Age of Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Age: 4.603 billion years''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Sun_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 696,340 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Sun_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Earth''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance to Earth: 149.6 million km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Sun():
    root1 = Tk()
    root1.title("Sun")
    root1.geometry("960x250")

    frame1 = Frame(root1)
    frame1.pack(side=LEFT, anchor="nw")

    b = Label(frame1, text='''Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''\nThe Sun is the star at the center of the Solar System. It is a nearly perfect sphere of
     hot plasma,heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as visible 
     light, ultraviolet light, and infrared radiation. It is by far the most important source of energy for life on 
     Earth. Its diameter is about 1.39 million kilometres (864,000 miles), or 109 times that of Earth. Its mass is about
     330,000 times that of Earth; it accounts for about 99.86% of the total mass of the Solar System.[20] Roughly three 
     quarters of the Sun's mass consists of hydrogen (~73%); the rest is mostly helium (~25%), with much smaller 
     quantities of heavier elements, including oxygen, carbon, neon and iron.[21]

       ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button1_1 = Button(frame1, text="temp", command=Sun_temp, width="20", height="2", bg="grey")
    button1_1.pack(side=LEFT)

    button1_2 = Button(frame1, text="Mass", command=Sun_Mass, width="20", height="2", bg="grey")
    button1_2.pack(side=LEFT)

    button1_3 = Button(frame1, text="Age", command=Sun_Age, width="20", height="2", bg="grey")
    button1_3.pack(side=LEFT)

    button1_4 = Button(frame1, text="Radius", command=Sun_Radius, width="20", height="2", bg="grey")
    button1_4.pack(side=LEFT)

    button1_5 = Button(frame1, text="Distance", command=Sun_Distance, width="20", height="2", bg="grey")
    button1_5.pack(side=LEFT)

    root1.mainloop()


button1 = Button(frame, text="SUN", command=Sun, width="20", height="2", bg="grey")

button1.pack(side=LEFT)


# start  of code for Mercury


def Mercury_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 57.91 million km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mercury_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Mercury''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 3.285 × 10^23 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mercury_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Mercury''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 74.8 million km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mercury_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Mercury''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 88 days''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mercury_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of day")
    c = Label(top, text='''Day length of Mercury''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 58d 15h 30m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mercury_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Mercury''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 2,439.7 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mercury():
    root2 = Tk()
    root2.title("Mercury")
    root2.iconbitmap()
    root2.geometry("960x300")

    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")

    b = Label(frame1, text='''Mercury''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''\nMercury is the smallest planet in the Solar System and the closest to the Sun. 
    Its orbit around the Sun takes 87.97 Earth days, the shortest of all the Sun's planets. 
    It is named after the Roman god Mercurius (Mercury), god of commerce, messenger of the gods, and mediator between gods and mortals, 
    corresponding to the Greek god Hermes. Like Venus, Mercury orbits the Sun within Earth's orbit as an inferior planet, 
    and its apparent distance from the Sun as viewed from Earth never exceeds 28°. 
    This proximity to the Sun means the planet can only be seen near the western horizon after sunset or the eastern horizon before sunrise,
     usually in twilight. At this time, it may appear as a bright star-like object but is often far more difficult to observe than Venus. 
     From Earth, the planet telescopically displays the complete range of phases, similar to Venus and the Moon, 
     which recurs over its synodic period of approximately 116 days.
     
     ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button2_1 = Button(frame1, text="Distance", command=Mercury_Distance, width="20", height="2", bg="grey")
    button2_1.pack(side=LEFT)

    button2_2 = Button(frame1, text="Mass", command=Mercury_Mass, width="20", height="2", bg="grey")
    button2_2.pack(side=LEFT)

    button2_3 = Button(frame1, text="Surface Area", command=Mercury_SurfaceArea, width="20", height="2", bg="grey")
    button2_3.pack(side=LEFT)

    button2_4 = Button(frame1, text="Orbital Period", command=Mercury_OrbitalPeriod, width="20", height="2", bg="grey")
    button2_4.pack(side=LEFT)

    button2_5 = Button(frame1, text="Length of Day", command=Mercury_LengthOfDay, width="20", height="2", bg="grey")
    button2_5.pack(side=LEFT)

    button2_6 = Button(frame1, text="Radius", command=Mercury_Radius, width="20", height="2", bg="grey")
    button2_6.pack(side=LEFT)

    root2.mainloop()


button2 = Button(frame, text="MERCURY", command=Mercury, width="20", height="2", bg="grey")
button2.pack(side=LEFT)


def Venus_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 108.2 million km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Venus_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Venus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 4.867 × 10^24 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Venus_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Venus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 460.2 million km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Venus_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Venus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 225 days''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Venus_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of day")
    c = Label(top, text='''Day length of Venus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 116d 18h 0m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Venus_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Venus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 6,051.8 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Venus():
    root2 = Tk()
    root2.title("Venus")
    root2.geometry("960x290")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Venus''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''\nVenus is the second planet from the Sun. It is named after the Roman goddess of love and
     beauty. As the brightest natural object in Earth's night sky after the Moon, Venus can cast shadows and can be, on 
     rare occasions, visible to the naked eye in broad daylight. Venus lies within Earth's orbit, and so never 
     appears to venture far from the Sun, either setting in the west just after dusk or rising in the east a little 
     while before dawn. Venus orbits the Sun every 224.7 Earth days. It has a synodic day length of 117 Earth days 
     and a sidereal rotation period of 243 Earth days. As a consequence, it takes longer to rotate about its axis than 
     any other planet in the Solar System, and does so in the opposite direction to all but Uranus. This means the Sun 
     rises in the west and sets in the east.Venus does not have any moons, a distinction it shares only with 
     Mercury among the planets in the Solar System

      ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button3_1 = Button(frame1, text="Distance", command=Venus_Distance, width="20", height="2", bg="grey")
    button3_1.pack(side=LEFT)

    button3_2 = Button(frame1, text="Mass", command=Venus_Mass, width="20", height="2", bg="grey")
    button3_2.pack(side=LEFT)

    button3_3 = Button(frame1, text="Surface Area", command=Venus_SurfaceArea, width="20", height="2", bg="grey")
    button3_3.pack(side=LEFT)

    button3_4 = Button(frame1, text="Orbital Period", command=Venus_OrbitalPeriod, width="20", height="2", bg="grey")
    button3_4.pack(side=LEFT)

    button3_5 = Button(frame1, text="Length of Day", command=Venus_LengthOfDay, width="20", height="2", bg="grey")
    button3_5.pack(side=LEFT)

    button3_6 = Button(frame1, text="Radius", command=Venus_Radius, width="20", height="2", bg="grey")
    button3_6.pack(side=LEFT)

    root2.mainloop()


button3 = Button(frame, text="VENUS", command=Venus, width="20", height="2", bg="grey")
button3.pack(side=LEFT)


def Earth_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 149.6 million km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Earth_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Earth''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 5.972 × 10^24 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Earth_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Earth''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 510.1 million km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Earth_Age():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Age")
    c = Label(top, text='''Age of Earth''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Age: 4.543 billion years''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Earth_Population():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Population")
    c = Label(top, text='''Population of Human Being in Earth''', fg="black", bg="grey", width="500", height="1",
              font="10")
    c.pack()
    b = Label(top, text='''Population: 7.674 billion''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Earth_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Earth''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 6,371 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Earth():
    root2 = Tk()
    root2.title("Earth")
    root2.geometry("950x250")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Earth''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''\nEarth is the third planet from the Sun and the only astronomical object known to harbor
     and support life. About 29.2% of Earth's surface is land consisting of continents and islands. The remaining 70.8% 
     is covered with water, mostly by oceans, seas, gulfs, and other salt-water bodies, but also by lakes, rivers, and 
     other freshwater, which together constitute the hydrosphere. Much of Earth's polar regions are covered in ice. 
     Earth's outer layer is divided into several rigid tectonic plates that migrate across the surface over many 
     millions of years, while its interior remains active with a solid iron inner core, a liquid outer core that 
     generates Earth's magnetic field, and a convective mantle that drives plate tectonics.

          ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button4_1 = Button(frame1, text="Distance", command=Earth_Distance, width="20", height="2", bg="grey")
    button4_1.pack(side=LEFT)

    button4_2 = Button(frame1, text="Mass", command=Earth_Mass, width="20", height="2", bg="grey")
    button4_2.pack(side=LEFT)

    button4_3 = Button(frame1, text="Surface Area", command=Earth_SurfaceArea, width="20", height="2", bg="grey")
    button4_3.pack(side=LEFT)

    button4_4 = Button(frame1, text="Age", command=Earth_Age, width="20", height="2", bg="grey")
    button4_4.pack(side=LEFT)

    button4_5 = Button(frame1, text="Population", command=Earth_Population, width="20", height="2", bg="grey")
    button4_5.pack(side=LEFT)

    button4_6 = Button(frame1, text="Radius", command=Earth_Radius, width="20", height="2", bg="grey")
    button4_6.pack(side=LEFT)

    root2.mainloop()


button4 = Button(frame, text="EARTH", command=Earth, width="20", height="2", bg="grey")
button4.pack(side=LEFT)


def Mars_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 227.9 million km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mars_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Mars''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 6.39 × 10^23 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mars_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Mars''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 144.8 million km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mars_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Mars''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 687 days''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mars_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of Day")
    c = Label(top, text='''Day length of Mars''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 1d 0h 37m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mars_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Mars''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 3,389.5 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Mars():
    root2 = Tk()
    root2.title("Mars")
    root2.geometry("940x250")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Mars''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System,
                              being larger than only Mercury. In English, Mars carries the name of the Roman god of war 
                              and is often referred to as the "Red Planet".[17][18] The latter refers to the effect of 
                              the iron oxide prevalent on Mars's surface, which gives it a reddish appearance distinctive
                              among the astronomical bodies visible to the naked eye.[19] Mars is a terrestrial planet 
                              with a thin atmosphere, with surface features reminiscent of the impact craters of the Moon 
                              and the valleys, deserts and polar ice caps of Earth.

              ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button5_1 = Button(frame1, text="Distance", command=Mars_Distance, width="20", height="2", bg="grey")
    button5_1.pack(side=LEFT)

    button5_2 = Button(frame1, text="Mass", command=Mars_Mass, width="20", height="2", bg="grey")
    button5_2.pack(side=LEFT)

    button5_3 = Button(frame1, text="Surface Area", command=Mars_SurfaceArea, width="20", height="2", bg="grey")
    button5_3.pack(side=LEFT)

    button5_4 = Button(frame1, text="Orbital Period", command=Mars_OrbitalPeriod, width="20", height="2", bg="grey")
    button5_4.pack(side=LEFT)

    button5_5 = Button(frame1, text="Length of Day", command=Mars_LengthOfDay, width="20", height="2", bg="grey")
    button5_5.pack(side=LEFT)

    button5_6 = Button(frame1, text="Radius", command=Mars_Radius, width="20", height="2", bg="grey")
    button5_6.pack(side=LEFT)

    root2.mainloop()


button5 = Button(frame, text="MARS", command=Mars, width="20", height="2", bg="grey")
button5.pack(side=LEFT)


def Jupiter_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 778.5 million km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Jupiter_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Jupiter''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 1.898 × 10^27 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Jupiter_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Jupiter''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 61.42 billion km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Jupiter_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Jupiter''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 12 years''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Jupiter_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of Day")
    c = Label(top, text='''Day length of Jupiter''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 0d 9h 56m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Jupiter_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Jupiter''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 69,911 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Jupiter():
    root2 = Tk()
    root2.title("Jupiter")
    root2.geometry("940x230")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Jupiter''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas 
    giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but 
    slightly less than one-thousandth the mass of the Sun. Jupiter is the third-brightest natural object in the Earth's 
    night sky after the Moon and Venus. It has been observed since pre-historic times and is named after the Roman god 
    Jupiter, the king of the gods, because of its observed sizeJupiter is primarily composed of hydrogen, but helium 
    comprises one quarter of its mass and one tenth of its volume. It likely has a rocky core of heavier elements, but 
    like the other giant planets, Jupiter lacks a well-defined solid surface. 

              ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button6_1 = Button(frame1, text="Distance", command=Jupiter_Distance, width="20", height="2", bg="grey")
    button6_1.pack(side=LEFT)

    button6_2 = Button(frame1, text="Mass", command=Jupiter_Mass, width="20", height="2", bg="grey")
    button6_2.pack(side=LEFT)

    button6_3 = Button(frame1, text="Surface Area", command=Jupiter_SurfaceArea, width="20", height="2", bg="grey")
    button6_3.pack(side=LEFT)

    button6_4 = Button(frame1, text="Orbital Period", command=Jupiter_OrbitalPeriod, width="20", height="2", bg="grey")
    button6_4.pack(side=LEFT)

    button6_5 = Button(frame1, text="Length of Day", command=Jupiter_LengthOfDay, width="20", height="2", bg="grey")
    button6_5.pack(side=LEFT)

    button6_6 = Button(frame1, text="Radius", command=Jupiter_Radius, width="20", height="2", bg="grey")
    button6_6.pack(side=LEFT)

    root2.mainloop()


button6 = Button(frame, text="JUPITER", command=Jupiter, width="20", height="2", bg="grey")
button6.pack(side=LEFT)


def Saturn_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 1.434 billion km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Saturn_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Saturn''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 5.683 × 10^26 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Saturn_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Saturn''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 42.7 billion km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Saturn_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Saturn''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 29 years''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Saturn_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of Day")
    c = Label(top, text='''Day length of Saturn''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 0d 10h 42m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Saturn_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Saturn''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 58,232 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Saturn():
    root2 = Tk()
    root2.title("Saturn")
    root2.geometry("950x250")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Saturn''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after 
    Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It only has one-eighth 
    the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive. Saturn is named 
    after the Roman god of wealth and agriculture; its astronomical symbol (♄) represents the god's sickle. The Romans 
    named the seventh day of the week Saturday, Sāturni diēs ("Saturn's Day") no later than the 2nd century for the planet 
    Saturn.Saturn's interior is most likely composed of a core of iron–nickel and rock (silicon and oxygen compounds). 
    Its core is surrounded by a deep layer of metallic hydrogen, an intermediate layer of liquid hydrogen and liquid helium,
    and finally a gaseous outer layer.

              ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button7_1 = Button(frame1, text="Distance", command=Saturn_Distance, width="20", height="2", bg="grey")
    button7_1.pack(side=LEFT)

    button7_2 = Button(frame1, text="Mass", command=Saturn_Mass, width="20", height="2", bg="grey")
    button7_2.pack(side=LEFT)

    button7_3 = Button(frame1, text="Surface Area", command=Saturn_SurfaceArea, width="20", height="2", bg="grey")
    button7_3.pack(side=LEFT)

    button7_4 = Button(frame1, text="Orbital Period", command=Saturn_OrbitalPeriod, width="20", height="2", bg="grey")
    button7_4.pack(side=LEFT)

    button7_5 = Button(frame1, text="Length of Day", command=Saturn_LengthOfDay, width="20", height="2", bg="grey")
    button7_5.pack(side=LEFT)

    button7_6 = Button(frame1, text="Radius", command=Saturn_Radius, width="20", height="2", bg="grey")
    button7_6.pack(side=LEFT)

    root2.mainloop()


button7 = Button(frame, text="SATURN", command=Saturn, width="20", height="2", bg="grey")
button7.pack(side=LEFT)


def Uranus_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 2.871 billion km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Uranus_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Uranus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 8.681 × 10^25 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Uranus_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Uranus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 8.083 billion km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Uranus_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Uranus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 84 years''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Uranus_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of Day")
    c = Label(top, text='''Day length of Uranus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 0d 17h 14m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Uranus_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Uranus''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 25,362 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Uranus():
    root2 = Tk()
    root2.title("Uranus")
    root2.geometry("950x270")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Uranus''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''Uranus is the seventh planet from the Sun. It has the third-largest planetary radius and 
    fourth-largest planetary mass in the Solar System. Uranus is similar in composition to Neptune, and both have bulk 
    chemical compositions which differ from that of the larger gas giants Jupiter and Saturn. For this reason, scientists 
    often classify Uranus and Neptune as "ice giants" to distinguish them from the other giant planets. Uranus's 
    atmosphere is similar to Jupiter's and Saturn's in its primary composition of hydrogen and helium, but it contains 
    more "ices" such as water, ammonia, and methane, along with traces of other hydrocarbons. It has the coldest planetary 
    atmosphere in the Solar System, with a minimum temperature of 49 K (−224 °C; −371 °F), and has a complex, layered cloud
    structure with water thought to make up the lowest clouds and methane the uppermost layer of clouds. The interior of 
    Uranus is mainly composed of ices and rock.

              ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button8_1 = Button(frame1, text="Distance", command=Uranus_Distance, width="20", height="2", bg="grey")
    button8_1.pack(side=LEFT)

    button8_2 = Button(frame1, text="Mass", command=Uranus_Mass, width="20", height="2", bg="grey")
    button8_2.pack(side=LEFT)

    button8_3 = Button(frame1, text="Surface Area", command=Uranus_SurfaceArea, width="20", height="2", bg="grey")
    button8_3.pack(side=LEFT)

    button8_4 = Button(frame1, text="Orbital Period", command=Uranus_OrbitalPeriod, width="20", height="2", bg="grey")
    button8_4.pack(side=LEFT)

    button8_5 = Button(frame1, text="Length of Day", command=Uranus_LengthOfDay, width="20", height="2", bg="grey")
    button8_5.pack(side=LEFT)

    button8_6 = Button(frame1, text="Radius", command=Uranus_Radius, width="20", height="2", bg="grey")
    button8_6.pack(side=LEFT)

    root2.mainloop()


button8 = Button(frame, text="URANUS", command=Uranus, width="20", height="2", bg="grey")
button8.pack(side=LEFT)


def Neptune_Distance():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Distance ")
    c = Label(top, text='''Distance from Sun''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Distance from Sun: 4.495 billion km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Neptune_Mass():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Mass")
    c = Label(top, text='''Mass of Neptune''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Mass: 1.024 × 10^26 kg''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Neptune_SurfaceArea():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Surface Area")
    c = Label(top, text='''Surface Area of Neptune''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Surface area: 7.618 billion km²''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Neptune_OrbitalPeriod():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Orbital Period")
    c = Label(top, text='''Orbital Period of Neptune''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Orbital period: 165 years''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Neptune_LengthOfDay():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Length of Day")
    c = Label(top, text='''Day length of Neptune''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Length of day: 0d 16h 6m''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Neptune_Radius():
    top = Toplevel(root)
    top.geometry("450x550")
    top.title("Radius")
    c = Label(top, text='''Radius of Neptune''', fg="black", bg="grey", width="500", height="1", font="10")
    c.pack()
    b = Label(top, text='''Radius: 24,622 km''', fg="black", width="500", height="1",
              font="10")

    b.pack()


def Neptune():
    root2 = Tk()
    root2.title("Neptune")
    root2.geometry("950x280")
    frame1 = Frame(root2)
    frame1.pack(side=LEFT, anchor="nw")
    b = Label(frame1, text='''Neptune''', fg="black", bg="grey", width="500", height="1", font="10")
    b.pack(side=TOP)
    f = Label(frame1, text='''Neptune is the eighth and farthest known Solar planet from the Sun. In the Solar System,
    it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet. It is 17 
    times the mass of Earth, slightly more massive than its near-twin Uranus. Neptune is denser and physically smaller 
    than Uranus because its greater mass causes more gravitational compression of its atmosphere. The planet orbits the 
    Sun once every 164.8 years at an average distance of 30.1 AU (4.5 billion km; 2.8 billion mi).Like Jupiter and Saturn, 
    Neptune's atmosphere is composed primarily of hydrogen and helium, along with traces of hydrocarbons and possibly 
    nitrogen, though it contains a higher proportion of "ices" such as water, ammonia and methane. However, similar to 
    Uranus, its interior is primarily composed of ices and rock; Uranus and Neptune are normally considered "ice giants" 
    to emphasise this distinction. 

              ''', fg="black",
              font="10")
    f.pack(side=TOP)

    button8_1 = Button(frame1, text="Distance", command=Neptune_Distance, width="20", height="2", bg="grey")
    button8_1.pack(side=LEFT)

    button8_2 = Button(frame1, text="Mass", command=Neptune_Mass, width="20", height="2", bg="grey")
    button8_2.pack(side=LEFT)

    button8_3 = Button(frame1, text="Surface Area", command=Neptune_SurfaceArea, width="20", height="2", bg="grey")
    button8_3.pack(side=LEFT)

    button8_4 = Button(frame1, text="Orbital Period", command=Neptune_OrbitalPeriod, width="20", height="2", bg="grey")
    button8_4.pack(side=LEFT)

    button8_5 = Button(frame1, text="Length of Day", command=Neptune_LengthOfDay, width="20", height="2", bg="grey")
    button8_5.pack(side=LEFT)

    button8_6 = Button(frame1, text="Radius", command=Neptune_Radius, width="20", height="2", bg="grey")
    button8_6.pack(side=LEFT)

    root2.mainloop()


button9 = Button(frame, text="NEPTUNE", command=Neptune, width="20", height="2", bg="grey")
button9.pack(side=LEFT)

root.mainloop()
