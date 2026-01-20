include("$(PORT_DIR)/boards/manifest.py")

freeze("modules", opt=3)
freeze(".", script="main.py", opt=3)
freeze(".", script="boot.py", opt=3)