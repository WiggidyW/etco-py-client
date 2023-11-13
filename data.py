from typing import Optional

import etco_pb2

class NamedSystem():
    def __init__(
        self,
        maps: etco_pb2.LocationNamingMaps,
        system_id: int,
        region_id: int,
    ):
        self._maps: etco_pb2.LocationNamingMaps = maps
        self._system_id: int = system_id
        self._region_id: int = region_id

    @property
    def system_id(self) -> Optional[int]:
        if self._system_id >= 0:
            return self._system_id
        else:
            return None

    @property
    def system_name(self) -> Optional[str]:
        return self._maps.system_names.get(self._system_id, None)
    
    @property
    def region_id(self) -> Optional[int]:
        if self._region_id >= 0:
            return self._region_id
        else:
            return None
    
    @property
    def region_name(self) -> Optional[str]:
        return self._maps.region_names.get(self.region_id, None)

class NamedLocation(NamedSystem):
    def __init__(
        self,
        maps: etco_pb2.LocationNamingMaps,
        info: etco_pb2.LocationInfo,
        location_id: int,
    ):
        self._maps: etco_pb2.LocationNamingMaps = maps
        self._info: etco_pb2.LocationInfo = info
        self._location_id: int = location_id
        super().__init__(maps, info.system_id, info.region_id)

    @property
    def name(self) -> Optional[str]:
        return self._maps.location_names.get(self._location_id, None)
    
    @property
    def location_id(self) -> int:
        return self._location_id


class NamedItem():
    def __init__(
        self,
        lists: etco_pb2.TypeNamingLists,
        indexes: etco_pb2.TypeNamingIndexes,
        type_id: int,
        quantity: int,
    ):
        self._lists: etco_pb2.TypeNamingLists = lists
        self._indexes: etco_pb2.TypeNamingIndexes = indexes
        self._type_id: int = type_id
        self._quantity: int = quantity
        self._market_groups: Optional[list[str]] = None

    @property
    def type_id(self) -> int:
        return self._type_id
    
    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def name(self) -> str:
        return self._indexes.name
    
    @property
    def category(self) -> Optional[str]:
        if self._indexes.category_index == -1:
            return None
        else:
            return self._lists.categories[self._indexes.category_index]
        
    @property
    def group(self) -> Optional[str]:
        if self._indexes.group_index == -1:
            return None
        else:
            return self._lists.groups[self._indexes.group_index]
        
    @property
    def market_groups(self) -> list[str]:
        if self._market_groups is None:
            self._market_groups = [self._lists.market_groups[i] for i in self.indexes.market_group_indexes]
        return self._market_groups
    
class ParsedItem():
    def __init__(
        self,
        item: etco_pb2.NamedBasicItem,
        known: bool,
    ):
        self._item: etco_pb2.NamedBasicItem = item
        self._known: bool = known

    @property
    def type_id(self) -> int:
        return self._item.type_id
    
    @property
    def name(self) -> str:
        return self._item.name
    
    @property
    def known(self) -> bool:
        return self._known
    
    @property
    def unknown(self) -> bool:
        return not self._known
    
class BuybackAppraisalStatus():
    def __init__(
        self,
        rep: etco_pb2.StatusBuybackAppraisalResponse,
    ):
        self._contract: etco_pb2.Contract = rep.contract
        self._contract_location: NamedLocation = NamedLocation(
            maps=rep.location_naming_maps,
            info=rep.location_info,
            location_id=rep.contract.location_id,
        )
        self._contract_items: list[NamedItem] = [NamedItem(
            lists=rep.type_naming_lists,
            indexes=item,
            type_id=item.type_id,
            quantity=item.quantity,
        ) for item in rep.contract_items]

    @property
    def has_contract(self) -> bool:
        return self._contract.contract_id > 0
    
    @property
    def contract(self) -> etco_pb2.Contract:
        return self._contract
    
    @property
    def contract_location(self) -> NamedLocation:
        return self._contract_location
    
    @property
    def contract_items(self) -> list[NamedItem]:
        return self._contract_items
