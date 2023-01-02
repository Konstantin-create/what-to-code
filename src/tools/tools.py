class ParseResponse:
    """Class of parser response"""

    header: str = ''
    body: str = ''
    error: int = 100

    """
    Error codes:
    100 - OK
    200 - Server error
    300 - Another error
    """

    def __repr__(self):
        return f'<ParseResponse: {self.error} | {self.header}>'
