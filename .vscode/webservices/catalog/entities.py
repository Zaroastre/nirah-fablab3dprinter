class Dimension:
    def __init__(self, x: int, y: int, z: int):
        self.x = x;
        self.y = y;
        self.z = z;

class Model:
    
    def __init__(self) -> None:
        self.identifier: int = -1;
        self.dimension: Dimension = Dimension();
        self.weight: float = 0.0;