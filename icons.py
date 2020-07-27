from colors import colors_dict
import numpy as np

icons = {
"sun" : { "icon": [[0, 0, 1, 0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 1, 1, 1, 0, 1],
                   [0, 1, 1, 1, 1, 1, 1, 0],
                   [0, 1, 1, 1, 1, 1, 1, 0],
                   [1, 0, 1, 1, 1, 1, 0, 1],
                   [0, 0, 0, 1, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0, 1, 0, 0]],
        "color_map": ["black", "yellow"]
                   },

"cloud" : { "icon": [[0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 1, 1, 1, 0, 1],
                     [0, 0, 1, 1, 1, 2, 2, 0],
                     [0, 2, 2, 1, 2, 2, 2, 2],
                     [2, 2, 2, 1, 2, 2, 2, 2],
                     [2, 2, 2, 2, 2, 2, 2, 2],
                     [0, 2, 2, 2, 2, 2, 2, 0]],
        "color_map": ["black", "yellow", "white"]
                   },

"checked" : { "icon": [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0],
                       [1, 1, 0, 1, 1, 0, 0, 0],
                       [0, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]],
        "color_map": ["black", "green"]
                   },
"heart" :   { "icon": [[0, 1, 1, 0, 0, 1, 1, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 0, 1, 1, 1, 1, 1],
                       [0, 1, 1, 1, 1, 1, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0]],
        "color_map": ["black", "red"]
                   },

"gmail" :   { "icon": [[1, 1, 0, 0, 0, 0, 1, 1],
                       [1, 1, 1, 0, 0, 1, 1, 1],
                       [1, 0, 1, 1, 1, 1, 0, 1],
                       [1, 0, 0, 1, 1, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 1]],
        "color_map": ["white", "red"]
                   },

"bulb" :    { "icon": [[0, 1, 1, 1, 1, 0],
                       [1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1],
                       [2, 3, 3, 3, 3, 2],
                       [0, 2, 3, 3, 2, 0],
                       [0, 0, 3, 3, 0, 0],
                       [0, 0, 3, 3, 0, 0],
                       [0, 0, 2, 2, 0, 0]],
        "color_map": ["black", "yellow", "grey", "white"]
                   },

"bulb0" :    { "icon": [[0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]],
        "color_map": ["black", "yellow",]
                   },

"bulb1" :    { "icon": [[0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]],
        "color_map": ["black", "yellow"]
                   },

"bulb2" :    { "icon": [[0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [0, 1, 1, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]],
        "color_map": ["black", "yellow"]
                   },
}

def make_icon(name):
    icon_dict = icons[name]
    icon_matrix = []
    for line in icon_dict["icon"]:
        mline = []
        for pix_c in line:
            mline.append(colors_dict[icon_dict["color_map"][pix_c]])
        icon_matrix.append(mline)
    return np.array(icon_matrix)
