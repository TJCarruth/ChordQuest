# ChordQuest
A synthesizer app designed for the Anbernic 35XX H which is heavily inspired by the [HiChord from Pocket Audio](https://hichord.shop/). 

## Project Parameters
While this project is supposed to be a synthesizer, it's also meant to be a project I can use to learn more about python, music theory, code development, CLI tools, and other related topics. To anyone else reading this, I'm not sure how much use this app will be to you.  

## Controls

### Right Joystick: Chord 
Chords follow the Nashville Number System, starting in the up/right position with 1 and counts up to 7 as the joystick rolls clockwise.
* up/right  - Tonic (I) (Major)
* right     - Supertonic (II) (Minor)
* down/right- Mediant (III) (Minor)
* down      - Subdominant (IV) (Major)
* down/left - Dominant (V) (Major)
* left      - Submediant (VI) (Minor)
* up/left   - Leading Tone (VII) (Diminished)

### Left Joystick: Chord Modifiers
move both sticks simultaneously to modify a chosen chord.
* up        - major/minor
* up/right  - seventh
* right     - major/minor seventh
* down/right- major/minor 9
* down      - suspended 4
* down/left - sus2/maj6
* left      - Diminished
* up/left   - Augmented

### Additional functions

* chord inversion: Right stick + left/right hat
* change key: left/right hat
* change octave: up/down hat
* change individual chord octaves: right joystick + up/down hat
* Change waveform: Y + up/down hat
* Change effects: X + hat (left/right to select, up/down for modes&on/off)
* Change modes (chords, arpeggios, drums): A
* change BPM: B + up/down hat
* Loop: click left joystick (start loop, end loop and start playing, stop playing loop.)

* Record: start button to toggle
* list of recordings: select, opens a menu navigatable by hat. 
