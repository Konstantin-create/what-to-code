class ParseResponse:
    """Class of parser response"""

    def __init__(self, header: str = '', body: str = '', error: int = 100):
        self.header = header
        self.body = body
        self.error = error

    """
    Error codes:
    100 - OK
    200 - Server error
    300 - Another error
    400 - NET error
    """

    def __repr__(self):
        return f'<ParseResponse: {self.error} | {self.header}>'
