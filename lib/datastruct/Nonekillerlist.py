class NoneKillerList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append(self, obj):
        if obj is None:
            return
        super().append(obj)