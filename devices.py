class Devices:
    devices = {
        "macbook13": (1280, 800),
        "macbook15": (1440, 900),
        "imac27": (2560, 1440),
        "imac21": (1920, 1080),
        "ipad": (1024, 768)
    }

    def get(self, name):
        return self.devices[name];
