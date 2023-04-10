import math

def reward_function(params):
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    distance_from_center = params['distance_from_center']
    
    reward = 1.0
    
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    
    track_direction = math.degrees(track_direction)
    
    direction_diff = abs(track_direction - heading)
    
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
    
    if direction_diff > 10.0:
        reward *= 0.5
        
    reward += (1 - distance_from_center)
    
    return float(reward)
