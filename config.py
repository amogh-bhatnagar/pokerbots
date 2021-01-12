# PARAMETERS TO CONTROL THE BEHAVIOR OF THE GAME ENGINE
# DO NOT REMOVE OR RENAME THIS FILE
PLAYER_1_NAME = 'Hero'
PLAYER_1_PATH = './cur_bot'
# NO TRAILING SLASHES ARE ALLOWED IN PATHS
PLAYER_2_NAME = 'Villain'
PLAYER_2_PATH = './prev_bot'
# GAME PROGRESS IS RECORDED HERE
GAME_LOG_FILENAME = 'gamelog'
# PLAYER_LOG_SIZE_LIMIT IS IN BYTES
PLAYER_LOG_SIZE_LIMIT = 524288
# STARTING_GAME_CLOCK AND TIMEOUTS ARE IN SECONDS
ENFORCE_GAME_CLOCK = True
STARTING_GAME_CLOCK = 30.
BUILD_TIMEOUT = 10.
CONNECT_TIMEOUT = 10.
# THE GAME VARIANT FIXES THE PARAMETERS BELOW
# CHANGE ONLY FOR TRAINING OR EXPERIMENTATION
NUM_BOARDS = 3
NUM_ROUNDS = 500
STARTING_STACK = 200
BIG_BLIND = 2
SMALL_BLIND = 1