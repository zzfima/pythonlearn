from builder import Builder


class SkylarkBuilder(Builder):
    """Concrete builder"""

    def add_model(self):
        self.car._model = "Skylark"

    def add_tires(self):
        self.car._tires = "Regular tires"

    def add_engine(self):
        self.car._engine = "322 cu in (5.3 L) Nailhead V8"
