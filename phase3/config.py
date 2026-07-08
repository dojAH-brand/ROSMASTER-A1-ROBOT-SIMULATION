# ── Robot dimensions (from URDF, in metres) ─────────────
WHEEL_RADIUS = 0.06    # radius of each wheel
WHEEL_WIDTH  = 0.045   # thickness of each wheel

WHEELBASE    = 0.135   # front-to-back distance between axles
TRACK_WIDTH  = 0.115   # side-to-side distance between left/right wheels

BODY_LENGTH  = 0.34    # chassis length (front to back)
BODY_WIDTH   = 0.24    # chassis width (left to right)
BODY_HEIGHT  = 0.05    # chassis height (top to bottom)


BLACK_COL=(0.08, 0.08, 0.08, 1)
 
DARK_GREY_COL=(0.28, 0.28, 0.28, 1)
 
LIGHT_GREY_COL= (0.75, 0.75, 0.75, 1)

BLUE_COL=(0.05, 0.28, 0.82, 1)
 
ORANGE_COL =(1, 0.45, 0.05, 1)

WHEEL_BLUE_COL=(0, 0, 1, 1)

# ── LiDAR dimensions (from URDF, in metres) ─────────────
LIDAR_X = 0.07   
LIDAR_Y = 0
LIDAR_Z = 0.08   

LIDAR_BODY_RADIUS = 0.04    
LIDAR_BODY_LENGTH = 0.03   

LIDAR_PEDESTAL_RADIUS = 0.018 
LIDAR_PEDESTAL_LENGTH = 0.04   
LIDAR_PEDESTAL_X = 0
LIDAR_PEDESTAL_Y = 0
LIDAR_PEDESTAL_Z = -0.02  

LIDAR_RING_RADIUS = 0.041  
LIDAR_RING_LENGTH = 0.004  
LIDAR_RING_X = 0
LIDAR_RING_Y = 0
LIDAR_RING_Z = 0.01 

# Camera dimensionas

CAMERA_X = 0.17
CAMERA_Y = 0
CAMERA_Z = 0.03

CAMERA_BODY_LENGTH = 0.095
CAMERA_BODY_WIDTH = 0.028
CAMERA_BODY_HEIGHT = 0.028

CAMERA_LENS_RADIUS = 0.006  
CAMERA_LENS_LENGTH = 0.004    
CAMERA_LENS_OFFSET_Y  =  0.009  
CAMERA_LENS_OFFSET_NY = -0.009   
CAMERA_LENS_X      =  0.03   


CAMERA_DEPTH_W = 0.01    
CAMERA_DEPTH_D = 0.008   
CAMERA_DEPTH_H = 0.004   
CAMERA_DEPTH_X = 0.03 


# ── Physics constants (from Phase 1) ─────────────────────
MAX_SPEED      = 3.0    
MAX_STEER      = 30     
THROTTLE_FORCE = 5.0    
FRICTION       = 0.90   
STEER_RETURN   = 0.85   