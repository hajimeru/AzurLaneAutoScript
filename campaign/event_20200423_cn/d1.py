from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger


MAP = CampaignMap()
MAP.map_data = '''
    -- -- -- -- -- -- -- -- --
    -- ++ ++ -- -- -- -- ++ --
    -- -- -- -- -- -- -- -- --
    -- -- ++ ++ ++ -- -- -- --
    -- -- -- -- -- -- -- -- --
    ++ ++ -- -- -- -- ++ -- --
    ++ ++ SP SP -- -- ++ -- --
'''


class Config:
    SUBMARINE = 0
    FLEET_BOSS = 2

    POOR_MAP_DATA = True
    MAP_HAS_AMBUSH = False
    MAP_HAS_FLEET_STEP = True
    MAP_HAS_MOVABLE_ENEMY = True
    MAP_HAS_SIREN = True
    MAP_HAS_DYNAMIC_RED_BORDER = True
    MAP_SIREN_COUNT = 2

    TRUST_EDGE_LINES = True

    INTERNAL_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (80, 255 - 40),
        'width': (0.9, 10),
        'prominence': 10,
        'distance': 35,
    }
    EDGE_LINES_FIND_PEAKS_PARAMETERS = {
        'height': (255 - 40, 255),
        'prominence': 10,
        'distance': 50,
        'wlen': 1000
    }


class Campaign(CampaignBase):
    MAP = MAP