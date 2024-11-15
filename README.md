# ObstakelVermijding
# Obstakelvermijding Package

Dit ROS 2-pakket bevat een robot die autonoom beweegt en obstakels vermijdt op basis van LiDAR-sensorinformatie. De robot kan oneindig blijven bewegen totdat het programma wordt beëindigd. De robot doorloopt het speelveld in de kortst mogelijke tijd, zonder steeds hetzelfde pad te volgen.

## Installatie en Gebruik

Volg de onderstaande stappen om het pakket op je laptop te installeren en uit te voeren.

### Stap 1: Installeer ROS 2

Zorg ervoor dat je **ROS 2** hebt geïnstalleerd op je systeem. Volg de instructies voor de installatie van **ROS 2 Humble** (of een andere versie die je gebruikt) op de officiële [ROS 2 installatiehandleiding](https://docs.ros.org/en/foxy/Installation.html).

### Stap 2: Maak een ROS 2 workspace aan

Maak een werkruimte aan waarin je ROS 2-pakketten kunt bouwen:

In bash:

mkdir -p ~/ros2ws/src
cd ~/ros2ws/src

### Stap 3: Clone je pakket
cd ~/ros2ws/src
git clone https://github.com/senneclauwaert/Obstakelvermijding.git

### Stap 4: Bouw je workspace
cd ~/ros2ws
colcon build

### Stap 5 : Source je workspace
source ~/ros2ws/install/setup.bash

### Stap 6: Start de simulatie
ros2 launch patrol_pkg patrol_pkg_launch_file.launch.py

