# ROS2 REST API Integration Project

This project demonstrates the integration of a REST API with ROS2 nodes. The system includes:

1. A REST API for accepting and retrieving missions.
2. Two ROS2 nodes:
   - RN1: Fetches missions from the API and publishes them.
   - RN2: Subscribes to the missions and processes them.

## Architecture

1. REST API:

- Provides endpoints to POST and GET missions.
- Runs on a Flask server.

2. ROS2 Node 1 (RN1):

- Periodically polls the API to check for new missions.
- Publishes mission data to a ROS2 topic (mission_topic).

3. ROS2 Node 2 (RN2):

- Subscribes to mission_topic to receive mission data.
- Logs the received mission for processing.

## Running the Project

1. Start the REST API

Run the API server in a separate terminal:

```bash
cd ros2_ws/src/api
python app.py
```

The API will be accessible at `http://localhost:5000`.

API Endpoints:

- POST `/mission`: Add a new mission.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"mission": "Test Mission"}' http://localhost:5000/mission
```

- GET `/mission`: Retrieve all missions.

```bash
curl -X GET http://localhost:5000/mission
```

2. Run RN2 (Mission Subscriber)

Start RN2 in a separate terminal:

```bash
source ros2_ws/install/setup.bash
ros2 run rn2 rn2
```

3. Run RN1 (Mission Publisher)

Start RN1 in a separate terminal:

```bash
source ros2_ws/install/setup.bash
ros2 run rn1 rn1
```

4. Send a Mission

POST a mission using the API:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"mission": "Test Mission"}' http://localhost:5000/mission
```

- RN1 fetches the mission from the REST API and publishes it to the `mission_topic`.
- RN2 receives the mission from `mission_topic` and logs it.
