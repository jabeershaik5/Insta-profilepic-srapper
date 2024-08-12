class MainError(Exception):
    def __init__(self, error_code, message):
        self.error_code = error_code
        super().__init__(message)
