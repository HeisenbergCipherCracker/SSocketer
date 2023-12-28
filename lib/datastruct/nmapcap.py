class Nmapcap(list):
    """
    >>> ls = [2,3,4,5,5]
    >>> obj = Nmapcap()
    >>> obj.save_nmap_datas(ls)
    >>> print(obj)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self,index):
        return super().__getitem__(index)
    
    def save_nmap_datas(self,datas:(list,tuple)):
        self.extend(data for data in datas)
    





        