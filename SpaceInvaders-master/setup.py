import os
import cx_Freeze

executables = [cx_Freeze.Executable("spaceinvaders.py")]
os.environ['TCL_LIBRARY'] = r'C:\Users\Tomas\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Tomas\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'
cx_Freeze.setup(
    name="Anillos de Saturno",
    options={"build_exe": {"packages":["pygame"],
             "include_files":["spaceinvaders.py","assets/a1_0.png","assets/a1_1.png","assets/a2_0.png",
                              "assets/a2_1.png","assets/a3_0.png","assets/a3_1.png","2a1_0.png","2a1_1.png","2a2_0.png","2a2_1.png",
                              "2a3_0.png","2a3_1.png","shooter.png",
                              "fondonuevo.jpeg","controles.jpeg","618.jpg","star.jpg","laser.wav","video game.wav"]}},
    executables = executables

    )
