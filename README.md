# Deepracer_FloridaMen
I participated in the AWS hosted DeepRacer competition at Howard University and was thrilled to win first place! I trained a DeepRacer model to autonomously navigate a track and stay on the correct path. This is a brief desription of the approach that I used to train my DeepRacer model and the reward function and hyperparameters that I used.


## Reward Function
We did some trial and errors on the paramenters, and found out that the three main parameters that give the best results.

The `I_Want_to_Break_Free.py` reward function prioritizes staying on the track, following the correct direction, and being close to the center of the track. The function calculates the track direction based on the closest waypoints, and compares it to the heading of the car. If the direction difference is greater than 10 degrees, the reward is halved. Otherwise, the reward is set to 1.0. Additionally, the reward is increased by the distance from the center of the track, with a maximum value of 1.0 when the car is perfectly centered on the track.


## Hyperparameters
The hyperparameters used for this DeepRacer setup are:

```json
{
    "batch_size": 64,
    "beta_entropy": 0.01,
    "discount_factor": 0.888,
    "loss_type": "huber",
    "lr": 0.0003,
    "num_episodes_between_training": 18,
    "num_epochs": 4
}
```

The minimum and maximum speeds for the car are set to 1.1 and 2.0, respectively. Additionally, the car is given an angle control of -30 to 30 degrees.


## Results
Using my reward function and hyperparameters, my DeepRacer model learned to follow the track and stay on the correct path, resulting in winning first place in the competition! You can see my model in action in the following YouTube video: (click the picture to play the video)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/nHD-ifZz1SU/0.jpg)](https://www.youtube.com/watch?v=nHD-ifZz1SU)

I'm proud of the work that I put into this project and grateful for the opportunity to learn more about reinforcement learning and robotics through the DeepRacer platform. A big shoutout to Queen for the epic music that fueled my all-nighters and filename inspirations.
