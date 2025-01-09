import sys
import os
from GUI.menu_principal import MenuPrincipal

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

interface = MenuPrincipal()
interface.run()