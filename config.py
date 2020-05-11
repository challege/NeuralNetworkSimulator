import configparser


ext_cfg = configparser.ConfigParser()
ext_cfg.read('config.cfg')

# Screen size
WIDTH = int(ext_cfg['Display']['width'])
HEIGHT = int(ext_cfg['Display']['height'])

# Neurons
NEURON_SIZE = 25
NEURON_FONT_SIZE = 14
NEURON_FONT = 'freesansbold.ttf'
DEFAULT_NUM_NEURONS = 9
NEURON_START_X = 200
NEURON_START_Y = 100
NEURON_SPACING_X = 180
NEURON_SPACING_Y = 90
TENSOR_FONT_SIZE = 14

# NN Params
TRAINING_DATA_FILE = ext_cfg['Training']['training_data']
NUM_EPOCHS = int(ext_cfg['Training']['epochs'])
LEARNING_RATE = float(ext_cfg['Training']['learning_rate'])
MIN_LAYERS = 3
MAX_LAYERS = 9
MAX_NEURONS = 9
MIN_NEURONS = 1
MAX_SPEED = 100
MIN_OUTPUTS = 1
MAX_OUTPUTS = 1

# Default network
DEFAULT_NETWORK_LAYERS = 3
DEFAULT_NETWORK_INPUTS = 2
DEFAULT_NETWORK_OUTPUTS = 1
DEFAULT_NETWORK_HIDDEN = 5
DEFAULT_NETWORK_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLUE = (114, 188, 212)
RED = (200, 0, 0)
BRIGHT_RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
SILVER = (192, 192, 192)
DARK_SILVER = (96, 96, 96)
LIGHT_SILVER = (224, 224, 224)

# Controls
BUTTON_FONT = 'freesansbold.ttf'
BUTTON_FONT_SIZE = 14
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 100

BUTTON_BUILD_NETWORK_X = 850
BUTTON_BUILD_NETWORK_Y = 15

BUTTON_START_TRAINING_X = 850
BUTTON_START_TRAINING_Y = 50

BUTTON_RESET_NETWORK_X = 1000
BUTTON_RESET_NETWORK_Y = 15

BUTTON_TICK_HEIGHT = 15
BUTTON_TICK_WIDTH = 30

BUTTON_TICK_UP_1_X = 150
BUTTON_TICK_UP_1_Y = 15

BUTTON_TICK_DOWN_1_X = 150
BUTTON_TICK_DOWN_1_Y = 32

INPUT_BOX_FONT_SIZE = 32
INPUT_BOX_LAYERS_X = 110
INPUT_BOX_LAYERS_Y = 18
INPUT_BOX_LAYERS_WIDTH = 30
INPUT_BOX_LAYERS_HEIGHT = 32

INPUT_BOX_INPUT_LAYER_X = 310
INPUT_BOX_INPUT_LAYER_Y = 18
INPUT_BOX_INPUT_LAYER_WIDTH = 30
INPUT_BOX_INPUT_LAYER_HEIGHT = 32
BUTTON_TICK_UP_INPUT_X = 350
BUTTON_TICK_UP_INPUT_Y = 15
BUTTON_TICK_DOWN_INPUT_X = 350
BUTTON_TICK_DOWN_INPUT_Y = 32

INPUT_BOX_HIDDEN_LAYER_X = 510
INPUT_BOX_HIDDEN_LAYER_Y = 18
INPUT_BOX_HIDDEN_LAYER_WIDTH = 30
INPUT_BOX_HIDDEN_LAYER_HEIGHT = 32
BUTTON_TICK_UP_HIDDEN_X = 550
BUTTON_TICK_UP_HIDDEN_Y = 15
BUTTON_TICK_DOWN_HIDDEN_X = 550
BUTTON_TICK_DOWN_HIDDEN_Y = 32

INPUT_BOX_OUTPUT_LAYER_X = 710
INPUT_BOX_OUTPUT_LAYER_Y = 18
INPUT_BOX_OUTPUT_LAYER_WIDTH = 30
INPUT_BOX_OUTPUT_LAYER_HEIGHT = 32
BUTTON_TICK_UP_OUTPUT_X = 750
BUTTON_TICK_UP_OUTPUT_Y = 15
BUTTON_TICK_DOWN_OUTPUT_X = 750
BUTTON_TICK_DOWN_OUTPUT_Y = 32

MESSAGE_BOX_TOP_X = (WIDTH//2)
MESSAGE_BOX_TOP_Y = HEIGHT-150
MESSAGE_BOX_TOP_WIDTH = 1500
MESSAGE_BOX_TOP_HEIGHT = 32

MESSAGE_BOX_BOTTOM_X = (WIDTH//2)
MESSAGE_BOX_BOTTOM_Y = HEIGHT-100
MESSAGE_BOX_BOTTOM_WIDTH = 1500
MESSAGE_BOX_BOTTOM_HEIGHT = 32
MESSAGE_BOX_FONT_SIZE = 32

TEXT_BOX_LOSS_X = WIDTH - 100
TEXT_BOX_LOSS_Y = 450
TEXT_BOX_LOSS_WIDTH = 25
TEXT_BOX_LOSS_HEIGHT = 32
TEXT_BOX_LOSS_FONT_SIZE = 24

TEXT_BOX_EPOCH_X = WIDTH - 100
TEXT_BOX_EPOCH_Y = 250
TEXT_BOX_EPOCH_WIDTH = 25
TEXT_BOX_EPOCH_HEIGHT = 32
TEXT_BOX_EPOCH_FONT_SIZE = 24

TEXT_BOX_EXAMPLES_X = WIDTH - 100
TEXT_BOX_EXAMPLES_Y = 350
TEXT_BOX_EXAMPLES_WIDTH = 25
TEXT_BOX_EXAMPLES_HEIGHT = 32
TEXT_BOX_EXAMPLES_FONT_SIZE = 24

TEXT_BOX_SPEED_X = WIDTH - 100
TEXT_BOX_SPEED_Y = 150
TEXT_BOX_SPEED_WIDTH = 25
TEXT_BOX_SPEED_HEIGHT = 32
TEXT_BOX_SPEED_FONT_SIZE = 24
BUTTON_TICK_UP_SPEED_X = TEXT_BOX_SPEED_X + 40
BUTTON_TICK_UP_SPEED_Y = 132
BUTTON_TICK_DOWN_SPEED_X = TEXT_BOX_SPEED_X + 40
BUTTON_TICK_DOWN_SPEED_Y = 150
