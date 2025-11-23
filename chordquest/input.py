class AnbernicInput:
    def __init__(self, engine, synth):
        self.engine = engine
        self.synth = synth
        self.current_degree = None
        self.current_quality = "maj"

    def handle_right_stick(self, direction):
        degree_map = {
            "up_right": 1, 
            "right": 2, 
            "down_right": 3,
            "down": 4, 
            "down_left": 5, 
            "left": 6, 
            "up_left": 7
        }
        self.current_degree = degree_map.get(direction)

    def handle_left_stick(self, direction):
        quality_map = {
            "up": "maj/min", 
            "up_right": "7", 
            "right": "maj7/min7",
            "down_right": "9", 
            "down": "sus4", 
            "down_left": "sus2/maj6",
            "left": "dim", 
            "up_left": "aug"
        }
        self.current_quality = quality_map.get(direction, "maj")

    def play_chord(self):
        if self.current_degree:
            chord = self.engine.get_chord(self.current_degree, self.current_quality)
            self.synth.play_chord(chord)
