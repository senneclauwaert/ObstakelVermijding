import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/senne/ros2_ws/src/lidar_pkg/install/lidar_pkg'
