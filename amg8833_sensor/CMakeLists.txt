cmake_minimum_required(VERSION 3.5)
project(amg8833_sensor)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(
  DIRECTORY scripts/
  DESTINATION lib/${PROJECT_NAME}
  USE_SOURCE_PERMISSIONS
)

install(
  PROGRAMS scripts/amg8833_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
