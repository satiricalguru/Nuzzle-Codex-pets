# Anya look mechanics

Anya is a humanoid chibi pet with a stable lower-body baseline and a soft, rounded head. Keep the feet, dress hem, and torso registration anchored. The eyes lead the gaze with the original green eye construction preserved; the eyelids and brows follow subtly, then the head turns a small amount through the neck and hair. Her hair ornaments follow the head without independently floating. No whole-sprite rotation, skew, new props, or replacement eyes.

Cardinal pose families, in viewer/screen coordinates:

- `000` up: pupils and upper eyelids lift; chin and head tip slightly upward while feet and dress hem stay fixed.
- `090` screen-right: nose/face center and pupils shift toward the right edge; the right cheek becomes more visible and the left cheek/hair edge is slightly occluded.
- `180` down: pupils and upper face aim downward; chin lowers with a restrained neck fold while the lower body stays anchored.
- `270` screen-left: nose/face center and pupils shift toward the left edge; the left cheek becomes more visible and the right cheek/hair edge is slightly occluded.

Intermediate directions interpolate these cardinal families evenly around the clockwise loop. Motion budget: each 22.5-degree step changes the same facial/head landmarks by a similar small amount; the prop-free silhouette should remain stable, with no sudden scale, baseline, hair, or eye construction change.
