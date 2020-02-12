def construct_payload(HEADER_BLOCK, DIVIDER_BLOCK, MESSAGE_BLOCK):

    return {
        "channel": "testing",
        "username": "test",
        "icon_emoji": ":robot_face:",
        "text": ":wave: Your daily dose of motivation has arrived",
        "blocks": [
            HEADER_BLOCK,
            DIVIDER_BLOCK,
            MESSAGE_BLOCK
        ],
    }
