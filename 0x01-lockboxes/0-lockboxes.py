#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """
    unlocked_boxes = set([0])

    key_queue = boxes[0].copy()

    while key_queue:
        key = key_queue.pop(0)

        if key in unlocked_boxes:
            continue
        unlocked_boxes.add(key)

        key_queue.extend(boxes[key])

    return len(unlocked_boxes) == len(boxes)
