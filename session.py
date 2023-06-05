def init_session():
    global session
    session = {
        "items": {
            "plastic_bottle": False,
            "piece_of_wood": False,
            "glass_bottle": False,
        },
        "scene_count": 0,
        "username": "",
    }