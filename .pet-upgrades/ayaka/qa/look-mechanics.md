# Ayaka look mechanics

Ayaka is a humanoid chibi pet. Keep the feet and skirt hem anchored; the original eyes lead the gaze, then the head, bangs, and hair ornaments follow subtly. Preserve existing props and eye construction. No replacement eyes, text, detached effects, whole-sprite rotation, or skew.

Cardinal pose families in viewer/screen coordinates: 000 up lifts pupils and upper eyelids with a slight head tip; 090 screen-right shifts the face and pupils right with the right cheek more visible; 180 down lowers the eyes and chin; 270 screen-left shifts the face and pupils left with the left cheek more visible. Interpolate the intermediate directions evenly around the clockwise loop with a stable feet/torso baseline and similar landmark movement per 22.5-degree step.
